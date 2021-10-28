from copy import deepcopy

from cpr.mooks.mook import Mook
from cpr.mooks.stats import Stats
from cpr.mooks.skills import Skills, Skill
from cpr.weapons import very_heavy_pistol


class Netrunner(Mook):
    def __init__(self):
        name = 'Netrunner'
        mook_type = 'lieutenant'
        stats = Stats(
            INT=7,
            REF=5,
            DEX=4,
            TECH=7,
            COOL=4,
            WILL=5,
            LUCK=0,
            MOVE=5,
            BODY=3,
            EMP=4,
        )
        weapons = [very_heavy_pistol()]
        armor = {'head': 11, 'body': 11}

        skills = deepcopy(Skills())
        skills.from_rank_dict({
            'athletics': 5,
            'basic_tech': 6,
            'brawling': 3,
            'conceal_reveal_object': 6,
            'concentration': 4,
            'conversation': 2,
            'cryptography': 4,
            'deduction': 4,
            'education': 4,
            'electronics_security_tech': 4,
            'evasion': 2,
            'first_aid': 2,
            'forgery': 2,
            'handgun': 5,
            'human_perception': 2,
            'language': 2,
            'local_expert': 6,
            'library_search': 2,
            'perception': 4,
            'persuasion': 2,
            'pick_lock': 4,
            'resist_torture_drug': 2,
            'stealth': 5,
        })
        special = ['Interface Rank 4', 'Banhammer', 'DeckKrash', 'Eraser', 'Hellbolt', 'Shield', 'Sword', 'Worm']
        super().__init__(name, mook_type, stats, weapons, armor, skills, special)
