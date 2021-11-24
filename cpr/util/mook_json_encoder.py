import json

from cpr.mooks.mook import Mook
from cpr.weapons.weapon import Weapon


class MookJsonEncoder(json.JSONEncoder):

    def default(self, o):

        if isinstance(o, Weapon):
            return o.__dict__

        return super().default(o)
