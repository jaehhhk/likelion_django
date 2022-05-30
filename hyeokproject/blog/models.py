from turtle import title
from django.db import models

# Create your models here.
class Blog(models.Model):
    #블로그 글 하나하나에 들어갈 라벨(기능들)
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()

    # 모델 만든 후 python manage.py makemigrations -> python manage.py migrate 
    # (장고에 이 모델 만들어 줬다는거 알려야) 그리고 admin에게도 알려줘야(admin.py로)
    # 런서버한 후 admin 페이지에서 확인 -> 이를 위해 슈퍼유저 만들어줘야

    #admin 페이지에서 글 제목으로 보이게
    def __str__(self):
        return self.title

    # 글자 수 제한
    def summary(self):
        return self.body[:100]