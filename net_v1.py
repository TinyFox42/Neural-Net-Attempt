import node_v1
class net(object):
    def __init__(self, ins, outs):
        self.ins=[]
        for i in range(ins):
            self.ins.append(node_v1.start_node())
        self.outs=[]
        for i in range(outs):
            self.outs.append(node_v1.node())