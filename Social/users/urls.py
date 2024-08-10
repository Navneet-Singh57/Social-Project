from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('login/',views.Login,name="login"),
    path('logout',views.user_logout,name="logout"),
    path('',views.index,name="index"),
    path('password-change',auth_view.PasswordChangeView.as_view(template_name='users/password-change.html'),name="password_change"),
    path('password-change-done',auth_view.PasswordChangeDoneView.as_view(template_name='users/password-change-done.html'),name="password_change_done"),
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='users/password-reset.html'),name="password_reset"),
    path('password-reset-done/',auth_view.PasswordResetDoneView.as_view(template_name='users/password-reset-done.html'),name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>',auth_view.PasswordResetConfirmView.as_view(template_name='users/password-reset-confirm.html'),name="password_reset_confirm"),
    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='users/password-reset-complete.html'),name="password_reset_complete"),
    path('register/',views.register,name="register"),
    path('edit/',views.edit,name="edit"),
    
    
]