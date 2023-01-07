# Django - URL Shortener
This repository contains a Django URL shortener application. This application is designed as a REST API to create short URL, redirect it to a long URL and keep track of the number of redirects for each URL. 
For example, A short URL `https://short.url/jdj23d` can redirect to the long URL `https://ravkavonline.co.il/he/faq#ravkav-online`.

## Getting Started
1. Clone this repo.
2. Make sure you have installed the relevant [requirements](requirements.txt) inside your working environment. 
3. From the command line, cd into a directory where you have stored the project code, then run the following command `python manage.py migrate` to create the models. <a id="step4"> </a> 
4. Run the development server by inputting this command `python manage.py runserver`.
   You’ll see the following output on the command line:

   ```
   Performing system checks...
   
   System check identified no issues (0 silenced).
   January 04, 2023 - 11:42:12
   Django version 4.1.4, using settings 'example_project.settings'
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CTRL-BREAK.
   ```
5. Open Powershell and run the next command if you want to create a new short url:
   ```
   $ curl -X POST "http://localhost:8000/create"
     -H "Content-Type: application/json" \
     -d '{"url": "https://ravkavonline.co.il"}'
   ```
   It should return the shortened URL, for example, `http://localhost:8000/s/slKj289`.
   When you click on this URL you'll be redirected to `https://ravkavonline.co.il` and the hit counter of this short url will increase by 1. The short URL is unique while different short URLs can reference the same full URL. 

#### In case you just want to add the url shortener application to your own Django project:
1. Clone this repo.
2. Copy the `url_shortener` directory into your project.
3. Add `url_shortener` to your Django project's setting where the INSTALLED_APPS are:
    ```
    INSTALLED_APPS = [
        ...
        'url_shortener',
    ]
    ```
4. Include the url_shortener URLconf in your project `urls.py`:
    ```
    urlpatterns = [
        ...
        path('', include('url_shortener.urls')),
    ]
    ```
5. Go back to step 4 that is written [here](#step4). 

In this repository you can see [example_project](example_project) as a demonstration of how to include this application inside your project. 

Url shortener application includes [unit tests](url_shortener/tests.py). For example, tests for creating and redirecting a short URL and
a test for non-existing short URL. You can run them by this command `python manage.py test url-shortener.tests`.

### Implementation References
- The program is implemented with:
- Python 3.10.5
- Django REST framework 3.14.0
- Django 4.1.4
  - SQLite

