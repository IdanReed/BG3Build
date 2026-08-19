---
roster:
- slot: 1
  nickname: Charles
  class: Oath of Vengeance Paladin 7 / Hexblade Warlock 5
  role: Melee crit-smite nova + own Hold Person
  character: Dark Urge (Half-Orc)
  played_by: Idan
- slot: 2
  nickname: Asterion
  class: Open Hand Monk 9 / Thief Rogue 3
  role: Stun/flurry striker + party thief + Bless battery
  character: Astarion
  played_by: Idan
- slot: 3
  nickname: Gale
  class: Draconic (Red) Sorcerer 11 / Fiend Warlock 1
  role: Fire striker + Command control + Haste engine
  character: Gale
  played_by: Alondra
- slot: 4
  nickname: Bonbon
  class: Swords Bard 11 / Fighter 1
  role: Ranged Acuity control + damage + face
  character: Bard
  played_by: Alondra
combat_gameplan:
  note: |-
    **This party is defined by four concentration lanes that never collide.** Everything else is detail; if you remember one thing, remember who is holding what.

    - **Charles → Hold Person.** Paralysed humanoids auto-crit, which is his whole nova. Nothing else ever takes his concentration.
    - **Gale → Twinned Haste.** Permanently on Charles and Bonbon. This is why Gale can never hold Bless, and why his Command matters — Command needs no concentration.
    - **Bonbon → Hold Monster** (or Fear). She covers the non-humanoid targets Charles's Hold Person cannot touch.
    - **Asterion → Bless**, cast off the Staff of Arcane Blessing. He is the only member with nothing else to concentrate on, which is the entire reason the job is his.

    Non-concentration effects stack freely on top: Phalar Shriek, Darkness Arrows, Command, Inquisitor's Might, Stunning Strike, Radiating Orb and Reverberation all cost nobody their lane.
  per_character:
  - character: Charles — the nova
    role: Melee crit-smite frontline that sets up its own auto-crits
    priority_actions: |-
      - **Build-defining gear:** Gloves of Battlemage's Power (Arcane Acuity → the Hold Person DC) · Luminous Armour (Radiant Shockwave → party-wide Radiating Orb) · Phalar Aluve (Shriek) · Risky Ring. All three of the first are LOCKED for the whole run.
      - **Build-defining spell:** Hold Person, free from the Vengeance oath at Paladin 5. Divine Smite is the payload; Inquisitor's Might is the per-hit Radiant that feeds the armour.
      - **Concentration:** Hold Person, always. Hunger of Hadar is the only substitute, and only when nothing is Holdable.
      - **Each round:** Inquisitor's Might (bonus action) → Booming Blade to build Acuity → Hold Person → dump the largest smites into guaranteed crits.
  - character: Asterion — the striker and the Bless battery
    role: Mobile unarmed stun-lock striker, party thief, Resonance Stone carrier
    priority_actions: |-
      - **Build-defining gear:** Gloves of Soul Catching (Act 3) · Graceful Cloth · Eversight Ring (lets him fight inside Charles's darkness) · Staff of Arcane Blessing as a pre-combat swap · carries the Resonance Stone within 9m of Charles.
      - **Build-defining spell:** none of his own — Bless, granted by the staff once per long rest. Stunning Strike is his real control.
      - **Concentration:** Bless, and nothing else ever competes for it.
      - **Each round:** Flurry of Blows with Stunning Strike on the priority target; Thief's second bonus action is what makes any utility he adds effectively free.
  - character: Gale — the engine
    role: Fire striker, non-concentration control, party Haste
    priority_actions: |-
      - **Build-defining gear:** Boots of Stormy Clamour + Gloves of Belligerent Skies (the Reverberation engine, 5–7 applications per Scorching Ray) · Potent Robe · Markoheshkir.
      - **Build-defining spell:** Twinned Haste, online at char 5. Scorching Ray is the damage; Command is the control that costs no concentration.
      - **Concentration:** Twinned Haste, permanently, on **Charles and Bonbon**.
      - **Each round:** keep Haste up, then Scorching Ray into a target inside Phalar Shriek's aura; Command when control beats damage.
  - character: Bonbon — the controller and face
    role: Ranged Acuity control, damage, all social checks
    priority_actions: |-
      - **Build-defining gear:** Helmet of Arcane Acuity + Band of the Mystic Scoundrel (bonus-action control) · dual hand crossbows · Gloves of Dexterity · Adamantine Splint Armour (crit immunity protects her concentration).
      - **Build-defining spell:** Hold Monster — the answer to every non-humanoid Charles cannot Hold. Command and Conjure Elemental are her non-concentration options.
      - **Concentration:** Hold Monster, or Hold Person on humanoids Charles is not already holding. MORE HOLD IS BETTER — a held target auto-crits and simply gets deleted, so prefer a second Hold over Fear in almost every fight.
      - **Each round:** open with a ranged **Slashing Flourish** to stack Arcane Acuity across multiple targets at once, then spend the bonus action on a control spell through the Band.
watch_outs:
- watch_out: Deepened Pact stacking is non-Honour only
  detail: Charles's three attacks depend on Paladin 5 Extra Attack stacking with Warlock 5 Deepened Pact, which only happens outside Honour Mode. This guide is explicitly non-Honour.
- watch_out: One Channel Oath charge per short rest
  detail: Charles gets exactly one. It buys Inquisitor's Might or Vow of Enmity, never both. From Act 2 the Risky Ring covers advantage, so it is always Inquisitor's Might.
- watch_out: Arcane Acuity decays when Charles is hit
  detail: Duration drops by 2 every time he takes damage, and his Hold Person DC rides it. Build stacks and cast Hold Person before the enemy's turn — Haste is what makes that possible in one turn.
- watch_out: Bless is once per long rest and hits only three targets
  detail: The Staff of Arcane Blessing's free cast is 1/long rest at level 1, so it covers three creatures. Give it to Charles, Gale and Bonbon and leave Asterion out. Do not let Gale consume the staff.
- watch_out: The Resonance Stone hurts the party too
  detail: It gives ALLIES Psychic Vulnerability and disadvantage on mental saves, which lands on the concentration Charles and Bonbon are both holding. Holster it against Psychic attackers and mental-save effects, and it has no effect on Undead or Constructs.
- watch_out: Temporary HP never stacks
  detail: Armour of Agathys, illithid Shield of Thralls and Fiendish Vigour's False Life all overwrite each other. Pick one, and cast Aid after it rather than before.
- watch_out: Charles is AC 17–18 all run
  detail: Locking Luminous Armour forfeits Adamantine Scale Mail's crit immunity and Helldusk Armour's AC 21. Mirror Image, Shield, Aura of Protection and the Act 3 Helm of Balduran are the compensation — and a crit roughly doubles a concentration save DC, so crit immunity matters more than usual here.
skills_face:
- duty: Face (Persuasion / Deception / Intimidation)
  who: Bonbon — Expertise ×4 plus Jack of All Trades
- duty: Sleight of Hand / Stealth
  who: Asterion (Expertise, Charlatan background)
- duty: Arcana / History
  who: Gale (Sage)
- duty: Athletics
  who: Bonbon (Fighter proficiency)
---
