from django.urls import path
from .views import main, article, article_main, article_uniq

urlpatterns = [
    path('',article_main),
    path('5/',article_uniq),
    path('<int:article_id>/',article),
    path('<int:article_id>/<slug:name>',article),
    
]