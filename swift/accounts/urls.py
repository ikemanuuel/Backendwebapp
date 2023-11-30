
from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('user-create', views.UserCreateView.as_view(), name='user-create'),
    path('me', views.UserProfileView.as_view(), name='me'),
    path('account-requests', views.FetchAccountRequest.as_view(), name='account-requests'),
    path('registered-accounts', views.FetchRegisteredAccount.as_view(), name='registered-accounts'),
    path('accept-account-request/<int:pk>/', views.AcceptAccountRequest.as_view(), name='accept-account-request'),
    path('decline-account-request/<int:pk>/', views.DeclineAccountRequest.as_view(), name='decline-account-request'),
    path('activate-account/<int:pk>/', views.ActivateAccount.as_view(), name='activate-account'),
    path('deactivate-account/<int:pk>/', views.DeactivateAccount.as_view(), name='deactivate-account'),
]