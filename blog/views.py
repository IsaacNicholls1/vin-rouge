from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from .models import Comment, Wine
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# 'index view' is the home page view.


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
        comments = Comment.objects.filter(wine=self.object)
        context['comments'] = comments
        context['comment_count'] = comments.count()
        return context


class CommentCreateView(CreateView):
    model = Comment
    fields = ['title', "content", 'rating',]  # set the form fields here
    template_name = 'blog/comment_form.html'
    success_url = "/"

# not working, needs looking into

    def form_valid(self, form):
        wine_slug = self.kwargs.get('wine_slug')
        wine = get_object_or_404(Wine, slug=wine_slug)
        form.instance.wine = wine
        form.instance.author = self.request.user   # set form author to user.
        messages.success(
            self.request,
            'Thanks, Your comment has been received and is being moderated, '
            'it should be posted soon!'
        )
        return super().form_valid(form)

    # redirect user to previous page. not working.
    def get_success_url(self):
        return reverse_lazy(
            'wine_detail',
            kwargs={"slug": self.object.wine.slug}
        )

# comment edit/update view.
# https://ccbv.co.uk/projects/Django/5.0/django.views.generic.edit/UpdateView/

# ----- Editing reviews


class EditCommentView(UpdateView):
    model = Comment
    fields = ['title', 'content', 'rating']  # specify the fields you want.
    template_name = 'blog/edit_comment.html'
    context_object_name = 'comment'
    success_url = "/"

    def get_queryset(self):
        # Ensure only the author of the comment can edit it
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    def form_valid(self, form):
        messages.success(
            self.request,
            'Your comment has been updated and is under moderation.'
        )
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect back to the wine detail page after editing
        return reverse_lazy(
            'wine_detail', kwargs={'slug': self.object.wine.slug}
        )

# ----- Deleting comments


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted successfully!')
    else:
        messages.error(request, 'You can only delete your own comments.')
    return redirect('wine_detail', slug=comment.wine.slug)


# def search(request):
#     query = request.GET.get('q')
#     results = Wine.objects.filter(name__icontains=query)
#     return render(request, 'search_results.html', {'results': results})
