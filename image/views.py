from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.http import require_GET

from .models import Image


@require_GET
@login_required
def list(request):

    images = Image.objects.all()

    context = {
            'images': images,
        }

    return render(request, 'image/list.html', context)
