# Baldur's Gate 3, but It's Actually “Impossible”

- Playlist index: 27
- Video ID: `zTRKVG7saKE`
- Source: https://www.youtube.com/watch?v=zTRKVG7saKE
- Format: Modded Honour Mode exploit challenge

## Executive Summary

The challenge modifies every enemy with roughly +1,000 to all statistics, millions of additional hit points, +10,000 damage per damage instance, ten extra actions, and enormous initiative. Conventional combat becomes mathematically irrelevant: attacks miss, saving throws succeed, enemies act first, and almost any hit kills. Completing the game therefore requires replacing normal damage with instant kills, forced movement, state-manipulation bugs, and eventually an infinite-action damage engine.

The run begins as a Duergar Cleric because Sanctuary is the only practical way to survive, while Duergar supplies permanent out-of-combat invisibility and non-concentration Enlarge. Normal enemies are killed through cliffs using Lethargic's automatic failed Strength/Dexterity saves or Force Tunnel's no-save push. Bosses require distinct solutions: Balthazar is carried to a valid ledge, Myrkul is killed by reducing Strength to zero, Gortash dies through a Dominate Person–Polymorph–Gaseous Form interaction, and Orin is trapped in Yenna's five-HP disguise. The Netherbrain finally falls to infinite actions from Helmet of Grit plus Mind Sanctuary and 1,000 stacked Fierce Perilous Stakes.

## Challenge Rules and Consequences

The custom mod adds:

- Approximately +1,000 to enemy ability scores, AC-related statistics, and saves.
- Roughly one million additional health, leaving weak enemies with several million HP.
- +10,000 damage on every damage instance.
- Ten extra actions and extremely high initiative.

This eliminates ordinary optimization. Meta builds, barrelmancy at normal scale, high spell DC, tanking, and conventional healing cannot solve the numbers. The successful framework is instead:

1. Avoid being targeted through Sanctuary or invisibility.
2. Use effects that do not care about saves or HP.
3. Manipulate game states, locations, and scripted transitions.
4. Exploit item-equipping and resource-generation interactions when finite resources become insufficient.

## Major Techniques

| Technique | Mechanism and Use |
|---|---|
| Sanctuary survival | Prevents non-AoE targeting, allowing escape from the Nautiloid and other unavoidable encounters. |
| Lethargic shove | Throw a Potion of Speed at a target, wait for Haste to expire, then shove while Lethargic automatically fails Strength and Dexterity saves. |
| Force Tunnel | Illithid power pushes creatures without a saving throw, enabling cliff kills when ordinary shove odds are effectively zero. |
| Cloud Giant Strength | Raises Strength to 27 so Balthazar can be picked up and transported to a ledge where Honour Mode's anti-chasm protection does not apply. |
| Ability Drain + atrophy | Repeated zero-damage coin throws count as attack rolls and lower Strength by one. A summoned Shadow's Strength Drain supplies the final reduction to zero, triggering instant-death Atrophy. |
| Barrel fortress | Stacked crates and barrels physically block Githyanki attacks after a forced long rest strips all defensive buffs; Jaheira then Misty Steps out. |
| Infinite Bend Luck | Shield of Devotion repeatedly creates spell slots, which convert into Sorcery Points. Hundreds of Bend Luck stacks overwhelm otherwise impossible Athletics checks. |
| Dominate–Polymorph–Gaseous Form | Gortash becomes an ally, a sheep, and a gaseous creature; damaging the combined transformed state kills him rather than restoring millions of HP. |
| Yenna-state Orin | Interrupt Orin's sewer dialogue so she stays disguised as five-HP Yenna, bypass the temple door with geometry, then use Lethargic and nonlethal handling to trigger her defeat. |
| Helmet of Grit loop | In Mind Sanctuary, actions and bonus actions are interchangeable and equipment changes are free while one action remains. Re-equipping the helmet repeatedly grants unlimited bonus actions. |

## Act-by-Act Findings

