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

    def predict(self, input_vec):  # 根据输入得到预测值，输入为x，输出为单个的值
        return self.activator([lambda x: x*self.weight+self.bias for x in input_vec])

    def train(self, input_vec, labels, iteration, rate):
        for i in range(iteration):
            self.__one__it__(input_vec, labels, rate)

    def __one__it__(self, input_vec, labels, rate):
        for i, j in zip(input_vec, labels):
            output = self.predict(i)

    def update_th(self, input_vec, label):
        delta = label-input_vec
