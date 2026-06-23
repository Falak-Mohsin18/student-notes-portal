from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .models import Note
from .forms import NoteForm, RegisterForm


# Landing Page
def landing_page(request):
    return render(
        request,
        'notes/landing.html'
    )


# Browse Notes
def browse_notes(request):

    query = request.GET.get('q')

    if query:
        notes = Note.objects.filter(
            title__icontains=query
        )

    else:
        notes = Note.objects.all()

    return render(
        request,
        'notes/browse_notes.html',
        {
            'notes': notes
        }
    )


# Register
def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            user.set_password(
                form.cleaned_data['password']
            )

            user.save()

            return redirect('login')

    else:

        form = RegisterForm()

    return render(
        request,
        'notes/register.html',
        {
            'form': form
        }
    )


# Login
def login_view(request):

    if request.method == 'POST':

        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            user = form.get_user()

            login(
                request,
                user
            )

            return redirect(
                'dashboard'
            )

    else:

        form = AuthenticationForm()

    return render(
        request,
        'notes/login.html',
        {
            'form': form
        }
    )


# Logout
def logout_view(request):

    logout(request)

    return redirect(
        'landing'
    )


# Dashboard
@login_required
def dashboard(request):

    return render(
        request,
        'notes/dashboard.html'
    )


# Upload Notes
@login_required
def upload_note(request):

    if request.method == 'POST':

        form = NoteForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            note = form.save(
                commit=False
            )

            note.uploaded_by = request.user

            note.save()

            return redirect(
                'my_notes'
            )

    else:

        form = NoteForm()

    return render(
        request,
        'notes/upload.html',
        {
            'form': form
        }
    )


# My Notes
@login_required
def my_notes(request):

    notes = Note.objects.filter(
        uploaded_by=request.user
    )

    return render(
        request,
        'notes/my_notes.html',
        {
            'notes': notes
        }
    )


# Edit Note
@login_required
def edit_note(request, id):

    note = Note.objects.get(id=id)

    if note.uploaded_by != request.user:
        return redirect('my_notes')

    if request.method == 'POST':

        form = NoteForm(
            request.POST,
            request.FILES,
            instance=note
        )

        if form.is_valid():

            form.save()

            return redirect(
                'my_notes'
            )

    else:

        form = NoteForm(
            instance=note
        )

    return render(
        request,
        'notes/edit_note.html',
        {
            'form': form
        }
    )


# Delete Note
@login_required
def delete_note(request, id):

    note = Note.objects.get(id=id)

    if note.uploaded_by == request.user:
        note.delete()

    return redirect(
        'my_notes'
    )
    
@login_required
def profile(request):

    notes_count = Note.objects.filter(
        uploaded_by=request.user
    ).count()

    return render(
        request,
        'notes/profile.html',
        {
            'notes_count': notes_count
        }
    )