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
    This is the party's minimum coverage, not a list of every good spell. "Online" is character level for this exact multiclass order. Water, Darkness Arrows, Phalar Aluve, and the martial control abilities do not use Concentration, so they can coexist with the three combat concentration lanes below.

    Default hard-fight stack from character level 6: Charles holds Bless, Gale holds Twinned Haste, Bonbon holds Hold Person/Hypnotic Pattern, and Asterion uses Stunning Strike. Each effect belongs to a different character, so there is no concentration collision.
  rows:
  - need: Wet / water setup
    owner: Gale
    online: 'Char 1–5: prepared Create Water from Tempest Cleric. Char 6+: free Storm Spell after the pure-Sorcerer respec.'
    backup: 'Gale has Mage Hand at char 2 and Bonbon at char 5. Drop a water bottle where the Hand can reach it, then use the Hand''s Throw for a 2m Wet splash; any party member can also throw a bottle. Use the spell for clusters and the bottle for one target or when saving a slot.'
    concentration: None — Create Water, Mage Hand, and throwing water do not compete with Haste.
  - need: Guidance / ability checks
    owner: 'Gale through char 5; Silver Pendant after the char-6 respec'
    online: Char 1 from Gale; the pendant is available immediately southwest of the Grove.
    backup: 'Keep the Silver Pendant as a shared exploration swap, usually on the character making the check. Bonbon also takes Enhance Ability at char 5 for advantage on a chosen ability when a check matters.'
    concentration: 'Guidance and Enhance Ability each use Concentration. They are out-of-combat check buffs: do not carry them into a fight expecting Gale''s Haste or Bonbon''s control to remain.'
  - need: Longstrider
    owner: Bonbon
    online: Char 2 (Bard 1)
    backup: Cast on all four party members after each long rest; ritual casting outside combat costs no spell slot.
    concentration: None — lasts until long rest.
  - need: Bless
    owner: 'Gale at char 1–5; Charles at char 4+'
    online: 'Gale prepares it immediately; Charles gains Paladin spellcasting at Paladin 2 (char 4).'
    backup: 'From char 6 onward, Charles is the default Bless holder so Gale can hold Haste and Bonbon can hold control. Phalar Sing is a short-rest, concentration-free accuracy fallback when Shriek is not the better mode.'
    concentration: 'Yes, on Charles in the default stack. It competes only with Charles''s Hex, Divine Favour, Wrathful Smite, or later self-cast Darkness.'
  - need: Bane / save debuff
    owner: 'Gale at char 4–5; Charles from the relevant Act 1 items'
    online: 'When Bonbon gains Hold Person at char 4, Gale can prepare Cleric Bane for the two-level bridge. Phalar Aluve arrives in the Underdark; Gloves of Baneful Striking arrive on the Rosymorn trail.'
    backup: 'Bane first, then Bonbon casts Hold Person: different casters, so both Concentration effects coexist. Gale''s WIS 12 makes Bane only DC 11–12 in this window, so prefer low-CHA targets. Once available, Phalar Shriek applies −1d4 to nearby enemy saves without an initial save, and Charles''s Baneful Strike applies another concentration-free −1d4 save penalty for 2 turns after his weapon hit.'
    concentration: 'Bane uses Gale''s Concentration and never coexists with his Haste. At char 6, retire prepared Bane and use Shriek/Baneful Strike while Gale holds Twinned Haste.'
  - need: Darkness / protected melee lane
    owner: 'Charles uses it; Bonbon preferably fires the Arrow of Darkness'
    online: 'Devil''s Sight at char 2; use farmed Darkness Arrows throughout Act 1.'
    backup: 'The arrow makes a 3m cloud for 3 turns without Concentration. Bonbon places it before Charles swaps to Phalar and activates Shriek; keep Gale and Asterion outside unless they can see through magical Darkness.'
    concentration: None from the arrow — Charles remains free to hold Bless, Hex, or Divine Favour.
  - need: Haste
    owner: Gale
    online: Char 6, when the early Cleric/Sorcerer bridge respecs to pure Storm Sorcerer 6.
    backup: 'Twinned Spell targets Charles + Asterion for 3 Sorcery Points. This is the default boss-fight use of Gale''s concentration; protect it with Sorcerer-first CON proficiency, War Caster, Safeguard Shield, positioning, and Shield.'
    concentration: 'Yes. Gale must not cast Witch Bolt, Call Lightning, or Sleet Storm while maintaining Haste; ending Haste makes both targets Lethargic.'
  - need: Single-target hard control
    owner: Bonbon
    online: 'Tasha''s Hideous Laughter at char 3; Hold Person at char 4. Asterion adds Stunning Strike at char 6.'
    backup: 'Hold Person is the humanoid auto-crit setup for Charles. Charles''s Command (char 4) and Asterion''s Stunning Strike/Topple are non-concentration backups; use them when Bonbon is already holding another control spell or the target is not a humanoid.'
    concentration: 'Bonbon concentrates on Hold Person or Tasha''s, never both. Asterion''s control and Charles''s Command use no Concentration.'
  - need: Group control / caster denial
    owner: 'Bonbon for control; Gale for Counterspell'
    online: 'Bonbon gets Hypnotic Pattern at char 6; Gale learns Counterspell at char 6.'
    backup: 'Gale''s free Sleet Storm is excellent against groups and enemy concentration, but it replaces Haste. Bonbon''s Hypnotic Pattern preserves Gale''s Haste lane; Counterspell is a Reaction and consumes no Concentration.'
    concentration: 'Bonbon holds Hypnotic Pattern. Gale holds Haste; use Sleet Storm instead of Haste, not alongside it.'
  - need: Emergency recovery
    owner: Bonbon
    online: Char 2 (Bard 1); Gale also has it while Tempest Cleric is present at char 1–5.
    backup: Stock Healing Potions and Revivify scrolls; Healing Word is for a bonus-action ranged pickup, not sustained healing.
    concentration: None.
