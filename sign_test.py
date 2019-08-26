#A test of the neural nets, trains them to identify +/-
import pop_v1
import random
def make_qs(n):
    #makes n questions
    q=[]
    a=[]
    for i in range(n):
        x=random.randint(1,1000)
        x*=random.choice([-1,1])
        q+=[[x]]
        if x>0:
            a+=[0]
        else:
            a+=[1]
    return q,a

def step(pop):
    #Calls some functions on the pop. The net will be modified. No real need to return it, so it doesn't
    qs,ans=make_qs(1000)
    pop.test(qs,ans)
    print pop.fancy_stats()
    pop.cull()
    pop.repop()
    
def make_pop(n):
    return pop_v1.population(1,2,n)