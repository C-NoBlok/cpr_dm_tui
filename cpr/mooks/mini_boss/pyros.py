from copy import deepcopy

from cpr.mooks.mook import Mook
from cpr.mooks.stats import Stats
from cpr.mooks.skills import Skills
from cpr.weapons import poor_quality_shotgun, very_heavy_pistol, cattle_prod

class Pyro(Mook):
    def __init__(self):
        name='Pyro'
        mook_type='mini-boss'
        stats=Stats(
            INT=5,
            REF=8,
            DEX=6,
            TECH=7,
            COOL=4,
            WILL=4,
            LUCK=0,
            MOVE=6,
            BODY=5,
            EMP=3
        )
        weapons=[very_heavy_pistol, cattle_prod]
        armor={'head': 11, 'body': 11}
        skills = deepcopy(Skills())
        skills.from_rank_dict({
            'athletics': 5,
            'basic_tech': 5,
            'brawling': 4,
            'concentration': 3,
            'conversation': 1,
            'demolitions': 6,
            'drive_land_vehicle': 2,
            'education': 2,
            'evasion': 7,
            'first_aid': 2,
            'handgun': 6,
            'heavy_weapons': 6,
            'human_perception': 2,
            'interrogation': 6,
            'language': 2,
            'local_expert': 2,
            'melee_weapon': 7,
            'perception': 7,
            'persuasion': 2,
            'resist_torture_drug': 10,
            'science': 5,
            'stealth': 4,
            'streetwise': 4,
            'tactics': 3,
        })
        skills.science.subtype = 'Chemistry'
        special=['Combat Awareness: 4', 'Flamethrower Ammo', '(Incendiary Shotgun Shells) x8',
                 'VH Pistol Ammo x50', 'Incendiary Grenade x1',
                 'Flashbang Grenade x1', 'Cyberaudio Suite (Level Dampners)',
                 'Cybereye x2 (Anti-Dazzle x2)', 'Nasal Filters']
        super().__init__(name, mook_type, stats, weapons, armor, skills, special)


