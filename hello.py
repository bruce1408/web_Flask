def application(environ, start_reponse):
    """

    :param environ: 包含所有http请求信息的dict对象
    :param start_reponse: 发送HTTP响应的函数
    :return:
    """
    start_reponse('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>hello , web %s</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]