"""
A collection of monsters from D&D 5e's SRD

This file was autogenerated by https://github.com/stravajiaxen/5e-srd-to-py
"""

from dungeonsheets.monsters.monsters import Monster
from dungeonsheets.stats import Ability


class Camel(Monster):
    """
    Bite.

      Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage.
    """

    name = "Camel"
    description = "Large beast, unaligned"
    challenge_rating = 0.125
    armor_class = 9
    skills = ""
    senses = "Passive Perception 9"
    languages = ""
    strength = Ability(16)
    dexterity = Ability(8)
    constitution = Ability(14)
    intelligence = Ability(2)
    wisdom = Ability(8)
    charisma = Ability(5)
    speed = 50
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 15
    hit_dice = "2d10"


class Cat(Monster):
    """
    Keen Smell.

      The cat has advantage on Wisdom (Perception) checks that rely on smell.

    Claws.

      Melee Weapon Attack: +0 to hit, reach 5 ft., one target. Hit: 1 slashing damage.
    """

    name = "Cat"
    description = "Tiny beast, unaligned"
    challenge_rating = 0
    armor_class = 12
    skills = "Perception +3, Stealth +4"
    senses = "Passive Perception 13"
    languages = ""
    strength = Ability(3)
    dexterity = Ability(15)
    constitution = Ability(10)
    intelligence = Ability(3)
    wisdom = Ability(12)
    charisma = Ability(7)
    speed = 40
    swim_speed = 0
    fly_speed = 0
    climb_speed = 30
    hp_max = 2
    hit_dice = "1d4"


class Centaur(Monster):
    """
    Charge.

      If the centaur moves at least 30 ft. straight toward a target and then hits it with a pike attack on the same turn, the target takes an extra 10 (3d6) piercing damage.

    Multiattack.

      The centaur makes two attacks: one with its pike and one with its hooves or two with its longbow.

    Pike.

      Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 9 (1d10 + 4) piercing damage.

    Hooves.

      Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage.

    Longbow.

      Ranged Weapon Attack: +4 to hit, range 150/600 ft., one target. Hit: 6 (1d8 + 2) piercing damage.
    """

    name = "Centaur"
    description = "Large monstrosity, neutral good"
    challenge_rating = 2
    armor_class = 12
    skills = "Athletics +6, Perception +3, Survival +3"
    senses = "Passive Perception 13"
    languages = "Elvish, Sylvan"
    strength = Ability(18)
    dexterity = Ability(14)
    constitution = Ability(14)
    intelligence = Ability(9)
    wisdom = Ability(13)
    charisma = Ability(11)
    speed = 50
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 45
    hit_dice = "6d10"


class ChainDevil(Monster):
    """
    **Devil's Sight**: Magical darkness doesn't impede the devil's darkvision.

    Magic Resistance.

      The devil has advantage on saving throws against spells and other magical effects.

    Multiattack.

      The devil makes two attacks with its chains.

    Chain.

      Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 11 (2d6 + 4) slashing damage. The target is grappled (escape DC 14) if the devil isn't already grappling a creature. Until this grapple ends, the target is restrained and takes 7 (2d6) piercing damage at the start of each of its turns.

    Animate Chains.

      Up to four chains the devil can see within 60 feet of it magically sprout razor-edged barbs and animate under the devil's control, provided that the chains aren't being worn or carried.
    Each animated chain is an object with AC 20, 20 hit points, resistance to piercing damage, and immunity to psychic and thunder damage. When the devil uses Multiattack on its turn, it can use each animated chain to make one additional chain attack. An animated chain can grapple one creature of its own but can't make attacks while grappling. An animated chain reverts to its inanimate state if reduced to 0 hit points or if the devil is incapacitated or dies.
    """

    name = "Chain Devil"
    description = "Medium fiend, lawful evil"
    challenge_rating = 8
    armor_class = 16
    skills = ""
    senses = "Darkvision 120 ft., Passive Perception 11"
    languages = "Infernal, telepathy 120 ft."
    strength = Ability(18)
    dexterity = Ability(15)
    constitution = Ability(18)
    intelligence = Ability(11)
    wisdom = Ability(12)
    charisma = Ability(14)
    speed = 30
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 85
    hit_dice = "10d8"


