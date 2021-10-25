import unittest
from unittest import TestCase

import os
print(os.getcwd())

from cpr.mooks.mook import Mook
from cpr.mooks.stats import Stats
from cpr.mooks.skills import Skills


def create_mook():
    stats = Stats(8,8,8,8,8,8,8,8,8,8)
    mook = Mook(
        name='Test Mook',
        mook_type='mook',
        stats=stats,
        weapons=[],
        armor={},
        skills=Skills(),
        special={}
    )
    return mook

class TestMook(TestCase):

    def setUp(self):
        self.mook = create_mook()

    def test_init(self):
        self.assertIsInstance(self.mook, Mook)

    def test_init_hp(self):
        self.assertEqual(self.mook.hp, 50)

    def test_stats_max_hp(self):
        self.assertEqual(self.mook.stats.max_hp, 50)

    def test_combat_skills(self):
        self.mook.skills = {
            'evasion': 10,
            'melee weapon': 8,
            'brawling': 8,
            'acting': 14,
            'riding': 3,
        }

        c_skills = self.mook.combat_skills
        print(c_skills)
        self.assertIsInstance(c_skills, dict)
        self.assertNotIn('riding', c_skills)
        self.assertIn('brawling', c_skills)

    def test_non_combat_skills(self):
        self.mook.skills = Skills.from_rank_dict({
            'evasion': 10,
            'melee_weapon': 8,
            'brawling': 8,
            'acting': 14,
            'riding': 3,
        })
        c_skills = self.mook.non_combat_skills
        print(c_skills)
        self.assertIsInstance(c_skills, dict)
        self.assertIn('riding', c_skills)
        self.assertNotIn('brawling', c_skills)

    def test_to_dict(self):
        mook_dump = self.mook.to_dict()
        print(mook_dump)
        mook_from_dump = Mook.from_dict(mook_dump)
        print(self.mook)
        print(mook_from_dump)
        self.assertEqual(mook_from_dump, self.mook)




