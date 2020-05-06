def je_prastevilo(n):
    if n < 2:
        return False
    for i in range(2, int(n**(1/2) + 1)):
        if n % i == 0:
            return False
    return True

for stevilo in range(200):
    if je_prastevilo(stevilo):
        print(stevilo)