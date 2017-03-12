
# Python functions for solving Themodynamics problems
# Developed by Neal DeBuhr
# Intended application is university introductory thermodynamics courses

from iapws import IAPWS95 as w5
from iapws import IAPWS97 as w7
import CoolProp.CoolProp as cp
import scipy as sc
import scipy.optimize as sco
import numpy.linalg as npl
import math
import random
import sys

## Some Helper Functions ##

def secInYear():
	return 365*24*60*60

def nealSolve(eq,initials,watchvars):
	global watches
	watches=[]
	sol=[]
	for watchvar in watchvars:
		watches.append(watchvar)
	for x in range(0,10):
		try:
			sol.append(sco.fsolve(eq,guessWater(initials)))
			print 'Solution Found!'
		except ValueError:
			print '----Value Error----'
		except:
		    print "Unexpected error:", sys.exc_info()[0]
		    raise
	if sol==[]:
		return sco.fsolve(eq,guessWater(initials))
	return sol

def guessWater(list1):
	out=[]
	for item in list1:
		if item=='H':
			out.append(random.uniform(5e3,5410e3))
		if item=='T':
			out.append(random.uniform(274,1000))
		if item=='P':
			out.append(random.uniform(10e3,100e6))
		if item=='S':
			out.append(random.uniform(0.0001,156))
		if item=='WORK':
			out.append(random.uniform(1e6,1e9))
		if item=='BAL':
			out.append(0)
		if item=='MDOT':
			out.append(random.uniform(1,100))
	return out

def int2phase(int1):
	ind=phaseDict().index(int1)
	return phaseDict()[ind+1]

def phase2int(phase1):
	ind=phaseDict().index(phase1)
	return phaseDict()[ind-1]

def phaseDict():
	res=[]
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

def gal2in3(gal):
	return gal*231

def in32gal(in3):
	return in3/231

def psi2Pa(psi):
	return psi*6894.75728

def CtoK(celsius):
	return celsius+273

def KtoC(kelvin):
	return kelvin-273

def FtoR(far):
	return far+459.67

def makeCool(param1,val1,param2,val2,state):
	return [param1,val1,param2,val2,'state',state]

def getCool(param,pdict):
	if param=="Phase":
		return int2phase(cp.PropsSI(param,pdict[0],pdict[1],pdict[2],pdict[3],pdict[5]))
	return cp.PropsSI(param,pdict[0],pdict[1],pdict[2],pdict[3],pdict[5])

def makeIdeal(P=None,V=None,n=None,T=None,R=None):
	if R==None:
		print 'R needs to be specified for the ideal gas'
	if P==None:
		P=(n*R*T)/V
	if V==None:
		V=(n*R*T)/P
	if n==None:
		n=(P*V)/(R*T)
	if T==None:
		T=(P*V)/(R*n)
	return ['P',P,'V',V,'n',n,'R',R,'T',T]

def getIdeal(param,pdict):
	spot=pdict.index(param)
	return spot+1



