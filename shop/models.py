from django.db import models
from django.urls import reverse
from django.utils import timezone
from phone_field import PhoneField

class PublisherManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(status=Product.Status.Published)


class Category(models.Model):
    name=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250, unique=True)
    description=models.CharField(max_length=300)


    def __str__(self):
        return self.name






class Product(models.Model):

    class Status(models.TextChoices):
        Draft="DF", "Draft"
        Published="PB", "Published"


    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    body=models.TextField()
    image=models.ImageField(upload_to='product_picture/image')
    price=models.DecimalField(max_digits=10, decimal_places=3, default=0)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    published_time=models.DateTimeField(default=timezone.now)
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=2, choices=Status.choices, default=Status.Draft)


    objects=models.Manager()
    published=PublisherManager()


    class Meta:
        ordering=["-published_time"]


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail_view", args=[self.slug])



class Client(models.Model):


    class Status(models.TextChoices):
        New="YC", "YANGI BUYURTMALAR"
        Active="OC", "DASTAVKAGA TAYYOR "
        Later="KC", "Keyin oladi"
        Canceled="AC", "Atkaz"


    class Region(models.TextChoices):
        NotREgion="NR", "----"
        Tashkent="TSH", "Tashkent shahri"
        Tashkentv="TV", "Tashkent viloayti"
        Samarqand="SM", "Samarqand"
        Buxoro="SD", "Buxoro"
        Navoiy="NY", "Navoiy"
        Jizzax="JX", "Jizzax"
        Andijon="AN", "Andijon"
        Fargona="FC", "Farg'ona"
        Namangan="NG", "Namangan"
        Sirdaryo="SR", "Sirdaryo"
        Qaraqalpogiston="QR", "Qaraqalpog'iston"
        Xorazm="XC", "Xorazm"
        Qashqadaryo="KC", "Qashqadaryo"
        Surxondaryo="SC", "Surxondaryo"

    name=models.CharField(max_length=250)
    phone=models.CharField(max_length=200)
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='clients')
    address=models.CharField( choices=Region.choices,max_length=250, default="address")
    count=models.IntegerField(default=1)
    price=models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description=models.TextField(default='')
    published_time=models.DateTimeField(default=timezone.now)
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=2, choices=Status.choices, default=Status.New)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.product.title

    # def get_absolute_url(self):
    #     return reverse("home_page_view", args=[self.slug])

class ClientModel(models.Model):
    name=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)


    def __str__(self):
        return self.name

