django-admin startproject mywebsite
cd mywebsite
python manage.py startapp pages
pages/urls.py
from django.urls import path
from . import views
urlpatterns = [
 path('', views.home, name='home'),
 path('about/', views.about, name='about'),
 path('contact/', views.contact, name='contact'),
]
Pages/views.py
from django.shortcuts import render
def home(request):
 return render(request, 'home.html')
def about(request):
 return render(request, 'about.html')
def contact(request):
 return render(request, 'contact.html')
pages/templates/layout.html
<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>{% block title %}My Website{% endblock %}</title>
 <style>
 /* Basic CSS for layout */
 body {
 font-family: Arial, sans-serif;
 margin: 0;
 padding: 0;
 box-sizing: border-box;
 }
 header {
 background-color: #333;
color: #fff;
 padding: 10px 0;
 text-align: center;
 }
 nav {
 display: flex;
 justify-content: center;
 }
 nav a {
 color: #fff;
 text-decoration: none;
 padding: 10px 20px;
 }
 nav a:hover {
 background-color: #555;
 }
 footer {
 background-color: #333;
 color: #fff;
 text-align: center;
 padding: 10px 0;
 position: absolute;
 bottom: 0;
 width: 100%;
 }
 </style>
</head>
<body>
 <header>
 <h1>My Website</h1>
 <nav>
 <a href="{% url 'home' %}">Home</a>
 <a href="{% url 'about' %}">About Us</a>
 <a href="{% url 'contact' %}">Contact Us</a>
 </nav>
 </header>
 <div id="content">
 {% block content %}
 <!-- This block will be overridden by specific content of each page -->
 {% endblock %}
 </div>
 <footer>
 <p>&copy; {% now 'Y' %} My Website | Developed by Your Name</p>
 </footer>
</body>
</html>
pages/templates/home.html
{% extends 'layout.html' %}
{% block title %}Home - My Website{% endblock %}
{% block content %}
 <h2>Welcome to Our Home Page!</h2>
 <p>This is the Home Page content of My Website.</p>
 <!-- Add more content specific to the home page here -->
{% endblock %}
pages/templates/about.html
{% extends 'layout.html' %}
{% block title %}About Us - My Website{% endblock %}
{% block content %}
 <h2>About Us</h2>
 <p>Learn more about our company or organization.</p>
 <!-- Add more content specific to the about page here -->
{% endblock %}
pages/templates/contact.html
{% extends 'layout.html' %}
{% block title %}Contact Us - My Website{% endblock %}
{% block content %}
 <h2>Contact Us</h2>
 <p>Get in touch with us using the form below or via other contact information.</p>
 <!-- Add more content specific to the contact page here -->
{% endblock %}
Mywebsite/urls.py
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
 path('admin/', admin.site.urls),
 path('', include('pages.urls')), # Include the URLs from the pages app
]
mywebsite/settings.py
add--- import os
'DIRS': [os.path.join(BASE_DIR, 'pages/templates')], #replacet this in templates
To run python manage.py runserver
http://127.0.0.1:8000/home