### Acts 1 and 2

Free exploration and dialogue XP reaches level 4, after which enemies must die for further progression. Lethargic provides the first cliff kill, while Force Tunnel later expands this to many Moonrise and Last Light NPCs. Dialogue causes several Act 2 side bosses to kill themselves, supplying enough XP for Cloud Giant elixirs.

Balthazar cannot be beaten in his office and returns from many Honour Mode chasm deaths in the Shadowfell. The solution is to carry him out of his protected encounter region and drop him from another ledge.

Ketheric cannot be moved and is immune to Atrophy. The run first talks him into surrendering on the roof, deliberately loses, resurrects outside, and skips the rooftop encounter by jumping through Moonrise geometry into the colony. More than a thousand coin throws reduce Ketheric's Strength to one without starting combat, but only after the dialogue transition turns him into the Apostle of Myrkul can a Shadow's Strength Drain trigger Atrophy. Sanctuary protects the Shadow because Myrkul's relevant necrotic damage cannot hurt it.

### Transition to Act 3

The forced Githyanki camp ambush is a unique crisis because a long rest removes Sanctuary. A fortress of crates and barrels blocks both movement and projectiles long enough for Jaheira to escape. In the Astral Prism, invisibility enables setup, while roughly 1,000 Sorcery Points generated through Shield of Devotion support 500 Bend Luck casts. The enormous Athletics bonus then makes cliff throws possible despite enemy statistics.

### The Netherstones

Gortash is isolated, then subjected to Dominate Person. Resonance Stone removes his mental-save advantage, leaving a critical-failure chance. Polymorph and Gaseous Form stack incorrectly; once he has three HP in the combined transformed state, a small attack deals the game's displayed 16.7 million damage and kills him.

Orin is intercepted while mimicking Yenna. Triggering another dialogue before her reveal freezes that disguise state. Because this special Yenna has five HP rather than Orin's millions, the player can bypass the temple's normal progression with a chest jump and knock her out through Lethargic, immediately triggering her death scene.

## Final Netherbrain Solution

Greater Invisibility and Resilient Sphere allow the party to reach and activate the Crown of Karsus despite enemy initiative. The Netherbrain has nearly 16.8 million HP and destroys all platforms quickly. Twist of Fortune fails because planted gold is ignored; even fireworks exploding eight times each would require an impractical number.

The decisive exploit combines:

1. Mind Sanctuary, making actions and bonus actions interchangeable.
2. Helmet of Grit, granting a bonus action below half health.
3. Free repeated unequip/re-equip actions, granting effectively infinite actions.
4. Fierce Perilous Stakes, stacked 1,000 times for enormous bonus psychic damage.
5. Resonance Stone, doubling psychic damage through vulnerability.
6. Globe of Invulnerability, protecting the player and platform from Brain Quakes.
7. Doom Hammer on a summoned Azer, applying Bone Chill so the Stakes' healing cannot raise the player above half health and disable the helmet loop.
8. Stacks of bombs with multiple damage riders, each pile dealing millions of amplified damage.

The game slows below one frame per second, but repeated bomb piles finally remove the brain's health.

## Caveats and Context

This is intentionally an exploit showcase, not a legitimate Honour Mode strategy guide. It relies on a custom mod, save retries, forced movement, geometry skips, vendor resets, state bugs, unlimited Sorcery Points, and repeated equipment exploits. Several interactions were observed under Patch 7, and later patches may remove them. The transcript's rolling-caption duplication also obscures some exact item and skill wording, but the core sequence is clear.

## Conclusion

The challenge's achievement is not conventional character power but systems analysis. Each impossible number is bypassed by asking what the game does not calculate: no-save movement, scripted deaths, zero-stat Atrophy, transformed-state HP, dialogue timing, physical collision, or infinitely refreshed actions. The result is a tour of Baldur's Gate 3's most extreme edge cases, ending with a damage engine absurd enough to match an absurdly modified world.
