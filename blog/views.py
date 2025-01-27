from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Review, Comment
from .forms import CommentForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog/index.html')
    
def index(request):
    posts = Review.objects.filter(status=1)
    return render(request, 'index.html', {'posts': posts})
    
# Create your views here.
class ReviewList(generic.ListView):
    queryset = Review.objects.filter(status=1)
    template_name = "blog/review_list.html"
    paginate_by = 6


def post_detail(request, slug):
    queryset = Review.objects.filter(status=1)
    review = get_object_or_404(queryset, slug=slug)
    comments = review.comments.all().order_by("-created_on")
    comment_count = review.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.review = review
            comment.save()
            
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
    )
    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": review,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )

def comment_edit(request, slug, comment_id):
    queryset = Review.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
    else:
        comment_form = CommentForm(instance=comment)

    return render(
        request,
        'blog/comment_edit.html',
        {
            'comment_form': comment_form,
            'post': post,
        },
    )

def comment_delete(request, slug, comment_id):
    queryset = Review.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
