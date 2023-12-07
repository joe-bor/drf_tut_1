from django.urls import path, include
from snippets import views
from rest_framework.routers import DefaultRouter

# Create a router and register our Viewsets with it.
# It'll then take care of the url conf for us
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls))
]


#! This is what it looks like without ViewSets, when we manually configure the urls  
    # urlpatterns = [
    #     path('', views.api_root),
    #     path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    #     path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    #     path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    #     path('users/', views.UserList.as_view(), name='user-list'),
    #     path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail')
    # ]

    # urlpatterns = format_suffix_patterns(urlpatterns)