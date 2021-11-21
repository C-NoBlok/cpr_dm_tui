from copy import deepcopy

from cpr.mooks.mook import Mook
from cpr.mooks.stats import Stats
from cpr.mooks.skills import Skills
from cpr.weapons import assault_rifle, very_heavy_pistol, medium_melee_weapon


class SecurityOfficer(Mook):
    def __init__(self):
        name = 'Security Officer'
        mook_type = 'lieutenant'
        stats = Stats(
            INT=4,
            REF=6,
            DEX=4,
            TECH=4,
            COOL=6,
            WILL=5,
            LUCK=0,
            MOVE=4,
            BODY=7,
            EMP=4,
        )
        weapons = [assault_rifle(), very_heavy_pistol(), medium_melee_weapon()]
        armor = {'head': 13, 'body': 13}

        skills = deepcopy(Skills())

        skills.athletics.rank = 8 - stats.__getattribute__(skills.athletics.base_stat)
        skills.autofire.rank = 10 - stats.__getattribute__(skills.autofire.base_stat)
        skills.brawling.rank = 8 - stats.__getattribute__(skills.brawling.base_stat)
        skills.concentration.rank = 7 - stats.__getattribute__(skills.concentration.base_stat)
        skills.conversation.rank = 6 - stats.__getattribute__(skills.conversation.base_stat)
        skills.deduction.rank = 6 - stats.__getattribute__(skills.deduction.base_stat)
        skills.drive_land_vehicle.rank = 10 - stats.__getattribute__(skills.drive_land_vehicle.base_stat)
        skills.education.rank = 6 - stats.__getattribute__(skills.education.base_stat)
        skills.endurance.rank = 11 - stats.__getattribute__(skills.endurance.base_stat)
        skills.evasion.rank = 8 - stats.__getattribute__(skills.evasion.base_stat)
        skills.first_aid.rank = 6 - stats.__getattribute__(skills.first_aid.base_stat)
        skills.handgun.rank = 8 - stats.__getattribute__(skills.handgun.base_stat)
        skills.human_perception.rank = 6 - stats.__getattribute__(skills.human_perception.base_stat)
        skills.language.rank = 6 - stats.__getattribute__(skills.language.base_stat)
        skills.local_expert.rank = 6 - stats.__getattribute__(skills.local_expert.base_stat)
        skills.melee_weapon.rank = 8 - stats.__getattribute__(skills.melee_weapon.base_stat)
        skills.perception.rank = 6 - stats.__getattribute__(skills.perception.base_stat)
        skills.persuasion.rank = 8 - stats.__getattribute__(skills.persuasion.base_stat)
        skills.resist_torture_drug.rank = 10 - stats.__getattribute__(skills.resist_torture_drug.base_stat)
        skills.shoulder_arms.rank = 8 - stats.__getattribute__(skills.shoulder_arms.base_stat)
        skills.stealth.rank = 4 - stats.__getattribute__(skills.stealth.base_stat)
        skills.tactics.rank = 8 - stats.__getattribute__(skills.tactics.base_stat)

        special = ['Rifle Ammo x50', 'VH Pistol Ammo x30', 'Bulletproof Shield (10 HP)', 'Binoculars',
                   'Disposable Cellphone', 'Flashlight', 'Handcuffs x2', 'Radio Communicator',
                   'Radio Scanner / Music Player', 'Neural Link (Kerenzikov Speedware)']

        super().__init__(name, mook_type, stats, weapons, armor, skills, special)
