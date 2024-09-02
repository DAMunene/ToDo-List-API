from django.urls import path 
from .views import  SnippetList, SnippetDetail
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# urlpatterns = [
#     path('snippets/', snippet_list, name='snippet_list'),
#     path('snippets/<int:pk>/', snippet_detail, name='snippet_detail'),

# ]
urlpatterns = [
    path('snippets/', SnippetList.as_view(), name='snippet_list'),
    path('snippets/<int:pk>/', SnippetDetail.as_view(), name='snippet_detail'),

]
urlpatterns = format_suffix_patterns(urlpatterns)