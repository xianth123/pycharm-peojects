#coding=utf-8
import wx, math
from abc import ABCMeta, abstractmethod

class Example(wx.Frame):
    '''传入标题和形状的列表两个参数，会自动画出该形状'''
    def __init__(self,title, shapes):
        super(Example, self).__init__(None, title=title,
                                      size=(600, 400))

        self.shapes = shapes

        #绑定渲染窗口的动作到OnPaint
        #将绘画的方法传入进self.Bind
        #当resize窗口，会重新调用该函数
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.Centre()
        self.Show()

    def OnPaint(self, e):
        dc = wx.PaintDC(self)
        for shape in self.shapes:
            dc.SetPen(wx.Pen(shape.color))
            dc.DrawLines(shape.drawPoints())

class Point(object):
    '''这是点的类对象，由x， y两点坐标描述'''
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

class Polygon(object):
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
        return self.area<other.area

#rectangle 多边形的子类 矩形
class RectAngle(Polygon):
    '''传入三个参数来描述矩形，初始点，宽，高。面积为长乘以宽'''
    def __init__(self, startPoint, w, h, **kwargs):
        self._w = w
        self._h = h
        s = startPoint
        Polygon.__init__(self, [s, s+Point(w,0), s+Point(w,h), s+Point(0,h)], **kwargs)

    def area(self):
        return self._w*self._h

#trian  多边形的子类  三角形


class TriAngle(Polygon):
    def __init__(self, Point_1, Point_2, Point_3, **kwargs):
        self.P1 = Point_1
        self.P2 = Point_2
        self.P3 = Point_3
        if self.P1.x == self.P2.x == self.P3.x or self.P1.y == self.P2.y == self.P3.y:
            raise Exception("三角形三个点不能在同一条直线上")
        Polygon.__init__(self, [self.P1, self.P2, self.P3], **kwargs)

    def area(self):
        a = Point.dist(self.P1, self.P2)
        b = Point.dist(self.P2, self.P3)
        c = Point.dist(self.P1, self.P3)
        p = (a+b+c)/2.0
        return math.sqrt(p*(p-a)*(p-b)*(p-c))


#Circle类，多边形的子类 圆

class Circle(Polygon):
    '''接受三个参数Point类型的圆心点，半径radius长度， 圆的边数量'''
    def __init__(self, CentrePoint, radius, sides_number, **kwargs):
        self.centreangle = 2.0*math.pi/sides_number
        points = []
        self.radius = radius
        for i in range(sides_number):
            side_centreangle = i*self.centreangle
            CirPoint = CentrePoint + Point(math.sin(side_centreangle)*radius,
                                          math.cos(side_centreangle)*radius)
            points.append(CirPoint)
        Polygon.__init__(self, points, **kwargs)

    def area(self):
        return math.pi*self.radius**2


if __name__ == "__main__":
    prepare_draws = []

    #生成一个矩形实例
    start_p = Point(50, 60)
    a = RectAngle(start_p, 100, 80, color="#ff0000")

    prepare_draws.append(a)

    #生成一个三角形实例
    triangle_a = Point(200, 200)
    triangle_b = Point(200, 400)
    triangle_c = Point(400, 200)
    triangle_ceshi = TriAngle(triangle_a,triangle_b,triangle_c)

    prepare_draws.append(triangle_ceshi)

    #生成一个圆形实例
    centrepoint = Point(200,200)
    roundness = Circle(centrepoint, 100, 100)

    prepare_draws.append(roundness)

    for shape in prepare_draws:
        print shape.area()


    app = wx.App(True)
    Example("Shapes", prepare_draws)
    app.MainLoop()


