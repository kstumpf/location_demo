from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Proverb, Location

from forms import ProverbForm
from locations.forms import LocationForm
from django.core.context_processors import csrf

from django.core import serializers

# Create your views here.
def home(request):
    return render(request, 'home.html')

def prov_list(request):
    '''Displays a list of all proverbs in the database.'''
    proverbs = Proverb.objects.all()
    context = {}
    context['proverbs'] = proverbs

    return render_to_response('prov_list.html', context)


def prov_detail(request, pk, *args, **kwargs):
    '''Lists the proverb's detail. Called when one clicks on a linked proverb.'''
    proverb = Proverb.objects.get(pk=pk)
    context = {}
    context['proverb'] = proverb

    return render_to_response('prov_detail.html', context)


def master_create(request):
    '''This renders a template which loads multiple forms to one page to create a master form page!'''
    context = {}
    return render_to_response('master_create.html', context)


def prov_create(request):
    '''A model form for creating a new proverb.'''
    if request.method == 'POST':
        form = ProverbForm(request.POST)
        if form.is_valid():
            form.save()
            if request.is_ajax():
                return render(request, 'prov_list.html')
            else:
                return redirect('/prov_list/')
    else:
        form = ProverbForm() 

    continent_list = Location.objects.filter(type="continent")

    context = {}
    context.update(csrf(request)) 
    context['form'] = form
    context['continent_list'] = continent_list

    return render_to_response('prov_create.html', context)


def prov_edit(request, pk):
    '''A model form for editing the proverb.'''
    proverb = Proverb.objects.get(pk=pk)
    if request.POST:
        form = ProverbForm(request.POST, instance = proverb)
        if form.is_valid():
            form.save()
            if request.is_ajax():
                return render(request, 'prov_list.html')
            else:
                return redirect('/prov_list/')
    else:
        form = ProverbForm(instance = proverb)

    context = {}
    context.update(csrf(request))
    context['form'] = form
    context['pk'] = pk

    return render_to_response('prov_edit.html', context)


def all_json_countries(request, continent):
    '''Creates a json list of countries based on the current selected continent.
    This list is passed back to the script to finish the form selection process.'''
    current_continent = Location.objects.get(name = continent)
    countries = Location.objects.all().filter(parent=current_continent)
    json_countries = serializers.serialize("json", countries)
    return HttpResponse(json_countries, mimetype="application/javascript")
