from primality_fast import is_prime_fast

def get_primes(n_start, n_end):
    return [n for n in range(n_start,n_end) if is_prime_fast(n)==True]


