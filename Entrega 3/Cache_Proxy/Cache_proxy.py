class CacheProxy:
    def __init__(self, controller):
        self.controller = controller
        self.cache = {}

    def process_order(self, request):
        key = request.get('data')
        if key in self.cache:
            return f"Cache hit (Proxy): {self.cache[key]}"

        response = self.controller.process_order(request)
        # Solo se guarda en caché si la respuesta es exitosa o es un cache hit
        if response.startswith("Request processed") or response.startswith("Cache hit"):
            self.cache[key] = response
        return response
