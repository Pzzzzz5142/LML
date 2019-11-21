from functools import reduce

# 本文件包含一个感知器

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
        su = 0
        ls = list(map(lambda x: x[0]*x[1]+self.bias,
                      zip(input_vec, self.weight)))
        # print(ls)
        for i in ls:
            su += i
        # print(su)
        return self.activator(su)
        # return self.activator(reduce(lambda x, y: x+y, [lambda x: x*self.weight+self.bias for x in input_vec]))

    def train(self, input_vecs, labels, iteration, rate):  # input_vec是数据集，里面的元素是训练参数向量
        for i in range(iteration):
            self.__one__it__(input_vecs, labels, rate)

    def __one__it__(self, input_vecs, labels, rate):
        for input_vec, j in zip(input_vecs, labels):
            pd_output = self.predict(input_vec)
            self.update_par(input_vec, pd_output, j, rate)

    def update_par(self, input_vec, pred_val, label, rate):
        delta = label-pred_val
        delta *= rate
        self.bias += delta
        self.weight = list(
            map(lambda x: x[0]+delta*x[1], zip(self.weight, input_vec)))


def F(x):
    '''
    激活函数
    '''
    return 1 if x > 0 else 0


def getdata():
    input_vecs = [[0, 0], [1, 1], [1, 0], [0, 1]]
    lables = [0, 1, 0, 0]
    return input_vecs, lables


def train_and_perception():

    p = MyTrain(2, F)
    input_vecs, labels = getdata()
    p.train(input_vecs, labels, 10, 0.1)
    return p


if __name__ == "__main__":
    ls = range(10)
    a = [lambda x: x+10 for x in ls]
    print(a)
    xxx = train_and_perception()
    print(xxx)

    print('1 and 1 = %d' % xxx.predict([1, 1]))
    print('0 and 0 = %d' % xxx.predict([0, 0]))
    print('1 and 0 = %d' % xxx.predict([1, 0]))
    print('0 and 1 = %d' % xxx.predict([0, 1]))
