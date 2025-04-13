class ValidationHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def process(self, request):
        if not self.validate(request):
            return "Request validation failed."

        if self.next_handler:
            return self.next_handler.process(request)

        return "Request validated successfully."

    def validate(self, request):
        return isinstance(request.get('data'), str) and len(request.get('data')) > 0
