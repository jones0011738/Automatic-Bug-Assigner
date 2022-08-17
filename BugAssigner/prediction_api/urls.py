from django.urls import path
from .views import ResultList, RequestList, ResultDetail, RequestDetail
from . import views

urlpatterns = [
        path('request/', RequestList.as_view()),
        path('results/', ResultList.as_view()),
        path('request/<int:pk>', RequestDetail.as_view()),
        path('results/<int:pk>', ResultDetail.as_view()),
        path('', views.prediction),
        ]

