from django.shortcuts import redirect, render
from .models import blog
from .forms import BlogForm
from django.contrib import messages

# Create your views here.
def new_blog(request):
    
    if request.method == "POST":
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'New Blog successfully posted.')
            return redirect('new_blog')
        else:
            messages.error(request,'New Blog could not be posted.')
    else:
        form = BlogForm()
    ctx = {
        "form": form,
        "title":"Add new Blog"
    }
    return render(request,"new_blog.html",ctx)

def blogs_view(request):
    blogs = blog.objects.all()
    ctx = {
        'title':"all blogs",
        'blogs': blogs,
    }
    return render(request,"index.html",ctx)

def blog_tourist(request):
    q = "Tourist Places"
    tourist = blog.objects.filter(category__contains=q)
    ctx = {
        'title' : 'Tourist Places',
        'blogs' : tourist,
    }
    return render(request,"tourist_places.html",ctx)

def blog_top(request):
    q = "Top 10 Places"
    tourist = blog.objects.filter(category__contains=q)
    ctx = {
        'title' : 'Top 10 Places',
        'blogs' : tourist,
    }
    return render(request,"top_10_loca.html",ctx)

def blog_seven(request):
    q = "Seven Wonder"
    tourist = blog.objects.filter(category__contains=q)
    ctx = {
        'title' : 'Seven Wonder',
        'blogs' : tourist,
    }
    return render(request,"seven_wonder.html",ctx)

def blog_religious(request):
    q = "Religious Places"
    tourist = blog.objects.filter(category__contains=q)
    ctx = {
        'title' : 'Religious Places',
        'blogs' : tourist,
    }
    return render(request,"religious.html",ctx)

def detailed_blogs(request,id):
    try:
        blogs = blog.objects.get(id=id)
        ctx ={
            'title':"blogs detail",
            'blogs':blogs,
        }
        return render(request,"detailed_blog.html",ctx)
    except:
        return redirect("index")

def search_blog(request):
    q = request.GET.get('query')
    results = blog.objects.filter(title__contains=q)
    ctx = {
        'title':'search results',
        'results':results,
        'query':q,
    }
    return render(request, "search.html",ctx)

def blog_delete(request,id):
    try:
        blog.objects.get(id=id).delete()
        messages.success(request,"Blog deleted successfully")
        return redirect("index")
    except Exception as e:
        print(e)
        messages.error(request,"Blog could not be deleted!")
        return redirect("detailed_blog",id=id)

def blog_edit(request,id):
    try:
        Blog = blog.objects.get(id=id)
        if request.method == "POST":
            form = BlogForm(request.POST,request.FILES,instance=Blog)
            if form.is_valid():
                form.save()
                messages.success(request,"Blog updated successfully")
                return redirect("detailed_blog",id=id)
            else:
                messages.error(request,"Blog update error")
        else:
            form = BlogForm(instance=Blog)
        ctx = {
            'title':"blog edit",
            'form':form,
            'id':id,
        }
        return render(request,"edit_blog.html",ctx)
    except Exception as e:
        print(e)
        return redirect("index")