class Chimera(Monster):
    """
    Multiattack.

      The chimera makes three attacks: one with its bite, one with its horns, and one with its claws. When its fire breath is available, it can use the breath in place of its bite or horns.

    Bite.

      Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) piercing damage.

    Horns.

      Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 10 (1d12 + 4) bludgeoning damage.

    Claws.

      Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) slashing damage.

    Fire Breath.

      The dragon head exhales fire in a 15-foot cone. Each creature in that area must make a DC 15 Dexterity saving throw, taking 31 (7d8) fire damage on a failed save, or half as much damage on a successful one.
    """

    name = "Chimera"
    description = "Large monstrosity, chaotic evil"
    challenge_rating = 6
    armor_class = 14
    skills = "Perception +8"
    senses = "Darkvision 60 ft., Passive Perception 18"
    languages = "understands Draconic but can't speak"
    strength = Ability(19)
    dexterity = Ability(11)
    constitution = Ability(19)
    intelligence = Ability(3)
    wisdom = Ability(14)
    charisma = Ability(10)
    speed = 30
    swim_speed = 0
    fly_speed = 60
    climb_speed = 0
    hp_max = 114
    hit_dice = "12d10"


class Chuul(Monster):
    """
    Amphibious.

      The chuul can breathe air and water.

    Sense Magic.

      The chuul senses magic within 120 feet of it at will. This trait otherwise works like the detect magic spell but isn't itself magical.

    Multiattack.

      The chuul makes two pincer attacks. If the chuul is grappling a creature, the chuul can also use its tentacles once.

    Pincer.

      Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage. The target is grappled (escape DC 14) if it is a Large or smaller creature and the chuul doesn't have two other creatures grappled.

    Tentacles.

      One creature grappled by the chuul must succeed on a DC 13 Constitution saving throw or be poisoned for 1 minute. Until this poison ends, the target is paralyzed. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.
    """

    name = "Chuul"
    description = "Large aberration, chaotic evil"
    challenge_rating = 4
    armor_class = 16
    skills = "Perception +4"
    senses = "Darkvision 60 ft., Passive Perception 14"
    languages = "understands Deep Speech but can't speak"
    strength = Ability(19)
    dexterity = Ability(10)
    constitution = Ability(16)
    intelligence = Ability(5)
    wisdom = Ability(11)
    charisma = Ability(5)
    speed = 30
    swim_speed = 30
    fly_speed = 0
    climb_speed = 0
    hp_max = 93
    hit_dice = "11d10"


class ClayGolem(Monster):
    """
    Acid Absorption.

      Whenever the golem is subjected to acid damage, it takes no damage and instead regains a number of hit points equal to the acid damage dealt.

    Berserk.

      Whenever the golem starts its turn with 60 hit points or fewer, roll a d6. On a 6, the golem goes berserk. On each of its turns while berserk, the golem attacks the nearest creature it can see. If no creature is near enough to move to and attack, the golem attacks an object, with preference for an object smaller than itself. Once the golem goes berserk, it continues to do so until it is destroyed or regains all its hit points.

    Immutable Form.

      The golem is immune to any spell or effect that would alter its form.

    Magic Resistance.

      The golem has advantage on saving throws against spells and other magical effects.

    Magic Weapons.

      The golem's weapon attacks are magical.

    Multiattack.

      The golem makes two slam attacks.

    Slam.

      Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 16 (2d10 + 5) bludgeoning damage. If the target is a creature, it must succeed on a DC 15 Constitution saving throw or have its hit point maximum reduced by an amount equal to the damage taken. The target dies if this attack reduces its hit point maximum to 0. The reduction lasts until removed by the greater restoration spell or other magic.

    Haste.

      Until the end of its next turn, the golem magically gains a +2 bonus to its AC, has advantage on Dexterity saving throws, and can use its slam attack as a bonus action.
    """

    name = "Clay Golem"
    description = "Large construct, unaligned"
    challenge_rating = 9
    armor_class = 14
    skills = ""
    senses = "Darkvision 60 ft., Passive Perception 9"
    languages = "understands the languages of its creator but can't speak"
    strength = Ability(20)
    dexterity = Ability(9)
    constitution = Ability(18)
    intelligence = Ability(3)
    wisdom = Ability(8)
    charisma = Ability(1)
    speed = 20
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 133
    hit_dice = "14d10"


