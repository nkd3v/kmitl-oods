def weirdSubtract(n, k):
    if k == 0:
        return n
    elif n % 10 == 0:
        return weirdSubtract(n // 10, k - 1)
    else:
        return weirdSubtract(n - 1, k - 1)
    
n, s = input("Enter num and sub : ").split(" ")

print(weirdSubtract(int(n), int(s)))
