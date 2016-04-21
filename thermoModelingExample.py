# Thermodynamics II - Design Project #

from iapws import IAPWS95 as w5
from iapws import IAPWS97 as w7
import CoolProp.CoolProp as cp
import scipy as sc
import scipy.optimize as sco
import numpy.linalg as npl
import math
import random
import sys
import njdTemplate as n

print '\n'

## Notes ##

# IAPWS uses K, MPa 
# CoolProp uses K, kPa, kJ/kg
# print cp.FluidsList()

## System Modeling ##

# Design parameters
mdot_g=15 #kg/s air flow
mdot3=3 # kg/s water flow
T19=320 # exhaust temperature controllable via size of HEX

# Metallurgical limits
T17=1200 #Kelvin
P3=5e6 #Pa
T3=700 #Kelvin

# Plant operation parameters
elecReq_pUnit=41500 # MWh/yr
elecReq=1.494e14 # Joules per year

elecMarginalCost_pUnit=0.07 # USD/(kWh)
elecMarginalCost=0.07/3600000 # USD/Joule

natGasMarginalCost_pUnit=16.0 # USD/(1000 s.c.f)
natGasMarginalCost=16.0/1000.0 # USD/s.c.f.
natgasHV_pUnit=1050.0 # BTU/s.c.f.
natgasHV=1.10781e6 # Joules/s.c.f.
opsSec=12.0*350*60*60 # operating seconds in a year

# Efficiencies
eta_boiler=0.82
eta_pump=0.9
eta_T=0.83
eta_comp=0.75
eta_gT=0.83

#Temperatures
approxT4=505.4 #K - given
approxT6=449.8 #K - given
approxT9=394 #K - given
T15=298.2 #K - air ambient

# Compression ratios
r=12 #compression ratio

# Pressures
# Given
P12=101.3e3 #Pa - condenser at atmospheric
P15=101.3e3 #Pa - air inlet at atmospheric
P19=101.3e3 #Pa - air outlet at atmospheric
# Turbine Outlets
cool4=n.makeCool('T',approxT4,'Q',0,'water')
P4=n.getCool('P',cool4)
cool6=n.makeCool('T',approxT6,'Q',0,'water')
P6=n.getCool('P',cool6)
cool9=n.makeCool('T',approxT9,'Q',0,'water')
P9=n.getCool('P',cool9)
# Isobaric from Above Values
P10=P9
P7=P6
P5=P4
# Isobaric around mixing chamber
P8=P5
P11=P5
P14=P5
# Using compression ratio
P16=P15*r
# Isobaric from Above Values
P17=P16
P18=P19
P2=P3
P1=P5
P13=P12

# Outside air
cool15=n.makeCool('P',P15,'T',T15,'air')
h15=n.getCool('H',cool15)
s15=n.getCool('S',cool15)

# Point 16 Pseudostate
s16s=s15
cool16s=n.makeCool('S',s16s,'P',P16,'air')
h16s=n.getCool('H',cool16s)

h16=h15-eta_comp*h15+eta_comp*h16s
cool16=n.makeCool('H',h16,'P',P16,'air')

# After Combustion Chamber
cool17=n.makeCool('T',T17,'P',P17,'air')
h17=n.getCool('H',cool17)
s17=n.getCool('S',cool17)

# Point 18 Pseudostate
s18s=s17
cool18s=n.makeCool('S',s18s,'P',P18,'air')
h18s=n.getCool('H',cool18s)

# Gas Turbine Efficiency
h18=h17-eta_gT*h17+eta_gT*h18s
cool18=n.makeCool('H',h18,'P',P18,'air')
T18=n.getCool('T',cool18)

# Exhaust Analysis
cool19=n.makeCool('T',T19,'P',P19,'air')
h19=n.getCool('H',cool19)

# Energy Calculations
Q_HEX=mdot_g*(h18-h19)

# Process Heater Outlets
cool5=n.makeCool('P',P4,'Q',0,'water')
h5=n.getCool('H',cool5)
s5=n.getCool('S',cool5)
cool7=n.makeCool('P',P6,'Q',0,'water')
h7=n.getCool('H',cool7)
s7=n.getCool('S',cool7)
cool10=n.makeCool('P',P9,'Q',0,'water')
h10=n.getCool('H',cool10)
s10=n.getCool('S',cool10)

# Point 11 Pseudostate
s11s=s10
cool11s=n.makeCool('S',s11s,'P',P11,'water')
h11s=n.getCool('H',cool11s)

