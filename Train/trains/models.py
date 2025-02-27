from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
from django.utils.timezone import now

User = get_user_model()

# Create your models here.

class Train(models.Model):
    data = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)], unique= True, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trains')
    deadline = models.DateTimeField(blank=True, null=True, default=None)
    upload_at = models.DateTimeField(blank=True, null=True, default=None)
    deadline_failed_time = models.IntegerField( default=0, null=True, blank=True,
                                                validators=[MinValueValidator(0), MaxValueValidator(3)])
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.data}'
    
    # def save(self, *args, **kwargs):
    #     if self.deadline_failed_time == 3:
    #         send_warrning_mail(self.user.email)
    #     if now() > self.deadline:
    #         self.deadline_failed_time += 1
    #         super().save(*args, **kwargs)
    #     else:
    #         super.save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Train'
        verbose_name_plural = 'Trains'
        db_table = 'trains'