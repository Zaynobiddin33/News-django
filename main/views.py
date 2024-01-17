from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . import models

def index(request):
    context = {}
    return render(request, 'front/index.html', context)


def allnews(request):
    context = {}
    return render(request, 'front/allnews.html', context)

def category(request):
    context = {}
    return render(request, 'front/category.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        body = request.POST['body']
        models.Form.objects.create(
            name = name,
            email = email,
            body = body
        )
        return redirect('contact')
    return render(request, 'front/contact.html')

def details(request):
    context = {}
    return render(request, 'front/details.html', context)

# dashboard

def dashboard(request):
    users = User.objects.all().count()
    news = models.Item.objects.filter(is_active=True).count()
    regions = models.Region.objects.all().count()
    category = models.Category.objects.all().count()

    context = {
        'users':users,
        'news':news,
        'regions':regions,
        'category':category
    }

    return render(request, 'dashboard/index.html', context)


def create_region(request):
    if request.method == 'POST':
        models.Region.objects.create(
            name=request.POST['name']
        )
        return redirect('regions')
    return render(request, 'dashboard/region/create.html')


def regions(request):
    regions = models.Region.objects.all().order_by('name')
    return render(request, 'dashboard/region/list.html', {'regions':regions})



def region_update(request, id):
    region = models.Region.objects.get(id=id)
    if request.method == 'POST':
        region.name = request.POST['name']
        region.save()
        return redirect('regions')
    return render(request, 'dashboard/region/update.html', {'region':region})


def region_delete(request, id):
    models.Region.objects.get(id=id).delete()
    return redirect('regions')

#category CRUD

def create_category(request):
    if request.method == 'POST':
        models.Category.objects.create(
            name=request.POST['name']
        )
        return redirect('categories')
    return render(request, 'dashboard/category/create.html')

def categories(request):
    categories = models.Category.objects.all()
    return render(request, 'dashboard/category/list.html', {'categories':categories})

def category_update(request, id):
    category = models.Category.objects.get(id=id)
    if request.method == 'POST':
        category.name = request.POST['name']
        category.save()
        return redirect('categories')
    return render(request, 'dashboard/category/update.html', {'category':category})


def category_delete(request, id):
    models.Category.objects.get(id=id).delete()
    return redirect('categories')

# items

def create_item(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST["body"]
        category = models.Category.objects.get(id=request.POST['category_id'])
        region = models.Region.objects.get(id=request.POST['region_id'])  
        image = request.FILES['image']

        models.Item.objects.create(
            title=title,
            body=body,
            category=category,
            region=region,
            image=image
        )

    context = {
        "categories": models.Category.objects.all(),
        "regions": models.Region.objects.all()
    }

    return render(request, 'dashboard/news/create.html', context)


def items(request):
    items = models.Item.objects.all()
    context = {
        "items" : items
    }
    return render(request, "dashboard/news/list.html", context)

def update_item(request, id):
    item = models.Item.objects.get(id=id)
    if request.method == 'POST':
        category = models.Category.objects.get(id=request.POST['category_id'])
        region = models.Region.objects.get(id=request.POST['region_id'])  
        item.title = request.POST['title']
        item.body = request.POST['body']
        item.category = category
        item.region = region
        image = request.FILES.get("image")
        if image:
            item.image = image
        item.save() 
        return redirect('items')
    context = {
        "item" : item,
        "categories": models.Category.objects.all(),
        "regions": models.Region.objects.all()
    }
    return render(request, 'dashboard/news/update.html', context)

def delete_item(request, id):
    models.Item.objects.get(id=id).delete()
    return redirect('items') 

# messages
def messages(request):
    messages = models.Form.objects.all().order_by( 'status', '-sent_time')
    context = {
        'messages' : messages
    }
    return render(request, 'dashboard/message/list.html', context)

def update_status(request, id):
    message = models.Form.objects.get(id=id)
    if request.method == "POST":
        message.status = request.POST['status']
        message.save()
        return redirect('messages')
    context = {
        'message' : message
    }
    return render(request, 'dashboard/message/update.html', context)
