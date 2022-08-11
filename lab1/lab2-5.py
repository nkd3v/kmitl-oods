def bon(w):
    return (ord([x for x in w if w.count(x) > 1][0]) - 96) * 4

secretCode = input("Enter secret code : ")
print(bon(secretCode))
