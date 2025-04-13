from Handlers.Authentication_Handler import AuthenticationHandler
from Handlers.Validation_Handler import ValidationHandler
from Handlers.Cache_Handler import CacheHandler

class RequestController:
    def __init__(self):
        # La cadena de verificación inicia con el AuthenticationHandler y sigue con ValidationHandler y CacheHandler
        self.verification_chain = AuthenticationHandler(next_handler=ValidationHandler(next_handler=CacheHandler())
        )

    def process_order(self, request):
        # Procesa la solicitud pasando por la cadena de responsabilidad
        return self.verification_chain.process(request)
    
