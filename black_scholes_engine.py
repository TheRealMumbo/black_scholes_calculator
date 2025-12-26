import math
import numpy as np

#s0 = None Stock Price
#x = None exercise price
#r = None risk free interest rate
#t = None time to expiration
#sigma = standard deviation of returns, shortly volatility
#q = dividends


#EUROPEAN CALL OPTION
def calc_european_call_option (s0, x, r, q, t, sigma):
    #d1, d2 CALCULATION
    d1_1 = (np.log(s0/x) + (r-q+1/2*sigma**2)*t) #first component of d1
    d1_2 = sigma*math.sqrt(t) #2nd component of d1
    d1 = d1_1/d1_2
    d2 = d1 - sigma*math.sqrt(t)#

    #CDF values N(d1), N(d2)

    n_d1 = 1/2 * (1 + math.erf(d1/math.sqrt(2))) 
    n_d2 = 1/2 * (1 + math.erf(d2/math.sqrt(2)))

    #COMPUTE DISCOUNT FACTORS
    discount_2nd_part = pow(np.exp(1),-r*t)
    discount_1st_part = pow(np.exp(1),-q*t)

    #EUROPEAN CALL PRICES
    first_part_get = s0*discount_1st_part*n_d1
    second_part_pay = x*discount_2nd_part*n_d2
    result = first_part_get - second_part_pay

    return result

def calc_european_put_option (s0, x, r, q, t, sigma):
    #d1, d2 CALCULATION
    d1_1 = (np.log(s0/x) + (r-q+1/2*sigma**2)*t) #first component of d1
    d1_2 = sigma*math.sqrt(t) #2nd component of d1
    d1 = d1_1/d1_2
    d2 = d1 - sigma*math.sqrt(t)#

    #CDF values N(d1), N(d2)

    n_d1 = 1/2 * (1 + math.erf(d1/math.sqrt(2))) 
    n_d2 = 1/2 * (1 + math.erf(d2/math.sqrt(2)))

    n_d1 = 1-n_d1 #complementary probability for puts
    n_d2 = 1-n_d2 #complementary probability for puts

    #COMPUTE DISCOUNT FACTORS
    discount_1st_part = pow(np.exp(1),-r*t)
    discount_2nd_part = pow(np.exp(1),-q*t)

    #EUROPEAN CALL PRICES
    first_part_get = x*discount_1st_part*n_d2
    second_part_pay = s0*discount_2nd_part*n_d1
    result = first_part_get - second_part_pay
    
    return result



def main():

    print("Please Enter the actual stock price now:")
    s0 = float(input())
    print("Please Enter the strike (exercise) price now:")
    x = float(input())
    print("Please Enter the risk free interest rate:")
    r = float(input())
    print("Please Enter any dividends, if none enter 0:")
    q = float(input())
    print("Please Enter time until expiration:")
    t = float(input())
    print("Please Enter sigma of the stock (anualized volatility):")
    sigma = float(input())

    print(f"European Option Price is: {calc_european_call_option(s0, x, r, q, t, sigma)}")
    print(f"European Option Price is: {calc_european_put_option(s0, x, r, q, t, sigma)}")


main()