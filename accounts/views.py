from django.http import HttpResponse
from django.shortcuts import redirect, render

from accounts.forms import UserForm
from accounts.models import User

# Create your views here.
def registerUser(request):
    # return HttpResponse('Test')
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = User.CUSTOMER
            user.save()
            return redirect('registerUser')
    else:
        form = UserForm()

    context = {
        'form':form,
    }
    return render(request, 'accounts/registerUser.html',context)