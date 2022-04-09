from django.urls import path

from . import views

urlpatterns = [
    #path('notes',views.list,name='notes'),
    path('notes',views.NoteListView.as_view(),name='notes'),
    #path('notes/<int:pk>',views.detail,name='notes.pk')
    path('notes/<int:pk>',views.NotesDetailView.as_view(),name='notes.pk'),
    path('notes/new',views.NoteCreateView.as_view(),name='notes_new'),
    path('notes/<int:pk>/edit',views.NotesUpdateView.as_view(),name='notes.update'),
    path('notes/<int:pk>/delete',views.NotesDeleteView.as_view(),name='notes.delete'),
]

