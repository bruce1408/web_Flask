## 1 flask route 作用 
flask route的作用就是建立url与处理函数的映射

## 2 flask 和 WSGI 关系
WSGI协议将处理请求的组件按照功能及调用关系分成了三种：server, middleware, application。
其中，server可以调用middleware和application，middleware可以调用application。

符合WSGI的框架对于一次http请求的完整处理过程为：
server读取解析请求，生成environ和start_response，然后调用middleware；
middleware完成自己的处理部分后，可以继续调用下一个middleware或application，形成一个完整的请求链；
application位于请求链的最后一级，其作用就是生成最终的响应

>  http服务器（比如，nginx）--> WSGI server(比如gunicorn，SimpleHttpServer)-->middleware-->
 middleware--> ... -->application
## 3 flask route 实现思路
