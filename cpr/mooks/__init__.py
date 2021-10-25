from .grunts.bodyguards import Bodyguard
from .grunts.booster_ganger import BoosterGanger
from .grunts.security_operative import SecurityOperative
from .lieutenants.netrunners import Netrunner
from .boss.cyberpsychos import CyberPsycho
from .mini_boss.pyros import Pyro


mooks = {
    'Body Guard': Bodyguard,
    'Booster Ganger': BoosterGanger,
    'Security Operative': SecurityOperative,
    'Netrunner': Netrunner,
    'Pyro': Pyro,
    'CyberPsycho': CyberPsycho,
}
