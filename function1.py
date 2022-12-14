#1.导入进程包    执行带有参数的任务
import multiprocessing
import time
import os

def sing(name, num):
    print("唱歌进程的编号： ", os.getpid())
    print("唱歌进程的父进程的编号： ", os.getppid())
    for i in range(num):
        print("%s在唱歌。。。"%name)
        time.sleep(0.5)
        
def dance(num):
    print("跳舞进程的编号： ", os.getpid())
    print("跳舞进程的父进程的编号： ", os.getppid())
    for i in range(num):
        print("跳舞。。。")
        time.sleep(0.5)
        
if __name__ == '__main__':
    print("主进程的编号： ", os.getpid())
    # 2.使用进程类创建进程对象
    #  target: 指定进程执行的函数名
    # args: 使用元组方式给指定任务传参
    # kwargs: 使用字典方式给指定任务传参
   

    # 以元组形式传参   顺序和参数顺序一致
    s1 = multiprocessing.Process(target=sing, args=('小明', 3))
    # 以字典形式传参   key和参数名保持一致
    d1 = multiprocessing.Process(target=dance, kwargs={"num": 5, })
    s1.start()
    d1.start()

    
单任务
使用多进程实现多任务
进程执行带有参数的任务
获取进程的编号
        
        
