---
roster:
- slot: 1
  nickname: Charles
  class: Oathbreaker Paladin 7 / Hexblade Warlock 5
  role: Melee crit-smite nova
  character: Dark Urge (Half-Orc)
  played_by: Idan
- slot: 2
  nickname: Asterion
  class: Open Hand Monk 9 / Thief Rogue 3
  role: Stun/flurry striker + party thief
  character: Astarion
  played_by: Idan
- slot: 3
  nickname: Gale
  class: Storm Sorcerer 10 / Tempest Cleric 2
  role: Wet+Lightning nuke + Haste engine
  character: Gale
  played_by: Alondra
- slot: 4
  nickname: Bonbon
  class: Swords Bard 11 / Fighter 1
  role: Control + damage + face
  character: Bard
  played_by: Alondra
act1_coverage:
  note: |-
    Minimum coverage, not every good spell. "Online" = character level in this multiclass order. Water, Darkness Arrows, Phalar Aluve and the martial control abilities cost no Concentration, so they stack on top of the three lanes below.

    Default hard-fight stack from char 6 — Charles: Bless · Gale: Twinned Haste · Bonbon: Hold Person/Hypnotic Pattern · Asterion: Stunning Strike. Four characters, zero collision.
  rows:
  - need: Wet / water setup
    owner: Gale
    online: 'Char 1–5 prepared Create Water (Tempest Cleric); char 6+ free Storm Spell after the respec.'
    backup: Mage Hand at char 2 (Gale) / char 5 (Bonbon) — drop a bottle in reach, Hand throws it for a 2m splash. Anyone can throw a bottle. Spell for clusters, bottle for one target.
    concentration: None — Create Water, Mage Hand and thrown bottles never touch Haste.
  - need: Guidance / ability checks
    owner: Gale to char 5; Silver Pendant after
    online: Char 1 from Gale; the pendant sits SW of the Grove from the start.
    backup: Pendant is a shared swap — wear it on whoever makes the check. Bonbon adds Enhance Ability at char 5.
    concentration: Both concentrate. Out-of-combat buffs only — never carry them into a fight.
  - need: Longstrider
    owner: Bonbon
    online: Char 2 (Bard 1)
    backup: All four after every long rest — ritual, no slot.
    concentration: None — lasts until long rest.
  - need: Bless
    owner: Gale char 1–5; Charles char 4+
    online: 'Gale preps it immediately; Charles gets Paladin casting at Paladin 2 (char 4).'
    backup: From char 6 Charles holds it, freeing Gale for Haste and Bonbon for control. Phalar Sing is the short-rest, concentration-free accuracy fallback.
    concentration: Yes, on Charles. Competes only with Hex, Divine Favour, Wrathful Smite or later Darkness.
  - need: Bane / save debuff
    owner: Gale char 4–5; then Charles's items
    online: 'Gale preps Cleric Bane once Bonbon has Hold Person (char 4). Phalar Aluve in the Underdark; Gloves of Baneful Striking on the Rosymorn trail.'
    backup: Bane, then Bonbon's Hold Person — different casters, both stick. Gale's WIS 12 is only DC 11–12, so pick low-CHA targets. Later, Phalar Shriek and Baneful Strike apply −1d4 saves concentration-free.
    concentration: Never coexists with Haste. Retire it at char 6 for Shriek/Baneful Strike.
  - need: Darkness / protected melee lane
    owner: Charles uses it; Bonbon fires the arrow
    online: Devil's Sight at char 2; farmed Darkness Arrows all of Act 1.
    backup: Arrow = 3m cloud, 3 turns, free. Bonbon places it, Charles swaps to Phalar and activates Shriek. Keep Gale and Asterion outside unless they see through magical Darkness.
    concentration: None from the arrow — Charles keeps Bless, Hex or Divine Favour.
  - need: Haste
    owner: Gale
    online: Char 6, at the pure Storm Sorcerer 6 respec.
    backup: Twinned on Charles + Asterion, 3 Sorcery Points — the default boss use. Protect it with CON proficiency, War Caster, Safeguard Shield, positioning and Shield.
    concentration: 'Yes. No Witch Bolt, Call Lightning or Sleet Storm while it is up; ending Haste makes both targets Lethargic.'
  - need: Single-target hard control
    owner: Bonbon
    online: 'Tasha''s at char 3, Hold Person at char 4; Asterion adds Stunning Strike at char 6.'
    backup: Hold Person is the humanoid auto-crit setup for Charles. Charles's Command and Asterion's Stun/Topple are free backups for non-humanoids or when Bonbon is busy.
    concentration: Bonbon holds Hold Person or Tasha's, never both. Asterion's control and Charles's Command are free.
  - need: Group control / caster denial
    owner: Bonbon for control; Gale for Counterspell
    online: Both at char 6 — Hypnotic Pattern and Counterspell.
    backup: Sleet Storm is excellent vs groups and enemy concentration but replaces Haste. Hypnotic Pattern preserves the Haste lane; Counterspell is a Reaction.
    concentration: Bonbon holds Hypnotic Pattern. Sleet Storm is instead of Haste, never alongside.
  - need: Emergency recovery
    owner: Bonbon
    online: Char 2 (Bard 1); Gale also has it while the Tempest level exists at char 1–5.
    backup: Stock Healing Potions and Revivify scrolls. Healing Word is a bonus-action pickup, not sustained healing.
    concentration: None.
