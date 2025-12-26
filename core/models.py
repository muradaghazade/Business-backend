from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon = models.ImageField(upload_to='icons/')

    def __str__(self):
        return self.title
    
class Client(models.Model):
    name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='logos/')

    def __str__(self):
        return self.name
    
class Promo_video(models.Model):
    description = models.TextField()
    video = models.TextField()

    def __str__(self):
        return self.description[:50]
    
class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Portfolio(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/')
    category = models.ManyToManyField(Category, related_name='portfolios')

    def __str__(self):
        return self.title
    
class Pricing(models.Model):
    price = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    description = models.TextField()
    bio_1 = models.CharField(max_length=150)
    bio_2 = models.CharField(max_length=150)
    bio_3 = models.CharField(max_length=150)
    bio_4 = models.CharField(max_length=150)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    comment = models.TextField()
    full_name = models.CharField(max_length=150)
    profession = models.CharField(max_length=150)
    image = models.ImageField(upload_to='reviews/')

    def __str__(self):
        return self.full_name
    
class Blog(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='blogs/')
    author = models.CharField(max_length=150)

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Team_member(models.Model):
    image = models.ImageField(upload_to='team/')
    full_name = models.CharField(max_length=150)
    profession = models.CharField(max_length=150)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.full_name