import random 
import math
def random_weight():
    #invNorm mean=0 stDev=1
    return random.normalvariate(0, 1)
    
class net(object):
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
        for i in range(1,self.vals):#layers loop
            for j in range(self.vals[i]): #nodes loop
                x=0 #count of effects
                w=self.weights[i-1][j] #weights for this node
                for k in range(self.vals[i-1]): #lower nodes
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
    def retrieve(self):
        s=[]
        for n in self.vals[-1]:
            s+=[n]
        return s
    @staticmethod
    def activate(x):
        a=1/(1+math.e**(-x))
        return a