act1_concentration:
  note: One concentration effect per character. Starting another immediately ends the first; Haste also inflicts Lethargic when it ends. The defaults deliberately occupy three different casters.
  rows:
  - character: Charles
    default: Bless from char 4 onward.
    alternatives: Hex for repeated personal damage; Divine Favour for short radiant burst; Wrathful Smite for fear.
    rule: 'Pick one. Act 1 Darkness must come from an arrow so it does not evict the chosen buff.'
  - character: Asterion
    default: None — his attacks, Stunning Strike, Flurry variants, and Giant Strength elixir need no Concentration.
    alternatives: None in the selected build.
    rule: He is the safe martial control lane and cannot break another party member's spell by acting.
  - character: Gale
    default: Twinned Haste from char 6 onward; at char 4–5 use Bane when setting up Bonbon's Hold Person.
    alternatives: 'Before char 6: Bless or Witch Bolt. After char 6: Call Lightning for slot-efficient damage or Sleet Storm for terrain/caster control.'
    rule: 'After casting Haste, cast only non-concentration spells: Create Water, Lightning Bolt, Chromatic Orb, Shield, and Counterspell are all safe.'
  - character: Bonbon
    default: Hold Person against a priority humanoid; Hypnotic Pattern against a group from char 6.
    alternatives: Tasha's Hideous Laughter early; Faerie Fire before it is replaced; Enhance Ability or Invisibility outside combat.
    rule: Choose exactly one control effect. Guidance/Enhance Ability/Friends are also Concentration and should be treated as exploration modes.
