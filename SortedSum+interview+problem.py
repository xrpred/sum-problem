
# coding: utf-8

# In[ ]:

def sortedSum(a):

    sum = 0
    b = a
    new = []
    newnew = []
    newnew2 = []
    
    for j in range(1,len(b)+1):
        s_i = new + b[0:j]
        newnew.append(s_i)
        
    for i in newnew:
        s_i = sorted(i)
        newnew2.append(s_i)
        
    for b in newnew2:
        for i in range(len(b)):
            sum += b[i] * (i + 1)
            
    return sum


print(sortedSum([9, 5, 8]))

c = [5, 9, 8]