act1_concentration:
  note: One effect per character — starting another ends the first, and ending Haste inflicts Lethargic. The defaults sit on three different casters.
  rows:
  - character: Charles
    default: Bless from char 4.
    alternatives: Hex for sustained damage · Divine Favour for radiant burst · Wrathful Smite for fear.
    rule: Pick one. Act 1 Darkness must come from an arrow so it does not evict the buff.
  - character: Asterion
    default: None — attacks, Stunning Strike, Flurry and the Giant Strength elixir are all free.
    alternatives: None in this build.
    rule: The safe martial control lane; he can never break an ally's spell.
  - character: Gale
    default: Twinned Haste from char 6; Bane at char 4–5 to set up Hold Person.
    alternatives: 'Pre-6 Bless or Witch Bolt. Post-6 Call Lightning for slot efficiency, Sleet Storm for terrain/caster control.'
    rule: 'After Haste, only non-concentration spells — Create Water, Lightning Bolt, Chromatic Orb, Shield, Counterspell.'
  - character: Bonbon
    default: Hold Person on a priority humanoid; Hypnotic Pattern on a group from char 6.
    alternatives: Tasha's early · Faerie Fire until replaced · Enhance Ability or Invisibility out of combat.
    rule: One control effect only. Guidance/Enhance Ability/Friends also concentrate — treat them as exploration modes.
act1_core_items:
  note: The plan-defining Act 1 assignments. Full route and checklist in Loot; complete loadouts on the character pages.
  rows:
  - item: Silver Pendant
    owner: Shared utility swap
    timing: Ravaged Beach / Harper outpost, before the Grove
    why: Keeps Guidance after Gale drops Tempest Cleric at char 6. Never feed it to Gale's orb.
  - item: Phalar Aluve
    owner: Charles
    timing: Underdark, near the Selûnite Outpost
    why: Bind and two-hand. Pre-cast Shriek for serious fights — 6m aura, −1d4 to enemy saves and attacks, +1d4 Thunder per damage instance. Amplifies Asterion's multi-hit turns and helps Hold Person land, with no Concentration. Stops if unequipped.
  - item: Titanstring Bow + Club of Hill Giant Strength
    wiki:
    - Titanstring Bow
    - Club of Hill Giant Strength
    owner: Bonbon
    timing: Zhentarim Basement + Arcane Tower
    why: Club sets STR 19 from the melee set; Titanstring adds the +4 STR mod to every ranged hit and Flourish projectile.
  - item: The Spellsparkler / Melf's First Staff
    wiki:
    - The Spellsparkler
    - Melf's First Staff
    owner: Gale
    timing: Waukeen's Rest reward / Blurg in the Underdark
    why: Spellsparkler for multi-hit and Lightning-Charge turns; Melf's +1 spell attack/DC when a save-based cast matters more.
  - item: Safeguard Shield
    owner: Gale
    timing: Dammon in the Emerald Grove
    why: +2 AC, +1 all saves — guards Twinned Haste. Civil Militia keeps shield proficiency after the respec.
  - item: Boots of Striding
    owner: Charles
    timing: Minthara in the Shattered Sanctum
    why: Starting a concentration buff grants Momentum; the boots block Prone and forced movement so it survives.
  - item: Graceful Cloth + Bracers of Defence
    wiki:
    - The Graceful Cloth
    - Bracers of Defence
    owner: Asterion
    timing: Rosymorn trail / Blighted Village cellar
    why: DEX 20, advantage on DEX checks, +2 AC unarmoured and shieldless — the Monk baseline. Offensive gloves swap in situationally.
  - item: The Protecty Sparkswall
    owner: Bonbon
    timing: Grymforge trapped bridge chest
    why: +1 Spell Save DC — the late-Act-1 bridge for Hold Person, Hypnotic Pattern, Fear, Slow and Glyph until Arcane Acuity.
