---
roster:
- slot: 1
  nickname: Charles
  class: Oath of Vengeance Paladin 6 / Hexblade Warlock 6
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
    **Four concentration lanes, never crossed.** If you remember one thing, remember who holds what.

    - **Charles → Hold Person.** A Paralysed target is an auto-crit for ANY attack within 3 m. Nothing else takes his concentration; Hunger of Hadar only when nothing is Holdable.
    - **Gale → Twinned Haste** on Charles and Bonbon, every fight. Command is his control because it needs no concentration.
    - **Bonbon → Hold Monster** (or Hold Person on a second humanoid). She covers everything Charles cannot Hold.
    - **Asterion → Bless** from the Staff of Arcane Blessing, or Celestial Haste from Gontr Mael in Act 3. He is the only member with a free lane.

    **Opener.** Start every fight you can see coming from Stealth: Surprised enemies skip their first turn and the Holds land before anything moves. Gale pre-casts Twinned Haste before initiative. Hide outside vision cones and release Shift so only the hider rolls.

    **Standing rules.**
    - Phalar Aluve is ALWAYS Shriek, never Sing.
    - Gale's Plant Growth (Armour of Landfall, once per short rest) goes under Charles's Hunger of Hadar. No Fireball, Scorching Ray or Heat into that zone: fire burns Plant Growth off. Bonbon layers Silence or her own Plant Growth there on non-Holdable fights.
    - Arsonist's Oil vulnerability, boss turns only: throw an Elixir of Fire Resistance at the target, hit it with Bonbon's oiled weapon, throw a second elixir. It is now Vulnerable to fire for Gale's rays.
    - Radiant Shockwave (Luminous Armour) hits non-allies only, neutrals included. Asterion stands on the Held target freely; watch neutral NPCs.
    - Snowburst ice: Bonbon shoots the back line first so no ice lands under Charles or Asterion. Gale's fire melts it.
    - Mirror of Loss (Act 3): each character gets ONE DC 25 Religion check (fail = locked out) then a 60% roll. Enhance Ability from Bonbon, Guidance from the Silver Pendant, quicksave before each prayer.

    Non-concentration effects stack freely on top: Shriek, Darkness Arrows, Command, Inquisitor's Might, Stunning Strike, Radiating Orb and Reverberation cost nobody their lane.
  per_character:
  - character: Charles — the nova
    role: Melee crit-smite frontline that sets up its own auto-crits
    priority_actions: |-
      - **Build-defining gear:** Gloves of Battlemage's Power (Arcane Acuity → the Hold Person DC) · Luminous Armour · a shield from the Grove on (+2 Shield → Adamantine → Walking Fortress) · Alert. The first two are LOCKED all run; never two-handed, never dual-wielded.
      - **Build-defining spell:** Hold Person, free from the Vengeance oath at Paladin 5; from an L3 pact slot it Holds two humanoids. Divine Smite is the payload; Inquisitor's Might is the per-hit Radiant that feeds the armour.
      - **Concentration:** Hold Person, always. Hunger of Hadar only when nothing is Holdable. Cast Aura of Protection once when gained (char 8, again at char 11 after the Stone respec); allies stay inside its 3 m.
      - **Each round:** Hexblade's Curse the nova target on the set-up turn → Inquisitor's Might (bonus action) → Booming Blade for Acuity → Hold Person → the largest smites into the guaranteed crits.
  - character: Asterion — the striker and the Bless battery
    role: Mobile unarmed stun-lock striker, party thief, Resonance Stone carrier
    priority_actions: |-
      - **Build-defining gear:** Gloves of Soul Catching (Act 3) · Graceful Cloth · Eversight Ring (fights unblinded inside Charles's Darkness) · Staff of Arcane Blessing as a pre-combat swap · Gontr Mael (Act 3) · the Resonance Stone within 9 m of Charles.
      - **Boots:** Night Walkers Acts 1–2, Kushigo Act 3. Charles's Stormy Clamour in fights where Asterion inflicts more conditions than Charles.
      - **Build-defining spell:** none of his own; Bless comes from the staff. Stunning Strike is his control. Spikes: Fast Hands (second Flurry) at char 9, Alert at char 11, Ki Resonation at char 12. ASCEND after Cazador: +1d10 Necrotic on every punch.
      - **Concentration:** Bless, or Celestial Haste from Gontr Mael in Act 3. Each is once per long rest, so a two-fight day gets one of each; he is the only member Gale never Hastes.
      - **Each round:** Flurry of Blows with Stunning Strike on the priority target; Topple a concentrating caster (Prone ends concentration, no save). End the turn 50 ft from melee enemies; Dash out when a Stun fails. Thief's second bonus action makes any utility free.
  - character: Gale — the engine
    role: Fire striker, non-concentration control, party Haste
    priority_actions: |-
      - **Build-defining gear:** Gloves of Belligerent Skies + Spineshudder Amulet (Reverberation per ray) · Hat of Fire Acuity · Markoheshkir + Rhapsody · Armour of Landfall (Plant Growth, CON-save advantage). Boots: Evasive Shoes Act 2, Night Walkers Act 3. · AWAKENED from the Crèche Zaith'isk (Act 1): every illithid power is a bonus action.
      - **Drakethroat Glaive:** once per long rest, Twinned Draconic Elemental Weapon, COLD every day, on Bonbon's bow and Charles's blade.
      - **Build-defining spell:** Twinned Haste, online at char 5. Scorching Ray is the damage; Command is the control that costs no concentration.
      - **Concentration:** Twinned Haste on **Charles and Bonbon**, pre-cast before initiative whenever the fight is visible.
      - **Each round:** keep Haste up, then Scorching Ray into Shriek's aura, standing within 3 m of a Held target for crits; Command when control beats damage. Fire never into the Plant Growth zone; Heat goes into Fireball, not Scorching Ray. **Bonus action (Awakened):** Black Hole to the Held target's feet every turn from Act 3; Perilous Stakes on the boss on turn 2 once Scorching Ray has capped Acuity; Stage Fright when a mob threatens Haste; Force Tunnel when melee reaches him.
  - character: Bonbon — the controller and face
    role: Ranged Acuity control, damage, all social checks
    priority_actions: |-
      - **Build-defining gear:** Helmet of Arcane Acuity + Band of the Mystic Scoundrel (bonus-action control) · Titanstring Bow Acts 1–2 on a Hill Giant elixir every long rest, The Dead Shot from Act 3 on Vigilance · Gloves of Dexterity ALL GAME · Alert at char 9.
      - **Gear by act:** melee set never swung: Knife + Safeguard Shield, then Phalar Aluve + Sentinel Shield from Moonrise (Ketheric's Shield the +1 DC option) · rings: Caustic Band + Snowburst (Act 2), Band + Ring of Feywild Sparks (Act 3) · Adamantine Splint, then Helldusk Armour.
      - **Build-defining spell:** Hold Monster for every non-humanoid Charles cannot Hold. Command, Plant Growth and Conjure Elemental (Air Myrmidon before the first fight, slot refunded by Spellcrux) need no concentration.
      - **Concentration:** Hold Monster, or Hold Person on a humanoid Charles is not holding. MORE HOLD IS BETTER: a Held target auto-crits and gets deleted, so prefer a second Hold over Fear. Silence over Hunger of Hadar on non-Holdable fights.
      - **Each round:** ranged **Slashing Flourish** to stack Acuity (two Arrows of Many Targets cap it on turn 1), then a Band control spell as the bonus action. From the Stone: turn 1 Shriek with the Haste action from 3–6 m, then Flourish.
      - **Never:** an Arrow of Darkness before her last attack (aim it at the ground), or any shot into Charles's Darkness (Keen Attack switches off under disadvantage).
watch_outs:
- watch_out: Deepened Pact stacking is non-Honour only
  detail: Charles's three attacks need Paladin 5 Extra Attack stacking with Warlock 5 Deepened Pact, which only happens outside Honour Mode. This guide is non-Honour.
- watch_out: One Channel Oath charge per short rest
  detail: Charles gets exactly one. It buys Inquisitor's Might or Vow of Enmity, never both. From Act 2 the Risky Ring covers advantage, so it is always Inquisitor's Might.
- watch_out: Arcane Acuity decays when Charles is hit
  detail: Duration drops by 2 every time he takes damage, and his Hold Person DC rides it. Build stacks and cast Hold Person before the enemy turn; Haste makes that one turn.
- watch_out: Bless is once per long rest and hits only three targets
  detail: The Staff of Arcane Blessing's free cast is level 1, so three creatures. Bless Charles, Gale and Bonbon and leave Asterion out. Do not let Gale consume the staff.
- watch_out: The Resonance Stone hurts the party too
  detail: It gives ALLIES Psychic Vulnerability and disadvantage on mental saves, which lands on the concentration Charles and Bonbon hold. Holster it against Psychic attackers and mental-save effects; no effect on Undead or Constructs.
- watch_out: Temporary HP never stacks
  detail: Armour of Agathys, illithid Shield of Thralls, Fiendish Vigour's False Life and the Elixir of Heroism all overwrite each other. Pick one, and cast Aid after it rather than before.
- watch_out: Charles is AC 19–20 behind a shield
  detail: Luminous Armour caps the chest at 17, so the shield carries the rest (+2 Shield → Adamantine Shield → Walking Fortress) and Mirror Image, Shield and Aura of Protection sit on top. Crit immunity matters because a crit roughly doubles a concentration save DC.
- watch_out: Shriek is Bonbon's job from the Stone
  detail: 'Phalar Aluve joins her melee set at the Stone respec; ALWAYS Shriek. The 6 m aura sits on the WIELDER and ends if the sword is unequipped, so she stands 3–6 m from the targets. Costs an Action: the Haste action on turn 1, or pre-cast from stealth.'
skills_face:
- duty: Face (Persuasion / Deception / Intimidation)
  who: Bonbon — Expertise ×4 plus Jack of All Trades
- duty: Sleight of Hand / Stealth
  who: Asterion (Expertise, Charlatan background)
- duty: Arcana / History
  who: Gale (Sage)
- duty: Athletics
  who: Asterion (Rogue 1 proficiency, on the Giant Strength elixir); Bonbon (Fighter proficiency)
---
