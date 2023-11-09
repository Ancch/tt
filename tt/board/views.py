from django.shortcuts import render, redirect
from .models import TT, Comment

# Create your views here.
def index(request):
    return render(request, 'board/index.html', {'recent_tts': TT.objects.all().order_by('-pub_date')[:5]})

def all(request):
    return render(request, 'board/all.html', {'all_tts': TT.objects.all().order_by('-pub_date')})

def new(request):
    if request.method == 'POST':
        tt = TT()
        tt.title = request.POST['title']
        tt.body = request.POST['body']
        tt.save()
        return render(request, 'board/tt.html', {'tt': tt})
    return render(request, 'board/new.html')

def comment(request, slug):
    if request.method == 'POST':
        tt = TT.objects.get(slug=slug)
        comment = Comment()
        comment.post = tt
        comment.text = request.POST['text']
        comment.save()
    return redirect('tt', slug=tt.slug)

def tt(request, slug):
    tt = TT.objects.get(slug=slug)
    comments = tt.comments.filter(post=tt).order_by('-created_date') #! just testing .filter(approved_comment=True)
    return render(request, 'board/tt.html', {'tt': tt, 'comments': comments})