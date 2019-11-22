'''
仅仅作为Connection的集合对象，提供一些集合操作。
'''

from Connection import Connection


class ConnectionLayer(object):
    def __init__(self, la1=None, la2=None):
        self.connections = []
        if la1 != None and la2 != None:
            for index, val in enumerate(la1.cells):
                cell_fr = la1.cells[index]
                for index1, val1 in enumerate(la2.cells):
                    cell_to = la2.cells[index1]
                    self.connections.append(Connection(cell_fr, cell_to))
        self.forwards = {}
        self.backwards = {}
        for connection in self.connections:
            if connection.fr_cell.cell_index not in self.forwards:
                self.forwards[connection.fr_cell.cell_index] = []
            self.forwards[connection.fr_cell.cell_index].append(connection)
            if connection.to_cell.cell_index not in self.backwards:
                self.backwards[connection.to_cell.cell_index] = []
            self.backwards[connection.to_cell.cell_index].append(connection)

    def add_connection(self, new_connection):
        self.connections.append(new_connection)
        if new_connection.fr_cell.cell_index not in self.forwards:
            self.forwards[new_connection.fr_cell.cell_index] = []
        self.forwards[new_connection.fr_cell.cell_index].append(new_connection)
        if new_connection.to_cell.cell_index not in self.backwards:
            self.backwards[new_connection.to_cell.cell_index] = []
        self.backwards[new_connection.to_cell.cell_index].append(
            new_connection)
