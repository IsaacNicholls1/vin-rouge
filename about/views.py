from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About, WineReviewSubmission
from .forms import NewsletterForm, WineReviewSubmissionForm


def about_me(request):
    """
    Renders the most recent info on the website author, and allows users to request A newsletter.
    Displays an instance of :model:`about.About`.
    """

    if request.method == "POST":
        newsletter_form = NewsletterForm(data=request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            messages.add_message(request, messages.SUCCESS, "Request received! Your personal newsletter will be with you within 3 working days!  respond within 2 working days.")

    about = About.objects.all().order_by('-updated_on').first()
    newsletter_form = NewsletterForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "newsletter_form": newsletter_form
        },
    )

def contact(request):
    if request.method == 'POST':
        form = WineReviewSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has been submitted!')
            return redirect('contact')
    else:
        form = WineReviewSubmissionForm()
    return render(request, 'about/contact.html', {'form': form})