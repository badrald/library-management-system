from django.db import models
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name



class Book(models.Model):
    status_books=[
        ("available","available"),
        ("retailed","retailed"),
        ('sold','sold'),
        ("outOfStock","Out Of Stock"),]
    status_active=[
        (True,"active"),
        (False,"Not active"),
        (False,"Out of Sotck")]

    title=models.CharField(max_length=250)
    author=models.CharField(max_length=50)
    description=models.TextField(blank=True, null=True)
    photo_book=models.ImageField(upload_to="photos/books/%y%m%d",null=True,blank=True)
    pages=models.IntegerField(null=True,blank=True)
    price=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    retail_price=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    active=models.BooleanField(default=True,choices=status_active)
    status=models.CharField(max_length=50,choices=status_books)
    category=models.ForeignKey(Category,on_delete=models.PROTECT,null=True,blank=True)
    amount= models.IntegerField(default=1)
    def __str__(self) -> str:
        return self.title
    class Meta:
        db_table = ''
        managed = True
        ordering = ['-id']



