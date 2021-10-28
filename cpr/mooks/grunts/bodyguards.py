from copy import deepcopy

from cpr.mooks.mook import Mook
from cpr.mooks.stats import Stats
from cpr.mooks.skills import Skills
from cpr.weapons import shotgun, very_heavy_pistol


class Bodyguard(Mook):
    def __init__(self):
        name = 'Body Guard'
        mook_type = 'grunt'
        stats = Stats(
            INT=3,
            REF=6,
            DEX=5,
            TECH=2,
            COOL=4,
            WILL=4,
            LUCK=0,
            MOVE=4,
            BODY=6,
            EMP=3
        )
        pq_shotgun = shotgun()
        pq_shotgun.name = 'Poor Quality Shotgun'
        pq_shotgun.modifier = -1

        weapons = [pq_shotgun, very_heavy_pistol()]
        armor = {'head': 7, 'body': 7}

        # Why does Skills not instantiate a new object?
        skills = deepcopy(Skills())
        skills.from_rank_dict({
            'athletics': 4,
            'brawling': 5,
            'concentration': 3,
            'conversation': 2,
            'drive_land_vehicle': 4,
            'education': 2,
            'endurance': 5,
            'evasion': 2,
            'shoulder_arms': 4,
            'first_aid': 2,
            'handgun': 4,
            'human_perception': 2,
            'interrogation': 2,
            'language': 2,
            'local_expert': 2,
            'perception': 5,
            'persuasion': 2,
            'resist_torture_drug': 4,
            'shoulder_arms': 4,
            'stealth': 2,
        })
        special = ['Slug Ammo x24', 'VH Pistol Ammo x25', 'Radio Communicator']

        super().__init__(name, mook_type, stats, weapons, armor, skills, special)



