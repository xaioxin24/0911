# 使用super函数解决砖石继承的方法
# 函数继承加重写

class A:
    def _init_(self):
        print("哈喽，我是A~")
        
class B1(A):
    def _init_(self):
        super._init_()
        print("哈喽，我是B1~")

class B2(A):
    def _init_(self):
        super._init_()
        print("哈喽，我是B2~")
        
class C(B1,B2):
    def _init_(self):
        super._init_()
        print("哈喽，我是C~") 
c=C()
