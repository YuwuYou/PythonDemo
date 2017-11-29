#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/11/29 0029
# @Author  : TaoYuan (1876665310@qq.com)
# @Link    : http://blog.csdn.net/lftaoyuan  Python互助学习qq群：315857408
# @Version : V1.0.0

# 面向对象的程序设计思想
# 我们首选思考的不是程序的执行流程，而是Student这种数据类型应该被视为一个对象
# 这个对象拥有name和score这两个属性（Property）。
# 如果要打印一个学生的成绩，
# 首先必须创建出这个学生对应的对象，
# 然后给对象发一个print_score消息
# 让对象自己把自己的数据打印出来。
class Student(object):
    """docstring for Student"""

    def __init__(self, name, score, remark):
        self.name = name
        self.score = score
        self.remark = remark

    def print_score(self):
        print("{0} {1} {2}".format(self.name, self.score, self.remark))

# 面向过程
# 假设我们要处理学生的成绩表，为了表示一个学生的成绩，面向过程的程序可以用一个dict表示：
std1 = {'name': 'Michael', 'score': 98}
std2 = {'name': 'Bob', 'score': 81}

# 而处理学生成绩可以通过函数实现，比如打印学生的成绩：
def print_score(std):
    print('%s: %s' % (std['name'], std['score']))


if __name__ == '__main__':
    print('----------------')
    Student("zhangsan", 59, "命不好").print_score()
    Student("lisi", 99, "屌爆了").print_score()
    print('----------------')
    print_score(std1)
    print_score(std2)
    print('----------------')
