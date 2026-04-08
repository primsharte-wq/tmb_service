from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class Profil(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ROLE_CHOICES = (('admin', 'Admin'), ('user', 'User'))
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Category(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'

    def __str__(self):
        return self.nom

class Service(models.Model):
    categorie = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='services')
    nom = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.nom

class Modele(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='modeles')
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='modeles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Modèle'
        verbose_name_plural = 'Modèles'

    def __str__(self):
        return self.titre

    @property
    def likes_count(self):
        return self.gouts.count()

    @property
    def comments_count(self):
        return self.commentaires.count()

class Commentaire(models.Model):
    modele = models.ForeignKey(Modele, on_delete=models.CASCADE, related_name='commentaires')
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    contenu = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    def __str__(self):
        return f"Commentaire par {self.profil.username}"

class Gout(models.Model):
    modele = models.ForeignKey(Modele, on_delete=models.CASCADE, related_name='gouts')
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('modele', 'profil')
        verbose_name = 'Goût'
        verbose_name_plural = 'Goûts'

    def __str__(self):
        return f"{self.profil.username} aime {self.modele.titre}"

class Message(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.SET_NULL, null=True, blank=True)
    nom = models.CharField(max_length=255)
    telephone = models.CharField(max_length=50)
    contenu = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return f"Message de {self.nom}"
        
# Create your models here.
