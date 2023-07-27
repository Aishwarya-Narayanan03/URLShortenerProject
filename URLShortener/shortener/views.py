from django.shortcuts import render, get_object_or_404, redirect
import shortuuid
from .models import ShortenedURL

def generate_short_code():
    return shortuuid.uuid()[:8]

def shorten_url(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']
        short_code = generate_short_code()
        ShortenedURL.objects.create(original_url=original_url, short_code=short_code)
        return render(request, 'shortener/success.html', {'shortened_url': short_code})
    return render(request, 'shortener/index.html')

def redirect_to_original(request, short_code):
    shortened_url = get_object_or_404(ShortenedURL, short_code=short_code)
    return redirect(shortened_url.original_url)
