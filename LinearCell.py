from First_Train import MyTrain
import matplotlib.pyplot as plt
import numpy as np

'''
名义上是个线性单元，实际上就继承了上一个代码就没了，，，
'''

class LinearCell(MyTrain):
    def __init__(self, input_len, activator):
        super().__init__(input_len, activator)


def F(x):
    return x


def get_training_dataset():
    '''
    捏造5个人的收入数据
    '''
    # 构建训练数据
    # 输入向量列表，每一项是工作年限
    input_vecs = [[5], [3], [8], [1.4], [10.1]]
    # 期望的输出列表，月薪，注意要与输入一一对应
    labels = [5500, 2300, 7600, 1800, 11400]
    return input_vecs, labels


def train_xxx():
    '''
    使用数据训练线性单元
    '''
    # 创建感知器，输入参数的特征数为1（工作年限）
    lu = LinearCell(1,F)
    # 训练，迭代10轮, 学习速率为0.01
    input_vecs, labels = get_training_dataset()
    lu.train(input_vecs, labels, 10, 0.01)
    # 返回训练好的线性单元
    return lu


if __name__ == "__main__":
    xxx = train_xxx()
    print(xxx)
    # 测试
    print('Work 3.4 years, monthly salary = %.2f' % xxx.predict([3.4]))
    print('Work 15 years, monthly salary = %.2f' % xxx.predict([15]))
    print('Work 1.5 years, monthly salary = %.2f' % xxx.predict([1.5]))
    print('Work 6.3 years, monthly salary = %.2f' % xxx.predict([6.3]))
