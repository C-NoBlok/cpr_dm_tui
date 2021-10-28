from copy import deepcopy

from cpr.mooks.mook import Mook
from cpr.mooks.stats import Stats
from cpr.mooks.skills import Skills, Skill
from cpr.weapons import medium_melee_weapon, very_heavy_pistol


class BoosterGanger(Mook):
    def __init__(self):
        name = 'Booster Ganger'
        mook_type = 'grunt'
        stats = Stats(
            INT=2,
            REF=6,
            DEX=5,
            TECH=2,
            COOL=4,
            WILL=2,
            LUCK=0,
            MOVE=4,
            BODY=4,
            EMP=3,
        )
        pistol = very_heavy_pistol()
        pistol.name = 'Poor Quality VH Pistol'
        pistol.modifier = -1
        ripper = medium_melee_weapon()
        ripper.name = 'Ripper'
        weapons = [pistol, ripper]
        armor = {'head': 4, 'body': 4}

        skills = deepcopy(Skills())
        skills.athletics.rank = 9 - stats.__getattribute__(skills.athletics.base_stat)
        skills.brawling.rank = 9 - stats.__getattribute__(skills.brawling.base_stat)
        skills.conceal_reveal_object.rank = 4 - stats.__getattribute__(skills.conceal_reveal_object.base_stat)
        skills.concentration.rank = 4 - stats.__getattribute__(skills.concentration.base_stat)
        skills.conversation.rank = 5 - stats.__getattribute__(skills.conversation.base_stat)
        skills.drive_land_vehicle.rank = 10 - stats.__getattribute__(skills.drive_land_vehicle.base_stat)
        skills.education.rank = 5 - stats.__getattribute__(skills.education.base_stat)
        skills.endurance.rank = 9 - stats.__getattribute__(skills.endurance.base_stat)
        skills.evasion.rank = 7 - stats.__getattribute__(skills.evasion.base_stat)
        skills.first_aid.rank = 4 - stats.__getattribute__(skills.first_aid.base_stat)
        skills.handgun.rank = 10 - stats.__getattribute__(skills.handgun.base_stat)
        skills.human_perception.rank = 5 - stats.__getattribute__(skills.human_perception.base_stat)
        skills.interrogation.rank = 6 - stats.__getattribute__(skills.interrogation.base_stat)
        skills.perception.rank = 9 - stats.__getattribute__(skills.perception.base_stat)
        skills.persuasion.rank = 6 - stats.__getattribute__(skills.persuasion.base_stat)
        skills.resist_torture_drug.rank = 8 - stats.__getattribute__(skills.resist_torture_drug.base_stat)
        skills.shoulder_arms.rank = 10 - stats.__getattribute__(skills.shoulder_arms.base_stat)
        skills.stealth.rank = 7 - stats.__getattribute__(skills.stealth.base_stat)

        special = ['VH Pistol Ammo x30', 'Disposable Cellphone', 'Rippers', 'Techhair']
        super().__init__(name, mook_type, stats, weapons, armor, skills, special)
