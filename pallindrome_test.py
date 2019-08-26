#looks for 4 bit pallindromes
import pop_v1
import random
reload(pop_v1)
def make_qs(n):
    qs=[]
    ans=[]
    for i in range(n):
        a=random.choice([0,1])
        b=random.choice([0,1])
        c=random.choice([0,1])
        d=random.choice([0,1])
        if a==d and b==c:
            ans+=[1]
        else:
            ans+=[0]
        qs+=[[a,b,c,d]]
    return qs, ans

def step(pop):
    #Calls some functions on the pop. The net will be modified. No real need to return it, so it doesn't
    qs,ans=make_qs(1000)
    pop.test(qs,ans)
    print pop.fancy_stats()
    pop.cull()
    pop.repop()
    
def make_pop(n):
    return pop_v1.population(4,2,n,[4,4,4])