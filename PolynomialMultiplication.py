import numpy as np

def mult (a,b):
    return (a*b)%256

def add (a,b):
    return (a+b)%256

def polyMult(p,q):
    final = np.zeros(len(p) + len(q) - 1)
    for i in np.nditer(np.arange(len(p))):
        for j in np.nditer(np.arange(len(q))):
            final[i+j] = add(final[i+j],mult(p[i],q[j]))
    k = len(final)-1
    for i in np.nditer(np.arange(len(final))):
        if (final[k] != 0):
            break
        else:
            k -= 1
    if (k != -1):
        final2 = np.zeros(k+1)
        for i in np.nditer(np.arange(k+1)):
            final2[i] = final[i]
        return final2
    else:
        return [0]
