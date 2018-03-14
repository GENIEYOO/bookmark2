from django.db import models

# Create your models here.
#데이터 베이스에 어떤 자료를 어떻게 저장할 것인가
#각 모델에 관련된 기능들을 만드는 부분

#ORM 직접접근이아니라 모델을 클래스로 제공되는 모듈을 제공
#models.model을 상속받으면 데이터베이스 제어기능이 다 포함되어있다.
class Bookmark(models.Model):
    #필드를 써줌
    #컬럼명 = 모델.필드종류(길이)
    #필드 종류의 목적
    #1.데이터페이스에 어떤 식으로 데이터를 저장할 것인가?
    #2.사용자의 입력을 받을 때 어떤 form 태그를 보여줄 것이냐
    #2-1 입력폼의 제한 사항, 유효성검사
    
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    # 모델을 다룰 때 옵션값을 지정해줌
    class Meta:
        ordering = ['site_name']
        #오름차순
    def __str__(self):
        return self.site_name

    def get_absolute_url(self):
        pass
    #객체에게 너 자신의 주소는 뭐냐?






