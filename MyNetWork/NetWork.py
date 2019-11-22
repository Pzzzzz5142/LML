'''
Network 神经网络对象，提供API接口。它由若干层对象组成以及连接对象组成。
'''

from Layer import Layer
from ConnectionLayer import ConnectionLayer


class Network(object):
    def __init__(self, input_num):
        self.layers = [Layer(input_num, 0)]
        self.layer_num = 1
        self.connectionLayers = []

    def train(self, data_set, labels, rate, iter_time):
        for i in range(iter_time):
            print('爷开始练第 %d 次了',i)
            cnt=0
            for data, label in zip(data_set, labels):
                cnt+=1
                self.train_one_time(data, label, rate)
                if cnt % 1000 == 0:
                    print('爷练完第 %d 次了' % i)
            print('爷练完第 %d 次数据集了',i)

    def train_one_time(self, data, label, rate):
        self.predict(data)
        self.err_cal(label)
        self.update_par(rate)
        return

    def update_par(self, rate):
        for index, val in enumerate(self.connectionLayers):
            Clayers = self.connectionLayers[index]
            for index1, val1 in enumerate(Clayers.connections):
                connection = Clayers.connections[index1]
                connection.weight += rate*connection.to_cell.eps*connection.fr_cell.output

    def err_cal(self, label):
        self.layers[-1].set_err(label)
        for i in range(len(self.layers)-2, -1, -1):
            self.layers[i].cal_err(self.connectionLayers[i])
        return

    def predict(self, data):
        self.layers[0].set_output(data)
        for i in range(1, len(self.layers)):
            self.layers[i].cal_output(self.connectionLayers[i-1])
        return self.layers[-1].output_vec

    def add_layer(self, cell_num):
        self.layers.append(Layer(cell_num, self.layer_num))
        self.connectionLayers.append(ConnectionLayer(la1=self.layers[-2],la2=self.layers[-1]))
        self.layer_num += 1
