from django.shortcuts import render, get_object_or_404
from .models import Item

def index(request):
    items = Item.objects.all().order_by('-date')  # newest first
    return render(request, 'web_app/index.html', {"items": items})

def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, "web_app/detail.html", {"item": item})
