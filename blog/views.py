from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from .models import Review, Comment
from .forms import CommentForm, ReviewForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog/index.html')
    
def index(request):
    posts = Review.objects.filter(status=1)
    return render(request, 'blog/index.html', {'posts': posts})
    
# Create your views here.
class ReviewList(View):
    def get(self, request, *args, **kwargs):
        region = request.GET.get('region', 'all')
        if region == 'all':
            reviews = Review.objects.filter(status=1).order_by('-created_on')
        else:
            reviews = Review.objects.filter(status=1, region=region).order_by('-created_on')

        paginator = Paginator(reviews, 5)  # Show 5 reviews per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        form = ReviewForm()
        return render(request, 'blog/review_list.html', {'page_obj': page_obj, 'form': form, 'region': region})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            return redirect('index')
        reviews = Review.objects.filter(status=1).order_by('-created_on')
        paginator = Paginator(reviews, 5)  # Show 5 reviews per page

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'blog/review_list.html', {'page_obj': page_obj, 'form': form})


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
            return redirect('post_detail', slug=review.slug)
    else:
        comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "review": review,
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
