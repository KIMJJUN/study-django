from django.db import models
from django.urls import reverse
# Create your models here.

# 글의 분류(입양홍보, 길냥이 정보)
class Category(models.Model):
    name = models.CharField(max_length=50, help_text="글의 분류를 입력하세요. (ex: 입양홍보)")

    def __str__(self):
        return self.name

# 글(제목, 작성일, 대표이미지, 내용, 분류)
class Post(models.Model):
    title = models.CharField(max_length=200)
    title_image = models.ImageField(blank=True)
    content = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now_add=True)
    #하나의 글이 여러가지 분류에 해당될 수 있다. (ex. 입양, 정보, 커뮤니티) 하나의 카테고리에 여러가지 글이 포함될 수 있다(정보 카테고리에 글 10개)
    category = models.ManyToManyField(Category, help_text="글의 분류를 설정하세요.")

    def __str__(self):
        return self.title

    # 1번 글 => post/1
    def get_absolute_url(self):
        return reverse("post", args=[str(self.id)])
    
    def is_content_more100(self):
        return len(self.content) > 100

    def get_content_under100(self):
        return self.content[:100]
    
    def is_content_more300(self):
        return len(self.content) > 300

    def get_content_under300(self):
        return self.content[:300]