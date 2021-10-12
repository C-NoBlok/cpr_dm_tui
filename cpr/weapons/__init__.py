from .weapon import RangedWeapon, MeleeWeapon

poor_quality_shotgun = RangedWeapon(
    name='Poor Quality Shotgun',
    damage=5,
    concealable=False,
    cost=100,
    ROF=1,
    skill='shoulder arms',
    hands_required=2
)

very_heavy_pistol = RangedWeapon(
    name='Very Heavy Pistol',
    damage=4,
    concealable=False,
    cost=100,
    ROF=1,
    skill='handgun',
    hands_required=1
)

cattle_prod = MeleeWeapon(
    name='cattle prod',
    melee_weapon_type='Heavy',
    damage=3,
    concealable=False,
    cost=500,
    ROF=2
)