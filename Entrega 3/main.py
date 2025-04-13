from Controllers.Request_Controller import RequestController
from Cache_Proxy.Cache_proxy import CacheProxy

if __name__ == "__main__":
    # Definición de una solicitud de prueba
    request = {
        'ip': '192.168.0.1',
        'username': 'admin',
        'password': 'password',
        'data': 'order_details'
    }

    controller = RequestController()  # Se crea el controlador
    proxy = CacheProxy(controller)      # Se crea el proxy para gestionar la caché

    # Primera solicitud: se procesa normalmente por la cadena de verificación.
    response = proxy.process_order(request)
    print(response)  # Debería pasar todas las verificaciones y procesarse la solicitud

    # Segunda solicitud con el mismo 'data': se espera cache hit a nivel de proxy.
    response = proxy.process_order(request)
    print(response)  # Debería devolver "Cache hit (Proxy): ..."

    # Solicitud fallida (cambiar usuario y contraseña)
    request['username'] = 'wrong_user'
    request['password'] = 'wrong_pass'
    response = proxy.process_order(request)
    print(response)  # Debería devolver "Authentication failed."
