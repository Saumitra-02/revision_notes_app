from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Note
from django.contrib.auth.decorators import login_required
from .forms import NoteForm
import cv2
import pytesseract
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize.treebank import TreebankWordDetokenizer
import pdfkit

@login_required
def home(request):
    return render(request, 'home.html')

# @login_required
# def create_note(request):
#     if request.method == 'POST':
#         note_content = request.POST.get('note_content')
#         user=request.user
#         note = Note.objects.create(user=user, content=note_content)
#         return redirect('note_created', note_id=note.id)
#     return render(request, 'create_note.html')

@login_required
def note_created(request, note_id):
    return render(request, 'note_created.html', {'note_id': note_id})

def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = foimage_path = note.image.path
            image = cv2.imread(image_path)
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            extracted_text = pytesseract.image_to_string(gray_image)

            # Generate a text summary
            sentences = sent_tokenize(extracted_text)
            stop_words = set(stopwords.words("english"))
            words = [word for word in sentences if word.lower() not in stop_words]
            fdist = FreqDist(words)
            most_common = fdist.most_common(5)  # Get the top 5 most common sentences
            summary = TreebankWordDetokenizer().detokenize([sent for sent, freq in most_common])

            # Update the 'extracted_text' and 'summary' fields of the note model
            note.extracted_text = extracted_text
            note.summary = summary
            note.save()           

            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm()
    return render(request, 'note_form.html', {'form': form})

@login_required
def note_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'note_detail.html', {'note': note})

@login_required
def list(request):
    notes = Note.objects.filter(user=request.user)

    return render(request, 'list.html', {'notes': notes})

@login_required
def note_detail(request, pk):
    note = Note.objects.get(pk=pk)

    # Generate an HTML representation of the note details
    html_content = f"<h2>{note.title}</h2><p>{note.extracted_text}</p><p>Summary: {note.summary}</p>"

    # Configure pdfkit options
    options = {
        'page-size': 'A4',
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
    }

    # Generate the PDF document
    pdfkit.from_string(html_content, f'media/notes/Note_{note.pk}.pdf', options=options)

    return render(request, 'note_detail.html', {'note': note})