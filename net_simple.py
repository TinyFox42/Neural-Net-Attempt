#Config stuff here:

#mutation chances. Right now, these are times it will occur out of chance_base tries (theoretically)
chance_base=100
weight_chance=5 #chance that a weight will mutate. Rolled once per weight
node_chance=1 #chance that a new node will appear. Rolled once per layer


#####End config, start code#####
#Config sanity check: (as in, won't raise errors, not works well)
chance_base=int(chance_base)
if chance_base<=1:
    chance_base=2
weight_chance=int(weight_chance)
node_chance=int(node_chance)

#Start real code
import decimal
decimal.getcontext().prec = 100
import random 
import math
def random_weight():
    #invNorm mean=0 stDev=1
    return random.normalvariate(0, 1)
def mutate_weight(w):
    return w+random.normalvariate(0, 0.5)

class net(object):
    @staticmethod
    def activate(x):
        if x<-10: #because when it tries to do this, it will get close to an overflow error with the exponenet
            return 0
        a=1/(1+math.e**(-x))
        return a
        
    def add_node(self, layer):
        #layer should be the index for the val layer it is added in
        if layer==(len(self.vals)-1):
            print "Well, something got messed up. It tried to add a node to the top layer. So I'm just going to stop the mutation here."
            raise
        if layer==0:
            print "Well, this is even weirder. It did the lowest layer..."
            raise
        #print "To layer {0}, total {1} layers".format(layer, len(self.vals))
        self.vals[layer].append(None)
        w=[]
        for i in range(len(self.weights[layer-1])):
            #can you tell that I made this at a different time from the rest of this code?
            w.append(random_weight())
            #See, here I was smart, and remembered that append() existed, instead of muddling with +=[]. Later on I might test to see which is faster, and possibly optimize the rest of this code
        w.append(random_weight()) #For the bias
        self.weights[layer-1].append(w)
        for i in range(len(self.weights[layer])):#layer-1+1=layer
            #loop for the nodes one layer up
            x=self.weights[layer][i][-1]#need to save the bias. Ok, that sounds so bad, but it's the term for a constant value in a neural net
            self.weights[layer][i][-1]=random_weight()
            self.weights[layer][i].append(x)
        
    def mutate(self):
        #right now just has some random variations to the weights, maybe does something else later on
        for l in range(len(self.weights)):#layer
            if l<len(self.weights)-1:#so that the output layer doesn't get a new node
                if random.randint(1,chance_base)<=node_chance:
                    self.add_node(l+1)
            for s in range(len(self.weights[l])):#node_target
                for i in range(len(self.weights[l][s])):#node_source
                    if random.randint(1,chance_base)<=weight_chance:
                        w=mutate_weight(self.weights[l][s][i])
                        self.weights[l][s][i]=w
        
    def __init__(self, inputs, outputs, inners=[]):
        self.vals=[[None]*inputs] #A place to store the data
        for l in inners:
            self.vals+=[[None]*l]
        self.vals+=[[None]*outputs]
        self.weights=[] #the weights of the connections
        
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
                    if type(w[k])==type(None):
                        print "Weight is none"
                    if type(self.vals[i-1][k])==type(None):
                        print "Val is none"
                    n=w[k]*self.vals[i-1][k] #somehow, one of these is a null
                    x+=n
                x+=w[-1]
                x=net.activate(x)
                self.vals[i][j]=x#later on, make this a real decision function
    
    def assign(self, ins):
        if len(self.vals[0])!=len(ins):
            print "Input count mismatch. This net should have {0} inputs, not {1}.".format(len(self.vals[0]), len(ins))
            raise
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
        