# Pump Efficiency 2
h11=-h10/eta_pump+h10+h11s/eta_pump
cool11=n.makeCool('H',h11,'P',P11,'water')

# Point 8 Pseudostate
s8s=s7
cool8s=n.makeCool('S',s8s,'P',P8,'water')
h8s=n.getCool('H',cool8s)

# Pump Efficiency 3
h8=-h7/eta_pump+h7+h8s/eta_pump
cool8=n.makeCool('H',h8,'P',P8,'water')

# Heat Exchanger Outlet
cool3=n.makeCool('P',P3,'T',T3,'water')
h3=n.getCool('H',cool3)
s3=n.getCool('S',cool3)

# Point 4 Pseudostate
s4s=s3
cool4s=n.makeCool('S',s4s,'P',P4,'water')
h4s=n.getCool('H',cool4s)

# Turbine Efficiency 1
h4=h3-eta_T*h3+eta_T*h4s
cool4=n.makeCool('H',h4,'P',P4,'water')
s4=n.getCool('S',cool4)

# Point 6 Pseudostate
s6s=s4
cool6s=n.makeCool('S',s6s,'P',P6,'water')
h6s=n.getCool('H',cool6s)

# Turbine Efficiency 2
h6=h4-eta_T*h4+eta_T*h6s
cool6=n.makeCool('H',h6,'P',P6,'water')
s6=n.getCool('S',cool6)

# Point 9 Pseudostate
s9s=s6
cool9s=n.makeCool('S',s9s,'P',P9,'water')
h9s=n.getCool('H',cool9s)

# Turbine Efficiency 3
h9=h6-eta_T*h6+eta_T*h9s
cool9=n.makeCool('H',h9,'P',P9,'water')
s9=n.getCool('S',cool9)

# Point 12 Pseudostate
s12s=s9
cool12s=n.makeCool('S',s12s,'P',P12,'water')
h12s=n.getCool('H',cool12s)

# Turbine Efficiency 4
h12=h9-eta_T*h9+eta_T*h12s
cool12=n.makeCool('H',h12,'P',P12,'water')

# Process Heating Energy
Q_PH_pUnit=205000.0e6/350/12/60/60 # BTU/s
Q_PH=2.16286e13/350/12/60/60 # W
Q_PH1=0.500*Q_PH
Q_PH2=0.375*Q_PH
Q_PH3=0.125*Q_PH

# Process Heat mdots
mdot4=Q_PH1/(h4-h5)
mdot6=Q_PH2/(h6-h7)
mdot9=Q_PH3/(h9-h10)

# Remaining Water mdot Calculations
mdot12=mdot3-mdot4-mdot6-mdot9

# Condenser Computations
W_dot_wTurb=mdot4*(h3-h4)+mdot6*(h3-h6)+mdot9*(h3-h9)+mdot12*(h3-h12)
Q_dot_cond=Q_HEX-W_dot_wTurb-Q_PH
h13=h12-Q_dot_cond/mdot12
cool13=n.makeCool('P',P13,'H',h13,'water')
s13=n.getCool('S',cool13)

# Point 14 Pseudostate
s14s=s13
cool14s=n.makeCool('S',s14s,'P',P14,'water')
h14s=n.getCool('H',cool14s)

# Pump Efficiency 1
h14=-h13/eta_pump+h13+h14s/eta_pump
cool14=n.makeCool('H',h14,'P',P14,'water')

# Mixing Chamber Analysis
h1=(h14*mdot12+h5*mdot4+h8*mdot6+h11*mdot9)/mdot3
cool1=n.makeCool('H',h1,'P',P1,'water')
s1=n.getCool('S',cool1)

# Point 2 Pseudostate
s2s=s1
cool2s=n.makeCool('S',s2s,'P',P2,'water')
h2s=n.getCool('H',cool2s)

# Pump Efficiency 4
h2=-h1/eta_pump+h1+h2s/eta_pump
cool2=n.makeCool('H',h2,'P',P2,'water')

# Energy Uses
Q_dot_comb=mdot_g*(h17-h16)
W_dot_comp=mdot_g*(h16-h15)
W_dot_gTurb=mdot_g*(h17-h18)
W_dot_wTurb=mdot4*(h3-h4)+mdot6*(h3-h6)+mdot9*(h3-h9)+mdot12*(h3-h12)
W_dot_p1=mdot3*(h2-h1)
W_dot_p7=mdot6*(h8-h7)
W_dot_p10=mdot9*(h11-h10)
W_dot_p13=mdot12*(h14-h13)
Q_dot_cond=mdot12*(h12-h13)

