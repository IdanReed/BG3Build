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
  class: Draconic (Red) Sorcerer 11 / Fiend Warlock 1
  role: Fire striker + Command control + Haste engine
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
    This is the party's minimum coverage, not a list of every good spell. "Online" is character level for this exact multiclass order. Darkness Arrows, Phalar Aluve, Command, and the martial control abilities do not use Concentration, so they can coexist with the two combat concentration lanes below.

    Default hard-fight stack from character level 7: Charles holds Bless, Gale holds Twinned Haste AND spams non-concentration Command, Bonbon holds Hold Person/Hypnotic Pattern, and Asterion uses Stunning Strike. Each effect belongs to a different character, so there is no concentration collision — and Gale covers two lanes at once because Command needs no Concentration.

    The party has no Cleric level anywhere, so it has no Create Water, no Destructive Wrath, no Bane, and no spell-list source of Guidance, Bless or Healing Word beyond what is listed below. Every one of those gaps is covered by a named owner or an item in the rows that follow.
  rows:
  - need: Wet / water setup
    owner: 'Nobody has the spell — thrown bottles only'
    online: 'Any character, any level, using Water Bottles.'
    backup: 'Nobody in the party can cast Create Water. Throw a water bottle for a small splash, or drop one where a Mage Hand (Gale char 1, Bonbon char 5) can reach it and use the Hand''s Throw for a 2m Wet splash. Wet is a niche tool for stripping enemy fire resistance and for the occasional cold or lightning source, not a party engine.'
    concentration: None — thrown water and Mage Hand do not compete with Haste.
  - need: Guidance / ability checks
    owner: Silver Pendant, from character level 1
    online: The pendant is available immediately southwest of the Grove, before the Grove itself.
    backup: 'This is now MANDATORY rather than a convenience. Gale has no Cleric level and therefore never has Guidance, so the pendant is the party''s only source from level 1. Keep it as a shared exploration swap on whoever is making the check. Bonbon adds Enhance Ability at char 5.'
    concentration: 'Guidance and Enhance Ability each use Concentration. They are out-of-combat check buffs: do not carry them into a fight expecting Gale''s Haste or Bonbon''s control to remain.'
  - need: Longstrider
    owner: Bonbon
    online: Char 2 (Bard 1)
    backup: All four after every long rest — ritual, no slot.
    concentration: None — lasts until long rest.
  - need: Bless
    owner: 'Charles at char 4+ (spell); The Whispering Promise on Bonbon covers char 1–3'
    online: Charles gains Paladin spellcasting at Paladin 2 (char 4). The Whispering Promise is buyable from Volo or Grat at the Goblin Camp for ~40g, so it covers the gap from the start.
    backup: 'Charles is the ONLY Bless CASTER — Gale has no Cleric level. The char 1–3 hole is now filled by The Whispering Promise: any healing Bonbon does gives the target +1d4 to attacks and saves for 2 turns with no Concentration, and a THROWN Potion of Healing applies it to everyone it splashes. ⚠ The ring applies the SAME condition as the spell, so the two do NOT stack — the ring is the early-game and off-turn substitute, not an addition. From the Underdark on, Charles should cast Bless while holding the STAFF OF ARCANE BLESSING (Arcane Tower basement), which adds Mystra''s Blessing (+1d4 to spell ATTACK rolls) to everyone he blesses — worth +1d4 accuracy on every one of Gale''s rays. Upcast to a level 2 slot to cover all four party members instead of three.'
    concentration: 'Yes, on Charles — and it stays that way. It competes with Charles''s Hex, Divine Favour, Wrathful Smite, or later self-cast Darkness; on those turns the Whispering Promise carries Bless instead.'
  - need: Bane / save debuff
    owner: 'Phalar Shriek (Charles) and Gloves of Baneful Striking; Ring of Mental Inhibition (Gale) from Act 2'
    online: 'Phalar Aluve arrives in the Underdark; Gloves of Baneful Striking arrive on the Rosymorn trail; Ring of Mental Inhibition is in the House in Deep Shadows in Act 2.'
    backup: 'The Bane spell is gone with the Cleric dip, and nothing replaces it directly — but nothing needs to. Phalar Shriek applies −1d4 to nearby enemy saves with no initial save and no Concentration, Charles''s Baneful Strike adds another −1d4 for 2 turns after a weapon hit, and Gale''s Ring of Mental Inhibition applies Mental Fatigue whenever an enemy fails a save against him. Gale''s own spell save DC also climbs far higher than Bane ever compensated for, via Arcane Acuity.'
    concentration: None from any of these — all three are item or aura effects, so Gale keeps Twinned Haste.
  - need: Darkness / protected melee lane
    owner: 'Charles uses it; Bonbon preferably fires the Arrow of Darkness'
    online: 'Devil''s Sight at char 2; use farmed Darkness Arrows throughout Act 1.'
    backup: 'The arrow makes a 3m cloud for 3 turns without Concentration. PLACEMENT RULE: put the cloud so CHARLES is inside it and the enemies are NOT. He is then an unseen attacker (advantage in, disadvantage out) while his targets stay visible and shootable for Gale — the cloud explicitly blocks ranged attacks into and out of itself, so an enemy standing inside it is a target Gale cannot touch. Keep Gale and Asterion outside.'
    concentration: 'None from the arrow — Charles remains free to hold Bless, Hex, or Divine Favour. This also does NOT interact with Gale''s illumination package: Coruscation keys off Gale being lit, not the enemy, and Daylight only dispels Darkness at the instant it is cast.'
  - need: Haste
    owner: Gale
    online: Char 5 (Sorcerer 5).
    backup: 'Twinned Spell for 3 Sorcery Points. WHO GETS IT: Gale''s own hasted action is a second Scorching Ray worth roughly 150 damage, so self-Haste genuinely competes with hasting both martials. Default to Charles + Asterion for adds-heavy fights and Gale + Charles for single-boss fights. Protect the concentration with CON-save proficiency from level 1, Spidersilk Armour''s CON-save advantage from Act 1, Armour of Landfall''s from Act 3, positioning, and Shield. ⚠ Gale has neither a shield nor War Caster — Dual Wielder fills both hands and both feats are spent.'
    concentration: 'Yes — but Command, Scorching Ray, and Fireball are all non-concentration, so Gale holds Haste and still controls and nukes every turn. Ending Haste makes both targets Lethargic.'
  - need: Single-target hard control
    owner: 'Bonbon for Concentration control; Gale for concentration-free Command'
    online: 'Tasha''s Hideous Laughter at char 3; Bonbon Hold Person at char 4; Gale Hold Person at char 4 and Command at char 7. Asterion adds Stunning Strike at char 6.'
    backup: 'CLEAN SPLIT: Bonbon holds Hold Person/Hold Monster as the auto-crit setup for Charles, while Gale spams Extended Command — which lasts two turns and costs no Concentration, so it stacks on top of Bonbon''s lock rather than competing with it. Gale''s Command DC becomes the highest in the party once Arcane Acuity is online. Charles''s Command and Asterion''s Stunning Strike/Topple remain non-concentration backups. ⚠ Command does not work on Undead.'
    concentration: 'Bonbon concentrates on one control spell. Gale concentrates on Haste and controls with Command anyway. Asterion''s control and Charles''s Command use no Concentration.'
  - need: Group control / caster denial
    owner: 'Bonbon for Hypnotic Pattern; Gale for Command and Counterspell'
    online: 'Bonbon gets Hypnotic Pattern at char 6; Gale learns Counterspell at char 6 and Command at char 7.'
    backup: 'Gale can Extended-Command an arbitrary number of enemies across successive turns without ever dropping Haste — a group-control lane that costs him no Concentration at all. Command: Approach also pulls scattered enemies into one Fireball. Counterspell is a Reaction and consumes no Concentration.'
    concentration: 'Bonbon holds Hypnotic Pattern; Gale holds Haste and controls with Command. Nothing collides.'
  - need: Emergency recovery
    owner: Bonbon
    online: Char 2 (Bard 1).
    backup: 'Bonbon is the party''s ONLY healer. Stock Healing Potions and Revivify scrolls heavily; her Healing Word is a bonus-action ranged pickup, not sustained healing. Character level 1 has no healing spell at all.'
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
    default: Twinned Haste from char 5 onward.
    alternatives: Hold Person (char 4) or Hold Monster (char 10) in fights where someone else supplies Haste; Telekinesis for repositioning a single dangerous target.
    rule: 'Gale''s entire main loop is concentration-free, so he holds Haste permanently and still deals damage and controls. Scorching Ray, Fireball, Command, Counterspell, and Shield are ALL safe to cast while concentrating. Only Hold X, Hex, and Telekinesis would evict Haste.'
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
    why: 'MANDATORY from character level 1. With no Cleric level anywhere in the party, this pendant is the only source of Guidance for the entire run. Do not feed it to Gale''s orb.'
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
    why: The club sets STR 19 while sitting in Bonbon's melee set; Titanstring adds the +4 STR modifier to every ranged hit and Slashing-Flourish projectile.
  - item: The Spellsparkler + Melf's First Staff
    wiki:
    - The Spellsparkler
    - Melf's First Staff
    owner: Gale
    timing: Waukeen's Rest reward / Blurg in the Underdark
    why: 'Both at once from character level 4, once Dual Wielder is taken — they are stat sticks, not weapons. Scorching Ray''s 3–5 separate damage instances build Spellsparkler charges very fast, and Melf''s +1 spell attack/DC applies to every single ray.'
  - item: Hat of Fire Acuity
    owner: Gale
    timing: 'ACT 2 — carried by the Strange Ox at Dammon''s blacksmith, Last Light Inn'
    why: 'THE build-defining item. Dealing Fire damage grants 2 turns of Arcane Acuity (+1 spell attack and +1 spell save DC per remaining turn, cap 10). Each Scorching Ray ray counts separately, so one level-4 cast caps it. ⚠ DO NOT kill the Strange Ox at the Druid Grove in Act 1 — it does not carry the hat until Last Light. If missed in Act 2, the Ox reappears in Rivington in Act 3.'
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
  - item: The Whispering Promise
    owner: Bonbon
    timing: Volo, or Grat at the Goblin Camp — ~40g, available before the Grove resolves
    why: 'Fills the char 1–3 Bless hole the plan has always admitted to. Healing a creature gives it +1d4 to attacks and saves for 2 turns, no Concentration; a thrown Potion of Healing blesses everyone it splashes, and Bonbon''s bonus-action Healing Word also fires Broodmother''s Revenge at the same time. ⚠ Same condition as the Bless spell, so it does not stack with Charles — it is the early and off-turn substitute.'
  - item: Staff of Arcane Blessing
    owner: Charles (pre-combat swap)
    timing: Arcane Tower BASEMENT, Underdark
    why: 'Every Bless cast by its wielder also grants Mystra''s Blessing, +1d4 to spell ATTACK rolls. Charles was already spending concentration on Bless, so the routine costs only a weapon swap — and Gale gains +1d4 accuracy on each of his 3–7 Scorching Ray rays.'
  - item: Spidersilk Armour
    owner: Gale
    timing: Worn by Minthara, Shattered Sanctum — the same kill as Charles's Boots of Striding
    why: 'ADVANTAGE ON CONSTITUTION SAVES from Act 1, which is the only thing protecting Twinned Haste until Armour of Landfall in Act 3. Gale has no War Caster, no feat left for one, and no shield after Dual Wielder. Costs 1 AC versus going unarmoured.'
  - item: Elixir of Vigilance
    owner: Gale (standing daily elixir)
    timing: ~25g from Danthelon's, Kith in Grymforge, or Popper at the Circus
    why: '+5 Initiative and immunity to Surprise until long rest. BG3 rolls initiative on a d4 + DEX, not a d20, so this is larger than the whole die — it is the Alert feat Gale cannot afford. He is the only party member with no competing elixir, so the slot is free.'
