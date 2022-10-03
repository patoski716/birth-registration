from django.db import models

# Create your models here.

Gender = (
    ('male', 'MALE'),
    ('female', 'FEMALE'),  
)

class Birth(models.Model):
    gender=models.CharField(max_length=200,null=False,choices=Gender,default='')
    reg_center=models.CharField(max_length=500,default='')
    certificate_no=models.CharField(max_length=500,default='')
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    other_name=models.CharField(max_length=200)
    state_of_origin=models.CharField(max_length=200)
    lga_of_origin=models.CharField(max_length=200)
    residential_address=models.TextField(blank=True)
    date_of_birth=models.DateField()
    mother_name=models.CharField(max_length=200)
    father_name=models.CharField(max_length=200)
    town_of_birth=models.CharField(max_length=200,default='')
    lga_of_birth=models.CharField(max_length=200,default='')
    state_of_birth=models.CharField(max_length=200,default='')
    place_of_issue=models.CharField(max_length=200,default='')
    Authorised_by=models.CharField(max_length=200,default='')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.first_name