class Cloaker(Monster):
    """
    Damage Transfer.

      While attached to a creature, the cloaker takes only half the damage dealt to it (rounded down). and that creature takes the other half.

    False Appearance.

      While the cloaker remains motionless without its underside exposed, it is indistinguishable from a dark leather cloak.

    Light Sensitivity.

      While in bright light, the cloaker has disadvantage on attack rolls and Wisdom (Perception) checks that rely on sight.

    Multiattack.

      The cloaker makes two attacks: one with its bite and one with its tail.

    Bite.

      Melee Weapon Attack: +6 to hit, reach 5 ft., one creature. Hit: 10 (2d6 + 3) piercing damage, and if the target is Large or smaller, the cloaker attaches to it. If the cloaker has advantage against the target, the cloaker attaches to the target's head, and the target is blinded and unable to breathe while the cloaker is attached. While attached, the cloaker can make this attack only against the target and has advantage on the attack roll. The cloaker can detach itself by spending 5 feet of its movement. A creature, including the target, can take its action to detach the cloaker by succeeding on a DC 16 Strength check.

    Tail.

      Melee Weapon Attack: +6 to hit, reach 10 ft., one creature. Hit: 7 (1d8 + 3) slashing damage.

    Moan.

      Each creature within 60 feet of the cloaker that can hear its moan and that isn't an aberration must succeed on a DC 13 Wisdom saving throw or become frightened until the end of the cloaker's next turn. If a creature's saving throw is successful, the creature is immune to the cloaker's moan for the next 24 hours.

    Phantasms.

      The cloaker magically creates three illusory duplicates of itself if it isn't in bright light. The duplicates move with it and mimic its actions, shifting position so as to make it impossible to track which cloaker is the real one. If the cloaker is ever in an area of bright light, the duplicates disappear.
    Whenever any creature targets the cloaker with an attack or a harmful spell while a duplicate remains, that creature rolls randomly to determine whether it targets the cloaker or one of the duplicates. A creature is unaffected by this magical effect if it can't see or if it relies on senses other than sight.
    A duplicate has the cloaker's AC and uses its saving throws. If an attack hits a duplicate, or if a duplicate fails a saving throw against an effect that deals damage, the duplicate disappears.
    """

    name = "Cloaker"
    description = "Large aberration, chaotic neutral"
    challenge_rating = 8
    armor_class = 14
    skills = "Stealth +5"
    senses = "Darkvision 60 ft., Passive Perception 11"
    languages = "Deep Speech, Undercommon"
    strength = Ability(17)
    dexterity = Ability(15)
    constitution = Ability(12)
    intelligence = Ability(13)
    wisdom = Ability(12)
    charisma = Ability(14)
    speed = 10
    swim_speed = 0
    fly_speed = 40
    climb_speed = 0
    hp_max = 78
    hit_dice = "12d10"


class CloudGiant(Monster):
    """
    Keen Smell.

      The giant has advantage on Wisdom (Perception) checks that rely on smell.

    Innate Spellcasting.

      The giant's innate spellcasting ability is Charisma. It can innately cast the following spells, requiring no material components:

    At will: detect magic, fog cloud, light
    3/day each: feather fall, fly, misty step, telekinesis
    1/day each: control weather, gaseous form

    Multiattack.

      The giant makes two morningstar attacks.

    Morningstar.

      Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 21 (3d8 + 8) piercing damage.

    Rock.

      Ranged Weapon Attack: +12 to hit, range 60/240 ft., one target. Hit: 30 (4d10 + 8) bludgeoning damage.
    """

    name = "Cloud Giant"
    description = "Huge giant, neutral good (50%) or neutral evil (50%)"
    challenge_rating = 9
    armor_class = 14
    skills = "Insight +7, Perception +7"
    senses = "Passive Perception 17"
    languages = "Common, Giant"
    strength = Ability(27)
    dexterity = Ability(10)
    constitution = Ability(22)
    intelligence = Ability(12)
    wisdom = Ability(16)
    charisma = Ability(16)
    speed = 40
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 200
    hit_dice = "16d12"


class Cockatrice(Monster):
    """
    Bite.

      Melee Weapon Attack: +3 to hit, reach 5 ft., one creature. Hit: 3 (1d4 + 1) piercing damage, and the target must succeed on a DC 11 Constitution saving throw against being magically petrified. On a failed save, the creature begins to turn to stone and is restrained. It must repeat the saving throw at the end of its next turn. On a success, the effect ends. On a failure, the creature is petrified for 24 hours.
    """

    name = "Cockatrice"
    description = "Small monstrosity, unaligned"
    challenge_rating = 0.5
    armor_class = 11
    skills = ""
    senses = "Darkvision 60 ft., Passive Perception 11"
    languages = ""
    strength = Ability(6)
    dexterity = Ability(12)
    constitution = Ability(12)
    intelligence = Ability(2)
    wisdom = Ability(13)
    charisma = Ability(5)
    speed = 20
    swim_speed = 0
    fly_speed = 40
    climb_speed = 0
    hp_max = 27
    hit_dice = "6d6"