synergies:
- name: Haste engine
  how: 'Gale Twinned-Hastes two of Charles / Asterion / himself from character level 5. The extra Actions are strongest on Charles''s three-attack non-Honour turn, Asterion''s Attack action, and Gale''s own second Scorching Ray — which is why the target choice is now a real decision rather than an automatic Charles + Asterion.'
- name: Control into melee
  how: Asterion opens bosses with Stunning Strike; Bonbon adds Hold Person/Monster. Stun grants advantage; Paralyzed makes melee hits crit automatically, turning Charles's smites into the finisher. Gale's Extended Command layers on top without using Concentration.
- name: Per-ray riders
  how: 'The core of the new build. Scorching Ray fires 3 rays at level 2 and one more per slot level above (7 on a level-6 slot), and the wiki confirms flat bonus damage applies to EACH ray. So Charles''s Phalar Aluve Shriek (1d4 Thunder), Elemental Affinity (+CHA), Callous Glow (+2 radiant), Rhapsody (+3), Markoheshkir Flame of Wrath (+prof), and Spellmight (+1d8) all multiply by the ray count. Charles pre-activating Shriek is worth roughly 7d4 extra on a single Gale turn.'
- name: Illumination chain (self-contained on Gale)
  how: 'Coruscation Ring applies Radiating Orb when the WEARER is illuminated — the target does not need to be lit. Radiating Orb then makes the target Illuminated, which switches on Callous Glow''s +2 radiant, which in turn procs Gloves of Belligerent Skies'' Reverberation. So: light on Gale → ray 1 applies Radiating Orb → rays 2+ each add radiant and Reverberation. Because only GALE needs to be lit, Charles''s Darkness cloud is completely independent of this and the two packages never conflict.'
