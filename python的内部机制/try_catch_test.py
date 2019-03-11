def try_sample():
    try:
        a = [1, 2, 3]
        # 捕获到异常就跳到except代码块执行
        print(a[4])
        # 抛出异常
        raise KeyError
        # 执行到这压入堆栈
        return 1
    except KeyError as key_error:
        # 捕获KeyError时执行
        print(key_error)
        # 执行到这压入堆栈
        return 2
    except IndexError as index_error:
        # 捕获IndexError时执行
        print(index_error)
        # 执行到这压入堆栈
        return 3
    except:
        # 最后一个except可以忽略异常名称
        # 执行到这压入堆栈
        return 4
    else:
        # try代码块无异常时执行
        print('else block')
        # 执行到这压入堆栈
        return 5
    finally:
        # 是否有异常都会执行
        # 一般用于资源释放
        print('finally block')
        # 执行到这压入堆栈
        return 6


a = try_sample()
# 从栈顶取值 6
print(a)
