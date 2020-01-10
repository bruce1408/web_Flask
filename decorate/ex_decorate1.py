# -*- coding: utf-8 -*-
# !/usr/bin/env python
__author__ = 'Bruce Cui'
import logging
from functools import wraps

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(filename)s - %(message)s')


# 它能把原函数的元信息拷贝到装饰器函数中,这使得装饰器函数也有和原函数一样的元信息了
# def a_new_function(a_func):
#     @wraps(a_func)
#     def wrapTheFunction():
#         print("I am doing some boring work before executing a_func()")
#
#         a_func()
#
#         print("I am doing some boring work after executing a_func()")
#
#     return wrapTheFunction
#
#
# def a_function_requiring_decoration():
#     print("I am the function which needs some Decoration to remove my foul smell")
#
#
# print("after wrap is:", a_function_requiring_decoration.__name__)

# @Time    : 2017/12/5 22:45
# @File    : decorators_exercise.py


# 装饰器
# def outer(some_func):
#     def inner():
#         print("before some_func")
#         ret = some_func()  # 1
#         return ret + 1
#     return inner


# def foo():
#     return 1


# foo = outer(foo)
# print(foo())


# 简单装饰器1
# def foo():
#     print('i am foo')
#
#
# def foo1():
#     """
#     # 这是为了打印出日志做的修改而已，但是实际会很麻烦，不可能每一个都去打印出一个日志
#     :return:
#     """
#     print('i am foo')
#     logging.info("the foo is runing....")

# 这里是因为它改变了业务逻辑，原来执行的是foo，现在却是use_long
# def use_long(func):
#     logging.info("the func %s is running"%func.__name__)
#     func()


# def use_long(func):
#     def wraper(*args, **kwargs):
#         logging.info("the func %s is running..." % func.__name__)
#         return func(*args, **kwargs)
#     return wraper
#
#
# foo = use_long(foo)
# foo()


# 简单装饰器升级2
# def use_long(func):
#     def wrapper(*args, **kwargs):
#         logging.info("the func {} is running".format(func.__name__))
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @use_long  # 相当于 foo = use_long(foo)
# def foo():
#     print('i am foo')
#
#
# @use_long
# def bar():
#     print('i am bar')
#
#
# foo()
# bar()


# 简单装饰器升级3
def use_long(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == 'info':
                logging.info('the %s is running' % func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@use_long(level='info')
def foo(name='foo'):
    print(('i am the %s ' % name))


foo()

# 高级装饰器用法
# class Coordinate(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __repr__(self):
#         return "Coord: " + str(self.__dict__)
#
#
# def add(a, b): # a 和 b 都是函数名称
#     return Coordinate(a.x + b.x, a.y + b.y)
# def sub(a, b):
#     return Coordinate(a.x - b.x, a.y - b.y)
#
# one = Coordinate(100, 200)
# two = Coordinate(200, 200)
# three = Coordinate(200, 200)
#
#
# def wrapper(func):
#     def checker(a, b): # 1
#         if a.x < 0 or a.y < 0:
#             a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
#         if b.x < 0 or b.y < 0:
#             b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
#         ret = func(a, b)
#         print('the ret is: ',ret)
#         if ret.x < 0 or ret.y < 0:
#             ret = Coordinate(ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else 0)
#         return ret
#     return checker
# add = wrapper(add)
# sub = wrapper(sub)
# print(sub(one, three))


# def wrapper(option):
#     def outer(func):
#         def inner(*args, **kwargs):
#             return func(*args, **kwargs)
#         return inner
#     return outer
#
#
# @wrapper({"k": 'v'})
# def index():
#     print("this is func is:")
#
# index()


# def tag(func):
#     def wrapper(text):
#         value = func(text)
#         return "<p>" + value + "</p>"
#
#     return wrapper
#
#
# @tag  # 相当于my_upper = tag(my_upper)
# def my_upper(text):
#     value = text.upper()
#     return value
#
#
# print(my_upper('hello'))


# example 1, 业务代码逻辑外面可以添加其他修改
def tag(name):
    def decorate(func):
        def wrapper(text):
            value = func(text)  # func 接收返回一个参数
            return "<{name}>{value}</{name}>".format(name=name, value=value)
        return wrapper
    return decorate


@tag("p")
def my_upper(text):
    value = text.upper()
    return value


print(my_upper('hello'))
# # example 2, 正常函数的形式
# def valueStr(name, value):
#     value = value.upper()
#     return "<{name}>{value}</{name}>".format(name=name, value=value)


# print(valueStr("p", "hello"))


# example 3, 装饰器传递参数
# def not_very_simply_decorator(enter_msg, exit_msg):
#     def simple_decorator(f):
#         def wrapper():
#             print(enter_msg)
#             f()
#             print(exit_msg)
#         return wrapper
#     return simple_decorator
#
#
# @not_very_simply_decorator("func enter", "func exit")
# def hello():
#     print("Hello World")
#
#
# hello()


# class FlaskBother():
#     def route(self, route_str):
#         def decorator(f):
#             def wrapper(*args, **kwargs):
#                 return f(*args, **kwargs)
#             return wrapper
#         return decorator
#
#
# app = FlaskBother()
#
#
# @app.route('/')
# def hello(strWord):
#     return strWord
#
#
# print(hello('name hello'))
#

