from django.shortcuts import render

# Create your views here.

def index(request):


    data_dict = {
        "items": [
            {
                "id": 1,
                "title": "Introduction to Django",
                "author": "Anuj",
                "date": "2026-02-09",
                "summary": "Learn the basics of Django framework for building web apps."
            },
            {
                "id": 2,
                "title": "Advanced Python Tips",
                "author": "Aakriti",
                "date": "2026-02-08",
                "summary": "Boost your Python skills with these pro-level tips and tricks."
            },
            {
                "id": 3,
                "title": "Data Science Project",
                "author": "Anuj",
                "date": "2026-02-07",
                "summary": "Step-by-step guide to building a data science project from scratch."
            },
            {
                "id": 4,
                "title": "Machine Learning Basics",
                "author": "Aakriti",
                "date": "2026-02-06",
                "summary": "Understand the core concepts of machine learning and modeling."
            },
            {
                "id": 5,
                "title": "Web Scraping with Python",
                "author": "Anuj",
                "date": "2026-02-05",
                "summary": "Learn how to scrape websites using BeautifulSoup and Selenium."
            },
            {
                "id": 6,
                "title": "Deploy Django App",
                "author": "Aakriti",
                "date": "2026-02-04",
                "summary": "Guide to deploying your Django app on a real server."
            },
            {
                "id": 7,
                "title": "Portfolio Website Tips",
                "author": "Anuj",
                "date": "2026-02-03",
                "summary": "Make a professional portfolio website to showcase your projects."
            }
        ]
    }

    return render(request, 'web_app/index.html',data_dict)
