from django.http import HttpResponse
from django.shortcuts import render

from App.models import Categary, Item, Students


def test(request):
    return render(request, "test.html")

def cate_view(request):

    # cates = Categary.objects.filter(name="饮料")

    cates = Item.objects.all()

    return render(request, "test.html", context={"cates": cates})

def item_view(request):

    print(request.GET)

    cate_id = request.GET.get("cate_id")

    items = Item.objects.all()

    items = items.filter(categary_id=cate_id)

    return render(request, "items.html", {"items": items})

def get_item(request):
    item_id = request.GET.get("item_id")

    try:

        my_item = Item.objects.get(pk=int(item_id))

    except Item.DoesNotExist:

        return HttpResponse("没有")

    return HttpResponse(my_item.name)

def search_item_by_price(request):

    price = request.GET.get("price")

    items = Item.objects.filter(price__in=[price,5])

    return render(request, "items.html", {"items": items})

def search_item_by_name(request):

    name = request.GET.get("i_name")

    items = Item.objects.filter(name__startswith=name)

    return render(request, "items.html", {"items", items})

def search_item_by_time(request):

    my_time = request.GET.get("t")

    items = Item.objects.filter(come_in_time__year=my_time)

    return render(request, "items.html", {"items", items})

def Grade(request):

    return render(request, "grade.html")

def gra_view(request):
    gras = Students.objects.all(),
    return render(request, "grade.html", context={"gras"})