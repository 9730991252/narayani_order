from django.db import models
from PIL import Image
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    status = models.IntegerField(default=1)
    
class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image1 = models.ImageField(upload_to='item_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='item_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='item_images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='item_images/', blank=True, null=True)
    image5 = models.ImageField(upload_to='item_images/', blank=True, null=True)
    status = models.IntegerField(default=1)
    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)
        
        image1 = Image.open(self.image1.path)
        output_size = (350,350)
        image1.thumbnail(output_size)
        image1.save(self.image1.path)
        
        if self.image2:
            image2 = Image.open(self.image2.path)
            image2.thumbnail(output_size)
            image2.save(self.image2.path)
        
        if self.image3:
            image3 = Image.open(self.image3.path)
            image3.thumbnail(output_size)
            image3.save(self.image3.path)
        
        if self.image4:
            image4 = Image.open(self.image4.path)
            image4.thumbnail(output_size)
            image4.save(self.image4.path)
        
        if self.image5:
            image5 = Image.open(self.image5.path)
            image5.thumbnail(output_size)
            image5.save(self.image5.path)
            
class Price_and_weight(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    price = models.FloatField(default=0)
    weight = models.IntegerField()
    unit = models.CharField(max_length=100)
    status = models.IntegerField(default=1)
    
class Category_item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    status = models.IntegerField(default=1)