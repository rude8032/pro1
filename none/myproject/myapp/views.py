from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import InventoryItemForm
from .models import InventoryItem, Item
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
import logging

logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info("User registered successfully.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def add_item(request):
    if request.method == "POST":
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            item_name = form.cleaned_data['item']  # Assuming 'item' is the name of the text input
            # Fetch or create the item instance based on the input
            item_instance, created = ItemModel.objects.get_or_create(name=item_name)
            
            inventory_item = form.save(commit=False)
            inventory_item.item = item_instance
            inventory_item.user = request.user
            inventory_item.save()
            
            logger.info(f"Item added successfully: {inventory_item}")
            return redirect('list_items')
        else:
            logger.error(f"Form errors: {form.errors}")
    else:
        form = InventoryItemForm()
    return render(request, 'add_item.html', {'form': form})


@login_required
def list_items(request):
    items = InventoryItem.objects.filter(user=request.user)
    return render(request, 'list_items.html', {'items': items})

def inventory(request):
    items = Item.objects.all()
    return render(request, 'inventory.html', {'items': items})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                logger.info(f"User {username} logged in successfully.")
                return redirect('home')
            else:
                logger.error("Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def profile_view(request):
    return render(request, 'profile.html')