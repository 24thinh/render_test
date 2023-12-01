from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Work, Description, Entry
from django.http import Http404

from .forms import WorkForm, DescriptionForm, EntryForm
# Create your views here.
def index(request):
    """The homepage for to do list."""
    return render(request, 'to_do_list_app/index.html')

@login_required
def works(request):
    """The page to show all the works"""
    works = Work.objects.filter(owner=request.user).order_by('date_added')
    context = {'works':works}
    return render(request, 'to_do_list_app/works.html', context)

@login_required
def work(request, work_id):
    """The page to show a specific page."""
    work = Work.objects.get(id=work_id)
    # Make sure the topic belongs to the current user.
    if work.owner != request.user:
        raise Http404

    descriptions = work.description_set.all
    entries = work.entry_set.all
    context = {'work': work, 'descriptions':descriptions, 'entries': entries}
    return render(request, 'to_do_list_app/work.html', context)

@login_required
def new_work(request):
    """THe page to create a new work."""
    if request.method == 'POST':
        form = WorkForm(request.POST)
        # POST data submitted, process data.
        new_work = form.save(commit=False)
        new_work.owner = request.user
        new_work.save()
        return redirect('to_do_list_app:works')
        #return HttpResponseRedirect(reverse('to_do_list_app:works'))
    else:
        # No data submitted, create a blankk form
        form = WorkForm()
    
    context = {'form': form}
    return render(request, 'to_do_list_app/new_work.html', context)

@login_required
def new_description(request, work_id):
    """Add a new entry for a particular topic."""
    work = Work.objects.get(id=work_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = DescriptionForm()        
    else:
        # POST data submitted; process data.
        form = DescriptionForm(data=request.POST)
        if form.is_valid():
            new_description = form.save(commit=False)
            new_description.work = work
            new_description.save()
            return redirect('to_do_list_app:work', work_id=work_id)
            #return HttpResponseRedirect(reverse('to_do_list_app:work',
            #                            args=[work_id]))
    #Display a blank or invalid form.
    context = {'work': work, 'form': form}
    return render(request, 'to_do_list_app/new_description.html', context)

@login_required
def new_entry(request, work_id):
    """Add a new entry for a particular topic."""
    work = Work.objects.get(id=work_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()        
    else:
        # POST data submitted; process data.
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.work = work
            new_entry.save()
            return redirect('to_do_list_app:work', work_id=work_id)
            #return HttpResponseRedirect(reverse('to_do_list_app:work',
            #                            args=[work_id]))
    #Display a blank or invalid form.
    context = {'work': work, 'form': form}
    return render(request, 'to_do_list_app/new_entry.html', context)

@login_required
def edit_description(request, description_id):
    """Edit a description."""
    description = Description.objects.get(id=description_id)
    work = description.work
    if work.owner != request.user:
        raise Http404

    if request.method == 'POST':
        # POST data submitted, process data.
        form = DescriptionForm(request.POST or None, instance=description)
        if form.is_valid():
            form.save()
            return redirect('to_do_list_app:work', work_id=work.id)
        
    else:
        # Initial request; pre-fill form with the current description.
        form = DescriptionForm(instance=description)
    
    #Display a blank or invalid form.
    context = {'work': work, 'form': form, 'description': description}
    return render(request, 'to_do_list_app/edit_description.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit a description."""
    entry = Entry.objects.get(id=entry_id)
    work = entry.work
    if work.owner != request.user:
        raise Http404

    if request.method == 'POST':
        # POST data submitted, process data.
        form = EntryForm(request.POST or None, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('to_do_list_app:work', work_id=work.id)
        
    else:
        # Initial request; pre-fill form with the current description.
        form = EntryForm(instance=entry)
    
    #Display a blank or invalid form.
    context = {'work': work, 'form': form, 'entry': entry}
    return render(request, 'to_do_list_app/edit_entry.html', context)

@login_required
def delete_work(request, work_id):
    work = Work.objects.get(id=work_id)
    work.delete()
    return redirect('to_do_list_app:works')

@login_required
def delete_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    work = entry.work
    image = entry.image
    image.delete()
    entry.delete()
    
    return redirect('to_do_list_app:work',work_id=work.id)