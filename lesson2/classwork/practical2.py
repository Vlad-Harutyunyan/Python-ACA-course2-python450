#practical 2

def type1(l):
    sets = [set(x) for x in l]
    print(len(sets[0].intersection(*sets[1:])))


def type2(l):
    matching = []
    cnts = []
    for item in l:
        for elem in item :
            pass
    print(matching)

if __name__ == "__main__" :
    l  = ['aaae','aaaeb','aaaefc']
    type1(l)
    type2(l)
    

