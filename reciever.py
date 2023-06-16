import poplib
import ssl

# Configuración del servidor POP3
pop3_server = 'localhost'  # Cambia 'localhost' por la dirección IP o el nombre de dominio del servidor POP3
pop3_port = 110  # Puerto estándar para POP3 sin encriptar 995 par encriptado
pop3_use_ssl = False  # Cambia a True si deseas utilizar POP3 encriptado

# Establecer conexión con el servidor POP3
if pop3_use_ssl:
    # Conexión POP3 encriptada
    pop3_server = 'pop3s://' + pop3_server
    pop3_context = ssl.create_default_context()
    server = poplib.POP3_SSL(pop3_server, port=pop3_port, context=pop3_context)
else:
    # Conexión POP3 sin encriptar
    server = poplib.POP3(pop3_server, port=pop3_port)

# Iniciar sesión en el servidor POP3
server.user('usuario')  # Reemplaza 'usuario' por el nombre de usuario del servidor POP3
server.pass_('contraseña')  # Reemplaza 'contraseña' por la contraseña del servidor POP3

# Obtener información del servidor
messages = server.list()[1]
print("Mensajes disponibles en el servidor:")

for msg in messages:
    print(msg)

# Obtener el primer mensaje
msg_number = 1
resp, msg_lines, octets = server.retr(msg_number)

# Decodificar el mensaje
msg_content = b'\n'.join(msg_lines).decode('utf-8')
print("Contenido del mensaje:")
print(msg_content)

server.quit()
