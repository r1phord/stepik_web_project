def wsgi(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    if environ['REQUEST_METHOD'] == 'GET':
        parameters = environ['QUERY_STRING'].split('&')
        return '\n'.join(parameters)
