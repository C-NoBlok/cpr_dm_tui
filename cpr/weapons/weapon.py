from dataclasses import dataclass
from random import randint
import uuid
import inspect
import json


class Weapon(dict):
    def __init__(self,
                 name: str = '',
                 damage: int = 2,
                 concealable: bool = False,
                 cost: int = 100,
                 ROF: int = 2,
                 hands_required: int = 1,
                 modifier: int = 0,
                 melee_weapon_type: str = None,
                 skill: str = None,
                 clip_size: int = 8,
                 ammo_loaded: int = None,
                 total_ammo: int = None
                 ):
        self.name = name
        self.damage = damage
        self.concealable = concealable
        self.cost = cost
        self.ROF = ROF
        self.hands_required = hands_required
        self.modifier = modifier
        self.melee_weapon_type = melee_weapon_type
        if melee_weapon_type is not None:
            self.skill = 'melee_weapon'
        else:
            self.skill = skill

        self.clip_size = clip_size
        if ammo_loaded is None:
            self.ammo_loaded = self.clip_size
        else:
            self.ammo_loaded = ammo_loaded

        if total_ammo is None:
            self.total_ammo = self.clip_size * 3
        else:
            self.total_ammo = total_ammo

        self.update(
            name=self.name,
            damage=self.damage,
            concealable=self.concealable,
            cost=self.cost,
            ROF=self.ROF,
            hands_required=self.hands_required,
            modifier=self.modifier,
            melee_weapon_type=self.melee_weapon_type,
            skill=self.skill,
            clip_size=self.clip_size,
            ammo_loaded=self.ammo_loaded,
            total_ammo=self.total_ammo
        )

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


    # @property
    # def __dict__(self):
    #     weapon_dict = {
        #     'name': self.name,
        #     'damage': self.damage,
        #     'concealable': self.concealable,
        #     'cost': self.cost,
        #     'ROF': self.ROF,
        #     'hands_required': self.hands_required,
        #     'modifier': self.modifier,
        #     'melee_weapon_type': self.melee_weapon_type,
        #     'skill': self.skill,
        #     'clip_size': self.clip_size,
        #     'ammo_loaded': self.ammo_loaded,
        #     'total_ammo': self.total_ammo
        # }
    #     return weapon_dict


# class MeleeWeapon(Weapon):
#     melee_weapon_type: str = 'heavy melee'
#     skill: str = 'melee_weapon'
#
#     def __init__(self,
#                  melee_weapon_type: str = 'heavy melee',
#                  skill: str = 'melee_weapon',
#                  **kwargs):
#         self.melee_weapon_type = melee_weapon_type
#         self.skill = skill
#         super().__init__(**kwargs)
#
#     @property
#     def __dict__(self):
#         weapon_dict = {
#             'name': self.name,
#             'damage': self.damage,
#             'concealable': self.concealable,
#             'cost': self.cost,
#             'ROF': self.ROF,
#             'hands_required': self.hands_required,
#             'modifier': self.modifier,
#             'melee_weapon_type': self.melee_weapon_type,
#             'skill': self.skill
#         }
#         return weapon_dict
#
#
# class RangedWeapon(Weapon):
#
#     def __init__(self,
#                  skill: str = 'handgun',
#                  clip_size: int = 8,
#                  **kwargs):
#         self.skill = skill
#         self.clip_size = clip_size
#         self.ammo_loaded = self.clip_size
#         self.total_ammo = self.clip_size * 3
#         super().__init__(**kwargs)
#
#     @property
#     def __dict__(self):
#         weapon_dict = {
#             'name': self.name,
#             'damage': self.damage,
#             'concealable': self.concealable,
#             'cost': self.cost,
#             'ROF': self.ROF,
#             'hands_required': self.hands_required,
#             'modifier': self.modifier,
#             'skill': self.skill,
#             'clip_size': self.clip_size,
#             'ammo_loaded': self.ammo_loaded,
#             'total_ammo': self.total_ammo
#         }
#         return weapon_dict


