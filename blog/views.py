from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Review, Comment
from .forms import CommentForm, ReviewForm


class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "latest_reviews"

    def get_queryset(self):
        return Review.objects.filter(status=1).order_by("-created_on")[:3]

class ReviewList(generic.ListView):
    queryset = Review.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    queryset = Review.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    user_reviews = post.user_reviews.all().order_by("-created_on")
    user_review_count = post.user_reviews.filter(approved=True).count()
    if request.method == "POST":
        user_review_form = CommentForm(data=request.POST)
        if user_review_form.is_valid():
            user_review = user_review_form.save(commit=False)
            user_review.reviewer = request.user
            user_review.location = post
            user_review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your Wine review has been submitted for approval!🐕')

    user_review_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "user_reviews": user_reviews,
            "user_review_count": user_review_count,
            "user_review_form": user_review_form,
        },
    )


# ----- Editing reviews


def user_review_edit(request, slug, user_review_id):
    queryset = Review.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    user_review = get_object_or_404(Comment, pk=user_review_id)
    user_review_form = CommentForm(data=request.POST, instance=user_review)
    if request.method == "POST":
        if user_review_form.is_valid() and user_review.reviewer == request.user:
            user_review = user_review_form.save(commit=False)
            user_review.location = post
            user_review.approved = False
            user_review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Wine review updated!' 
                'Close this tab and refresh to see your updated review')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating your wine review...')
    context = {
        "post": post,
        "user_review": user_review,
        "user_review_form": user_review_form,
    }

    return render(request, "blog/edit_user_reviews.html", context)


    # ----- Deleting reviews


def user_review_delete(request, slug, user_review_id):
    """
    view to delete user review
    """
    queryset = Review.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    user_review = get_object_or_404(Comment, pk=user_review_id)

    if user_review.reviewer == request.user:
        user_review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))