from django.db import models

class Doctors(models.Model):
    code        = models.CharField(max_length=20)
    first_name  = models.CharField(max_length=30)
    last_name   = models.CharField(max_length=30)
    certify     = models.CharField(max_length=30)
    job_code    = models.CharField(max_length=15,blank=True)
    ssn         = models.CharField(max_length=16)
    email       = models.EmailField()
    phone_num   = models.CharField(max_length=11)
    work_days   = models.TextField(blank=True)
    notes       = models.TextField(blank=True)
    spcial      = models.CharField(max_length=30)
    late_time   = models.CharField(max_length=30,blank=True)
    rate        = models.CharField(max_length=2,choices=((str(i),str(i)) for i in range(1,11)))
    def __str__(self):
        return f"{self.first_name} {self.last_name} - ({self.code})"
    class Meta:
        verbose_name_plural = 'Doctors'
    
class Students(models.Model):
    doctor      = models.ForeignKey(Doctors, on_delete=models.CASCADE,blank=True)
    hall        = models.ForeignKey('Halls', on_delete=models.CASCADE,blank=True)
    code        = models.CharField(max_length=10)
    full_name   = models.CharField(max_length=200)
    group       = models.CharField(max_length=15,choices=((f"Group-{i}",f"Group-{i}") for i in ["A","B","C"]))
    group_split = models.CharField(max_length=15,choices=((f"G-{i}",f"G-{i}") for i in range(1,9) ))
    
    def __str__(self):
        return f"{self.full_name} - ({self.code})"
    class Meta:
        verbose_name_plural = 'Students'
        
class Halls(models.Model):
    doctor       = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    code         = models.CharField(max_length=30)
    stage        = models.CharField(max_length=30)
    bulding      = models.CharField(max_length=5)
    spcial       = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.code} - ({self.bulding})"
    class Meta:
        verbose_name_plural = 'Halls'