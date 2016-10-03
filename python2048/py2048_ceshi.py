#coding=utf-8
import math
from abc import ABCMeta, abstractmethod
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

a = Point(20, 20)
b = Point(20, 40)
ab_dist = Point.dist(a, b)
print "ab_dist = %d" %ab_dist
print a, b
print a.xy,  b.xy

class Polygon():
    '''多边形的类，由一系列的点来描述，点分别是Point点对象
    __init__初始化，输入一系列的点的列表，和颜色
    drawPoints：打印出所有的点坐标，并且返回点坐标的元组。'''
    # __metaclass__ = ABCMeta
    def __init__(self, points_list, **kwargs):
        for point in points_list:
            assert isinstance(point, Point), "input must be Point type"
        #确定输入的点为Point类型
        self.points = points_list[:]
        self.points.append(points_list[0])
        self.color = kwargs.get('color', '#000000')

    def drawPoints(self):
        points_xy = []
        for point in self.points:
            points_xy.append(point.xy)
        print points_xy
        return tuple(points_xy)

    @abstractmethod
    def area(self):
        raise Exception("not implement")

    def __lt__(self, other):
        assert isinstance(other, Polygon)
        return self.area < other.area

P1 = Polygon([a, b])
P2 = P1.drawPoints()
print b


































