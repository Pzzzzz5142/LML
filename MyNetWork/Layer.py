'''
由多个节点组成，提供层界面的管理
'''
from ConnectionLayer import ConnectionLayer
from Cell import Cell


class Layer(object):
    def __init__(self, cell_num, layer_index):
        self.cells = [Cell(i, layer_index) for i in range(cell_num)]
        self.output_vec = []

    def add_cell(self, cells):
        self.cells += cells

    def cal_output(self, connectionLayer):
        res = []
        for index, val in enumerate(self.cells):
            cell = self.cells[index]
            res.append(cell.output_cell(
                connectionLayer.backwards[cell.cell_index]))
        self.output_vec = res

    def set_err(self, label):
        for i in range(len(label)):
            self.cells[i].set_err(label[i])

    def cal_err(self, connectionLayer):
        res = []
        for index, val in enumerate(self.cells):
            cell = self.cells[index]
            res.append(cell.backput_err(
                connectionLayer.forwards[cell.cell_index]))
        return

    def set_output(self, data):
        for i in range(len(data)):
            self.cells[i].set_output(data[i])