- name: Resonance Stone into Command
  how: 'Asterion''s Resonance Stone aura gives nearby creatures disadvantage on mental saving throws. Command and both Hold spells are WIS saves, so Gale''s control becomes close to unresistable against anything standing near Asterion — on top of an Arcane Acuity spell save DC in the low 30s.'
- name: Reverberation to Prone
  how: Boots of Stormy Clamour (condition inflicted), Spineshudder Amulet (ranged spell-attack hits), and Gloves of Belligerent Skies (radiant damage) all stack Reverberation, and Scorching Ray triggers all three several times per cast. Prone enemies then feed Charles's and Asterion's melee advantage.
- name: Psychic package
  how: Late in Act 2, the Resonance Stone pickup triggers Charles's Shadow Blade respec. Asterion carries it for Manifestation of Mind and Psionic Overload across multiple Flurry hits while keeping Charles in the 9m aura to double Shadow Blade and Strange Conduit; holster it against psychic or mental-save threats.
- name: Inquisitor's Might onto the Monk
  how: 'Charles''s Oath of Vengeance Channel Oath (available from character level 3) grants a target +CHA modifier RADIANT damage on every weapon attack for 2 turns, plus a no-save Daze — and it has a 9m range, so it can be cast on an ally. Asterion lands 4–6 unarmed hits per turn against Charles''s 1–2 swings, so buffing the Monk extracts roughly three times the damage. The radiant rider also feeds Charles''s Luminous Armour shockwaves and any radiant-keyed gear. ⚠ One charge per short rest, and from Paladin 3 it competes with Vow of Enmity.'
