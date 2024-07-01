from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from .forms import UserForm
from .models import User


# Create your views here.

def registerUser(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = User.CUSTOMER
            # form.save()
            user.save()
            
            return redirect('registerUser')
    else:

        form = UserForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/registerUser.html', context)