# Costs
natCost_pre1=Q_dot_comb/natgasHV/eta_boiler #s.c.f./sec
natCost_pre2=natGasMarginalCost*natCost_pre1 #USD/sec
natCost_final=natCost_pre2*opsSec # USD/year
elecDif=elecReq-(W_dot_gTurb+W_dot_wTurb)*opsSec
natCostOld_pre1=Q_PH/natgasHV/eta_boiler
natCostOld_pre2=natGasMarginalCost*natCostOld_pre1
natCostOld_final=natCostOld_pre2*opsSec

print 'Utilities Stuff'
print 'Full Electricity Required'
print elecReq
print 'Additional Elec Needed w/ Cogen'
print elecDif
print 'Electricity Cost for New System'
print elecDif*elecMarginalCost
print 'Electricity Cost for Old System'
print elecReq*elecMarginalCost
print 'Nat Gas Cost for New System'
print natCost_final
print 'Nat Gas Cost for Old System'
print natCostOld_final
print 'Cost Savings'
print elecReq*elecMarginalCost+natCostOld_final-(elecDif*elecMarginalCost+natCost_final)

print '\n'

zetaCycle=(W_dot_gTurb+W_dot_wTurb)/(Q_dot_comb+W_dot_comp+W_dot_p1+W_dot_p7+W_dot_p10+W_dot_p13)
nuCycle=(W_dot_gTurb+W_dot_wTurb+Q_PH)/(Q_dot_comb+W_dot_comp+W_dot_p1+W_dot_p7+W_dot_p10+W_dot_p13)

print 'All in watts:'
print 'Combustion Qin'
print Q_dot_comb
print 'Compressor Work'
print W_dot_comp
print 'Gas Turbine Work'
print W_dot_gTurb
print 'Water Turbine Work'
print W_dot_wTurb
print 'Pumps'
print W_dot_p1+W_dot_p7+W_dot_p10+W_dot_p13
print 'Condenser'
print Q_dot_cond

print '\n'
print 'Utilization'
print nuCycle
print 'Efficiency (PH not included)'
print zetaCycle

print '\n'
print 'Temperatures (all 19 in sequential order and all Kelvin)'
T1=n.getCool('T',cool1)
print T1
T2=n.getCool('T',cool2)
print T2
T3=n.getCool('T',cool3)
print T3
T4=n.getCool('T',cool4)
print T4
T5=n.getCool('T',cool5)
print T5
T6=n.getCool('T',cool6)
print T6
T7=n.getCool('T',cool7)
print T7
T8=n.getCool('T',cool8)
print T8
T9=n.getCool('T',cool9)
print T9
T10=n.getCool('T',cool10)
print T10
T11=n.getCool('T',cool11)
print T11
T12=n.getCool('T',cool12)
print T12
T13=n.getCool('T',cool13)
print T13
T14=n.getCool('T',cool14)
print T14
T15=n.getCool('T',cool15)
print T15
T16=n.getCool('T',cool16)
print T16
T17=n.getCool('T',cool17)
print T17
T18=n.getCool('T',cool18)
print T18
T19=n.getCool('T',cool19)
print T19

print '\n'
print 'Pressuress (all 19 in sequential order and all Pa)'
P1=n.getCool('P',cool1)
print P1
P2=n.getCool('P',cool2)
print P2
P3=n.getCool('P',cool3)
print P3
P4=n.getCool('P',cool4)
print P4
P5=n.getCool('P',cool5)
print P5
P6=n.getCool('P',cool6)
print P6
P7=n.getCool('P',cool7)
print P7
P8=n.getCool('P',cool8)
print P8
P9=n.getCool('P',cool9)
print P9
P10=n.getCool('P',cool10)
print P10
P11=n.getCool('P',cool11)
print P11
P12=n.getCool('P',cool12)
print P12
P13=n.getCool('P',cool13)
print P13
P14=n.getCool('P',cool14)
print P14
P15=n.getCool('P',cool15)
print P15
P16=n.getCool('P',cool16)
print P16
P17=n.getCool('P',cool17)
print P17
P18=n.getCool('P',cool18)
print P18
P19=n.getCool('P',cool19)
print P19

print '\n'

print 'Massflows'
print 'Air'
print mdot_g
print 'mdot3'
print mdot3
print 'mdot 4'
print mdot4
print 'mdot 6'
print mdot6
print 'mdot 9'
print mdot9
print 'mdot12'
print mdot12

print 'Balance'
print W_dot_comp+Q_dot_comb-W_dot_gTurb-W_dot_wTurb-Q_PH-Q_dot_cond-mdot_g*(h19-h15)
