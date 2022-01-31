# Django Iran Map Image Gallery
![django-iran-map-image-gallery](https://s6.uupload.ir/files/2022-01-31_092506_659r.png)
## How to run
1. Clone the project
2. Open terminal and create a virtual environment:
<br />```virtualenv venv```
3. Activate virtual environment:
<br />```source venv/bin/activate```
4. Install packages:
<br />```pip install -r requirements.txt```
5. Migrate and create database:
<br />```python manage.py migrate```
6. Collect static files:
<br />```python manage.py collectstatic```
7. Run server:
<br />```python manage.py runserver```
8. You can run tests:
<br />```python manage.py test```
9. Open the browser and browse this URL:
<br />```127.0.0.1:8000```
## Image Gallery
You can upload images related to each state in the admin section and when you click on a state (on the map), the related image gallery will be shown up.
