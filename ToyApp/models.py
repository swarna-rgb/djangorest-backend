from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.dispatch import receiver
import uuid
import string
import random
from django.urls import reverse

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class Product(models.Model):
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True,null=True,blank=True)

    @property
    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.slug)])

    # def unique_slug_geneator(self):
    #     #instance = self.__class__
    #     print('toy name', self.name)
    #     original_slug = slugify(self.name)
    #     print('original_slug', original_slug)
    #     # check original_slug exists in db
    #     # klass = instance.__class__
    #     if Product.objects.filter(slug=original_slug).exists():
    #         # if yes, generate unique slug
    #         unique_slug = "{}-{}".format(random_string_generator(), original_slug)
    #         print(unique_slug)
    #         original_slug = unique_slug
    #     # else use the original slug
    #     return original_slug


    # def save(self, *args, **kwargs):
    #     self.slug = self.unique_slug_geneator()
    #     super(Product, self).save(*args, **kwargs)

@receiver(pre_save, sender=Product)
def generate_slug(sender, instance, *args, **kwargs):
    print(repr(instance))
    if not instance.slug:
        instance.slug = unique_slug_geneator(instance)
        print("slug created")
pre_save.connect(generate_slug, sender=Product)

def unique_slug_geneator(instance):
    print(repr(instance))
    original_slug = slugify(instance.name)
    print('original_slug',original_slug)
    #check original_slug exists in db
    klass = instance.__class__
    if klass.objects.filter(slug=original_slug).exists():
        #if yes, generate unique slug
        unique_slug = "{}-{}".format(random_string_generator(), original_slug)
        original_slug = unique_slug
    #else use the original slug
    return original_slug

class Toy(models.Model):
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    #slug = models.SlugField(unique=True)


# many toys -> one user
# If i delete toy, user is not deleted
# If i pull the user, all of that user's toys should be displayed

# class ToyStoreAPIUser(AbstractUser):
#     is_manager = models.BooleanField(null=True, blank=True)
#     is_employee = models.BooleanField(null=True, blank=True)
#     def __str__(self):
#         return self.username

# class Manager(models.Model):
#     user = models.OneToOneField(ToyStoreAPIUser,related_name='related_mtoys', on_delete=models.CASCADE)
#     fname = models.CharField(max_length=30)
#     lname = models.CharField(max_length=30)
#     def __str__(self):
#         return self.username
#
# class Employee(models.Model):
#     user = models.OneToOneField(ToyStoreAPIUser,related_name='related_etoys', on_delete=models.CASCADE)
#     fname = models.CharField(max_length=30)
#     lname = models.CharField(max_length=30)
#     def __str__(self):
#         return self.username

