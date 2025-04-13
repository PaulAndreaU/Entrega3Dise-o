class CacheHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler
        self.cache = {}

    def process(self, request):
        cached_response = self.cache.get(request['data'])
        if cached_response:
            return f"Cache hit: {cached_response}"

        response = "Request processed successfully."
        self.cache_response(request['data'], response)

        if self.next_handler:
            return self.next_handler.process(request)

        return response

    def cache_response(self, request_data, response):
        self.cache[request_data] = response
