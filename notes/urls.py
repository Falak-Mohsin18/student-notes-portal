from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.landing_page,
        name='landing'
    ),

    path(
        'register/',
        views.register_view,
        name='register'
    ),

    path(
        'login/',
        views.login_view,
        name='login'
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),
    
    path(
        'profile/',
        views.profile,
        name='profile'
    ),

    path(
        'notes/',
        views.browse_notes,
        name='browse_notes'
    ),

    path(
        'upload/',
        views.upload_note,
        name='upload'
    ),

    path(
        'my-notes/',
        views.my_notes,
        name='my_notes'
    ),

    path(
        'edit/<int:id>/',
        views.edit_note,
        name='edit_note'
    ),

    path(
        'delete/<int:id>/',
        views.delete_note,
        name='delete_note'
    ),
]