from math import ceil
from dataclasses import dataclass

@dataclass
class Stats:
    INT: int
    REF: int
    DEX: int
    TECH: int
    COOL: int
    WILL: int
    LUCK: int
    MOVE: int
    BODY: int
    EMP: int


    @property
    def max_hp(self):
        return ceil(10 + 5*(self.BODY + self.WILL)/2)

@dataclass
class Mook:
    name: str
    mook_type: str
    stats: Stats
    weapons: list
    armor: tuple
    skills: dict
    special: dict

    def __init__(self, name, mook_type, stats, weapons,
                 armor, skills, special):
        self.name = name
        self.mook_type = mook_type
        self.stats = stats
        self.weapons = weapons
        self.armor = armor
        self.skills = skills
        self.special = special
        self.hp = self.stats.max_hp
        self.seriously_wounded = ceil(self.stats.max_hp / 2)
        self.death_save = self.stats.BODY

        self.combat_skills_list = [
            'brawling',
            'evasion',
            'martial arts',
            'melee weapon',
            'archery',
            'autofire',
            'handgun',
            'heavy weapons',
            'shoulder arms',
            'athletics'
        ]

    @property
    def combat_skills(self):
        return { k:v for k,v in self.skills.items()
                if k in self.combat_skills_list }

    @property
    def non_combat_skills(self):
        return { k:v for k,v in self.skills.items()
                if k not in self.combat_skills_list }

    @property
    def weapons_by_name(self):
        weapons_data = {}
        for weapon in self.weapons:
            weapons_data[weapon.name] = weapon
        return weapons_data

