class AuthenticationHandler:
    def __init__(self, next_handler=None, max_attempts=3):
        self.next_handler = next_handler
        self.failed_attempts = {}
        self.max_attempts = max_attempts

    def process(self, request):
        user_ip = request['ip']
        if self.check_brute_force(user_ip):
            return "Acceso bloqueado por muchos intentos."

        if not self.authenticate(request):
            self.failed_attempts[user_ip] = self.failed_attempts.get(user_ip, 0) + 1
            return "Autenticación fallida."

        self.failed_attempts[user_ip] = 0

        if self.next_handler:
            return self.next_handler.process(request)

        return "Autenticación realizada con éxito."

    def authenticate(self, request):
        return request.get('username') == 'admin' and request.get('password') == 'password'

    def check_brute_force(self, ip_address):
        return self.failed_attempts.get(ip_address, 0) >= self.max_attempts
