from dataclasses import dataclass, asdict
from typing import Dict
import logging

logger = logging.getLogger('cpr')

@dataclass()
class Skill:
    name: str
    base_stat: str
    category: str
    rank: int = 0
    subtype: str = None


@dataclass()
class Skills:

    accounting: Skill = Skill('Accouting', 'INT', 'education')
    acting: Skill = Skill('Acting', 'COOL', 'performance')
    air_vehicle_tech: Skill = Skill('Air Vehicle Tech', 'TECH', 'technique')
    animal_handling: Skill = Skill('Animal Handling', 'INT', 'education')
    archery: Skill = Skill('Archer', 'REF', 'ranged weapon')
    athletics: Skill = Skill('Athletics', 'DEX', 'body', rank=2)
    autofire: Skill = Skill('Autofire', 'REF', 'ranged weapons')
    basic_tech: Skill = Skill('Basic Tech', 'TECH', 'technique')
    brawling: Skill = Skill('Brawling', 'DEX', 'fighting', rank=2)
    bribery: Skill = Skill('Bribery', 'COOL', 'social')
    bureaucracy: Skill = Skill('Bureaucracy', 'INT', 'education')
    composition: Skill = Skill('Composition', 'INT', 'education')
    conceal_reveal_object: Skill = Skill('Conceal/Reveal Object', 'INT', 'awareness')
    concentration: Skill = Skill('Concentration', 'WILL', 'awareness', rank=2)
    contortionist: Skill = Skill('Contortionist', 'DEX', 'body')
    conversation: Skill = Skill('Conversation', 'EMP', 'social', rank=2)
    criminology: Skill = Skill('Criminology', 'INT', 'education')
    cryptography: Skill = Skill('Cryptography', 'INT', 'education')
    cybertech: Skill = Skill('Cybertech', 'TECH', 'technique')
    dance: Skill = Skill('Dance', 'DEX', 'body')
    deduction: Skill = Skill('Deduction', 'INT', 'education')
    demolitions: Skill = Skill('Demolitions', 'TECH', 'technique')
    drive_land_vehicle: Skill = Skill('Drive Land Vehicle', 'REF', 'control')
    education: Skill = Skill('Education', 'INT', 'education', rank=2)
    endurance: Skill = Skill('Endurance', 'WILL', 'body')
    electronics_security_tech: Skill = Skill('Electronics/Security Tech', 'TECH', 'technique')
    evasion: Skill = Skill('Evasion', 'DEX', 'fighting', rank=2)
    first_aid: Skill = Skill('First Aid', 'TECH', 'technique', rank=2)
    forgery: Skill = Skill('Forgery', 'TECH', 'tecnique')
    gambling: Skill = Skill('Gambling', 'INT', 'education')
    handgun: Skill = Skill('Handgun', 'REF', 'ranged weapon')
    heavy_weapons: Skill = Skill('Heavy Weapons', 'REF', 'ranged weapon')
    human_perception: Skill = Skill('Human Perception', 'EMP', 'social', rank=2)
    interrogation: Skill = Skill('Interrogation', 'COOL', 'social')
    land_vehicle_tech: Skill = Skill('Land Vehicle Tech', 'TECH', 'technique')
    language: Skill = Skill('Language', 'INT', 'education', subtype='StreetSlang', rank=2)
    library_search: Skill = Skill('Library Search', 'INT', 'education')
    lip_reading: Skill = Skill('Lip Reading', 'INT', 'awareness')
    local_expert: Skill = Skill('Local Expert', 'INT', 'education', subtype='Home', rank=2)
    martial_arts: Skill = Skill('Martial Arts', 'DEX', 'fighting', subtype='Karate')
    melee_weapon: Skill = Skill('Melee Weapon', 'DEX', 'fighting')
    paint_draw_sculpt: Skill = Skill('Paint/Draw/Sculpt', 'TECH', 'tecnique')
    paramedic: Skill = Skill('Paramedic', 'TECH', 'technique')
    perception: Skill = Skill('Perception', 'INT', 'awareness')
    personal_grooming: Skill = Skill('Personal Grooming', 'COOL', 'social')
    persuasion: Skill = Skill('Persuasion', 'COOL', 'social', rank=2)
    photography_film: Skill = Skill('Photography/Film', 'TECH', 'technique')
    pick_lock: Skill = Skill('Pick Lock', 'TECH', 'technique')
    pick_pocket: Skill = Skill('Pick Pocket', 'TECH', 'technique')
    pilot_air_vehicle: Skill = Skill('Pilot Air Vehicle', 'REF', 'control')
    pilot_sea_vehicle: Skill = Skill('Pilot Sea Vehicle', 'REF', 'control')
    play_instrument: Skill = Skill('Play Instrument', 'TECH', 'performance')
    resist_torture_drug: Skill = Skill('Resist Torture/Drugs', 'WILL', 'body')
    riding: Skill = Skill('Riding', 'REF', 'control')
    sea_vehicle_tech: Skill = Skill('Sea Vehicle Tech', 'TECH', 'tecnhique')
    science: Skill = Skill('Science', 'INT', 'education', subtype='physics')
    shoulder_arms: Skill = Skill('Shoulder Arms', 'REF', 'ranged weapons')
    stealth: Skill = Skill('Stealth', 'DEX', 'body', rank=2)
    streetwise: Skill = Skill('Streetwise', 'COOL', 'social', rank=2)
    tactics: Skill = Skill('Tactics', 'INT', 'education')
    tracking: Skill = Skill('Tracking', 'INT', 'awareness')
    trading: Skill = Skill('Trading', 'COOL', 'social')
    weaponstech: Skill = Skill('Weaponstech', 'TECH', 'technique')
    wilderness_survival: Skill = Skill('Wilderness Survival', 'INT', 'education')
    wardrobe_and_style: Skill = Skill('Wardrobe & Style', 'COOL', 'social')

    @staticmethod
    def from_dict(skills_dict: Dict):
        """ This is probably not the right way to do this."""
        skills = Skills()
        for k, v in skills_dict.items():
            exec(f'skills.{k} = Skill(**{v})')
        return skills

    def from_rank_dict(self, skills_dict: Dict):
        for k, v in skills_dict.items():
            self.__getattribute__(k).rank = v

    @property
    def skills_by_name(self):
        skill_names = {}
        for skill, info in self.__dict__.items():
            skill_names[info.name] = info
        return skill_names

    @property
    def total_ranks(self):
        return sum([skill.rank for name, skill in self.__dict__.items()])

    def to_dict(self):
        return asdict(self)

