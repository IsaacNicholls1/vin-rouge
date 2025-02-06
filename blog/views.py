from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Review, Comment, Wine
from .forms import CommentForm, ReviewForm
from django.views.generic import View
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




# https://ccbv.co.uk/projects/Django/5.0/django.views.generic.edit/CreateView/

class CommentCreateView(CreateView):
    model = Comment
    fields = ['title', "body", 'rating',] # set the form fields here. 
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




# ----- Editing reviews

class EditCommentView(UpdateView):
    model = Comment
    fields = ['title', 'body', 'rating']  # specify the fields you want in the form
    template_name = 'blog/edit_comment.html'
    context_object_name = 'comment'
    success_url = "/"

    def get_queryset(self):
        # Ensure only the author of the comment can edit it
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Your comment has been updated and is under moderation.')
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect back to the wine detail page after editing
        return reverse_lazy('wine_detail', kwargs={'slug': self.object.wine.slug})


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