synergies:
- name: Haste engine
  how: Gale Twinned-Hastes Charles and Asterion at char 6. Strongest on Charles's three-attack non-Honour turn and Asterion's Attack action.
- name: Control into melee
  how: Asterion opens bosses with Stunning Strike; Bonbon adds Hold Monster later. Stun grants advantage, Paralyzed auto-crits melee hits — Charles's smites finish.
- name: Wet lane
  how: Gale Wets a cluster away from the melee and doubles Lightning/Cold into it. Asterion's mobility keeps the lanes apart.
- name: Psychic package
  how: The late-Act-2 Resonance Stone triggers Charles's Shadow Blade respec. Asterion carries it for Manifestation of Mind and Psionic Overload, keeping Charles in the 9m aura to double Shadow Blade and Strange Conduit. Holster vs psychic or mental-save threats.
- name: Auras
  how: Aura of Protection covers frontline saves; Aura of Hate adds Charles's CHA to nearby melee-weapon damage — not to Asterion's unarmed strikes.
combat_gameplan:
  note: |-
    Two separated lanes — Charles and Asterion own a priority target in melee while Gale Wets and detonates a second cluster. Never put the melee in Electrified Water.

    Act 1 is still assembling: Asterion's Stun + Charles's Divine Smite are the boss plan, Gale's Lightning handles adds, Bonbon deals Titanstring damage. The Hold Monster + Acuity + Band loop starts in Acts 2–3.
  per_character:
  - character: Bonbon (Bard)
    role: Ranged Titanstring damage in Act 1; Arcane-Acuity controller later.
    priority_actions: 'Act 1 — Titanstring shots and ranged Slashing Flourish. Acts 2–3 — land a weapon hit, then Band of the Mystic Scoundrel for a bonus-action Enchantment/Illusion.'
  - character: Gale (Sorcerer)
    role: Haste engine and Wet/lightning AoE, aimed away from the melee lane.
    priority_actions: 'Char 6+ Twinned Haste Charles + Asterion when the fight warrants it. Otherwise Create Water then Lightning Bolt/Chromatic Orb. Protect Haste over a second concentration spell.'
  - character: Charles (Paladin)
    role: The held-target crit-smite finisher and Aura carrier.
    priority_actions: 'ACT 1–mid ACT 2 — bound two-handed Phalar, pre-cast Shriek, fight inside a Darkness Arrow cloud; Booming Blade for the Ring of Arcane Synergy, then GWM attacks and Divine Smites. LATE ACT 2+ — Shadow Blade main hand, Phalar off-hand, self-cast Darkness, stay in the Stone aura.'
  - character: Asterion (Monk)
    role: Unarmed Tavern-Brawler striker, Stun setter, thief, later Stone carrier.
    priority_actions: 'Drink Giant Strength, punch, spend Ki on Stunning Strike. Flurry Topple for Prone/advantage, Stagger to strip reactions. Thief 3 gives two Flurries per turn; Deathstalker Mantle repositions on a kill.'
  opening_rotation:
  - step: 1
    who: All — before combat
    action: 'ACT 1/early ACT 2 — Bonbon places a Darkness Arrow, Charles swaps to bound two-handed Phalar and activates Shriek. LATE ACT 2+ — Charles summons Shadow Blade with Phalar off-hand, Asterion carries the Stone nearby. Post-Tavern-Brawler, Asterion drinks Giant Strength and empties both melee hands. Bonbon equips club + Knife behind Titanstring and drinks Bloodlust when there are adds (Hill Giant Strength for a lone boss). Keep water bottles for Gale.'
  - step: 2
    who: Asterion
    action: Reach the priority target, punch, try Stunning Strike. Flurry Topple when Prone helps the melee line.
  - step: 3
    who: Gale
    action: Twinned-Haste Charles + Asterion, or Wet a separate add cluster and hit it with Lightning. Never electrify the ground under the melee.
  - step: 4
    who: Charles
    action: 'Hexblade''s Curse, then Booming Blade for the Ring of Arcane Synergy. Act 1 — two-handed Phalar GWM attacks plus Divine Smite. Post-respec — Shadow Blade attacks, Phalar off-hand swing when the bonus action is free; once Paladin 5 returns, each non-Honour Attack action is three Shadow Blade attacks.'
  - step: 5
    who: Bonbon
    action: Titanstring shots or Slashing Flourish. Once the control package is online, hit first to build Acuity, then a Band-enabled bonus-action Hold Monster/Command.
