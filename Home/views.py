from django.shortcuts import render
from django.http import JsonResponse
from PIL import Image
import io
import base64
import os
from django.conf import settings
from .models import Image_Model
from django.utils.crypto import get_random_string
def upload_image(request):
    if request.method == 'POST':

        image_data = request.POST.get('image_data')
        # Remove header from dataURL
        image_data = image_data.replace('data:image/png;base64,', '')
        # Convert base64 string to image bytes
        image_bytes = io.BytesIO(base64.b64decode(image_data))
        # Open image from bytes
        image = Image.open(image_bytes).convert('RGB')
        # Save image to server
        image_name = f"webcam_image-{get_random_string(5)}.png"
        image_path = os.path.join(settings.MEDIA_ROOT, image_name)
        image.save(image_path)

        Image_Model.objects.create(image=image_path)
        # os.remove(os.path.join(settings.MEDIA_ROOT, image_name))

        return JsonResponse({'success': True})
    else:
        return render(request, 'HomeApp/insex.html')
