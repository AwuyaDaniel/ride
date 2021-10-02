from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from django.template import loader
from django.views import generic

from .forms import *
from .models import *
from django.views.generic import View
from django.contrib import messages

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime

from django.db.models import Max, Sum, Avg

# from django import forms
from django.contrib.auth import get_user_model


def post_delivery(request):

    if request.user != request.user:
        raise Http404

    user = request.user

    form = PostOrderForm(request.POST, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            new = form.save(commit=False)
            # new.status = '1'
            # new.user = user
            new.save()

            return redirect('Delivery:success')
    context = {'user': user, 'form': form}
    return render(request, 'Delivery/create.html', context)


def order_received(request):
    return render(request, 'Delivery/success.html')