act1_core_items:
  note: These are the plan-defining Act 1 assignments. The Loot tab keeps the full route and checklist; personal character pages contain the complete slot-by-slot loadouts.
  rows:
  - item: Silver Pendant
    owner: Shared utility swap
    timing: Ravaged Beach / Harper outpost, before the Grove
    why: Keeps Guidance available after Gale drops Tempest Cleric at character level 6. Do not feed it to Gale's orb.
  - item: Phalar Aluve
    owner: Charles
    timing: Underdark, near the Selûnite Outpost
    why: 'Bind and wield it two-handed. Pre-activate Shriek for serious fights: its 6m aura penalises enemy saves/attacks by 1d4 and adds 1d4 Thunder whenever the affected enemy is damaged, amplifying Asterion''s multi-hit turns and helping Bonbon''s Hold Person land. It replaces Gale''s short-lived Bane duty without using Concentration and stops if the sword is unequipped.'
  - item: Titanstring Bow + Club of Hill Giant Strength
    wiki:
    - Titanstring Bow
    - Club of Hill Giant Strength
    owner: Bonbon
    timing: Zhentarim Basement + Arcane Tower
    why: The club sets STR 19 while sitting in Bonbon's melee set; Titanstring adds the +4 STR modifier to every ranged hit and Slashing-Flourish projectile.
  - item: The Spellsparkler / Melf's First Staff
    wiki:
    - The Spellsparkler
    - Melf's First Staff
    owner: Gale
    timing: Waukeen's Rest reward / Blurg in the Underdark
    why: Use Spellsparkler for multi-hit/Lightning-Charge turns and Melf's +1 spell attack/DC when Haste, Lightning Bolt, or control reliability matters more.
  - item: Safeguard Shield
    owner: Gale
    timing: Dammon in the Emerald Grove
    why: +2 AC and +1 to all saves; the save bonus directly protects Twinned Haste, and Gale's Human Civil Militia keeps shield proficiency after the respec.
  - item: Boots of Striding
    owner: Charles
    timing: Minthara in the Shattered Sanctum
    why: Starting Bless/Hex/Divine Favour grants Momentum, and the boots prevent Prone or forced movement while concentrating so the frontline buff is harder to disrupt.
  - item: Graceful Cloth + Bracers of Defence
    wiki:
    - The Graceful Cloth
    - Bracers of Defence
    owner: Asterion
    timing: Rosymorn trail / Blighted Village cellar
    why: DEX 20 plus advantage on DEX checks and +2 AC while unarmoured/shieldless; this is the Monk/thief baseline, with offensive gloves swapped in only when appropriate.
  - item: The Protecty Sparkswall
    owner: Bonbon
    timing: Grymforge trapped bridge chest
    why: +1 Spell Save DC is the late-Act-1 bridge that makes Hold Person, Hypnotic Pattern, Fear, Slow, and Glyph of Warding more reliable before Arcane Acuity arrives.
synergies:
- name: Haste engine
  how: Gale Twinned-Hastes Charles and Asterion at character level 6, when the early Cleric bridge respecs to pure Storm Sorcerer 6. The extra Actions are strongest on Charles's three-attack non-Honour turn and Asterion's Attack action.
- name: Control into melee
  how: Asterion opens bosses with Stunning Strike; Bonbon later adds Hold Monster. Stun grants advantage; Paralyzed from Hold Monster makes melee hits crit automatically, turning Charles's smites into the finisher.
- name: Wet lane
  how: Gale applies Wet to a cluster away from the melee, then doubles Lightning/Cold damage into it. Asterion uses mobility to keep the melee lane physically separate.
- name: Psychic package
  how: Late in Act 2, the Resonance Stone pickup triggers Charles's Shadow Blade respec. Asterion carries it for Manifestation of Mind and Psionic Overload across multiple Flurry hits while keeping Charles in the 9m aura to double Shadow Blade and Strange Conduit; holster it against psychic or mental-save threats.
- name: Auras
  how: Charles's Aura of Protection protects the frontline's saving throws; Aura of Hate adds his CHA modifier to nearby melee-weapon damage, not to Asterion's unarmed strikes.
