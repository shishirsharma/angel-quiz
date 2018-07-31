
def mystery(alist):
    for index in range(1, len(alist)):
        pos = index
        current = alist[index]
        while pos > 0 and alist[pos-1] > current:
            alist[pos] = alist[pos-1]
            pos = pos - 1
        alist[pos] = current


a = [1,2,3,8,9,5,6,4,7]

mystery(a)

print(a)
