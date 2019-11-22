'''
Node 节点对象计算和记录节点自身的信息(包含节点标号、所在层次的标号、输出值、误差项)
'''


class Cell(object):
    def __init__(self, cell_index, layer_index):
        self.cell_index = cell_index
        self.layer_index = layer_index
        self.output = 0.0
        self.eps = 0.0

    def output_cell(self, connections=[]):
        res = 0
        for connection in connections:
            res += connection.fr_cell.output*connection.weight
        self.output = res
        return res

    def backput_err(self, connections=[]):
        res = 0
        for connection in connections:
            res += connection.to_cell.eps*connection.weight
        self.eps = res
        return res

    def set_err(self, label_element):
        self.eps = 0.0
        self.eps = self.output*(1-self.output)*(label_element-self.output)

    def set_output(self, data):
        self.output = data


class ConstCell(object):
    def __init__(self, cell_index, layer_index):
        self.cell_index = cell_index
        self.layer_index = layer_index
        self.output = 0.0
        self.eps = 0.0


class List(object):
    def __init__(self):
        self.data = 10
        self.nx = None


if __name__ == "__main__":
    root = List()
    root.nx = List()
    Loc = root.nx
    Loc.nx = List()
    Loc = Loc.nx
    Loc.data += 10
    ls = [Loc]
    ls[0].data += 10
    loc = root
    while loc != None:
        print(loc.data)
        loc = loc.nx