- name: Auras
  how: Aura of Protection covers frontline saves; Aura of Hate adds Charles's CHA to nearby melee-weapon damage — not to Asterion's unarmed strikes.
combat_gameplan:
  note: |-
    The party now focus-fires instead of running two separate lanes. Charles stands inside a Darkness cloud while his target stands OUTSIDE it, so Gale can put Scorching Ray into the same enemy Charles is meleeing — which is also the enemy inside Phalar Shriek's 6m aura. Asterion holds the Resonance Stone nearby so Gale's Command lands. Fireball is the exception: it goes to a separate adds cluster until Careful Spell arrives at character level 11.

    In Act 1, the party is still assembling: Asterion's Stun and Charles's Divine Smite are the boss plan, Gale's Scorching Ray comes online at char 3 and does real single-target work immediately, and Bonbon deals Titanstring damage. Gale's build only truly switches on in Act 2 with the Hat of Fire Acuity; the Hold Monster + Acuity + Band loop begins in Acts 2–3, not in early Act 1.
  per_character:
  - character: Bonbon (Bard)
    role: Ranged Titanstring damage in Act 1; Arcane-Acuity controller later.
    priority_actions: 'Act 1 — Titanstring shots and ranged Slashing Flourish. Acts 2–3 — land a weapon hit, then Band of the Mystic Scoundrel for a bonus-action Enchantment/Illusion.'
  - character: Gale (Sorcerer)
    role: Single-target Fire striker, concentration-free Command controller, and Haste engine.
    priority_actions: 'From char 5, Twinned Haste two of Charles / Asterion / himself. Then Quickened Scorching Ray (bonus action) into the priority target with Spellmight Gloves disabled to build Arcane Acuity, enabling them from the second cast onward. After that, choose each turn: more Scorching Ray on the boss, Fireball on a cluster of 4+, or Extended Command on anything worth disabling. Because none of that uses Concentration, Haste is never at risk from his own casting.'
  - character: Charles (Paladin)
    role: The held-target crit-smite finisher and Aura carrier.
    priority_actions: 'ACT 1–mid ACT 2 — bound two-handed Phalar, pre-cast Shriek, fight inside a Darkness Arrow cloud; Booming Blade for the Ring of Arcane Synergy, then GWM attacks and Divine Smites. LATE ACT 2+ — Shadow Blade main hand, Phalar off-hand, self-cast Darkness, stay in the Stone aura.'
  - character: Asterion (Monk)
    role: Unarmed Tavern-Brawler striker, Stun setter, thief, later Stone carrier.
    priority_actions: 'Drink Giant Strength, punch, spend Ki on Stunning Strike. Flurry Topple for Prone/advantage, Stagger to strip reactions. Thief 3 gives two Flurries per turn; Deathstalker Mantle repositions on a kill.'
  opening_rotation:
  - step: 1
    who: All — before combat
    action: 'ONCE PER LONG REST: Gale casts Daylight (Enchant Item) on Bonbon''s main-hand weapon — it lasts until the next rest and keeps Gale lit for the Coruscation chain. ⚠ Cast it BEFORE any Darkness Arrow is fired, since Daylight dispels Darkness only at the moment it is cast; and it cannot target Asterion, who has no main-hand weapon. ACT 1/early ACT 2: Bonbon places a Darkness Arrow so Charles is inside the cloud and the enemies are not, then Charles switches to bound two-handed Phalar Aluve and activates Shriek. LATE ACT 2+: Charles summons/binds Shadow Blade and off-hands Phalar, while Asterion carries the Resonance Stone nearby. Once Tavern Brawler is online, Asterion drinks Giant Strength and leaves both melee hands empty; Bonbon equips the Hill Giant club main hand + Knife of the Undermountain King off-hand behind Titanstring and drinks Bloodlust for encounters with adds (swap to Hill Giant Strength for a single boss).'
  - step: 2
    who: Asterion
    action: Reach the priority target, punch, try Stunning Strike. Flurry Topple when Prone helps the melee line.
  - step: 3
    who: Gale
    action: 'Twinned Haste (Charles + Asterion for adds-heavy fights, Gale + Charles for a single boss), then Quickened Scorching Ray into the priority target with Spellmight Gloves OFF to cap Arcane Acuity. Enable the gloves afterwards. Never drop Fireball on the melee before Careful Spell at character level 11.'
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
  to: Bow of Awareness; The Spellsparkler main hand + Melf's First Staff off hand (from char 4); The Shadespell Circlet; Boots of Stormy Clamour; Gloves of Belligerent Skies; Pearl of Power Amulet
  why: 'SELECTED DEFAULT. Dual Wielder at character level 4 lets Gale hold both staves as stat sticks, so Melf''s +1 spell attack/DC applies to every Scorching Ray ray alongside Spellsparkler''s charge generation. ⚠ Filling both hands rules out a shield for the rest of the run — Spidersilk Armour''s Constitution-save advantage is the substitute that protects Twinned Haste, and the Safeguard Shield belongs to another party member. Bow of Awareness holds the otherwise-unused ranged slot for +1 Initiative on top of the standing Elixir of Vigilance, because Gale has no feat left for Alert.'
