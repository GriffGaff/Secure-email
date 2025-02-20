from email_fetch import fetch_emails
from blacklist import is_blacklisted
from spam_detector import is_spam_email
from logger import log_message

def process_emails():
    emails = fetch_emails()
    for email in emails:
        sender = email["sender"]
        subject = email["subject"]
        body = email["body"]

        if is_blacklisted(sender):
            log_message("info", f"Email blocked from blacklisted sender {sender}: {subject}")
            continue

        if is_spam_email(body):
            log_message("info", f"Detected Spam email from {sender}: {subject}")
            continue

        log_message("info", f"Email received from {sender}: {subject}")

if __name__ == "__main__":
    process_emails()
