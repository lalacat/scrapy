import os,sys
from importlib import import_module
from pkgutil import iter_modules
import inspect
from scrapy.commands import ScrapyCommand
import re
import optparse

'''
   if hasattr(mod, '__path__'):
        for _, subpath, ispkg in iter_modules(mod.__path__):
            fullpath = path + '.' + subpath
            if ispkg:
                mods += walk_modules(fullpath)
            else:
                submod = import_module(fullpath)
                mods.append(submod)
'''


def import_command(path):
    """
    导入指定目录下的包
        一般可以用于命令的导入
    对指定目录下存在多个文件的的时候回也能递归导入
    例如import_command("scrapy.commands")
    """
    mods = []
    #这条命令执行完只导入了目标文件夹中第一个*.py文件
    mod = import_module(path)
    mods.append(mod)

    #通过第一个.py文件获取该文件夹的绝对地址，通过文件夹的绝对地址可以通过iter_modules(path)方法获得该文件夹下所有的文件
    if hasattr(mod,'__path__'):
        """
            三个参数:
            第一个通常不用
            subpath 获得的事文件或文件夹名（包名）
            ispkg 判断subpath是py文件还是文件夹（包），是包的话为true
            通过判断就可以实现指定目录下包括子目录的所有文件都能导入到执行环境中
        """
        for _,subpath,ispkg in iter_modules(mod.__path__):
            #取得模块的绝对路径
            fullpath = path+"."+subpath

            #判断是模块包还是模块
            if ispkg:
                #是模块包的话重新调用本方法将模块包下的所以模块都导入
                mods += import_command(fullpath)
            else:
                #是模块的话就直接导入到结果中
                submod = import_module(fullpath)
                mods.append(submod)
    return mods


def get_command(commands):
    for c in commands:
        for obj in vars(c).values():
            """
            vars（）实现返回对象object的属性和属性值的字典对象
            要过滤出obj是类的信息，其中类的信息包括，模块导入其他模块的类的信息，模块中的父类，模块中所有定义的类
            因此，条件过滤分别是：
            1.判断obj的类型为class
            2.判断是否继承父类，因此命令包中__init__文件中定义的就是整个包中所需要的父类
            3.判断类是否为模块本身定义的类还是导入其他模块的类(感觉第二个条件包含此条件了有些多余)
            4.剔除父类
            """
            if inspect.isclass(obj) and \
                    issubclass(obj, ScrapyCommand) and \
                    obj.__module__ == c.__name__ and \
                    not obj == ScrapyCommand :
                yield obj

def get_command_dict(commands):
    dict_command = {}
    for c in get_command(commands):
        dict_command[c.__module__.split(".")[-1]]=c()
    return dict_command

def __pop_command_name(agrs):
    i = 1
    print("start")
    for a in agrs[1:]:
        if a is not agrs.startswith("-"):
            print(a)
            del(agrs[i])
            return a
        else:
            print("-"+a)
        i += 1

if __name__ == "__main__":
    """
    os.chdir("..")
    print(os.getcwd())
    path= os.getcwd()
    sys.path.append(path)
    from scrapy.commands import ScrapyCommand
    __pop_command_name(sys.argv) 
    """