- item: Act 2 — Gale
  to: Hat of Fire Acuity; Callous Glow Ring + Coruscation Ring (damage) or Ring of Mental Inhibition (control); Spineshudder Amulet; Boots of Stormy Clamour; Gloves of Belligerent Skies
  why: 'SELECTED DEFAULT once the Strange Ox is killed at Last Light. The Hat is the build — each Scorching Ray ray is a separate Fire instance, so one level-4 cast takes Arcane Acuity from 0 to its 10 cap. Spineshudder is core for the same reason: it triggers on ranged spell-ATTACK hits, and Gale makes 3–7 of them per cast. Three good rings for two slots: run Callous Glow + Coruscation when nuking, and swap Coruscation for Mental Inhibition when the plan is Command spam.'
- item: Act 3 — Gale
  to: Markoheshkir main hand + Rhapsody off hand; Hat of Fire Acuity; Armour of Landfall; Spellmight Gloves; Cloak of the Weave; Spineshudder Amulet; Callous Glow + Coruscation/Mental Inhibition
  why: 'SELECTED DEFAULT. Attune Markoheshkir to FLAME OF WRATH, not Bolts of Doom. Armour of Landfall''s Constitution-save ADVANTAGE is the load-bearing piece: it replaces the Halfling Luck and War Caster this build cannot have, and it is what makes Markoheshkir''s unavoidable Heat self-damage safe while concentrating on Twinned Haste. ⚠ Do not attune Flame of Wrath before Landfall is equipped.'
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
  why: 'Acts 2–3 control engine: weapon hits build spell DC, then the Band turns Enchantment/Illusion spells into bonus actions.'
