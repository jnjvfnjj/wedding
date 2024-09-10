from django.urls import path
from .views import ReviewListCreate
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('reviews/', ReviewListCreate.as_view({'get': 'list', 'post': 'create'}), name='review-list-create'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)