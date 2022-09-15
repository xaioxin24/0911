#主进程结束后不会再继续执行子进程中剩余的工作

import time
import multiprocessing

def work():
    for i in range(10):
        print("工作中。。。。")
        time.sleep(0.2)

if __name__ == '__main__':
    # 设置守护主进程，主进程执行完成，则结束
    # 方式1
    work_process = multiprocessing.Process(target=work, daemon=True)
    # 方式2
    # work_process.daemon = True
    work_process.start()

    time.sleep(1)
    print("主进程执行结束")
