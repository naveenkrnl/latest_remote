from django.urls import path,include
from .views import bookshome,createrelated,TopicDetailView


urlpatterns = [
    path('', bookshome),
    path('topic/<slug>', TopicDetailView.as_view(),name="topicdetail"),
    path('related/', createrelated),

]

