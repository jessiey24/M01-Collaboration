def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

from django.shortcuts import redirect

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

$ git add .
$ git commit -m "Added views to create/edit blog post inside the site."
$ git push

$ cd ~/<your-pythonanywhere-domain>.pythonanywhere.com
$ git pull

$ workon <your-pythonanywhere-domain>.pythonanywhere.com
(ola.pythonanywhere.com)$ python manage.py collectstatic
