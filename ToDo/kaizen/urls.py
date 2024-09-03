from django.urls import path 
from .views import  SnippetList, SnippetDetail, UserList, UserDetail
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# urlpatterns = [
#     path('snippets/', snippet_list, name='snippet_list'),
#     path('snippets/<int:pk>/', snippet_detail, name='snippet_detail'),

# ]
urlpatterns = [
    path('snippets/', SnippetList.as_view(), name='snippet_list'),
    path('snippets/<int:pk>/', SnippetDetail.as_view(), name='snippet_detail'),
    path('users/', UserList.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user_detail'),

]
urlpatterns = format_suffix_patterns(urlpatterns)