from cpr.mooks.grunts.bodyguards import Bodyguard
from cpr.mooks.lieutenants.netrunners import Netrunner
from cpr.mooks.boss.cyberpsychos import CyberPscycho
from cpr.mooks.mini_boss.pyros import Pyro


available_mook_list = [Bodyguard, Netrunner, CyberPscycho, Pyro]

mooks = {available_mook.name: available_mook
         for available_mook in available_mook_list}
