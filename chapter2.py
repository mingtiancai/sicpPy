from base import base_sicp_class as bsc

class t1(bsc):

    def test_func(self):
        print("test func")

def test():
    t=t1()
    t.test_func()