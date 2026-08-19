//! BG3 party-guide local server.
//!
//!   bg3            Serve the guide on http://127.0.0.1:8787 (set BG3_PORT to change).
//!
//! Local, single-user, loopback-only: no auth, no TLS, nothing exposed off-box.

mod content;
mod progress;

use std::path::PathBuf;
use std::sync::Arc;

use anyhow::{Context, Result};
use axum::{
    extract::State,
    http::{header, HeaderValue, StatusCode},
    response::{IntoResponse, Response},
    routing::get,
    Json, Router,
};
use serde::Deserialize;
use tower_http::{services::ServeDir, set_header::SetResponseHeaderLayer};

use crate::progress::{Progress, ProgressStore};

#[derive(Clone)]
struct AppState {
    root: PathBuf,
    progress: Arc<ProgressStore>,
}

#[tokio::main]
async fn main() -> Result<()> {
    let root = std::env::current_dir().context("resolving current directory")?;

    let progress = Arc::new(ProgressStore::load(&root).context("loading progress.json")?);
    let state = AppState {
        root: root.clone(),
        progress,
    };

    let app = Router::new()
        .route("/api/plan", get(get_plan))
        .route("/api/progress", get(get_progress).post(post_progress))
        .fallback_service(ServeDir::new(root.clone()).append_index_html_on_directories(true))
        // Single-user local tool whose content is edited live: never let the
        // browser serve a stale index.html or plan from its cache.
        .layer(SetResponseHeaderLayer::overriding(
            header::CACHE_CONTROL,
            HeaderValue::from_static("no-store"),
        ))
        .with_state(state);

    let port: u16 = std::env::var("BG3_PORT")
        .ok()
        .and_then(|s| s.parse().ok())
        .unwrap_or(8787);
    let addr = format!("127.0.0.1:{port}");
    let listener = tokio::net::TcpListener::bind(&addr)
        .await
        .with_context(|| format!("binding {addr} (is it already in use?)"))?;

    println!("BG3 party guide serving from content/*.md");
    println!("  →  http://{addr}");
    println!("Press Ctrl-C to stop.");

    axum::serve(listener, app)
        .with_graceful_shutdown(shutdown_signal())
        .await
        .context("server error")?;
    Ok(())
}

async fn shutdown_signal() {
    let _ = tokio::signal::ctrl_c().await;
    println!("\nShutting down.");
}

/// `GET /api/plan` — the merged guide JSON (reloaded from disk each request so
/// edits to content/*.md show up on refresh without restarting the server).
async fn get_plan(State(st): State<AppState>) -> Response {
    match content::load_plan(&st.root) {
        Ok(v) => Json(v).into_response(),
        Err(e) => {
            eprintln!("GET /api/plan failed: {e:#}");
            (StatusCode::INTERNAL_SERVER_ERROR, format!("{e:#}")).into_response()
        }
    }
}

/// `GET /api/progress` — current checkoff state.
async fn get_progress(State(st): State<AppState>) -> Json<Progress> {
    Json(st.progress.snapshot())
}

#[derive(Deserialize)]
struct SetReq {
    key: String,
    checked: bool,
}

/// `POST /api/progress` — toggle one checkoff `{ "key": "...", "checked": true }`.
async fn post_progress(State(st): State<AppState>, Json(req): Json<SetReq>) -> Response {
    match st.progress.set(&req.key, req.checked) {
        Ok(()) => StatusCode::NO_CONTENT.into_response(),
        Err(e) => {
            eprintln!("POST /api/progress failed: {e:#}");
            (StatusCode::INTERNAL_SERVER_ERROR, format!("{e:#}")).into_response()
        }
    }
}
