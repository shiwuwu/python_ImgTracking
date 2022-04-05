import logging
import os
import time


class Log(object):
    """
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志存入指定的文件中
        需要输入，path，name，setlevel三个参数
        time为time.strftime("%Y_%m_%d")
        setlevel 为指定打印等级，默认为INFO
        调用方法为 LOG = Log(path=path,name=name).getlog()

    """
    def __init__(self,path=str(os.getcwd()),name="log",setlevel="INFO"):
        self.loger =logging.getLogger(name)
        self.setLevel = getattr(logging,setlevel)
        self.loger.setLevel(self.setLevel)
        self.log_time = time.strftime("%Y_%m_%d")
        self.log_path = path
        self.log_name = self.log_path + '\\' +name + '.log'

        if not os.path.isfile(self.log_name):
            # 创建一个输出到文件的 handler
            f = logging.FileHandler(self.log_name,'a')
            f.setLevel(self.setLevel)
            # 创建一个输出到控制台的hanler
            c = logging.StreamHandler()
            c.setLevel(self.setLevel)
            # 定义hanler
            formatter = logging.Formatter(
                '[%(asctime) %(filename)s -> %(funName)s line %(lineo)d [%(levelname)s]%(message)s\n %]'

            )
            # 添加handler
            f.setFormatter(formatter)
            c.setFormatter(formatter)
            # 给loger添加handler
            self.loger.addHandler(f)
            self.loger.addHandler(c)
            # 关闭文件
            f.close()
            c.close()

        def getlog(self):
            return self.loger