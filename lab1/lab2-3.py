class TorKham:

    def __init__(self):
        self.words = []

    def restart(self):
        self.words = []        
        return "game restarted"

    def play(self, word):
        if len(self.words) > 1 and self.words[-2][-2:].lower() == self.words[-1][:2].lower():
            return "game over"
        
        self.words.append(word)
        return self.words

torkham = TorKham()

print("*** TorKham HanSaa ***")

S = input("Enter Input : ").split(',')

for s in S:
    r = ""
    if s.split(' ')[0] == "R":
        r = torkham.restart()
        print(r)
    elif s.split(' ')[0] == "P":
        r = torkham.play(s.split(' ')[1])
        print("'{}' -> {}".format(s.split(' ')[1], r))
        if r == "game over":
            exit()
    elif s.split(' ')[0] == "X":
        exit()
    else:
        print("'{}' is Invalid Input !!!".format(s))
        exit()