combat_gameplan:
  note: |-
    Use two separated lanes: Charles and Asterion own a priority target in melee, while Gale Wets and detonates a second cluster. Do not put the melee in Electrified Water.

    In Act 1, the party is still assembling: Asterion's Stun and Charles's Divine Smite are the boss plan, Gale's Lightning/Spellsparkler handle the add lane, and Bonbon deals Titanstring damage. The Hold Monster + Acuity + Band loop begins in Acts 2–3, not in early Act 1.
  per_character:
  - character: Bonbon (Bard)
    role: Ranged Titanstring damage in Act 1; later the Arcane-Acuity controller.
    priority_actions: 'Act 1: use Titanstring shots and ranged Slashing Flourish when College of Swords is online. Acts 2–3: land a weapon hit before using the Band of the Mystic Scoundrel for a bonus-action Enchantment/Illusion control spell.'
  - character: Gale (Sorcerer)
    role: Haste engine and Wet/lightning AoE, always aimed away from the melee lane.
    priority_actions: 'At character level 6 (the pure-Sorcerer-6 respec), Twinned Haste Charles + Asterion when the encounter warrants it. In other fights, Create Water then Lightning Bolt/Chromatic Orb; keep Haste concentration protected rather than trying to maintain another concentration spell.'
  - character: Charles (Paladin)
    role: The held-target crit-smite finisher and Aura carrier.
    priority_actions: 'ACT 1 through most of ACT 2 — bind and two-hand Phalar Aluve, activate Shriek before combat, and fight inside a concentration-free Darkness Arrow cloud with Devil''s Sight; use Booming Blade to activate the Ring of Arcane Synergy, then GWM attacks and Divine Smites. LATE ACT 2+ — after the Resonance Stone respec, summon/bind Shadow Blade in the main hand, off-hand Phalar with Dual Wielder, self-cast Darkness, and stay in Asterion''s Stone aura.'
  - character: Asterion (Monk)
    role: Unarmed Tavern-Brawler striker, Stun setter, mobile thief, and later Resonance Stone carrier.
    priority_actions: 'Drink Giant Strength, make unarmed attacks, and spend Ki on Stunning Strike against the priority target. Use Flurry: Topple for Prone/advantage or Stagger to remove reactions. At Thief 3, two bonus actions enable two Flurries per turn; Deathstalker Mantle then provides repositioning on a kill.'
  opening_rotation:
  - step: 1
    who: All — before combat
    action: 'ACT 1/early ACT 2: Bonbon preferably places a Darkness Arrow first, then Charles switches to bound two-handed Phalar Aluve and activates Shriek. LATE ACT 2+: Charles summons/binds Shadow Blade and off-hands Phalar, while Asterion carries the Resonance Stone nearby. Once Tavern Brawler is online, Asterion drinks Giant Strength and leaves both melee hands empty; Bonbon equips the Hill Giant club main hand + Knife of the Undermountain King off-hand behind Titanstring and drinks Bloodlust for encounters with adds (swap to Hill Giant Strength for a single boss). Keep water bottles for Gale''s add lane.'
  - step: 2
    who: Asterion
    action: 'Reach the priority target, make unarmed attacks, and try Stunning Strike. Follow with Flurry: Topple when Prone will help the rest of the melee line.'
  - step: 3
    who: Gale
    action: 'Either Twinned-Haste Charles + Asterion, or Wet a separate add cluster and strike it with Lightning. Never electrify the ground beneath the melee.'
  - step: 4
    who: Charles
    action: 'Hexblade''s Curse the priority target and open with Booming Blade to activate the Ring of Arcane Synergy. In Act 1, follow with two-handed Phalar GWM attacks and Divine Smite. After the Act-2 respec, use Shadow Blade for the pact-weapon attacks and make the Phalar off-hand attack when the bonus action is free; once Paladin 5 returns, each non-Honour Attack action makes three Shadow Blade attacks.'
  - step: 5
    who: Bonbon
    action: 'Use Titanstring ranged attacks or Slashing Flourish. Once the late control package is online, hit first to build Acuity, then use the Band-enabled bonus-action Hold Monster/Command.'
item_allocation:
- item: Act 1 — Charles
  to: Two-handed bound Phalar Aluve; Darkness Arrows; Dual Hand Crossbows +1; Luminous Armour; Boots of Striding; Amulet of Misty Step; Haste Helm; Gloves of Baneful Striking; Ring of Arcane Synergy; Strange Conduit Ring; temporary Great Weapon Master
  why: 'SELECTED DEFAULT. Hexblade can bind the versatile Phalar while it is wielded in both hands, so character level 6 takes GWM instead of Dual Wielder. Pre-cast Shriek, then use concentration-free Darkness Arrow clouds for Devil''s Sight advantage while Charles concentrates on Bless, Divine Favour, or Hex. Booming Blade activates Arcane Synergy; Smite comes online at character level 4 and Extra Attack at 7.'
