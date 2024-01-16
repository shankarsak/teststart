from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test

'''def buyer_index(request):
    return render(request, "buyer_index.html")'''

@login_required
def buyer_index(request):
    if request.user.role == 'Buyer':

        # Content for krishi
        return render(request, 'buyer_index.html')
    else:
        # Unauthorized access
        return HttpResponse("Unauthorized access")