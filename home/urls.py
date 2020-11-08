
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),
    path('project/', views.project,  name='project'),
    path('project/<int:tip>/', views.project,  name='project'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blog/<int:pk>', views.AddComment.as_view(), name='add_comment'),
    path('email/', views.AddEmail.as_view(), name='add_email'),
    path('blog/<slug:slug>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('blog/d/<int:category>', views.BlogViewD.as_view(), name='blog-d'),

]

