from django.urls import path
from posts.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CategoryListView, UserPostListView, about, service
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('category/<str:category>/',
         CategoryListView.as_view(), name='category-posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<slug:slug>/update', PostUpdateView.as_view(), name='post-update'),
    path('posts/<slug:slug>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', about, name='about'),
    path('service/', service, name='service')
]

# for adding media file settings
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