- item: Markoheshkir
  to: Gale
  why: 'Act 3 main hand from Ramazith''s Tower. +1 spell attack/DC, Arcane Battery for a free spell of any level, and Kereska''s Favour attuned to Flame of Wrath for Fire resistance plus a +proficiency Fire damage rider that applies per ray. ⚠ Attuning also starts unavoidable Heat self-damage each turn, so do not attune until Armour of Landfall is equipped.'
- item: Spellmight Gloves + Spineshudder Amulet
  wiki:
  - Spellmight Gloves
  - Spineshudder Amulet
  to: Gale
  why: 'Both key off spell ATTACK rolls, and Scorching Ray fires 3–7 of them per cast — so Spellmight''s −5/+1d8 and Spineshudder''s spell-attack Reverberation are best-in-slot here. MANAGE SPELLMIGHT: first cast with the gloves OFF to build Arcane Acuity, then switch them ON once Acuity covers the −5.'
- item: Hellrider's Longbow
  wiki: Hellrider Longbow
  to: 'Bonbon (contested with Gale)'
  why: 'Both want to act first — Bonbon to land the weapon hit that opens her Band of the Mystic Scoundrel loop, Gale to establish Twinned Haste. Bonbon keeps it by default; Gale holds Bow of Awareness and drinks an Elixir of Vigilance for the fights where he must go first, since he has no feat left for Alert.'
- item: Amulet of Greater Health
  to: Bonbon
  why: Act 3 CON 23 and CON-save advantage armour the Hold Monster concentration.
progression:
- act: 1
  paladin: Warlock 2 supplies Hexblade and Devil's Sight, then Paladin 1–5 supplies Divine Smite at character level 4, temporary Great Weapon Master at 6, and Extra Attack at 7. Bind and two-hand Phalar Aluve; source Darkness from farmed arrows and keep the temporary Vengeance oath intact.
  asterion: Rogue 1 expertise, then Open Hand Monk; Tavern Brawler at character level 5 and Stunning Strike at 6.
  sorcerer: 'Draconic-Red Sorcerer from character level 1 — no bridge and no respec after the initial Withers respec out of Wizard. CON + CHA saves from level 1, Scorching Ray at 3, Dual Wielder at 4, Twinned Haste at 5, Elemental Affinity at 6. ⚠ Do not kill the Strange Ox at the Druid Grove.'
  bard: Fighter 1 then Swords Bard; Titanstring damage first, not the later Acuity-control loop.
- act: 2
  paladin: Keep two-handed Phalar/GWM and take Paladin 6 while travelling through most of Act 2. On acquiring the late-act Resonance Stone, usually respec at character level 9 to Warlock 5 / Paladin 4; Dual Wielder replaces GWM, Savage Attacker is the second feat, Shadow Blade starts at 3d8 in the main hand, and Phalar moves off-hand. Paladin 5 returns at character level 10 for the non-Honour three-attack stack. Break the fresh oath after the respec to become Oathbreaker.
  asterion: Monk 6 features, Graceful Cloth/Bracers, and the Resonance Stone late in the act.
  sorcerer: 'Fiend Warlock 1 at character level 7 adds Command, then Sorcerer resumes. The Hat of Fire Acuity from the Strange Ox at Last Light turns the build on, and the Callous Glow + Coruscation rings complete the illumination chain.'
  bard: Helmet of Arcane Acuity begins the ranged-hit-to-control transition. She also carries the party's until-long-rest Daylight from Gale.
- act: 3
  paladin: Shadow Blade + Phalar Aluve remains the endgame weapon package; Savage Attacker improves both weapons and every Divine Smite.
  asterion: Monk 9 / Thief 3; double Flurry and Ki Resonation.
  sorcerer: 'Careful Spell at character level 11 finally makes Fireball safe near the melee; Chain Lightning at 12 covers fire-immune enemies. Markoheshkir + Rhapsody + Armour of Landfall + Spellmight Gloves complete the loadout.'
  bard: Band of the Mystic Scoundrel completes the control loop.
