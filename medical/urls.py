from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('login',views.userlogin,name="login"),
    path('logout',views.logout,name="logout"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('home/',views.home,name="userhome"),
    path('medicine/',views.Medicine,name="medicine"),
    path('order/',views.myorder,name="order"),
    path('feedback/',views.feedback,name="feedback"),
    path('feedbackshow/',views.feedbackdetail,name="feedbackdetail"),
    path('signup/',views.signup,name="signup"),
    path("search/",views.search,name="search"),
   path('show/',views.show,name="orderdetails"),
    path('edit/<int:id>', views.edit,name="edit"),  
    path('update/<int:id>', views.update), 
    path("show/<id>",views.deleteOrder,name="deleteOrder"),
    path('delete/<int:id>',views.drop), 





    
]