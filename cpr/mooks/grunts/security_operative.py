from copy import deepcopy
from cpr.mooks.mook import Mook
from cpr.mooks.stats import Stats
from cpr.mooks.skills import Skills
from cpr.weapons import poor_quality_shotgun, very_heavy_pistol


class SecurityOperative(Mook):
    def __init__(self):
        name = 'Security Operative'
        mook_type = 'grunt'
        stats = Stats(
            INT=3,
            REF=7,
            DEX=4,
            TECH=2,
            COOL=2,
            WILL=3,
            LUCK=0,
            MOVE=3,
            BODY=5,
            EMP=3
        )
        weapons = [very_heavy_pistol]
        armor = {'head': 7, 'body': 7}
        skills = deepcopy(Skills())

        skills.athletics.rank = 8 - stats.__getattribute__(skills.athletics.base_stat)
        skills.autofire.rank = 10 - stats.__getattribute__(skills.autofire.base_stat)
        skills.brawling.rank = 6 - stats.__getattribute__(skills.brawling.base_stat)
        skills.concentration.rank = 7 - stats.__getattribute__(skills.concentration.base_stat)
        skills.conversation.rank = 5 - stats.__getattribute__(skills.conversation.base_stat)
        skills.education.rank = 5 - stats.__getattribute__(skills.education.base_stat)
        skills.evasion.rank = 6 - stats.__getattribute__(skills.evasion.base_stat)
        skills.first_aid.rank = 4 - stats.__getattribute__(skills.first_aid.base_stat)
        skills.handgun.rank = 10 - stats.__getattribute__(skills.handgun.base_stat)
        skills.human_perception.rank = 5 - stats.__getattribute__(skills.human_perception.base_stat)
        skills.interrogation.rank = 6 - stats.__getattribute__(skills.interrogation.base_stat)
        skills.perception.rank = 5 - stats.__getattribute__(skills.perception.base_stat)
        skills.persuasion.rank = 4 - stats.__getattribute__(skills.persuasion.base_stat)
        skills.melee_weapon.rank = 6 - stats.__getattribute__(skills.melee_weapon.base_stat)
        skills.resist_torture_drug.rank = 5 - stats.__getattribute__(skills.resist_torture_drug.base_stat)
        skills.shoulder_arms.rank = 10 - stats.__getattribute__(skills.shoulder_arms.base_stat)
        skills.stealth.rank = 6 - stats.__getattribute__(skills.stealth.base_stat)

        special = ['Rifle x40', 'VH Pistol Ammo x20', 'Radio Communicator']
        super().__init__(name, mook_type, stats, weapons, armor, skills, special)
