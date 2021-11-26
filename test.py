import math
import random
import primes_finder as pf

class stats:
    # track number of squarings and multiplications operations
    SQR = 0
    MULT = 0
    SUM_SQR = 0
    SUM_MULT = 0


def get_g(m, p):
    # finds a non square z randomly and computes g = z^m modulo p
    z = 2
    while isSquare(z, p):
        z += 1
    return pow(z, m, p)


def powers_g(g, n, p):
    # precomputes powers of g modulo p
    G = []
    for i in range(0, n-1):
        G.append(g)
        g = pow(g, 2, p)
    return G


def split(n):
    # finds l0 + l1 +.... lk-1 = n-1
    # for optimal complexity choose k=sqrt(n-1) and l accordingly
    if n == 1:
        return []
    n = n-1
    k = int(math.sqrt(n))
    rem = n % k
    l = (n-rem)//k

    return [l]*(k-rem) + [l+1]*rem


def fill_K(L):
    # computes K(i,j)
    k = len(L)
    s = sum(L)+1
    K = [[]]
    for i in range(1, k+1):
        elem = []
        for j in range(0, i):
            elem.append(s - sum(L[j:min(i, k-1)+1]))
        K.append(elem)
    return K


def isSquare(u, p):
    # returns whether u is a square in Zp
    m = (p-1)//2
    return pow(u, m, p) == 1



# ******** Algorithm ********

def compute_gt(i, p, G, Q, L, K, by2, ops):
    # computes (congruent to p) g^t or g^(t/2) using precomputed powers of g
    res = 1
    for j in range(0, i):
        for bit in range(0, L[j]):
            if Q[j] & (1 << bit):
                res *= G[K[i][j]+bit-by2]
                ops.MULT += 1
                res %= p
    return res


def computeXi(x, ops, L, p):
    # computes xi's
    X = []
    i = 0
    power = 0
    h = len(L)-1
    while 1:
        if i == power:
            X.append(x)
            power += L[h]
            h -= 1
            if h == -1:
                break
        x = pow(x, 2, p)
        ops.SQR += 1
        i += 1
    X.reverse()
    return X


def find(delta, p, ops):
    mu = delta
    i = 0
    while mu != p-1:
        mu = pow(mu, 2, p)
        ops.SQR += 1
        i += 1
    return i


def eval(alpha, p, n, g, G, ops):
    delta = alpha % p
    s = 0
    while delta != 1:
        i = find(delta, p, ops)
        s += 1 << (n-1-i)
        ops.MULT += 1
        if i > 0:
            delta *= G[n-1-i]
            delta %= p
        else:
            delta = p - delta
    return s


def findSqRoot(u, p, n, m, g, G, L, K, ops):
    v = pow(u, (m-1)//2, p)
    if n == 1:
        return (v*u) % p

    x = (u*v*v) % p
    ops.MULT += 1
    ops.SQR += 1
    X = computeXi(x, ops, L, p)

    # loop
    s = 0
    t = 0
    Q = []
    for i in range(0, len(L)):
        t = (s+t) >> L[i]
        gamma = 1
        if i:
            gamma = compute_gt(i, p, G, Q, L, K, 0, ops)  # gamma = g^t
            ops.MULT += 1
        alpha = X[i]*gamma
        s = eval(alpha, p, n, g, G, ops)
        Q.append(s >> (n-L[i]))

    t = s+t
    gamma = compute_gt(len(L), p, G, Q, L, K, 1, ops)  # gamma = g^(t/2)
    y = u*v*gamma
    ops.MULT += 2
    return y % p

# ****** Algorithm ends ********

def work(p, ops):

    # Select a random square u in Zp
    z = random.randint(1, p)    
    u = (z*z)%p
    ops.SQR=0
    ops.MULT=0
    
    #  precomputaions
    n = 0
    m = p-1
    while m % 2 == 0:
        m //= 2
        n += 1

    g = get_g(m, p)
    G = powers_g(g, n, p)
    L = split(n)
    K = fill_K(L)

    # find square root of u
    root = findSqRoot(u, p, n, m, g, G, L, K, ops)

    #verify
    if (root*root)%p != u :
        print("WRONG ANSWER!",p,u,root)
    
    


def main():

    print("Enter n (p = 1+m*2^n) : ", end='')
    n = int(input().strip())

    sample_len=1000
    print("Searching Primes")
    L = pf.get_primes(n,sample_len)
    # print("List of primes:")
    # print(L)
    print("Executing...")

    ops = stats()
    for p in L:
        work(p, ops)
        ops.SUM_MULT+=ops.MULT
        ops.SUM_SQR+=ops.SQR
    
    print("# Avg Squarings S = {:.2f} \n# Avg Multiplications M = {:.2f} \n# Avg Total ops = {:.2f}".format(
        ops.SUM_SQR/sample_len, ops.SUM_MULT/sample_len, (ops.SUM_SQR+ops.SUM_MULT)/sample_len))

if __name__ == '__main__':
    main()
