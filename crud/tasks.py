from celery import shared_task
from django.core.mail import send_mail
import time

@shared_task
def envoyer_email_bienvenue(email_destinataire):
    # Simulation d'un traitement long (ex: appel API externe)
    time.sleep(5) 
    
    send_mail(
        subject='Bienvenue !',
        message='Merci de votre inscription.',
        from_email='fygdev@gmail.com',
        recipient_list=[email_destinataire],
        fail_silently=False,
    )
    return f"Email envoyé à {email_destinataire}"