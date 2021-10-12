from dataclasses import dataclass
from random import randint

@dataclass
class Weapon:
    name: str
    damage: int
    concealable: bool
    cost: int
    ROF: int

    def hit(self):
        dmg = randint(self.damage, self.damage*6)
        print(f'{self.name} hits for {dmg} damage.')
        return dmg

@dataclass
class MeleeWeapon(Weapon):
    melee_weapon_type: str

@dataclass
class RangedWeapon(Weapon):
    skill: str
    hands_required: int


