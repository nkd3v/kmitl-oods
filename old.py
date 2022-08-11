def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def multiples_of_3_and_5(n):
    return sum(x for x in range(n) if x % 3 == 0 or x % 5 == 0)

def integer_right_triangles(p):
    r = []
    for a in range(1, p):
        for b in range(a, p):
            if a**2 + b**2 == (p - a - b)**2:
                r.append((a, b, p - a - b))
    return r

def gen_pattern(chars):
    r = []
    l = len(chars)
    for i in range(-l + 1, l):
        p = chars[:-l - 1 + abs(i):-1]
        q = '' if (-l + 1 + abs(i) == 0) else chars[-l + 1 + abs(i)::1]
        r.append(('.'.join(p + q)).center(l * 4 - 3, '.'))
    return '\n'.join(r) 
                
print(gen_pattern('XYZ'))

# -2 0
# -3 -1
# -4 -2
# -5 -3
# -4 -2
# -3 -1
# -2 0

# 3
# 3 2 3
# 3 2 1 2 3
# 3 2 1 0 1 2 3

# 0
# 1 0 1
# 2 1 0 1 2
# 3 2 1 0 1 2 3

# abs i
# 3
# 2
# 1
# 0