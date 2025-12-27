def funkcjadlafor(lb):
    for n in lb:
        print(n*2)

def funkcjadlalisty(lb):
    list = []
    list = [n * 2 for n in lb]
    for L in list:
        print(L)

funkcjadlafor([9,7,1,2,5])
funkcjadlalisty([9,7,1,2,5])