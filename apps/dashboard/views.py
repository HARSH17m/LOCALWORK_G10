from django.shortcuts import render,redirect
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

def delete_post(request,post_id):
    delete_post=Post.objects.get(id=post_id)
    delete_post.delete()
    return redirect('show')

def update_post(request,post_id):
    update_post=Post.objects.get(id=post_id)
    if request.method=='POST':
        if request.FILES:
            update_post.image=request.FILES['post_image']
        update_post.title=request.POST['title']
        update_post.context=request.POST['context']
        update_post.save()
        return redirect('show')
    context={
        'post':update_post
    }
    return render(request,'dashboard/update_post.html',context)