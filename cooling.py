"""
File: <cooling.py>

Copyright (c) 2016 <Stephanie Nguyen>

License: MIT

<Determining temperature of tea sitting at 20C after x minutes. >
"""
T_Tea = 100.0
T_Air = 20.0 #ambienttemp
t = 0 #mins
while t<= T_Air:
    print t,T_Tea
    T_Tea -= 0.055 * (T_Tea - T_Air)
    t = t + 1   ##everytime it loops it adds one to mins
