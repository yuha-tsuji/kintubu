from django.db import models

from accounts.models import CustomUser

# Create your models here.

BUI = (('nume','胸筋'), ('ashi', '脚'), ('nito', '二頭'), ('santo', '三頭'), ('kata', '肩'), ('hara', '腹筋'), ('senaka', '背中'))

class KintoreModel(models.Model):
	bui=models.CharField(
		max_length=50,
		choices = BUI
	)
	menu=models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	kaisu = models.IntegerField()
	setsu = models.IntegerField()
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

	