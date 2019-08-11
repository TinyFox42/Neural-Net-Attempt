import node_v1
#reload(node_v1)#only uncomment if you need to reload it
class net(object):
    def __init__(self, ins, outs):
        self.ins=[]
        for i in range(ins):
            self.ins.append(node_v1.start_node())
        self.outs=[]
        for i in range(outs):
            self.outs.append(node_v1.node())
        self.inner=[]
    def set_inputs(self, inputs):
        if len(inputs) != len(self.ins):
            return "Invalid number of inputs. This net should be given {0} inputs".format(len(self.ins))
        for i in range(len(self.ins)):
            self.ins[i].assign(inputs[i])
        return "Done"
    def get_outputs(self):
        #Note that in some networks, calling this without resolving all the nodes will throw the infinite loop
        x=[]
        for n in self.outs:
            x.append(n.get_val())
        return x 
    def reset(self):
        for n in self.ins:
            n.reset()
        for l in self.inner:
            for n in l:
                n.reset()
        for n in self.outs:
            n.reset()