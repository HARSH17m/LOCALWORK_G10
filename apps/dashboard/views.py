from django.shortcuts import render
from .models import Post
# Create your views here.
def insert(request):
    if request.method == 'POST':
        image_=request.FILES['post_image']
        title_=request.POST['title']
        context_=request.POST['context']
        new_post=Post.objects.create(
            image=image_,
            title=title_,
            context=context_
        )
        new_post.save()
    return render(request,'dashboard/insert.html')

def show(request):
    posts=Post.objects.all()
    context={
        'posts':posts
    }
    return render(request,'dashboard/show.html',context)
