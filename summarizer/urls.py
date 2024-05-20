from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('upload/', views.upload_document, name='upload'),
    path('enter_text/', views.enter_text, name='enter_text'),
    path('enter_url/', views.enter_url, name='enter_url'),
    path('summarize/<int:document_id>/', views.summarize_document, name='summarize_document'),
    path('summarize_text/<int:text_id>/', views.summarize_text, name='summarize_text'),
    path('summarize_url/<int:url_id>/', views.summarize_url, name='summarize_url'),
    path('history/', views.history, name='history'),
    path('summary/<int:summary_id>/', views.summary_detail, name='summary_detail'),
    path('delete_summary/<int:summary_id>/', views.delete_summary, name='delete_summary'),
    path('delete_history/', views.delete_history, name='delete_history'),
]
