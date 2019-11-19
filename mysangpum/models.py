from django.db import models

# Create your models here.
class Sangdata(models.Model):  # abc.py에서 복사 함 abc.py를 만드는법은 cmd에 python manage.py inspectdb > abc.py을 입력
    code = models.IntegerField(primary_key=True)
    sang = models.CharField(max_length=20, blank=True, null=True)
    su = models.IntegerField(blank=True, null=True)
    dan = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sangdata'