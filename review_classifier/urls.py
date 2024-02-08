from django.urls import path
from . import views

from .views import predict_review


urlpatterns = [
    # path('predict/', views.review_predict, name='review_predict'),
    path('predict/', predict_review, name='predict_review'),

]
