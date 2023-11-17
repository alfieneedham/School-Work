def power(A, n, p):
    if n == 0: return 1
    if n%2 == 1: return (power(A, n-1, p) * A) % p
    root = power(A, n//2, p)
    return (root * root) % p

if __name__=="__main__":
    pass