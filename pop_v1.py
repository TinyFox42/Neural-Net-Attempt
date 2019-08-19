import net_simple
import numpy
import random
def simple_ans_check(ans, ans_data):
    #the ans data should be the index that should be the highest
    m=max(ans)
    n=ans.index(m)
    if n==ans_data:
        return 1
    return -1
class population(object):
    def __init__(self, ins, outs, pop, inners=[]):
        if (pop%2)!=0:
            pop+=1#Nope, just nope
        self.gen=0
        self.pop=pop
        self.nets=[]
        for i in range(pop):
            n=net_simple.net(ins, outs, inners)
            n.random_weights()
            self.nets+=[[n, 0]]
    def test(self, qs, ans_data, ans_function=simple_ans_check):
        self.get+=1
        for n in self.nets:
            for i in range(len(qs)):
                n[0].assign(qs[i])
                n[0].calc()
                x=n[0].retrieve()
                n[1]+=ans_function(x, ans_data[i])
    def cull(self):
        tot=[]
        for n in self.nets:
            tot+=n[1]
        m=numpy.median(tot)
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
        
    def repop(self):
        cs=[]
        for i in range(len(self.pop)):
            d=self.pop[i][0].clone_data()
            n=net_simple.net(d[0], d[1], d[2])
            n.set_weights(d[3])
            n.mutate()
            cs+=[[n, 0]]
        self.pop+=cs
        
    def get_stats(self):
        #just gives a few statistics about the scores. Should be called in between testing and culling
        l=[]
        for n in self.nodes:
            l+=n[1]
        mean=numpy.mean(l)
        pers=numpy.percentile(l, [0,10,20,30,40,50,60,70,80,90,100])
        return self.gen, mean, pers