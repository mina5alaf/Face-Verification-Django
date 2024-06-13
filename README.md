# Face-Verification-Django
  - A system for face verification built in Django. Integrated with an AI model to recognize faces.
    
## User manual:
  ### using Django:
    1- fork this repo
    2- clone it on your local machine
    3- change the working directory to the cloned one using CMD
    4- then go to face_verification directory
    5- in the cmd write: python manage.py runserver

  ### using docker
    1- fork this repo
    2- clone it on your local machine
    3- change the working directory to the cloned one using CMD
    4- run: docker build -t "WRITE IMAGE NAME"
    5- run: docker run "IMAGE NAME"

## Request:
  - using Postman (or any other software), send a request in the body
    json```
"image_url": "C:/Users/minak/Desktop/Face Verification/img2.jpg"
     ```
