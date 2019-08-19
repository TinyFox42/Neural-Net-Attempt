import decimal
decimal.getcontext().prec = 100
import random 
import math
def random_weight():
    #invNorm mean=0 stDev=1
    return random.normalvariate(0, 1)
def mutate_weight(w):
    return w+random.normalvariate(0, 0.5)
    
weight_chance=5
class net(object):
    @staticmethod
    def activate(x):
        if x<-10: #because when it tries to do this, it will get close to an overflow error with the exponenet
            return 0
        a=1/(1+math.e**(-x))
        return a
        
    def mutate(self):
        #right now just has some random variations to the weights, maybe does something else later on
        for l in self.weights:#layer
            for s in l:#node_target
                for i in range(len(s)):#node_source
                    if random.randint(1,100)<=weight_chance:
                        w=mutate_weight(s[i])
                        s[i]=w
        
    def __init__(self, inputs, outputs, inners=[]):
        self.vals=[[None]*inputs]
        for l in inners:
            self.vals+=[[None]*l]
        self.vals+=[[None]*outputs]
        self.weights=[]
        
    def random_weights(self):
        #Note, resets the weights set
        self.weights=[]
        for i in range(1, len(self.vals)):
            a=[] #list for the layer
            for j in range(len(self.vals[i])):
                b=[] #list for the node
                for k in range(len(self.vals[i-1])):
                    b+=[random_weight()] #the actual weight
                b+=[random_weight()] #the bias
                a+=[b]
            self.weights+=[a]
    
    def calc(self):
        for i in range(1,len(self.vals)):#layers loop
            for j in range(len(self.vals[i])): #nodes loop
                x=0 #count of effects
                w=self.weights[i-1][j] #weights for this node
                for k in range(len(self.vals[i-1])): #lower nodes
                    n=w[k]*self.vals[i-1][k]
                    x+=n
                x+=w[-1]
                x=net.activate(x)
                self.vals[i][j]=x#later on, make this a real decision function
    
    def assign(self, ins):
        if len(self.vals[0])!=len(ins):
            return "Input count mismatch. This net should have {0} inputs, not {1}.".format(len(self.vals[0]), len(ins))
        for i in range(len(ins)):
            self.vals[0][i]=ins[i]
    
    def set_weights(self, weights):
        #maybe later on I'll put in some checks, but for now this should be fine.
        self.weights=weights
    
    def clone_data(self):
        ins=len(self.vals[0])
        outs=len(self.vals[-1])
        inners=[]
        for i in range(1, len(self.vals)-1):
            inners+=[len(self.vals[i])]
        return ins, outs, inners, self.weights
    
    def retrieve(self):
        s=[]
        for n in self.vals[-1]:
            s+=[n]
        return s
        