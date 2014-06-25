from django.shortcuts import render_to_response, redirect, render
from .models import Location

from django.http import HttpResponseRedirect

from forms import LocationForm
from django.core.context_processors import csrf

# Create your views here.
def loc_list(request):
    '''Displays a list of all locations in the database.'''
    locations = Location.objects.all()
    context = {}
    context['locations'] = locations
    return render_to_response('loc_list.html', context)


def loc_detail(request, pk, *args, **kwargs):
    '''Displays the location's detail. Used when one clicks on a linked location.'''
    location = Location.objects.get(pk=pk)
    overlaplist = location.overlapswith.all()

    context = {}
    context['location'] = location
    context['overlaplist'] = overlaplist
    
    return render_to_response('loc_detail.html', context)


def loc_create(request):
    '''Model form for creating a new location.'''
    if request.POST:
        form = LocationForm(request.POST, auto_id=True)
        if form.is_valid():
            form.save()
            # The problem w/ duplicate POST submissions is only a problem with traditional requests. With AJAX request can simply render the success page instead of redirecting to it.
            if request.is_ajax():
                return render(request, 'loc_list.html')
            else:
                return redirect('/loc_list/')
    else:
        form = LocationForm(auto_id=True)

    context = {}
    context.update(csrf(request))
    
    context['form'] = form

    return render_to_response('loc_create.html', context)


def loc_edit(request, pk):
    '''Model form for editing a location. This location is acquired with a pk.'''
    location= Location.objects.get(pk = pk)
    if request.POST:
        form = LocationForm(request.POST, instance = location)
        if form.is_valid():
            form.save()
            if request.is_ajax():
                return render(request, 'loc_list.html')
            else:
                return redirect('/loc_list/')
    else:
        form = LocationForm(instance = location)

    context = {}
    context.update(csrf(request))
    context['form'] = form
    context['location'] = location
    context['pk'] = pk
    
    return render_to_response('loc_edit.html', context)


def loc_root(request, *args, **kwargs):
    '''Displays the root locations (those locations without parents).'''
    locations = Location.objects.filter(parent=None)
    context = {
        'locations' : locations,
        }
    return render_to_response('loc_root.html', context)

   
def loc_children(request, pk, *args, **kwargs):
    '''Displays the children of whatever linked root location has been clicked.'''
    location = Location.objects.get(pk = pk)
    children = location.children
    
    context = {}
    context['parent'] = location
    context['children'] = children
    return render_to_response('loc_children.html', context)
