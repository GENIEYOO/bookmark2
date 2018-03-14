from django.contrib import admin

# Register your models here.
#작성한 모델을 관리자 페이지에서 다룰 수 있도록 등록하는 부분
#모델을 다루는데 관련된 옵션값을 설정

from .models import Bookmark
#현재 앱의 models.py에서 Bookmark만 불러와라

admin.site.register(Bookmark)

