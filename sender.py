import smtplib
import ssl

# Configuración del servidor SMTP
smtp_server = 'localhost'  # Cambia 'localhost' por la dirección IP o el nombre de dominio del servidor SMTP
smtp_port = 25  # Puerto estándar para SMTP sin encriptar, 465 para encriptado 
smtp_use_tls = False  # Cambia a True si deseas utilizar SMTP encriptado

# Configuración del remitente y destinatario
sender = 'remitente@example.com'  # Reemplaza 'remitente@example.com' por la dirección de correo electrónico del remitente
recipient = 'destinatario@example.com'  # Reemplaza 'destinatario@example.com' por la dirección de correo electrónico del destinatario

# Crear el mensaje
subject = 'Prueba de correo POP3'
body = 'Este es un correo de prueba para POP3.'
message = f'Subject: {subject}\n\n{body}'

# Conexión SMTP
if smtp_use_tls:
    # Conexión SMTP encriptada
    smtp_server = 'smtps://' + smtp_server
    smtp_context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, smtp_port, context=smtp_context) as server:
        server.sendmail(sender, recipient, message)
else:
    # Conexión SMTP sin encriptar
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.sendmail(sender, recipient, message)

print("Mensaje enviado correctamente.")
