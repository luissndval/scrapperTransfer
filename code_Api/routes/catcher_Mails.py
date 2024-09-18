import email
import imaplib
import re
from email.header import decode_header

from bs4 import BeautifulSoup


# Función para iniciar sesión en Gmail y buscar el correo que contiene el token
def get_token_from_gmail(username, password, search_subject):
    # Crear un objeto IMAP y conectarse al servidor de Gmail
    mail = imaplib.IMAP4_SSL("imap.gmail.com")

    # Iniciar sesión
    mail.login(username, password)

    # Seleccionar la bandeja de entrada
    mail.select("inbox")

    # Buscar correos con el asunto especificado (incluye leídos y no leídos)
    status, messages = mail.search(None, 'SUBJECT "{}"'.format(search_subject))

    # Obtener la lista de IDs de los correos
    mail_ids = messages[0].split()

    # Si no hay correos con el asunto especificado, salir
    if not mail_ids:
        print("No se encontraron correos con el asunto especificado.")
        return None

    # Obtener el correo más reciente
    latest_email_id = mail_ids[-1]

    # Obtener los datos del correo
    status, msg_data = mail.fetch(latest_email_id, "(RFC822)")

    # Parsear el correo
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding)
            print("Subject:", subject)

            # Si el correo tiene múltiples partes
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))

                    # Obtener el contenido del correo
                    if "attachment" not in content_disposition:
                        if content_type == "text/plain" or content_type == "text/html":
                            body = part.get_payload(decode=True)
                            if body:
                                try:
                                    body = body.decode()
                                except UnicodeDecodeError:
                                    body = body.decode('latin1')  # Probar con otro codec
                                return extract_token(body)
            else:
                body = msg.get_payload(decode=True)
                if body:
                    try:
                        body = body.decode()
                    except UnicodeDecodeError:
                        body = body.decode('latin1')  # Probar con otro codec
                    print("Body:", body)
                    return extract_token(body)

    return None


# Función para extraer el token del cuerpo del correo
def extract_token(body):
    # Analizar el contenido HTML usando BeautifulSoup
    soup = BeautifulSoup(body, 'html.parser')
    text = soup.get_text()

    # Usar expresiones regulares para encontrar el valor que sigue a "Clave Digital: "
    match = re.search(r"Clave Digital:\s*(\d+)", text)
    if match:
        return match.group(1)
    return None

# Ejemplo de uso
username = "luisllaneton@gmail.com"
password = "kzkw ecgu dbvj hssd"
# //vxup fcsg xrnf igxe
search_subject = "Clave Digital - BBVA Provincial"
token = get_token_from_gmail(username, password, search_subject)

if token:
    print("Token encontrado:", token)
else:
    print("No se encontró el token.")

