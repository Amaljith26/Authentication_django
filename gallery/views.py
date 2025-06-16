from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from .forms import ImageUploadForm
from .models import UploadedImage
from django.conf import settings
import os

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.save(commit=False)
            img.user = request.user
            img.save()
            return redirect('view-images')
    else:
        form = ImageUploadForm()
    return render(request, 'gallery/upload.html', {'form': form})

@login_required
def view_images(request):
    images = UploadedImage.objects.filter(user=request.user)
    return render(request, 'gallery/view.html', {'images': images})

@login_required
def protected_media(request, path):
    try:
        img = UploadedImage.objects.get(image=path)
        if img.user != request.user:
            return Http404("Permission denied")
    except UploadedImage.DoesNotExist:
        raise Http404("Image not found")

    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if not os.path.exists(file_path):
        raise Http404("File does not exist")

    return FileResponse(open(file_path, 'rb'))

from django.shortcuts import render

def landing_page(request):
    return render(request, 'gallery/landing.html')
