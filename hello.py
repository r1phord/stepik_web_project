def wsgi(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    if environ['REQUEST_METHOD'] == 'GET':
        parameters = environ['QUERY_STRING'].split('&')
        body = [bytes(i + '\n', 'ascii') for i in parameters]
        return body
    # return [bytes('Hello world', 'ascii')]
