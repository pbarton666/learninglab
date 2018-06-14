#py_except_2.py

#simplest possible custom exception
class SimpleException(Exception):
    pass

#upgrades a bot to customize output: __str__() used with print()
class WombatException(Exception):
    def __str__(self):
        return("Wombat!")

def wombat():
    raise WombatException

wombat()
