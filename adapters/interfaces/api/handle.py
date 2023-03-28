from webob import Request, Response

class API:
    """Handle server"""

    def __init__(self) -> None:
        self.routes = {}

    def __call__(self, environ, start_response):
        request = Request(environ)

        response = self.handle_request(request=request)

        return response(environ, start_response)

    def route(self, path: str):
        """This method is decorator for maper routers."""
        def wrapper(handler):
            self.routes[path] = handler
            return handler
        return wrapper

    def handle_request(self, request):
        """This method check what router was requested."""
        response =  Response()
        for path, handler in self.routes.items():
            if path == request.path:
                handler(request, response)
                return response

        return response
