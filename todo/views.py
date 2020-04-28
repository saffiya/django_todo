from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.
# All Django view functions have to take a request as an argument 
# because theyre handling the request and then they have to return some form of HTTP response
def get_todo_list(request):
    # Return all of the objects that are stored in the item table
    results = Item.objects.all()
    return render(request, "todo_list.html", {'items': results})
    #The 'items' matches the for {% item in items %} in the html
    
def create_an_item(request):
    if request.method=="POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    else:
        form = ItemForm()

    return render(request, "item_form.html", {'form': form})
    #Used in the item_form.html to add a new item page
    
def edit_an_item(request, id):
    item =get_object_or_404(Item, pk=id)
    
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    else:        
        form = ItemForm(instance=item)
        
    return render(request, "item_form.html", {'form': form})
    # for the todo_list.html edit button

def toggle_status(request, id):
    item =get_object_or_404(Item, pk=id)
    item.done = not item.done
    item.save()
    return redirect(get_todo_list)
    # for the todo_list.html toggle button

    
    
    
    
    
    
    
    
    
    
    
    