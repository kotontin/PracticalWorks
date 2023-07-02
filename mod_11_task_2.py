#python

import math

list_x = [-4, -3.7, 3.2, 0, 25.3, -1.5, 0.2, 1.678, -1000, -0.6, -0.2]

def logarithm_exponent(list_x: float):

    for x in list_x:
        if x > 0:
            x = math.ceil(x)
            print(f"ln({x}) = {math.log(x)}")

        if x <= 0:
            x = math.floor(x)
            print(f"{x}^e = {math.exp(x)}")

    return

logarithm_exponent(list_x)
