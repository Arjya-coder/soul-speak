import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USER = 'your-email@gmail.com'  # Replace with your email
SMTP_PASSWORD = 'your-email-password'  # Replace with your email password

def send_recovery_email(email):
    try:
        subject = "Password Recovery - SoulSpeak"
        body = f"Dear User,\n\nClick the link below to reset your password:\n\nhttp://example.com/reset-password?email={email}\n\nRegards,\nSoulSpeak Team"
        message = MIMEText(body)
        message['Subject'] = subject
        message['From'] = SMTP_USER
        message['To'] = email

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(SMTP_USER, email, message.as_string())
        server.quit()

        return {'status': f'Recovery email sent to {email}'}
    except Exception as e:
        return {'status': 'Error', 'message': str(e)}