- item: Act 2 — Charles (after Resonance Stone)
  to: 3d8 Shadow Blade main hand + Phalar Aluve off-hand; Resonance Stone aura; Dual Wielder; Risky Ring; Luminous Armour; Boots of Striding; Amulet of Misty Step; Strange Conduit Ring
  why: 'SELECTED DEFAULT after the late-Act-2 Stone pickup. Usually respec at character level 9 to Warlock 5 / Paladin 4: Dual Wielder replaces temporary GWM, Savage Attacker becomes the second feat, Shadow Blade immediately scales to 3d8 and becomes the bound main attacker, and Phalar stays equipped off-hand so Shriek remains active. Charles may now self-cast Darkness; Asterion carries the Stone within 9m to double Shadow Blade and Strange Conduit Psychic damage when the encounter is safe for the aura.'
- item: Act 1 — Asterion
  to: Empty melee hands; Dual Hand Crossbows +1; Graceful Cloth; Bracers of Defence; Disintegrating Night Walkers; Sentient Amulet; Ring of Protection; Crusher's Ring; Deathstalker Mantle
  why: 'SELECTED DEFAULT from character level 5 onward: empty hands keep ordinary Attack/Extra Attack strikes unarmed so Tavern Brawler applies. Corellon''s Grace is an early levels 2–4 weapon only. Swap Bracers to Sparkle Hands or Gloves of Cinder and Sizzle for damage, and Graceful Cloth to Armour of Uninhibited Kushigo for a Patient-Defence counter fight. Keep Gloves of Thievery and Smuggler''s Ring as theft swaps.'
- item: Act 1 — Gale
  to: Bow of Awareness; The Spellsparkler; The Shadespell Circlet; Boots of Stormy Clamour; Gloves of Belligerent Skies; Pearl of Power Amulet; Safeguard Shield
  why: 'SELECTED DEFAULT. Bow of Awareness occupies Gale''s otherwise-unused ranged slot for +1 Initiative, helping him establish Haste or Wet first. Safeguard''s +1 saves directly protects Haste concentration, while Tempestuous Magic replaces the Haste Helm''s mobility. Melf''s First Staff is the save-DC alternative for Lightning Bolt/control turns.'
- item: Act 1 — Bonbon
  to: Titanstring Bow + Club of Hill Giant Strength + Knife of the Undermountain King + Bloodlust; Gloves of Dexterity; The Protecty Sparkswall; Diadem of Arcane Synergy; Caustic Band; Broodmother's Revenge
  why: 'SELECTED DEFAULT. The Light Club and Knife share Bonbon''s melee set without a feat: the Club supplies STR 19 while the Knife lowers the critical threshold for Titanstring shots. Bloodlust preserves an extra Action after a kill; use a Hill Giant elixir for a boss without adds. Protecty raises control DC, and a successful condition activates the Diadem for subsequent Flourish hits.'
- item: Risky Ring
  to: Charles
  why: Act 2 permanent attack advantage and crit-fishing, with Aura of Protection helping offset its saving-throw drawback.
- item: Resonance Stone
  to: Asterion
  why: Act 2 psychic multiplier for his many Manifestation/Psionic Overload hits and the trigger for Charles's Shadow Blade respec. Keep Charles within its 9m aura to double Shadow Blade and Strange Conduit damage; holster it against psychic damage or dangerous mental-save effects.
- item: Helmet of Arcane Acuity + Band of the Mystic Scoundrel
  wiki:
  - Helmet of Arcane Acuity
  - Band of the Mystic Scoundrel
  to: Bonbon
  why: 'Acts 2–3 control engine: weapon hits build spell DC, then the Band turns Enchantment/Illusion spells into bonus actions.'
- item: Markoheshkir + Amulet of the Devout
  wiki:
  - Markoheshkir
  - Amulet of the Devout
  to: Gale
  why: Act 3 lightning empower, spell DC, and an extra Destructive Wrath charge.
