"""Defines URL patterns for to_do_list_app"""

from django.urls import path

from . import views

app_name = 'to_do_list_app'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #Page to show all the works.
    path('works/', views.works, name='works'),
    #Page to show a specific work.
    path('work/<int:work_id>/', views.work, name='work'),
    # Page to create a new work.
    path('new_work/', views.new_work, name='new_work'),
    #  Page to make new description.
    path('new_description/<int:work_id>/', views.new_description, name='new_description'),
    # page to create new entry.
    path('new_entry/<int:work_id>/', views.new_entry, name='new_entry'),
    # Page to edit a specific description,
    path('edit_description/<int:description_id>/', views.edit_description, name='edit_description'),
    # Page to edit a specific entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # Link to delete a specific work.
    path('delete_work/<int:work_id>/', views.delete_work, name='delete_work'),
    # Link to delete a specific entry.
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
]