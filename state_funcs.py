"""Handles thermodynamic state calculations"""
# Thermo State Solver
# Solves for state parameters at various points in a simple thermodynamic model
# Developed by Neal DeBuhr

import random
import sys
from iapws import IAPWS95 as w5
from iapws import IAPWS97 as w7
import CoolProp.CoolProp as cp
import scipy.optimize as sco

## Variable Declarations ##

minH = 5e3
maxH = 5410e3
minT = 274 #kelvin
maxT = 1000 #kelvin
minP = 10e3 #Pa
maxP = 100e6 #Pa
minS = 0.0001
maxS = 156
minW = 1e6
maxW = 1e9
minMDOT = 1
maxMDOT = 100

## Some Helper Functions ##

def therm_solve(eq, initials, watchvars):
    global watches
    watches = []
    sol = []
    for watchvar in watchvars:
        watches.append(watchvar)
    for x in range(0, 10):
        try:
            sol.append(sco.fsolve(eq, guess_water(initials)))
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
    if sol == []:
        return sco.fsolve(eq, guess_water(initials))
    return sol

def guess_water(list1):
    out = []
    for item in list1:
        if item == 'H':
            out.append(random.uniform(minH, maxH))
        if item == 'T':
            out.append(random.uniform(minT, maxT))
        if item == 'P':
            out.append(random.uniform(minP, maxP))
        if item == 'S':
            out.append(random.uniform(minS, maxS))
        if item == 'WORK':
            out.append(random.uniform(minW, maxW))
        if item == 'BAL':
            out.append(0)
        if item == 'MDOT':
            out.append(random.uniform(minMDOT, maxMDOT))
    return out

def int2phase(int1):
    ind = phase_dict().index(int1)
    return phase_dict()[ind+1]

def phase2int(phase1):
    ind = phase_dict().index(phase1)
    return phase_dict()[ind-1]

def phase_dict():
    res = []
    res.append(cp.get_phase_index('phase_twophase'))
    res.append('phase_twophase')
    res.append(cp.get_phase_index('phase_liquid'))
    res.append('phase_liquid')
    res.append(cp.get_phase_index('phase_gas'))
    res.append('phase_gas')
    res.append(cp.get_phase_index('phase_supercritical_liquid'))
    res.append('phase_supercritical_liquid')
    res.append(cp.get_phase_index('phase_supercritical'))
    res.append('phase_supercritical')
    res.append(cp.get_phase_index('phase_supercritical_gas'))
    res.append('phase_supercritical_gas')
    return res

def make_cool(param1, val1, param2, val2, state):
    return [param1, val1, param2, val2, 'state', state]

def get_cool(param, pdict):
    if param == "Phase":
        return int2phase(cp.PropsSI(param, pdict[0], pdict[1], pdict[2], pdict[3], pdict[5]))
    return cp.PropsSI(param, pdict[0], pdict[1], pdict[2], pdict[3], pdict[5])

def make_ideal(P=None, V=None, n=None, T=None, R=None):
    if R is None:
        print('R needs to be specified for the ideal gas')
    if P is None:
        P = (n*R*T)/V
    if V is None:
        V = (n*R*T)/P
    if n is None:
        n = (P*V)/(R*T)
    if T is None:
        T = (P*V)/(R*n)
    return ['P', P, 'V', V, 'n', n, 'R', R, 'T', T]

def get_ideal(param, pdict):
    spot = pdict.index(param)
    return spot+1
