import os
import re


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







if __name__=="__main__":
    string = "(* 1 2 )"
    pattern = re.compile(r'\s+')
    print(pattern.sub("",string))
    print(execute_operator("%",2,3))

    # while(1):
    #     print("please input command: ")
    #     input_str=input()
    #     parse(input_str)

    t=p_1_5()
    t.execute()