- item: Amulet of Greater Health
  to: Bonbon
  why: Act 3 CON 23 and CON-save advantage protect the concentration that enables the party's Hold Monster plan.
progression:
- act: 1
  paladin: Warlock 2 supplies Hexblade and Devil's Sight, then Paladin 1–5 supplies Divine Smite at character level 4, temporary Great Weapon Master at 6, and Extra Attack at 7. Bind and two-hand Phalar Aluve; source Darkness from farmed arrows and keep the temporary Vengeance oath intact.
  asterion: Rogue 1 expertise, then Open Hand Monk; Tavern Brawler at character level 5 and Stunning Strike at 6.
  sorcerer: Early Tempest Cleric 1 / Storm Sorcerer 4 is an Act 1 bridge; respec to pure Storm Sorcerer at character level 6 for the on-time Storm spike and CON saves.
  bard: Fighter 1 then Swords Bard; Titanstring damage first, not the later Acuity-control loop.
- act: 2
  paladin: Keep two-handed Phalar/GWM and take Paladin 6 while travelling through most of Act 2. On acquiring the late-act Resonance Stone, usually respec at character level 9 to Warlock 5 / Paladin 4; Dual Wielder replaces GWM, Savage Attacker is the second feat, Shadow Blade starts at 3d8 in the main hand, and Phalar moves off-hand. Paladin 5 returns at character level 10 for the non-Honour three-attack stack. Break the fresh oath after the respec to become Oathbreaker.
  asterion: Monk 6 features, Graceful Cloth/Bracers, and the Resonance Stone late in the act.
  sorcerer: Storm Sorcerer 6 supplies Create Water, Call Lightning, Sleet Storm, and Heart of the Storm.
  bard: Helmet of Arcane Acuity begins the ranged-hit-to-control transition.
- act: 3
  paladin: Shadow Blade + Phalar Aluve remains the endgame weapon package; Savage Attacker improves both weapons and every Divine Smite.
  asterion: Monk 9 / Thief 3; double Flurry and Ki Resonation.
  sorcerer: Tempest Cleric 2 at character levels 11–12 for Destructive Wrath.
  bard: Band of the Mystic Scoundrel completes the control loop.
watch_outs:
- watch_out: Modded Hag's Hair assumption
  detail: 'This run uses a mod that gives every party member a Hair. Charles, Bonbon, and Gale use it for CHA 17→18; Asterion uses it for DEX 17→18. In vanilla, only one exists.'
- watch_out: Monk equipment rule
  detail: 'Asterion must be unarmoured and shieldless. From Tavern Brawler onward, leave both melee hands empty: holding a monk weapon preserves Flurry and special unarmed commands, but ordinary Attack/Extra Attack actions swing that weapon and lose Tavern Brawler.'
- watch_out: Resonance Stone debuff
  detail: Its aura makes nearby creatures psychic-vulnerable and disadvantaged on mental saves. Use it around Charles's Aura of Protection, but holster it against psychic/mind enemies and do not rely on its known post-Act-2 reliability.
- watch_out: Charles's Resonance respec and oath
  detail: 'Keep the temporary Vengeance oath intact so Withers can perform the Stone respec normally. At the Resonance Stone, usually respec at character level 9 to Warlock 5 / Paladin 4, replace GWM with Dual Wielder, take Savage Attacker as the Paladin feat, then break the newly chosen oath into Oathbreaker. If Charles becomes an Oathbreaker early, he must first pay the Oathbreaker Knight to restore the oath before Withers will respec him.'
- watch_out: Deepened Pact (non-Honour)
  detail: The Paladin 5 Extra Attack and Warlock 5 Deepened Pact stack only outside Honour Mode; this guide is explicitly non-Honour.
- watch_out: Undead / crit-immune bosses
  detail: Hold Monster and Command do not control undead, and crit immunity prevents the held-target plan. Use Hypnotic Pattern/Slow where applicable; Charles still benefits from radiant Divine Smite against Undead/Fiends, while Gale and Asterion use lightning/force or Asterion's radiant Manifestation.
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
