import numpy as np

def generator(n,p):
    '''
    n - number of fermions/antifermions
    p - number of filled sites

    Generates a 2n vector with p filled fermions and p filled antifermions
    '''

    vec = np.zeros(2*n)
    #print(vec)

    fermions = np.random.choice(range(n),p, replace=False)
    #print(fermions)

    antifermions = np.random.choice(range(n),p,replace=False)
    #print(antifermions)

    for i in range(p): 
        vec[2*fermions[i]]=1
        vec[2*antifermions[i]+1]=1
    return vec

def Dealtal_calculation (v):

    '''
    given an occupancy configuration v 
    where even sites are reserved to fermions 
    and odd sites to antifermions,
    produces the associated Deltal
    
    '''

    #PRINCIPAL VARIABLES DEFINITION
    Deltal = 0

    #AUXILIARY VARIABLES
    l = [0]
    n = len(v)

    for i in range(0, n):
        l.append(l[i]+ v[i]*(-1)**i)

    Deltal = max(l)-min(l)

    return Deltal