item_allocation:
- item: Act 1 — Charles
  to: Two-handed bound Phalar Aluve; Darkness Arrows; Dual Hand Crossbows +1; Luminous Armour; Boots of Striding; Amulet of Misty Step; Haste Helm; Gloves of Baneful Striking; Ring of Arcane Synergy; Strange Conduit Ring; temporary Great Weapon Master
  why: 'SELECTED DEFAULT. Hexblade binds the Versatile Phalar while two-handed, so char 6 takes GWM over Dual Wielder. Pre-cast Shriek, then use free Darkness Arrow clouds for Devil''s Sight advantage while concentrating on Bless, Divine Favour or Hex. Booming Blade triggers Arcane Synergy; Smite at char 4, Extra Attack at 7.'
- item: Act 2 — Charles (after Resonance Stone)
  to: 3d8 Shadow Blade main hand + Phalar Aluve off-hand; Resonance Stone aura; Dual Wielder; Risky Ring; Luminous Armour; Boots of Striding; Amulet of Misty Step; Strange Conduit Ring
  why: 'SELECTED DEFAULT after the Stone. Respec at char 9 to Warlock 5 / Paladin 4 — Dual Wielder replaces GWM, Savage Attacker second, Shadow Blade lands at 3d8 as the bound main hand, Phalar stays off-hand so Shriek runs. Charles can now self-cast Darkness; Asterion keeps the Stone within 9m.'
- item: Act 1 — Asterion
  to: Empty melee hands; Dual Hand Crossbows +1; Graceful Cloth; Bracers of Defence; Disintegrating Night Walkers; Sentient Amulet; Ring of Protection; Crusher's Ring; Deathstalker Mantle
  why: 'SELECTED DEFAULT from char 5 — empty hands keep Attack/Extra Attack unarmed so Tavern Brawler applies. Corellon''s Grace is a levels 2–4 weapon only. Swap Bracers for Sparkle Hands or Cinder and Sizzle for damage, Graceful Cloth for Kushigo in a Patient-Defence fight. Keep Gloves of Thievery and Smuggler''s Ring as theft swaps.'
- item: Act 1 — Gale
  to: Bow of Awareness; The Spellsparkler; The Shadespell Circlet; Boots of Stormy Clamour; Gloves of Belligerent Skies; Pearl of Power Amulet; Safeguard Shield
  why: 'SELECTED DEFAULT. Bow of Awareness fills the unused ranged slot for +1 Initiative so Gale establishes Haste or Wet first. Safeguard''s +1 saves protects Haste; Tempestuous Magic covers the Haste Helm''s mobility. Melf''s First Staff is the save-DC alternative.'
- item: Act 1 — Bonbon
  to: Titanstring Bow + Club of Hill Giant Strength + Knife of the Undermountain King + Bloodlust; Gloves of Dexterity; The Protecty Sparkswall; Diadem of Arcane Synergy; Caustic Band; Broodmother's Revenge
  why: 'SELECTED DEFAULT. Light Club and Knife share the melee set without a feat — Club gives STR 19, Knife lowers the crit threshold for Titanstring. Bloodlust buys an extra Action after a kill; Hill Giant elixir for a boss with no adds. Protecty raises control DC, and a landed condition lights up the Diadem.'
- item: Risky Ring
  to: Charles
  why: Act 2 permanent attack advantage and crit-fishing; Aura of Protection offsets the save penalty.
- item: Resonance Stone
  to: Asterion
  why: Act 2 psychic multiplier for his many hits, and the trigger for Charles's Shadow Blade respec. Keep Charles inside the 9m aura; holster vs psychic damage or dangerous mental saves.
- item: Helmet of Arcane Acuity + Band of the Mystic Scoundrel
  wiki:
  - Helmet of Arcane Acuity
  - Band of the Mystic Scoundrel
  to: Bonbon
  why: Acts 2–3 control engine — weapon hits build spell DC, the Band turns Enchantment/Illusion into bonus actions.
