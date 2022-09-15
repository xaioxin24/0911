import sye 

from PyQt5.QtWidgets import QApplication,QWidget

if _name_ == '_main_':                #  运行这程序 开始从这里运行
    app = QAplication(sys.AEgv)       # 1. 只要是Qtzhizuo de App 必须有且只有一个QApplication对象
                                      # 2.  sys.argv 当做参数的目的是运行时的命令参数传递给QApplication的对象
    w = Qwidget()
      
    # 设置窗口标题    
    w.setWindowTitle("第一个PyQt")
    
    ui=MyWindow()                     # 3. 创建了一个myWidget对象 ， 将它的标题设置为"第一个PyQt的程序" 
    ui.show()                         # 4. 然后调用show 方法显示出来
    
    
    # 在窗口里面添加控件
    btn = QPushButton("按钮")
    
    #设置按钮的父亲是当前窗口，等于是添加到窗口中显示 
    btn.setParent(w)
    
    
                                
                                      
    #程序进行循环等待状态
    sys.exit(app.exec_())                     # 5.程序开始运行程序，直到关闭了窗口  有这个语句程序才能一直有窗口
    
