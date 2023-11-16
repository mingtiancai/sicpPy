import os
import re
import math

from abc import ABCMeta, abstractmethod


brackets_list=["(",")"]
operator_list=["+","-","*","/","%"]
num_list={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0}


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=Node

def execute_operator(operator,left,right):
    if(operator=="+"):
        return left+right
    elif(operator=="-"):
        return left-right
    elif(operator=="*"):
        return left*right
    elif(operator=="/"):
        return left/right
    elif(operator=="%"):
        return left%right


def parse(input_str):
    if(input_str=="stop"):
        os._exit(0)
    else:
        print("parse error! please input again!")


class p_1_5:
    def __test(self,x, y):
        if (x == 0):
            return 0
        else:
            return y
    def __p(self):
        self.__p()
    def execute(self):
        self.__test(0,self.__p())

class compute_sqrt:
    def __init__(self):
        self.__guess=1.0
        self.__error_limit=0.0001
    def __average(self,x,y):
        return 0.5*(x+y)
    def __imporve(self,x):
        t=x/self.__guess
        self.__guess=self.__average(self.__guess,t)
    def __good_enough(self,x):
        if(abs(self.__guess*self.__guess-x)<self.__error_limit):
            return True
        else:
            return False
    def __sqrt_iter(self,x):
        if(self.__good_enough(x)):
            return self.__guess
        else:
            self.__imporve(x)
            return self.__sqrt_iter(x)

    def execute(self,x):
        return self.__sqrt_iter(x)

def test_compute_sqrt():
    test=compute_sqrt()
    print(test.execute(3))
    print(test.execute(1000))

class p_1_10:
    def execute(self,x,y):
        if(y==0):
            return 0
        elif(x==0):
            return 2*y
        elif(y==1):
            return 2
        else:
            return self.execute(x-1,self.execute(x,y-1))

def test_p_1_10():
    test=p_1_10()
    print(test.execute(1,10))
    print(test.execute(2,4))
    print(test.execute(3,3))

def cube(x):
    return x*x*x
def sum_cube(x):
    res=0
    for i in range(x):
        res+=cube(i+1)
    return res
def test_cube():
    print("cube 2: ",cube(2))
    print("sum cube: ",sum_cube(2))

def g(x):
    return 2*x
def sum(a,b,f):
    res=0
    for i in range(a,b+1):
        res+=f(i)
    return res

def test_sum():
    print(sum(1,2,g))

def g1(x):
    return x*x
def integral(a,b,f,dx):
    res=0
    n=round((b-a)/dx)
    for i in range(n):
        res+=f(a+dx/2+i*dx)*dx
    return res

def test_integral():
    print(integral(1,2,g1,0.01))
    print(integral(1, 2, g1, 0.001))

tl=lambda x: x*x

def test_local_var():
    a=10

    def f(x):
        a=5
        print(a)
        return a*x

    print(f(10))
    print(a)

def test_lambda():
    print(tl(3))



class Shape(metaclass=ABCMeta):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

def test_abc():
    rectangle = Rectangle(5, 10)
    print("Rectangle Area:", rectangle.area())

    circle = Circle(3)
    print("Circle Area:", circle.area())


def test():
    string = "(* 1 2 )"
    pattern = re.compile(r'\s+')
    print(pattern.sub("", string))
    print(execute_operator("%", 2, 3))

    # while(1):
    #     print("please input command: ")
    #     input_str=input()
    #     parse(input_str)
    # test_p_1_10()
    # test_cube()
    # test_sum()
    # test_integral()
    # test_lambda()
    # test_local_var()
    test_abc()
