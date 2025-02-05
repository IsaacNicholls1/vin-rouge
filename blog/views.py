from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Review, Comment, Wine
from .forms import CommentForm, ReviewForm
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

#index view
def index(request):
    return render(request, 'blog/index.html')

class WineList(generic.ListView):
    model = Wine
    template_name = "blog/wine_list.html"
    context_object_name = "wines"
    paginate_by = 6

class WineDetail(generic.DetailView):
    model = Wine
    template_name = "blog/wine_detail.html"
    context_object_name = "wine"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(wine=self.object)
        return context



# class CommentCreateView(CreateView):
#     def post(self, request, wine_slug):
#         wine = get_object_or_404(Wine, slug=wine_slug)
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.review = wine.reviewed_wine.first()  # Assuming one review per wine
#             comment.save()
#             messages.success(request, 'Your comment has been submitted and is awaiting approval!')
#             return redirect('wine_detail', slug=wine_slug)
#         return render(request, 'blog/wine_detail.html', {'form': form, 'wine': wine})

# https://ccbv.co.uk/projects/Django/5.0/django.views.generic.edit/CreateView/
class CommentCreateView(CreateView):
    model = Comment
    fields = ['title','author', 'wine',  "body", 'rating',] # set the form fields here. 
    template_name = 'blog/comment_form.html'
    success_url = "/"

    # not working, needs looking into
    def form_valid(self, form):
        wine_slug = self.kwargs.get('wine_slug')
        wine = get_object_or_404(Wine, slug=wine_slug)
        form.instance.wine = wine
        form.instance.author = self.request.user # set form author to logged in user.
        return super().form_valid(form)
    
    # redirect user to previous page. not working. 
    def get_success_url(self):
        return reverse_lazy('wine_detail', kwargs={"slug": self.object.wine.slug})

# comment edit/update view.
# https://ccbv.co.uk/projects/Django/5.0/django.views.generic.edit/UpdateView/





# class ReviewList(generic.ListView):
#     queryset = Review.objects.filter(status=1)
#     template_name = "blog/review_list.html"
#     paginate_by = 6

# def review_list(request):
#     reviews = Review.objects.filter(status=1).order_by("-created_on")
#     return render(request, "blog/review_list.html", {"reviews": reviews})

# def post_detail(request, slug):
#     queryset = post.objects.filter(status=1)
#     post = get_object_or_404(queryset, slug=slug)
#     user_reviews = post.user_reviews.all().order_by("-created_on")
#     user_review_count = post.user_reviews.filter(approved=True).count()
#     if request.method == "POST":
#         user_review_form = CommentForm(data=request.POST)
#         if user_review_form.is_valid():
#             user_review = user_review_form.save(commit=False)
#             user_review.reviewer = request.user
#             user_review.location = post
#             user_review.save()
#             messages.add_message(
#                 request, messages.SUCCESS,
#                 'Your Wine review has been submitted for approval! 🍷 ')

#     user_review_form = CommentForm()

#     return render(
#         request,
#         "blog/wine_detail.html",
#         {
#             "post": post,
#             "user_reviews": user_reviews,
#             "user_review_count": user_review_count,
#             "user_review_form": user_review_form,
#         },
#     )


# ----- Editing reviews

class EditCommentView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/edit_comment.html'
    context_object_name = 'comment'

    def get_queryset(self):
        # Ensure only the author of the comment can edit it
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    def get_success_url(self):
        # Redirect back to the wine detail page after editing
        return reverse_lazy('wine_detail', kwargs={'pk': self.object.wine.pk})


# def user_review_edit(request, slug, user_review_id):
#     queryset = post.objects.filter(status=1)
#     post = get_object_or_404(queryset, slug=slug)
#     user_review = get_object_or_404(Comment, pk=user_review_id)
#     user_review_form = CommentForm(data=request.POST, instance=user_review)
#     if request.method == "POST":
#         if user_review_form.is_valid() and user_review.reviewer == request.user:
#             user_review = user_review_form.save(commit=False)
#             user_review.location = post
#             user_review.approved = False
#             user_review.save()
#             messages.add_message(
#                 request, messages.SUCCESS,
#                 'Wine review updated!' 
#                 'Close this tab and refresh to see your updated review')
#         else:
#             messages.add_message(
#                 request, messages.ERROR, 'Error updating your wine review...')
#     context = {
#         "post": post,
#         "user_review": user_review,
#         "user_review_form": user_review_form,
#     }

#     return render(request, "blog/edit_user_reviews.html", context)


    # ----- Deleting reviews


# def user_review_delete(request, slug, user_review_id):
#     """
#     view to delete user review
#     """
#     queryset = post.objects.filter(status=1)
#     post = get_object_or_404(queryset, slug=slug)
#     user_review = get_object_or_404(Comment, pk=user_review_id)

#     if user_review.reviewer == request.user:
#         user_review.delete()
#         messages.add_message(request, messages.SUCCESS, 'Review deleted!')
#     else:
#         messages.add_message(
#             request, messages.ERROR, 'You can only delete your own reviews!')

#     return HttpResponseRedirect(reverse('wine_detail', args=[slug]))