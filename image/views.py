import os
from base64 import b64decode

from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST

from .models import Image


@require_GET
@login_required
def list(request):

    images = Image.objects.all()

    context = {
            'images': images,
        }

    return render(request, 'image/list.html', context)


@require_POST
@login_required
def upload(request):

    img_b64 = request.POST.get('base64_image')

    if img_b64:
        prefix, data = img_b64.split(';base64,', 1)
        data = ContentFile(b64decode(data))

        # TODO resize image and convert to png
        if prefix.endswith('image/png'):
            filename = os.urandom(8).hex() + '.png'
        if prefix.endswith('image/jpeg'):
            filename = os.urandom(8).hex() + '.jpg'

        img = Image()
        img.uploaded_file.save(filename, data, save=True)
        img.save()

    return redirect('image-list')


@require_GET
@login_required
def delete(request, pk):

    img = get_object_or_404(Image, pk=pk)
    img.uploaded_file.delete(save=False)
    img.delete()

    return redirect('image-list')