watch_outs:
- watch_out: Strange Ox — do not kill it in the Grove
  detail: 'The Hat of Fire Acuity is the single item Gale''s build depends on, and the Strange Ox only carries it from Last Light Inn onward. Killing the Ox at the Druid Grove in Act 1 yields only the Shapeshifter''s Boon Ring. If you miss it at Last Light in Act 2, the Ox reappears in Rivington on a hill west of the requisitioned barn in Act 3.'
- watch_out: What the party lost with the Cleric dip
  detail: 'Switching Gale to Fire Sorlock removes Create Water, Destructive Wrath, Guidance, Bless from Gale, Bane, and Healing Word from Gale. The Silver Pendant becomes mandatory rather than convenient, Charles is the only Bless source from char 4, Bonbon is the only healer, and Wet is now a thrown-bottle tool rather than a party engine. Character levels 1–3 have no Bless and no healing spell.'
- watch_out: 'Gale has only two feats and no shield — but both gaps are now closed by gear, not left open'
  detail: 'Sorcerer grants feats at Sorc 4 and Sorc 8 (character levels 4 and 9), and the Warlock level grants none. Dual Wielder and Elemental Adept: Fire consume both, so there is no Alert and no War Caster, and Dual Wielder also removes the Safeguard Shield. THE FIXES: Alert is replaced by a standing ELIXIR OF VIGILANCE (+5 Initiative and Surprise immunity until long rest, ~25g — Gale is the only party member with no competing elixir, so the slot is free). War Caster is replaced by SPIDERSILK ARMOUR''s advantage on Constitution saves from Act 1, upgrading to Armour of Landfall in Act 3. Before those two, Twinned Haste rests on CON-save proficiency alone.'
- watch_out: Initiative is rolled on a d4 — flat bonuses are worth far more than they look
  detail: 'BG3 rolls initiative as d4 + Dexterity modifier, NOT d20, and it is explicitly not a Dexterity check (so Jack of All Trades and Enhance Ability do nothing for it). A flat +2 is therefore worth half the entire die. This is why Alert is one of only two S+ feats, and why the Elixir of Vigilance is a genuine substitute for it. Resulting party order: Asterion d4+10 (DEX 20 + Alert) → Gale d4+8 (DEX 16 + Vigilance) → Bonbon d4+7 (DEX 18 + Hellrider''s Longbow) → Charles d4+2. ⚠ CHARLES GOING LAST IS DELIBERATE, not a flaw: his whole job is to swing at a target the others have already Held, Stunned or Commanded, so the initiative build matches the opening rotation. If you ever want him faster, Bhaalist Armour and the Assassin of Bhaal Cowl are +2 each.'
- watch_out: Markoheshkir Heat vs Twinned Haste
  detail: 'Flame of Wrath generates Heat, which deals unavoidable self-damage every turn and forces a CON save against Haste each time. Gale is Human, so there is no Halfling Luck. Do not attune Flame of Wrath until Armour of Landfall is equipped.'
- watch_out: Fire resistance and fire immunity
  detail: 'Fire is the most resisted damage type in Act 3, and Bonbon''s move to dual hand crossbows means the party cannot mass-apply Arsonist''s Oil the way a bow archer with Arrows of Many Targets could — which is why Elemental Adept: Fire is effectively mandatory. Against fire-IMMUNE enemies (House of Hope, Raphael, the red dragon, Yurgir), switch Markoheshkir to a lightning attunement and use Chain Lightning. Gale contributes less damage in those fights; his Twinned Haste, Command and Counterspell are what he brings instead.'
- watch_out: Fireball before Careful Spell
  detail: 'Careful Spell is Gale''s fourth metamagic at Sorc 10 = character level 11. For the whole run before that, Fireball must go to a separate adds cluster, never onto Charles or Asterion. Scorching Ray is the focus-fire tool.'
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
  detail: 'Hold Monster and Command do not control undead, and crit immunity prevents the held-target plan. That bites hard through Act 2, which is dense with Undead and where both Command casters lose their main lane. Use Hypnotic Pattern/Slow where applicable; Charles still benefits from radiant Divine Smite against Undead/Fiends, Gale falls back on raw Scorching Ray and Fireball damage, and Asterion toggles Manifestation to Soul for radiant.'
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