class Commoner(Monster):
    """
    Club.

      Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage.
    """

    name = "Commoner"
    description = "Medium humanoid, any alignment"
    challenge_rating = 0
    armor_class = 10
    skills = ""
    senses = "Passive Perception 10"
    languages = "any one language (usually Common)"
    strength = Ability(10)
    dexterity = Ability(10)
    constitution = Ability(10)
    intelligence = Ability(10)
    wisdom = Ability(10)
    charisma = Ability(10)
    speed = 30
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 4
    hit_dice = "1d8"


class ConstrictorSnake(Monster):
    """
    Bite.

      Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 5 (1d6 + 2) piercing damage.

    Constrict.

      Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 6 (1d8 + 2) bludgeoning damage, and the target is grappled (escape DC 14). Until this grapple ends, the creature is restrained, and the snake can't constrict another target.
    """

    name = "Constrictor Snake"
    description = "Large beast, unaligned"
    challenge_rating = 0.25
    armor_class = 12
    skills = ""
    senses = "Blindsight 10 ft., Passive Perception 10"
    languages = ""
    strength = Ability(15)
    dexterity = Ability(14)
    constitution = Ability(12)
    intelligence = Ability(1)
    wisdom = Ability(10)
    charisma = Ability(3)
    speed = 30
    swim_speed = 30
    fly_speed = 0
    climb_speed = 0
    hp_max = 13
    hit_dice = "2d10"


class CopperDragonWyrmling(Monster):
    """
    Bite.

      Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (1d10 + 2) piercing damage.

    Breath Weapons.

      The dragon uses one of the following breath weapons.
    Acid Breath. The dragon exhales acid in an 20-foot line that is 5 feet wide. Each creature in that line must make a DC 11 Dexterity saving throw, taking 18 (4d8) acid damage on a failed save, or half as much damage on a successful one.
    Slowing Breath. The dragon exhales gas in a 1 5-foot cone. Each creature in that area must succeed on a DC 11 Constitution saving throw. On a failed save, the creature can't use reactions, its speed is halved, and it can't make more than one attack on its turn. In addition, the creature can use either an action or a bonus action on its turn, but not both. These effects last for 1 minute. The creature can repeat the saving throw at the end of each of its turns, ending the effect on itself with a successful save.
    """

    name = "Copper Dragon Wyrmling"
    description = "Medium dragon, chaotic good"
    challenge_rating = 1
    armor_class = 16
    skills = "Perception +4, Stealth +3"
    senses = "Blindsight 10 ft., Darkvision 60 ft., Passive Perception 14"
    languages = "Draconic"
    strength = Ability(15)
    dexterity = Ability(12)
    constitution = Ability(13)
    intelligence = Ability(14)
    wisdom = Ability(11)
    charisma = Ability(13)
    speed = 30
    swim_speed = 0
    fly_speed = 60
    climb_speed = 30
    hp_max = 22
    hit_dice = "4d8"


class Couatl(Monster):
    """
    Innate Spellcasting.

      The couatl's spellcasting ability is Charisma (spell save DC 14). It can innately cast the following spells, requiring only verbal components:

    At will: detect evil and good, detect magic, detect thoughts
    3/day each: bless, create food and water, cure wounds, lesser restoration, protection from poison, sanctuary, shield
    1/day each: dream, greater restoration, scrying

    Magic Weapons.

      The couatl's weapon attacks are magical.

    Shielded Mind.

      The couatl is immune to scrying and to any effect that would sense its emotions, read its thoughts, or detect its location.

    Bite.

      Melee Weapon Attack: +8 to hit, reach 5 ft., one creature. Hit: 8 (1d6 + 5) piercing damage, and the target must succeed on a DC 13 Constitution saving throw or be poisoned for 24 hours. Until this poison ends, the target is unconscious. Another creature can use an action to shake the target awake.

    Constrict.

      Melee Weapon Attack: +6 to hit, reach 10 ft., one Medium or smaller creature. Hit: 10 (2d6 + 3) bludgeoning damage, and the target is grappled (escape DC 15). Until this grapple ends, the target is restrained, and the couatl can't constrict another target.

    Change Shape.

      The couatl magically polymorphs into a humanoid or beast that has a challenge rating equal to or less than its own, or back into its true form. It reverts to its true form if it dies. Any equipment it is wearing or carrying is absorbed or borne by the new form (the couatl's choice).
    In a new form, the couatl retains its game statistics and ability to speak, but its AC, movement modes, Strength, Dexterity, and other actions are replaced by those of the new form, and it gains any statistics and capabilities (except class features, legendary actions, and lair actions) that the new form has but that it lacks. If the new form has a bite attack, the couatl can use its bite in that form.
    """

    name = "Couatl"
    description = "Medium celestial, lawful good"
    challenge_rating = 4
    armor_class = 19
    skills = ""
    senses = "Truesight 120 ft., Passive Perception 15"
    languages = "all, telepathy 120 ft."
    strength = Ability(16)
    dexterity = Ability(20)
    constitution = Ability(17)
    intelligence = Ability(18)
    wisdom = Ability(20)
    charisma = Ability(18)
    speed = 30
    swim_speed = 0
    fly_speed = 90
    climb_speed = 0
    hp_max = 97
    hit_dice = "13d8"


