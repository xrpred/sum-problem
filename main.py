#given the array can I work out F(4) = 1+2x+3x+4x
def sortedSum(a):

    sum = 0
    b = sorted(a)
    new = []
    newnew = []
    for j in range(0, len(b)):
        s_i = new + b[j:]
        newnew.append(s_i)

    for b in newnew:
        for i in range(len(b)):
            sum += b[i] * (i + 1)
            print(sum)
    return sum


print(sortedSum([9, 5, 8]))

c = [5, 9, 8]
