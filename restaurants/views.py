from django.shortcuts import redirect, render
from .forms import RestaurantForm
from django.views.generic import View
from django.contrib import messages
from .models import Restaurant

class RestaurantView(View):
    def get(self, request):
        form = RestaurantForm()
        return render(request, 'main/restaurant.html', context={
        "form": form,
        "posts": Restaurant.objects.all()
    }) 
    
    
    def post(self, request):
        form = RestaurantForm(data=request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, "Qo'shildi")
            return redirect('restaurant:index')