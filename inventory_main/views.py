from django.shortcuts import render, redirect
from .models import Item
from django.http import JsonResponse

def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list' : item_list
    }
    return render(request,'index.html',context)


def create_item(request):
    if request.method == 'POST':
        item_type = request.POST.get('itemType')
        brand_name = request.POST.get('brandName')
        model = request.POST.get('model')
        quantity = request.POST.get('quantity')
        serial_number = request.POST.get('serialNumber')
        description = request.POST.get('description')

        item = Item(
            itemType=item_type,
            brandName=brand_name,
            model=model,
            quantity=quantity,
            serialNumber=serial_number,
            description=description
        )
        item.save()
        return redirect('index')
    
    else:
        pass
    item_list = Item.objects.all()
    context = {
        'item_list' : item_list
    }

    return render(request,'index.html',context)


def delete_item(request,myid):
    item = Item.objects.get(id = myid)
    item.delete()
    return redirect('index')


def edit_item(request, myid):
    selected_item = Item.objects.get(id=myid)
    item_list = Item.objects.all()
    context = {
        'selected_item': selected_item,
        'item_list': item_list,
        'myid': myid,  # Include the ID in the context
    }

    return render(request, 'index.html', context)


def update_item(request, myid):
    item = Item.objects.get(id = myid)
    item.name = request.POST['name']
    item.description = request.POST['description']
    item.save()
    return redirect('index',)


   