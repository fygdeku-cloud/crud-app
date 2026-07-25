import os
from celery import Celery

# Définir les réglages Django par défaut
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Lire la configuration depuis settings.py avec le préfixe CELERY_
app.config_from_object('django.conf:settings', namespace='CELERY')

# Charger automatiquement les tâches dans tasks.py de chaque application
app.autodiscover_tasks()