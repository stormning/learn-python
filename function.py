# coding=utf-8
def add_func(a, b):
    return a + b


# 单独运行时运行,作为模块时不运行
if __name__ == "__main__":
    print add_func(1, 2)
