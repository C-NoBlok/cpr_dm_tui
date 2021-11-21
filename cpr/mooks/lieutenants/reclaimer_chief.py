from copy import deepcopy

from cpr.mooks.mook import Mook
from cpr.mooks.stats import Stats
from cpr.mooks.skills import Skills, Skill
from cpr.weapons import shotgun, heavy_pistol, light_melee_weapon, heavy_melee_weapon


class ReclaimerChief(Mook):
    def __init__(self):
        name = 'Reclaimer Chief'
        mook_type = 'lieutenant'
        stats = Stats(
            INT=3,
            REF=6,
            DEX=6,
            TECH=5,
            COOL=4,
            WILL=5,
            LUCK=0,
            MOVE=4,
            BODY=6,
            EMP=4,
        )
        weapons = [shotgun(), heavy_pistol(), light_melee_weapon(), heavy_melee_weapon()]
        armor = {'head': 11, 'body': 11}

        skills = deepcopy(Skills())

        skills.athletics.rank = 12 - stats.__getattribute__(skills.athletics.base_stat)
        skills.basic_tech.rank = 9 - stats.__getattribute__(skills.basic_tech.base_stat)
        skills.brawling.rank = 8 - stats.__getattribute__(skills.brawling.base_stat)
        skills.concentration.rank = 7 - stats.__getattribute__(skills.concentration.base_stat)
        skills.conversation.rank = 6 - stats.__getattribute__(skills.conversation.base_stat)
        skills.deduction.rank = 7 - stats.__getattribute__(skills.deduction.base_stat)
        skills.drive_land_vehicle.rank = 10 - stats.__getattribute__(skills.drive_land_vehicle.base_stat)
        skills.education.rank = 5 - stats.__getattribute__(skills.education.base_stat)
        skills.electronics_security_tech.rank = 9 - stats.__getattribute__(skills.electronics_security_tech.base_stat)
        skills.endurance.rank = 11 - stats.__getattribute__(skills.endurance.base_stat)
        skills.evasion.rank = 8 - stats.__getattribute__(skills.evasion.base_stat)
        skills.first_aid.rank = 7 - stats.__getattribute__(skills.first_aid.base_stat)
        skills.handgun.rank = 10 - stats.__getattribute__(skills.handgun.base_stat)
        skills.human_perception.rank = 6 - stats.__getattribute__(skills.human_perception.base_stat)
        skills.land_vehicle_tech.rank = 7 - stats.__getattribute__(skills.land_vehicle_tech.base_stat)
        skills.language.rank = 5 - stats.__getattribute__(skills.language.base_stat)
        skills.local_expert.rank = 5 - stats.__getattribute__(skills.local_expert.base_stat)
        skills.melee_weapon.rank = 10 - stats.__getattribute__(skills.melee_weapon.base_stat)
        skills.paramedic.rank = 7 - stats.__getattribute__(skills.paramedic.base_stat)
        skills.perception.rank = 8 - stats.__getattribute__(skills.perception.base_stat)
        skills.persuasion.rank = 6 - stats.__getattribute__(skills.persuasion.base_stat)
        skills.pick_lock.rank = 7 - stats.__getattribute__(skills.pick_lock.base_stat)
        skills.resist_torture_drug.rank = 10 - stats.__getattribute__(skills.resist_torture_drug.base_stat)
        skills.shoulder_arms.rank = 10 - stats.__getattribute__(skills.shoulder_arms.base_stat)
        skills.stealth.rank = 10 - stats.__getattribute__(skills.stealth.base_stat)
        skills.weaponstech.rank = 9 - stats.__getattribute__(skills.weaponstech.base_stat)
        skills.wilderness_survival.rank = 7 - stats.__getattribute__(skills.wilderness_survival.base_stat)

        special = ['Slug Ammo x25', 'H Pistol Ammo x25', 'Agent', 'Grapple Gun', 'Radio Communicator',
                   'Tent & Camping Equipment', 'Nasal Filters', 'Neural Link (Chipware Socket, Tactile Boost)']

        super().__init__(name, mook_type, stats, weapons, armor, skills, special)
