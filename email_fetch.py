from imapclient import IMAPClient
import email
from email.header import decode_header
import config

def fetch_emails():
    with IMAPClient(config.EMAIL_HOST) as server:
        server.login(config.EMAIL_ADDRESS, config.EMAIL_PASSWORD)
        server.select_folder("INBOX", readonly=True)
        
        messages = server.search("UNSEEN")
        email_list = []
        
        for msg_id in messages:
            raw_msg = server.fetch(msg_id, ["RFC822"])[msg_id][b"RFC822"]
            msg = email.message_from_bytes(raw_msg)
            
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes) and encoding:
                subject = subject.decode(encoding)
            
            sender = msg.get("From")
            body = ""

            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True).decode()
                        break
            else:
                body = msg.get_payload(decode=True).decode()

            email_list.append({"id": msg_id, "subject": subject, "sender": sender, "body": body})

        return email_list
