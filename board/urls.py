from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, upgrade_me, RegistrationView, AccountActivationView

urlpatterns = [
    path('', PostList.as_view(), name='posts'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('upgrade/', upgrade_me, name='upgrade'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('activate/<str:uidb64>/<str:token>/', AccountActivationView.as_view(), name='account_activation'),
]



