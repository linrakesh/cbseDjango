from django.urls import path
from . import views

app_name ="sitaji"

urlpatterns = [
    path('', views.indexView.as_view(), name="index"),
    path('<int:pk>', views.detailView.as_view(), name ="detail"),
    path('add-student', views.studentAdd.as_view(), name ="add-student"),
    path('register', views.UserFormView.as_view(), name ="register"),
    path('<int:pk>/update', views.studentUpdate.as_view(), name ="update-student"),
    path('<int:pk>/delete', views.studentDelete.as_view(), name ="delete-student")
]
	