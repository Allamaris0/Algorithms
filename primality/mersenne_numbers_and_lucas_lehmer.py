# Mersenne numbers can only be prime if their exponent p is prime.
# However '11' is the prime, but for p=11, the Mersenne number isn't prime. We can test if a Mersenne number is prime using the Lucas-Lehmer test

def mersenne_number(p:int):
    return 2**p - 1

def lucas_lehmer(p:int):
    M = 2**p-1
    ll = []
    i = p-2
    n = 4
    for number in range (i+1):
        if number>0:
            n = (n**2-2)%M
        ll.append(n)
    return ll

def is_mersenne_prime(p:int):
    """The Mersenne number is prime if the Lucas-Lehmer series is 0 at position p-2"""
    M = 2**p-1
    ll = []
    i = p-2
    n = 4
    for number in range (i+1):
        if number > 0:
            n = (n**2-2)%M
        ll.append(n)
    if ll[-1]==0:
        return True
    else:
        return False




