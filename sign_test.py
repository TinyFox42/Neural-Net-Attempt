#A test of the neural nets, trains them to identify +/-
import pop_v1
import random
def make_qs(n):
    #makes n questions
    q=[]
    a=[]
    for i in range(n):
        x=random.randint(1,100)
        x*=random.choice([-1,1])
        q+=[[x]]
        if x>0:
            a+=[0]
        else:
            a+=[1]
    return q,a

def step(pop):
    #Calls some functions on the pop. The net will be modified. No real need to return it, so it doesn't
    qs,ans=make_qs(100)
    pop.test(qs,ans)
    g,m,p=pop.get_stats()
    print "Generation: {0}".format(g)
    print "Mean score: {0}".format(m)
    print "Percentiles:"
    for i in [0,1,2,3,4,5,6,7,8,9,10]:
        print "\t{0}th: {1}".format(i*10, p[i])
    pop.cull()
    pop.repop()