#coding=utf-8
import wx, math

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y)

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)
    #两个点相加相减的多态

    @property
    def xy(self):
        return  (self.x, self.y)

    def __str__(self):
        return "x={0}, y={1}".format(self.x, self.y)

    def __repr__(self):
        return str(self.xy)
    #打印该点信息

    @staticmethod
    def dist(a, b):
        return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
    #计算距离的类方法