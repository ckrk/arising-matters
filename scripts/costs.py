import math
import numpy as np


def rinnereg(height,rated_capacity,diameter,age):
    # Implements Eq (8) from Rinne et al 2018
    # Output: Cost in Euro 2016
    # Input: height in m, rated_capacity in W, diameter in m, age in "years before 2016" i think in reality its (date of availibility)-2015
    beta1 = 620
    beta2 = -1.68
    beta3 = 182
    C  = -1005
    radius = diameter*0.5

    specific_power = rated_capacity/(math.pi*radius**2)
    cost = beta1*np.log(height)+beta2*specific_power+beta3*math.sqrt(age)+C
    #print(specific_power)
    return cost

#rinnereg(1,1,1,1)

# Testturbine 1 from Rinne et al: Year 2002 High winds V90-3.0 MW Height: 75 Price: 878 euro/kW
# the numbers from the paper are for vintage setting age=0! and new age=1!
#for i in range(20):
#    print(i)
#    print(rinnereg(75,3000000,90,i))

print(rinnereg(75,3000000,90,12))
print(rinnereg(75,3000000,90,14))
print(rinnereg(75,3000000,90,0))



# Testturbine 2 from Rinne et al: Year 2015 High winds V117-3.45 MW Height 125 Price:  1,448 euro/kW
print(rinnereg(125,3450000,117,1))
print(rinnereg(125,3450000,117,0))