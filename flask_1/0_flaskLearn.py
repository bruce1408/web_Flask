from flask import Flask
from flask import request
"""
通过路由把url和函数映射到一起
"""
# app = Flask(__name__)
#
#
# @app.route('/', methods=['GET', 'POST'])
# def home():
#     return '<h1>home</h1>'
#
#
# @app.route('/signin', methods=['GET'])
# def signin_from():
#     return """<form action="/signin" method='post'>
#     <p><input name="username"></p>
#     <p><input name="password" type="password"></p>
#     <p><button type="submit">Sign In</button></p>
#     </form>"""
#
#
# @app.route('/signin', methods=['POST'])
# def signin():
#     if request.form['username'] == 'admin' and request.form['password'] == 'password':
#         return "<h3>hello, admin!</h3>"
#     return "<h3>Bad username or password</h3>"
#
#
# if __name__ == "__main__":
#     print(app.url_map)
#     app.run()

import re
route_regex = re.compile(r'^/hello/(?P<username>.+)$')
match = route_regex.match("/hello/ains")
print(match.groupdict())


# 2 装饰器部分来复现app路由功能
# class FlaskBother():
#     def __init__(self):
#         self.routes = {}
#
#     def route(self, route_str):
#         def decorator(f):
#             def wrapper(test):
#                 a = route_str+f(test)
#                 self.routes[test] = a
#                 return self.routes
#             return wrapper
#         return decorator
#
#
# app = FlaskBother()
#
#
# @app.route('/')
# def hello(test):
#     return test+"/"+'Hello World'
#
#
# print(hello("name"))
# hello("name")


# 3 example 装饰器和正则表达式结合
# class MyFlask():
#     def __init__(self):
#         self.routes = []
#
#     @staticmethod
#     def build_route_pattern(route):
#         route_regex = re.sub(r'(<\w+>)', r'(?P\1.+)', route)
#         return re.compile("^{}$".format(route_regex))
#
#     def route(self, route_str):
#         def decorator(func):
#             route_pattern = self.build_route_pattern(route_str)
#             self.routes.append((route_pattern, func))
#             return func
#         return decorator
#
#     def get_route_match(self, path):
#         for route_pattern, view_function in self.routes:
#             m = route_pattern.match(path)
#             if m:
#                 return m.groupdict(), view_function
#         return None
#
#     def serve(self, path):
#         route_match = self.get_route_match(path)
#         if route_match:
#             kwargs, view_function = route_match
#             return view_function(**kwargs)
#         else:
#             raise ValueError('Route "{}"" has not been registered'.format(path))
#
#
# app = MyFlask()
#
#
# @app.route("/hello/<username>")
# def hello_user(username):
#     return "Hello {}!".format(username)
#
#
# print(app.serve("/hello/ains"))





