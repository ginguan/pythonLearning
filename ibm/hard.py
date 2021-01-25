#1012 Numbers With Repeated Digits

def numDupDigitsAtMostN(self, N):
    L = map(int, str(N + 1))
    res, n = 0, len(L)

    def permutation(m, n):
        return 1 if n == 0 else permutation(m, n - 1) * (m - n + 1)

    for i in range(1, n): 
        res += 9 * permutation(9, i - 1)
    s = set()
    for i, x in enumerate(L):
        for y in range(0 if i else 1, x):
            if y not in s:
                res += permutation(9 - i, n - i - 1)
        if x in s: 
            break
        s.add(x)
    return N - res