from copy import deepcopy
from cpr.mooks.mook import Mook
from cpr.mooks.stats import Stats
from cpr.mooks.skills import Skills
from cpr.weapons import poor_quality_shotgun, very_heavy_pistol

class CyberPsycho(Mook):

    def __init__(self):
        name = 'CyberPsycho'
        mook_type = 'boss'
        stats = Stats(
            INT=5,
            REF=8,
            DEX=8,
            TECH=5,
            COOL=4,
            WILL=7,
            LUCK=0,
            MOVE=8,
            BODY=10,
            EMP=0
        )
        weapons = [very_heavy_pistol]
        armor = {'head': 11, 'body': 11}
        skills = deepcopy(Skills())
        skills.from_rank_dict({
            'athletics': 8,
            'autofire': 6,
            'basic_tech': 6,
            'brawling': 7,
            'concentration': 1,
            'conversation': 2,
            'drive_land_vehicle': 2,
            'education': 2,
            'endurance': 3,
            'evasion': 5,
            'first_aid': 1,
            'handgun': 4,
            'heavy_weapons': 6,
            'human_perception': 2,
            'interrogation': 9,
            'language': 2,
            'local_expert': 2,
            'melee_weapon': 9,
            'perception': 4,
            'persuasion': 2,
            'resist_torture_drug': 8,
            'stealth': 2,
            'tracking': 5
        })
        special = ['Armor Piercing Grenade x2', 'Heavy Pistol Ammo x100',
                 'Cyberarm x2 ( Popup Grenade Launcher x2, Popup Heavy SMG, Wolvers)',
                 'Cyberleg x2 (Jump Boosters x2)', 'Cybersnake', 'Grafted Muscle & Bone Lace',
                 'Neural Link (Chipware Socket, Pain Editor)', 'Subdermal Armor']
        super().__init__(name, mook_type, stats, weapons, armor, skills, special)

