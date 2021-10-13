import unittest
from unittest import TestCase

from cpr.weapons.weapon import Weapon, MeleeWeapon, RangedWeapon

def create_weapon():
    w = Weapon(
        name='base_weapon',
        damage=1,
        concealable=True,
        cost=100,
        ROF=2
    )
    return w

def create_ranged_weapon():
    w = RangedWeapon(
        name='base_weapon',
        damage=1,
        concealable=True,
        cost=100,
        ROF=2,
        skill='handgun',
        hands_required=1
    )
    return w

def create_melee_weapon():
    w = MeleeWeapon(
        name='base_weapon',
        damage=1,
        concealable=True,
        cost=100,
        ROF=2,
        melee_weapon_type='light'
    )
    return w

class TestWeapon(TestCase):

    def setUp(self):
        self.weapon = create_weapon()

    def test_init(self):
        self.assertIsInstance(self.weapon, Weapon)

    def test_hit(self):
        dmg = self.weapon.hit()
        self.assertIsInstance(dmg, int)

class TestRangedWeapon(TestCase):

    def setUp(self):
        self.weapon = create_ranged_weapon()

    def test_init(self):
        self.assertIsInstance(self.weapon, RangedWeapon)

    def test_skill(self):
        self.assertEqual(self.weapon.skill, 'handgun')

class TestMeleeWeapon(TestCase):

    def setUp(self):
        self.weapon = create_melee_weapon()

    def test_init(self):
        self.assertIsInstance(self.weapon, MeleeWeapon)
        self.assertEqual(self.weapon.melee_weapon_type, 'light')
