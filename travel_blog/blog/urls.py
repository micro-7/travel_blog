from django.urls import path
from django.views.generic import TemplateView
from blog import views 

urlpatterns = [
        path('',views.blogs_view, name= 'index'),
        path('blog/new',views.new_blog, name= 'new_blog'),
        path('blog/detail/<int:id>/',views.detailed_blogs, name= 'detailed_blog'),
        path('search/',views.search_blog,name="search"),
        path('blog/delete/<int:id>/',views.blog_delete, name="blog_delete"),
        path('blog/edit/<int:id>/',views.blog_edit, name="edit_blog"),
        path('category/famous/tourist/places',views.blog_tourist, name="tourist_places"),
        path('category/seven/wonders/of/the/world',views.blog_seven, name="seven_wonder"),
        path('category/top/ten/places',views.blog_top, name="top_10_loca"),
        path('category/religious/places',views.blog_religious, name="religious"),
]