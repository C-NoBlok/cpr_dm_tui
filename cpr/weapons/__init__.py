from .weapon import RangedWeapon, MeleeWeapon


def light_melee_weapon():
    return MeleeWeapon(
        name='Light Melee Weapon',
        melee_weapon_type='light',
        damage=1,
        concealable=True,
        cost=50,
        ROF=2
    )


def medium_melee_weapon():
    return MeleeWeapon(
        name='Medium Melee Weapon',
        melee_weapon_type='medium',
        damage=2,
        concealable=False,
        cost=50,
        ROF=2
    )


def heavy_melee_weapon():
    return MeleeWeapon(
        name='Heavy Melee Weapon',
        melee_weapon_type='very heavy',
        damage=3,
        concealable=False,
        cost=100,
        ROF=2
    )


def very_heavy_melee_weapon():
    return MeleeWeapon(
        name='Very Heavy Melee Weapon',
        melee_weapon_type='very heavy',
        damage=4,
        concealable=False,
        cost=500,
        ROF=1
    )


def medium_pistol():
    return RangedWeapon(
        name='Medium Pistol',
        damage=2,
        concealable=True,
        cost=50,
        ROF=2,
        skill='handgun',
        hands_required=1,
        clip_size=12
    )


def heavy_pistol():
    return RangedWeapon(
        name='Heavy Pistol',
        damage=3,
        concealable=True,
        cost=100,
        ROF=2,
        skill='handgun',
        hands_required=1,
        clip_size=8
    )


def very_heavy_pistol():
    return RangedWeapon(
        name='Very Heavy Pistol',
        damage=4,
        concealable=False,
        cost=100,
        ROF=1,
        skill='handgun',
        hands_required=1,
        clip_size=8
    )


def smg():
    return RangedWeapon(
        name='SMG',
        damage=2,
        concealable=True,
        cost=100,
        ROF=1,
        skill='handgun',
        hands_required=1,
        clip_size=30
    )


def heavy_smg():
    return RangedWeapon(
        name='Heavy SMG',
        damage=3,
        concealable=False,
        cost=100,
        ROF=1,
        skill='handgun',
        hands_required=1,
        clip_size=40
    )


def shotgun():
    return RangedWeapon(
        name='Shotgun',
        damage=5,
        concealable=False,
        cost=100,
        ROF=1,
        skill='shoulder_arms',
        hands_required=2,
        clip_size=4
    )


def assault_rifle():
    return RangedWeapon(
        name='Assult Rifle',
        damage=5,
        concealable=False,
        cost=500,
        ROF=1,
        skill='shoulder_arms',
        hands_required=2,
        clip_size=25
    )


def sniper_rifle():
    return RangedWeapon(
        name='Sniper Rifle',
        damage=5,
        concealable=False,
        cost=500,
        ROF=1,
        skill='shoulder_arms',
        hands_required=2,
        clip_size=4
    )


def bows_and_crossbows():
    return RangedWeapon(
        name='Bows & Crossbows',
        damage=4,
        concealable=False,
        cost=100,
        ROF=1,
        skill='archery',
        hands_required=2,
        clip_size=None
    )


def grenade_launcher():
    return RangedWeapon(
        name='Grenade Launcher',
        damage=6,
        concealable=False,
        cost=500,
        ROF=1,
        skill='heavy_weapons',
        hands_required=2,
        clip_size=2
    )


def rocket_launcher():
    return RangedWeapon(
        name='Rocket Launcher',
        damage=8,
        concealable=False,
        cost=500,
        ROF=1,
        skill='heavy_weapons',
        hands_required=2,
        clip_size=1
    )


def flame_thrower():
    return RangedWeapon(
        name='Flame Thrower',
        damage=5,
        concealable=False,
        cost=500,
        ROF=1,
        skill='heavy_weapons',
        hands_required=2,
        clip_size=4
    )
