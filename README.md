# Face-Verification-Django
  - A system for face verification built in Django. Integrated with an AI model to recognize faces.

# Demo
[![Watch the video](https://i.sstatic.net/Vp2cE.png)](https://drive.google.com/file/d/1gyFmGWdkvYhsho1C8Kd1PTOWCozIzFHP/view?usp=sharing)

    
# User manual:
  ### Using Django:
  - fork this repo
  - clone it on your local machine
  - change the working directory to the cloned one using CMD
  - then go to face_verification directory
  - in the cmd write: `python manage.py runserver`
  
  ### Using docker
  - fork this repo
  - clone it on your local machine
  - change the working directory to the cloned one using CMD
  - run: `docker build -t "WRITE IMAGE NAME"`
  - run: `docker run "IMAGE NAME"`
  
  ## Request:
  - using Postman (or any other software), send a request in the body as
  
  `{
  "image_url": "ABSOLUTE PATH TO YOUR IMAGE"
  }`
