# Digital Roots

def superDigit(n, k):
    return 1 + (k * sum(int(x) for x in n) - 1) % 9


"""
Exceeds time limit even after memoization
memo = {}
def superDigit(n,k):
    if (n,k) in memo:
        return memo[(n,k)]
    s = 0
    n = n*k
    for i in range(len(n)):
        s += int(n[i])
    if s>=10:
        result = superDigit(str(s),1)
    else:
        result = s
        
    memo[(n,k)] = result

    return result


"""
