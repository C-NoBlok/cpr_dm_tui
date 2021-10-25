from unittest import TestCase
from dataclasses import is_dataclass

from cpr.mooks.skills import Skill, Skills
from cpr.mooks.grunts.bodyguards import Bodyguard

class TestSkills(TestCase):

    def setUp(self) -> None:
        self.skills = Skills()

    def test_from_dict(self):
        self.assertTrue(is_dataclass(self.skills))
        self.skills.from_dict({})
        print(dir(self.skills))

    def test_load_from_rank_dict(self):
        skills = Skills().from_rank_dict({
            'athletics': 4,
            'brawling': 7,
            'concentration': 3,
            'conversation': 2,
            'drive_land_vehicle': 4,
            'education': 2,
            'endurance': 5,
            'evasion': 2,
            'shoulder_arms': 9,
            'first_aid': 2,
            'handgun': 4,
            'human_perception': 2,
            'interrogation': 2,
            'language': 2,
            'local_expert': 2,
            'perception': 5,
            'persuasion': 2,
            'resist_torture_drug': 4,
            'shoulder_arms': 4,
            'stealth': 2,
        })
        print(skills)
        self.assertEqual(skills.athletics.rank, 4)
        self.assertEqual(skills.evasion.rank, 2)
        self.assertEqual(skills.brawling.rank, 7)
        self.assertEqual(skills.perception.rank, 5)

    def test_body_gaurd_skills(self):
        mook = Bodyguard
        print(mook.skills)
        assert 0

