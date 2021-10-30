from dataclasses import dataclass
from random import randint
import uuid

@dataclass
class Weapon:
    name: str
    damage: int
    concealable: bool
    cost: int
    ROF: int
    hands_required: int = 1
    modifier: int = 0

    def hit(self):
        dmg = randint(self.damage, self.damage*6)
        print(f'{self.name} hits for {dmg} damage.')
        return dmg

    def make_poor_quality(self):
        self.name = f'Poor Quality {self.name}'
        self.modifier = -1

    def make_excellent_quality(self):
        self.name = f'Excellent Quality {self.name}'
        self.modifier = 1

@dataclass
class MeleeWeapon(Weapon):
    melee_weapon_type: str = 'heavy melee'
    skill = 'melee_weapon'


@dataclass
class RangedWeapon(Weapon):
    skill: str = 'handgun'
    clip_size: int = 8
    ammo_loaded: int = clip_size
    total_ammo: int = 3*clip_size


