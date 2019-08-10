import math
class node(object):
    def __init__(self):
        self.sources=[]
        self.weights={} #later on, this should be random values, from a normal distribution centered around 0, sigma=1
        self.bias=0 #later on, this probably shouldn't start as 0. Or maybe it should
        self.val=None
        self.loop_catch=False
    def decide(self):
        n=self.bias
        for s in self.sources:
            n+=self.weights[s]*s.get_val()
        self.val=node.activation(n)
    def get_val(self):
        if self.val==None:
            if self.loop_catch:
                raise SyntaxError, "Node called without reset"
            self.loop_catch=True
            self.decide() #This has a very weak infinite loop catcher. Put in work to stop infinite loops without throwing errors
        return self.val
    def reset(self):
        #prepare for next run
        self.val=None
        self.loop_catch=False
    @staticmethod  
    def activation(x):
        a=1/(1+math.e**(-x))
        return a
        
class start_node(object):
    def __init__(self):
        self.val=None
    def assign(self, x):
        self.val=x
    def get_val(self):
        return self.val

