from cpr.mooks.mook import Mook, Stats
from cpr.weapons import poor_quality_shotgun, very_heavy_pistol

Netrunner = Mook(
    name='Netrunner',
    mook_type='lieutenant',
    stats=Stats(
        INT=7,
        REF=5,
        DEX=4,
        TECH=7,
        COOL=4,
        WILL=5,
        LUCK=0,
        MOVE=5,
        BODY=3,
        EMP=4
    ),
    weapons=[very_heavy_pistol],
    armor={'head': 11, 'body': 11},
    skills={
        'athletics': 9,
        'basic tech': 13,
        'brawling': 6,
        'conceal object': 11,
        'concentration': 9,
        'conversation': 6,
        'cryptograph': 11,
        'deduction': 11,
        'education': 11,
        'electronics/security tech': 11,
        'evasion': 6,
        'first aid': 9,
        'forgery': 9,
        'handgun': 10,
        'human perception': 6,
        'language (native)': 9,
        'local expert': 13,
        'library search': 11,
        'perception': 11,
        'persuasion': 6,
        'pick lock': 11,
        'shoulder arms': 5,
        'stealth': 9,
        'resist torture/drug': 7,
    },
    special=['Banhammer', 'DeckKrash', 'Eraser', 'Hellbolt', 'Shield', 'Sword', 'Worm']
)