from base import base_sicp_class as bsc

class t1(bsc):
    def valid_func(self):
        print("valid func")

    def test_func(self):
        self.valid_func()
        print("test func")

def test():
    t=t1()
    t.test_func()