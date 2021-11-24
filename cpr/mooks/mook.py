from math import ceil
from copy import deepcopy
from dataclasses import dataclass, asdict
from typing import Dict

from cpr.mooks.stats import Stats
from cpr.mooks.skills import Skills
from cpr.weapons import Weapon


@dataclass
class Mook:
    name: str
    mook_type: str
    stats: Stats
    weapons: list
    armor: dict
    skills: Skills
    special: list
    custom: bool = False

    def __post_init__(self):
        self.hp = self.stats.max_hp
        self.seriously_wounded = ceil(self.stats.max_hp / 2)
        self.death_save = self.stats.BODY
        self.combat_skills_list = [
            'brawling',
            'evasion',
            'martial_arts',
            'melee_weapon',
            'archery',
            'autofire',
            'handgun',
            'heavy_weapons',
            'shoulder_arms',
            'athletics'
        ]

    @property
    def is_seriously_wounded(self):
        return self.hp < self.seriously_wounded

    @property
    def combat_skills(self):
        return {k: v for k, v in self.skills.to_dict().items()
                if k in self.combat_skills_list and v['rank'] > 0}

    @property
    def non_combat_skills(self):
        return {k: v for k, v in self.skills.to_dict().items()
                if k not in self.combat_skills_list and v['rank'] > 0}

    @property
    def weapons_by_name(self):
        weapons_data = {}
        for weapon in self.weapons:
            weapons_data[weapon.name] = weapon
        return weapons_data

    def to_dict(self):
        return {
            'name': self.name,
            'mook_type': self.mook_type,
            'stats': self.stats.to_dict(),
            'weapons': [weapon.__dict__ for weapon in self.weapons],
            'armor': self.armor,
            'skills': self.skills.to_dict(),
            'special': self.special,
            'custom': True
        }
    @staticmethod
    def from_dict(mook_dict: Dict):
        stats = mook_dict.pop('stats')
        skills = mook_dict.pop('skills')
        weapons = mook_dict.pop('weapons')
        weapon_objs = []
        for weapon in weapons:
            if weapon['skill'] == 'melee_weapon':
                weapon_objs.append(Weapon(**weapon))
            else:
                weapon_objs.append(Weapon(**weapon))

        skills_obj = deepcopy(Skills())
        mook = Mook(**mook_dict, stats=Stats(**stats), skills=skills_obj.from_dict(skills), weapons=weapon_objs)
        return mook




