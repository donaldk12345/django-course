from django.db import models

from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom de la catégorie")
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nom du médecin / collègue")
    speciality = models.CharField(max_length=150, verbose_name="Spécialité")
    bio = models.TextField(verbose_name="Parcours / Biographie")
    photo = models.ImageField(upload_to='doctors/', blank=True, null=True, verbose_name="Photo")
    phone = models.CharField(max_length=30, blank=True, null=True, verbose_name="Téléphone")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")
    linkedin = models.URLField(blank=True, null=True, verbose_name="Lien LinkedIn")
    twitter = models.URLField(blank=True, null=True, verbose_name="Lien Twitter / X")

    def __str__(self):
        return f"Dr. {self.name} ({self.speciality})"

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titre de l'article")
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Catégorie")
    author = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Signé par (Auteur / Collègue)")
    content = models.TextField(verbose_name="Contenu")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de publication")
    image = models.ImageField(upload_to='articles/', blank=True, null=True, verbose_name="Illustration")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name="Article")
    author_name = models.CharField(max_length=100, verbose_name="Nom du lecteur / collègue")
    content = models.TextField(verbose_name="Commentaire")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date du commentaire")

    def __str__(self):
        return f"Commentaire de {self.author_name} sur {self.article.title}"
