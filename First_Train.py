from functools import reduce


class MyTrain():
    def __init__(self, input_num, activator):

        self.activator = activator
        self.bias = 0
        self.weight = [0.0 for i in range(input_num)]

    def __str__(self):
        '''
        打印学习到的权重、偏置项
        '''
        return 'weights\t:%s\nbias\t:%f\n' % (self.weight, self.bias)

    def predict(self, input_vec):  # 根据s输入得到预测值，输入为x向量，输出为单个的值
        return self.activator(reduce(lambda x, y: x+y, [lambda x: x*self.weight+self.bias for x in input_vec]))

    def train(self, input_vecs, labels, iteration, rate):  # input_vec是数据集，里面的元素是训练参数向量
        for i in range(iteration):
            self.__one__it__(input_vecs, labels, rate)

    def __one__it__(self, input_vecs, labels, rate):
        for input_vec, j in zip(input_vecs, labels):
            pd_output = self.predict(input_vec)
            self.update_par(input_vec, pd_output, j, rate)

    def update_par(self, intput_vec, pred_val, label, rate):
        delta = label-pred_val
        delta *= rate
        self.bias += delta
        self.weight
