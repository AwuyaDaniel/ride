from django.shortcuts import render

# Create your views here.


def home(request):

    user = request.user

    context = {'user': user}

    return render(request, 'Home/homepage.html', context)
