from django.db import models
from django.utils.text import slugify

# Create your models here.

class Parent(models.Model):
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    father_mobile = models.CharField(max_length=100)
    father_email=models.CharField(max_length=100)
    mother_name=models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)
    mother_mobile = models.CharField(max_length=100)
    mother_email = models.CharField(max_length=100)
    present_address = models.TextField()
    permanent_address = models.TextField()
    
    def __str__(self) -> str:
        return f"(self.father_name) & (self.mother_name)"
    
def generate_unique_slug(instance, new_slug=None):
        slug = new_slug or slugify(instance.first_name + "-" + instance.last_name)
        Klass = instance.__class__
        qs_exists = Klass.objects.filter(slug=slug).exists()
        if qs_exists:
            # Append a unique number if slug already exists
            slug = f"{slug}-{instance.id or Klass.objects.count() + 1}"
        return slug
    
class Student(models.Model):
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    student_id= models.CharField(max_length=100)
    gender= models.CharField(max_length=10,choices=[('male','male'),('female','female'),('others','others')])
    date_of_birth=models.DateField()
    student_class=models.CharField(max_length=100)
    religion = models.CharField(max_length=20)
    joining_date = models.DateField()
    mobile_number=models.CharField(max_length=15)
    admission_number=models.CharField(max_length=15)
    section = models.CharField(max_length=15)
    student_image =models.ImageField(upload_to='student/',blank=True)
    parent= models.ForeignKey(Parent,on_delete=models.CASCADE)
    slug=models.SlugField(max_length=255,unique=True,blank=True)
    
    

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug= generate_unique_slug(self)
        super(Student,self).save(*args,**kwargs)
    
    def __str__(self) -> str:
        return f"(self.first_name)  (self.last_name) (self.student_id)"
    
    
    