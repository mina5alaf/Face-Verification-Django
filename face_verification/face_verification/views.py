import cv2
import numpy as np
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from sklearn.preprocessing import normalize
from django.http import JsonResponse

import matplotlib.pyplot as plt

#from .predict import make_prediction  # This is a hypothetical function you'd create

@csrf_exempt  # Disable CSRF for simplicity, consider CSRF protection for production
def predict_image_url(request):
    if request.method == 'POST':
        json_data = json.loads(str(request.body, encoding='utf-8'))
        if json_data:
            image_url = json_data["image_url"]
            img = plt.imread(image_url)
            img = cv2.resize(img, (38, 38))
            #img = cv2.normalize(img, None, alpha=0, beta=1, norm_type=cv2.NORM_RELATIVE)
            img = img / img.max()
            print(img)
            img = np.asarray(img)[None, ...]
            results_ort = settings.SESS.run(['sequential_1'], {"image": img.astype(np.float32)})
            mse_lst = []
            for i in range(len(settings.X_FACES)):
                mse_lst.append(settings.MSE(settings.X_FACES[i], np.array(results_ort)))
                
            mse_lst = np.array(mse_lst)
            pred = settings.FACES.target_names[np.array(settings.Y_FACES[mse_lst.argmin()])]
            return JsonResponse({'prediction': pred})
        else:
            return JsonResponse({'error': 'No image URL provided.'}, status=400)
    
    return JsonResponse({'error': 'POST request required.'}, status=400)


