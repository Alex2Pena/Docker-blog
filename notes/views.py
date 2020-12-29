from django.shortcuts import render
from .models import Note

def show_notes(request):

    notes = Note.objects.all()
    context = {
        'notes': notes
    }

    return render(request, 'notes/list.html', context)

    
