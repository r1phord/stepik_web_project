def wsgi(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    parameters = environ['QUERY_STRING'].split('&')
    return '\n'.join(parameters)
