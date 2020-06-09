from django.db import models
import uuid 
from datetime import datetime
from django.utils import timezone
import time
# Create your models here.
class NkDaySign(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    userId = models.CharField(max_length=200)
    userNm = models.CharField(max_length=50)
    signDt = models.DateField()
    signDtm = models.DateTimeField()
class Nksign(models.Model):
    signNo = models.IntegerField('序号', default=0, db_column='col1')
    userId = models.CharField('ID',max_length=200, db_column='col2',blank = True)
    userNm = models.CharField('用户',max_length=200, db_column='col3',blank = True)
    signDt = models.CharField('打卡日期',max_length=200, db_column='col4',blank = True)
    signDtm = models.CharField('打卡时间',max_length=200, db_column='col5',blank = True)
    signPlace = models.CharField('位置',max_length=200, db_column='col6',blank = True)
    rec_crt_tm = models.DateTimeField('数据创建时间',default = timezone.now,db_column='rec_crt_tm')

    def __str__(self):
        return str(self.signDtm)+'-'+self.userNm
    class Meta:
        db_table = 'nk_sign_log' # 通过db_table自定义数据表名