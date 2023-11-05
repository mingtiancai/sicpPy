import os
import re
import math


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






if __name__=="__main__":
    string = "(* 1 2 )"
    pattern = re.compile(r'\s+')
    print(pattern.sub("",string))
    print(execute_operator("%",2,3))

    # while(1):
    #     print("please input command: ")
    #     input_str=input()
    #     parse(input_str)

    test=compute_sqrt()
    print(test.execute(3))

