from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Members(models.Model):  # 表示Members繼承自models.Model，也就是Members是一個名為Members的model的意思
    firstname = models.CharField(max_length=255)
    # 為資料表建立名為firstname的字串欄位並限制字串最大長度為255
    lastname = models.CharField(max_length=255)
    # 為資料表建立名為lastname的字串欄位並限制字串最大長度為255
