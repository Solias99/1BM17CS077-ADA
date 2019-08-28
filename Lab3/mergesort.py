def split(a, low, high):
    if low < high:
        middle = (low+high)//2
        split(a, low, middle)
        split(a, middle+1, high)
        combine(a, low, middle, high)

def combine(a, low, middle, high):
    i = low
    j = middle+1
    c = []
    print(low,high)
    while i <= middle and j <= high:
        if a[i] < a[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(a[j])
            j += 1

    if i > middle:
        while j <= high:
            c.append(a[j])
            j += 1
    if j > high:
        while i <= middle:
            c.append(a[i])
            i += 1 
    for i in range(low, high):
        a[i] = c[i]


a = [7,99,3,45,124]


split(a, 0, len(a)-1)


print(a)