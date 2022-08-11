ls = sorted([int(e) for e in input("Enter Your List : ").split()])

ans = []

if (len(ls) < 3):
    print('Array Input Length Must More Than 2')
    exit()

for i in range(len(ls)):
    for j in range(i+1, len(ls)):
        for k in range(j+1, len(ls)):
            if ls[i] + ls[j] + ls[k] == 5 and (len(ans) == 0 or ans[-1] != [ls[i], ls[j], ls[k]]):
                ans.append([ls[i], ls[j], ls[k]])
                
print(ans)