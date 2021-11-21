from .grunts.bodyguards import Bodyguard
from .grunts.booster_ganger import BoosterGanger
from .grunts.security_operative import SecurityOperative
from .lieutenants.netrunners import Netrunner
from .lieutenants.reclaimer_chief import ReclaimerChief
from .lieutenants.security_officer import SecurityOfficer
from .boss.cyberpsychos import CyberPsycho
from .mini_boss.pyros import Pyro
from .mini_boss.outrider import Outrider


mooks = {
    'Body Guard': Bodyguard,
    'Booster Ganger': BoosterGanger,
    'Security Operative': SecurityOperative,
    'Netrunner': Netrunner,
    'Pyro': Pyro,
    'CyberPsycho': CyberPsycho,
}

grunts = {
    'Body Guard': Bodyguard,
    'Booster Ganger': BoosterGanger,
    'Security Operative': SecurityOperative,
}

lieutenants = {
    'Netrunner': Netrunner,
    'Reclaimer Chief': ReclaimerChief,
    'Security Officer': SecurityOfficer,
}

mini_bosses = {
    'Pyro': Pyro,
    'Outrider': Outrider
}

bosses = {
    'CyberPsycho': CyberPsycho,
}