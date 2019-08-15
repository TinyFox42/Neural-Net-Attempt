import net_simple
from numpy import median
import random
class population(object):
    def __init__(self, ins, outs, pop, inners=[]):
        if (pop%2)!=0:
            pop+=1#Nope, just nope
        self.pop=pop
        self.nets=[]
        for i in range(pop):
            n=net_simple.net(ins, outs, inners)
            n.random_weights()
            self.nets+=[[n, 0]]
    def test(self, qs, ans):
        for n in self.nets:
            for i in range(len(qs)):
                n[0].assign(qs[i])
                n[0].calc()
                x=n[0].retrieve()
                if x == ans[i]:
                    n[1]+=1
                else:
                    n[1]-=1
    def cull(self):
        tot=[]
        for n in self.nets:
            tot+=n[1]
        m=median(tot)
        l=[]
        w=[]
        for n in self.nets:
            if n[1]>m:
                l+=[[n[0],0]]
            if n[1]==m:
                w+=[n]#please no. this would be so annoying to deal with
        if len(w)>0:
            #oh god, why
            d=(self.pop/2)-len(l)
            for i in range(d):
                x=random.randint(0,len(w))
                l+=[[w.pop(x),0]]
            #ok, this should kinda work
        self.pop=l
        