class Crab(Monster):
    """
    Amphibious.

      The crab can breathe air and water.

    Claw.

      Melee Weapon Attack: +0 to hit, reach 5 ft., one target. Hit: 1 bludgeoning damage.
    """

    name = "Crab"
    description = "Tiny beast, unaligned"
    challenge_rating = 0
    armor_class = 11
    skills = "Stealth +2"
    senses = "Blindsight 30 ft., Passive Perception 9"
    languages = ""
    strength = Ability(2)
    dexterity = Ability(11)
    constitution = Ability(10)
    intelligence = Ability(1)
    wisdom = Ability(8)
    charisma = Ability(2)
    speed = 20
    swim_speed = 20
    fly_speed = 0
    climb_speed = 0
    hp_max = 2
    hit_dice = "1d4"


class Crocodile(Monster):
    """
    Hold Breath.

      The crocodile can hold its breath for 15 minutes.

    Bite.

      Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 7 (1d10 + 2) piercing damage, and the target is grappled (escape DC 12). Until this grapple ends, the target is restrained, and the crocodile can't bite another target
    """

    name = "Crocodile"
    description = "Large beast, unaligned"
    challenge_rating = 0.5
    armor_class = 12
    skills = "Stealth +2"
    senses = "Passive Perception 10"
    languages = ""
    strength = Ability(15)
    dexterity = Ability(10)
    constitution = Ability(13)
    intelligence = Ability(2)
    wisdom = Ability(10)
    charisma = Ability(5)
    speed = 20
    swim_speed = 20
    fly_speed = 0
    climb_speed = 0
    hp_max = 19
    hit_dice = "3d10"


class CultFanatic(Monster):
    """
    Dark Devotion.

      The fanatic has advantage on saving throws against being charmed or frightened.

    Spellcasting.

      The fanatic is a 4th-level spellcaster. Its spell casting ability is Wisdom (spell save DC 11, +3 to hit with spell attacks). The fanatic has the following cleric spells prepared:

    Cantrips (at will): light, sacred flame, thaumaturgy
    - 1st level (4 slots): command, inflict wounds, shield of faith
    - 2nd level (3 slots): hold person, spiritual weapon

    Multiattack.

      The fanatic makes two melee attacks.

    Dagger.

      Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60 ft., one creature. Hit: 4 (1d4 + 2) piercing damage.
    """

    name = "Cult Fanatic"
    description = "Medium humanoid, any non-good alignment"
    challenge_rating = 2
    armor_class = 13
    skills = "Deception +4, Persuasion +4, Religion +2"
    senses = "Passive Perception 11"
    languages = "any one language (usually Common)"
    strength = Ability(11)
    dexterity = Ability(14)
    constitution = Ability(12)
    intelligence = Ability(10)
    wisdom = Ability(13)
    charisma = Ability(14)
    speed = 30
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 22
    hit_dice = "6d8"


class Cultist(Monster):
    """
    Dark Devotion.

      The cultist has advantage on saving throws against being charmed or frightened.

    Scimitar.

      Melee Weapon Attack: +3 to hit, reach 5 ft., one creature. Hit: 4 (1d6 + 1) slashing damage.
    """

    name = "Cultist"
    description = "Medium humanoid, any non-good alignment"
    challenge_rating = 0.125
    armor_class = 12
    skills = "Deception +2, Religion +2"
    senses = "Passive Perception 10"
    languages = "any one language (usually Common)"
    strength = Ability(11)
    dexterity = Ability(12)
    constitution = Ability(10)
    intelligence = Ability(10)
    wisdom = Ability(11)
    charisma = Ability(10)
    speed = 30
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 9
    hit_dice = "2d8"
