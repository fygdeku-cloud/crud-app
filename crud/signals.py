from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profile

@receiver(post_save, sender=User)
def creer_profil_utilisateur(sender, instance, created, **kwargs):
    """
    - sender   : Le modèle qui émet le signal (ici User).
    - instance : L'objet précis qui vient d'être sauvegardé.
    - created  : Un booléen qui vaut True SI l'objet vient d'être créé 
                 (et False s'il s'agit d'une simple mise à jour).
    """
    if created:
        Profile.objects.create(user=instance)
        print(f"--> [SIGNAL] Le profil de {instance.name} a été créé automatiquement !")