- item: Markoheshkir + Amulet of the Devout
  wiki:
  - Markoheshkir
  - Amulet of the Devout
  to: Gale
  why: Act 3 lightning empower, spell DC, and a second Destructive Wrath charge.
- item: Amulet of Greater Health
  to: Bonbon
  why: Act 3 CON 23 and CON-save advantage armour the Hold Monster concentration.
progression:
- act: 1
  paladin: 'Warlock 2 for Hexblade + Devil''s Sight, then Paladin 1–5 — Smite at char 4, temporary GWM at 6, Extra Attack at 7. Bind and two-hand Phalar, Darkness from farmed arrows, oath intact.'
  asterion: Rogue 1 for Expertise, then Open Hand Monk. Tavern Brawler at char 5, Stunning Strike at 6.
  sorcerer: Tempest Cleric 1 / Storm Sorcerer 4 is a bridge only. Respec to pure Storm Sorcerer at char 6 for the on-time spike and CON saves.
  bard: Fighter 1 then Swords Bard. Titanstring damage first — the Acuity loop comes later.
- act: 2
  paladin: 'Two-handed Phalar/GWM and Paladin 6 through most of Act 2. At the late-act Stone, respec at char 9 to Warlock 5 / Paladin 4 — Dual Wielder over GWM, Savage Attacker second, 3d8 Shadow Blade main hand, Phalar off-hand. Paladin 5 returns at char 10 for the three-attack stack. Break the fresh oath → Oathbreaker.'
  asterion: Monk 6 features, Graceful Cloth/Bracers, the Resonance Stone late in the act.
  sorcerer: Storm Sorcerer 6 — Create Water, Call Lightning, Sleet Storm, Heart of the Storm.
  bard: Helmet of Arcane Acuity starts the ranged-hit-to-control transition.
- act: 3
  paladin: Shadow Blade + Phalar is the endgame package; Savage Attacker improves both weapons and every Smite.
  asterion: Monk 9 / Thief 3 — double Flurry and Ki Resonation.
  sorcerer: Tempest Cleric 2 at char 11–12 for Destructive Wrath.
  bard: Band of the Mystic Scoundrel completes the loop.
watch_outs:
- watch_out: Modded Hag's Hair assumption
  detail: Every party member gets a Hair. Charles, Bonbon and Gale spend it on CHA 17→18; Asterion on DEX 17→18. Vanilla has exactly one.
- watch_out: Monk equipment rule
  detail: Unarmoured and shieldless, always. From Tavern Brawler on, both melee hands stay empty — a monk weapon keeps Flurry and special unarmed commands, but ordinary Attack/Extra Attack swings it and loses Tavern Brawler.
- watch_out: Resonance Stone debuff
  detail: The aura makes nearby creatures psychic-vulnerable and disadvantaged on mental saves — allies included. Keep it inside Aura of Protection, holster vs psychic/mind enemies, and do not count on it after Act 2.
- watch_out: Charles's Resonance respec and oath
  detail: 'Keep the Vengeance oath intact so Withers respecs normally. At the Stone: respec at char 9 to Warlock 5 / Paladin 4, GWM → Dual Wielder, Savage Attacker as the Paladin feat, then break the new oath. Break it early and you must pay the Oathbreaker Knight to restore it first.'
- watch_out: Deepened Pact (non-Honour)
  detail: Paladin 5 Extra Attack and Warlock 5 Deepened Pact stack only outside Honour Mode. This guide is explicitly non-Honour.
- watch_out: Undead / crit-immune bosses
  detail: Hold Monster and Command do not control undead, and crit immunity kills the held-target plan. Use Hypnotic Pattern/Slow. Charles keeps the radiant Smite bonus vs Undead/Fiends; Gale and Asterion fall back on lightning/force and radiant Manifestation.
skills_face:
- duty: Face (Persuasion / Deception / Intimidation)
  who: Bonbon (Expertise + Friends)
- duty: Sleight of Hand / Stealth
  who: Asterion (Rogue 1 Expertise)
- duty: Investigation / Perception
  who: Asterion (proficient; no second Expertise pair in this Rogue 3 build)
- duty: Athletics
  who: Bonbon (Fighter proficiency)
- duty: Arcana / History
  who: Gale (Sage)
---
