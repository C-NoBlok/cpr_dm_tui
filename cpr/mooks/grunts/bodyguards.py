from cpr.mooks.mook import Mook, Stats
from cpr.weapons import poor_quality_shotgun, very_heavy_pistol

Bodyguard = Mook(
    name='Body Guard',
    mook_type='mook',
    stats=Stats(
        INT=2,
        REF=5,
        DEX=4,
        TECH=1,
        COOL=3,
        WILL=3,
        LUCK=-1,
        MOVE=3,
        BODY=5,
        EMP=2
    ),
    weapons=[poor_quality_shotgun, very_heavy_pistol],
    armor={'head': 7, 'body': 7},
    skills={
        'handgun': 9,
        'brawling': 10,
        'shoulder arms': 9,
        'stealth': 6,
        'resist torture/drug': 7,
        'evasion': 6
    },
    special=['Slug Ammo x24', 'VH Pistol Ammo x25', 'Radio Communicator']
)
