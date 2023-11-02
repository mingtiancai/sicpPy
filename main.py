import os


def parse(input_str):
    if(input_str=="stop"):
        os._exit(0)
    else:
        print("parse error! please input again!")



if __name__=="__main__":
    while(1):
        print("please input command: ")
        input_str=input()
        parse(input_str)

