from django.urls import path,include
from .views import bookshome,createrelated,topicdetail,searchview,unitdetail,subjectdetail


urlpatterns = [
    path('', bookshome),
    path('topic/<slug>', topicdetail,name="topicdetail"),
    path('subject/<q>', subjectdetail,name="subjectdetail"),
    path('subject/unit/<slug>', unitdetail,name="unitdetail"),
    path('related/', createrelated),
    path('search/', searchview),

]

