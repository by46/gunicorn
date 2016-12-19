def app(environ, start_response):
    body = "hello"
    status = '200 OK'
    headers = [('Content-Type', 'plain'), ('Content-Length', str(len(body)))]
    start_response(status, headers)
    return body
