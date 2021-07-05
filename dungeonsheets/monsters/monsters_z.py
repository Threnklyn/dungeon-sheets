"""
A collection of monsters from D&D 5e's SRD

This file was autogenerated by https://github.com/stravajiaxen/5e-srd-to-py
"""

from dungeonsheets.monsters.monsters import Monster
from dungeonsheets.stats import Ability


class Zombie(Monster):
    """Undead Fortitude.

      If damage reduces the zombie to 0 hit points,
    it must make a Constitution saving throw with a DC of 5+the damage
    taken, unless the damage is radiant or from a critical hit. On a
    success, the zombie drops to 1 hit point instead.

    Slam.

      Melee Weapon Attack: +3 to hit, reach 5 ft., one
      target. Hit: 4 (1d6 + 1) bludgeoning damage.

    """

    name = "Zombie"
    description = "Medium undead, neutral evil"
    challenge_rating = 0.25
    armor_class = 8
    skills = ""
    senses = "Darkvision 60 ft., Passive Perception 8"
    languages = "understands all languages it spoke in life but can't speak"
    strength = Ability(13)
    dexterity = Ability(6)
    constitution = Ability(16)
    intelligence = Ability(3)
    wisdom = Ability(6)
    charisma = Ability(5)
    speed = 20
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 22
    hit_dice = "3d8"
