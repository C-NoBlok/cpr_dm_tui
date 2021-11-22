from copy import deepcopy

from cpr.mooks.mook import Mook
from cpr.mooks.stats import Stats
from cpr.mooks.skills import Skills
from cpr.weapons import assault_rifle, very_heavy_pistol, light_melee_weapon


class Outrider(Mook):
    def __init__(self):
        name = 'Outrider'
        mook_type = 'mini-boss'
        stats=Stats(
            INT=6,
            REF=8,
            DEX=8,
            TECH=3,
            COOL=5,
            WILL=6,
            LUCK=0,
            MOVE=6,
            BODY=6,
            EMP=6
        )
        weapons = [assault_rifle(), very_heavy_pistol(), light_melee_weapon()]
        armor = {'head': 11, 'body': 11}
        skills = deepcopy(Skills())
        skills.animal_handling.rank = 8 - stats.__getattribute__(skills.animal_handling.base_stat)
        skills.athletics.rank = 14 - stats.__getattribute__(skills.athletics.base_stat)
        skills.autofire.rank = 12 - stats.__getattribute__(skills.autofire.base_stat)
        skills.basic_tech.rank = 5 - stats.__getattribute__(skills.basic_tech.base_stat)
        skills.brawling.rank = 14 - stats.__getattribute__(skills.brawling.base_stat)
        skills.concentration.rank = 10 - stats.__getattribute__(skills.concentration.base_stat)
        skills.conversation.rank = 6 - stats.__getattribute__(skills.conversation.base_stat)
        skills.criminology.rank = 10 - stats.__getattribute__(skills.conversation.base_stat)
        skills.drive_land_vehicle.rank = 14 - stats.__getattribute__(skills.drive_land_vehicle.base_stat)
        skills.education.rank = 8 - stats.__getattribute__(skills.education.base_stat)
        skills.endurance.rank = 10 - stats.__getattribute__(skills.endurance.base_stat)
        skills.evasion.rank = 14 - stats.__getattribute__(skills.evasion.base_stat)
        skills.first_aid.rank = 5 - stats.__getattribute__(skills.first_aid.base_stat)
        skills.handgun.rank = 14 - stats.__getattribute__(skills.handgun.base_stat)
        skills.human_perception.rank = 8 - stats.__getattribute__(skills.human_perception.base_stat)
        skills.land_vehicle_tech.rank = 7 - stats.__getattribute__(skills.land_vehicle_tech.base_stat)
        skills.language.rank = 8 - stats.__getattribute__(skills.language.base_stat)
        skills.local_expert.rank = 10 - stats.__getattribute__(skills.local_expert.base_stat)
        skills.melee_weapon.rank = 12 - stats.__getattribute__(skills.melee_weapon.base_stat)
        skills.perception.rank = 14 - stats.__getattribute__(skills.perception.base_stat)
        skills.persuasion.rank = 7 - stats.__getattribute__(skills.persuasion.base_stat)
        skills.resist_torture_drug.rank = 12 - stats.__getattribute__(skills.resist_torture_drug.base_stat)
        skills.shoulder_arms.rank = 14 - stats.__getattribute__(skills.shoulder_arms.base_stat)
        skills.stealth.rank = 12 - stats.__getattribute__(skills.stealth.base_stat)
        skills.streetwise.rank = 9 - stats.__getattribute__(skills.streetwise.base_stat)
        skills.tracking.rank = 10 - stats.__getattribute__(skills.tracking.base_stat)

        skills.science.subtype = 'Chemistry'
        special = ['Moto Family (4)', 'Rifle Ammo x60', 'VH Pistol Ammo x40', 'Handcuffs x2', 'Homing Tracers',
                   ' Radio Communicator', 'Cyberaudio Suite (Amplified Hearing)',
                   'Cybereye (Targeting Scope, TeleOptics)', 'Neural Link (Interface Plugs)']

        super().__init__(name, mook_type, stats, weapons, armor, skills, special)


