from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from .models import WineReview, Wine
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# ---- 'index view' is the home page view.


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
        reviews = WineReview.objects.filter(wine=self.object)
        context['comments'] = reviews
        context['comment_count'] = reviews.count()
        return context


class WineReviewCreateView(CreateView):
    model = WineReview
    fields = [
        'title',
        'content',
        'rating',
        'featured_image'
    ]  # set the form fields here
    template_name = 'blog/winereview_form.html'
    success_url = "/"
    context_object_name = 'wine_review'

    def form_valid(self, form):
        wine_slug = self.kwargs.get('wine_slug')
        wine = get_object_or_404(Wine, slug=wine_slug)
        form.instance.wine = wine
        form.instance.author = self.request.user   # set form author to user.
        messages.success(
            self.request,
            'Thanks, Your Wine Review has been received and is being '
            'moderated, it should be posted soon!'
        )
        return super().form_valid(form)

    # redirect user to previous page. not working.
    def get_success_url(self):
        return reverse_lazy(
            'wine_detail',
            kwargs={"slug": self.object.wine.slug}
        )

# ----- Editing Wine reviews


class EditWineReviewView(UpdateView):
    model = WineReview
    fields = ['title', 'content', 'rating']
    template_name = 'blog/edit_winereview.html'
    context_object_name = 'wine_review'
    success_url = "/"

    def get_queryset(self):
        # Ensure only the author of the Wine Review can edit it
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    def form_valid(self, form):
        messages.success(
            self.request,
            'Your Wine Review has been updated and is under moderation.'
        )
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect back to the wine detail page after editing
        return reverse_lazy(
            'wine_detail', kwargs={'slug': self.object.wine.slug}
        )

# ----- Deleting Wine Reviews

@login_required
def delete_comment(request, winereview_id):
    review = get_object_or_404(WineReview, id=winereview_id)
    if review.author == request.user:
        review.delete()
        messages.success(request, 'Wine Review deleted successfully!')
    else:
        messages.error(request, 'You can only delete your own review.')
    return redirect('wine_detail', slug=review.wine.slug)
