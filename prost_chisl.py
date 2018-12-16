import math

def is_prime(one):
    chk = 0
    if one == 0:
        return(False)
    for i in range(1, one+1):
        test = one / i
        ost = math.modf(test)
        # print(ost[0])
        if ost[0] == 0:
            chk += 1 
    # print(chk)
    if chk == 2:
        # print('простое')
        return(True)
    else:
        return(False)
        # print('не Простое')
    
# for prov in range(1000000):
while True:
    prov = 0
    if is_prime(prov) is True:
        print(prov)
    prov += 1