# Face-Verification-Django
  - A system for face verification built in Django. Integrated with an AI model to recognize faces.

# Demo

https://github.com/mina5alaf/Face-Verification-Django/assets/36233029/f07cea2f-e0d0-4e9b-8d6a-24aa9b12052c

# User manual:
  ### Using Django:
  - fork this repo
  - clone it on your local machine
  - change the working directory to the cloned one using CMD
  - then go to face_verification directory
  - install the requirement file `pip install -r requirements.txt`
  - in the cmd write: `python manage.py runserver`
  - Make sure that you are activating a virtual env or conda env
  
  ### Using docker
  - fork this repo
  - clone it on your local machine
  - change the working directory to the cloned one using CMD
  - run: `docker build . -t "WRITE IMAGE NAME"`
  - run: `docker run "IMAGE NAME"`
  
  ## Request:
  - using Postman (or any other software), send a request in the body as

  `{
  "image_url": "ABSOLUTE PATH TO YOUR IMAGE"
  }`
