from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import quiz
import gspread
from google.oauth2.service_account import Credentials
from django import forms

# Path to your credentials JSON file
CREDS_FILE =  r"C:\Users\tarun\OneDrive\Coding\credentials\vocabnotecreds.json"

# Define the scope
SCOPE = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

def options_view(request):
    return render(request, 'options.html')


def get_sheet():
    creds = Credentials.from_service_account_file(CREDS_FILE, scopes=SCOPE)
    client = gspread.authorize(creds)
    sheet = client.open('German words and meanings').sheet1
    return sheet

class DataEntryForm(forms.Form):
    Gender = forms.CharField(max_length=10, required=False)
    Word = forms.CharField(max_length=100)
    English_Meaning = forms.CharField(max_length=200)
    Part_of_Speech = forms.CharField(max_length=50, required=False)
    Other_Comments = forms.CharField(widget=forms.Textarea, required=False)

def enter_data_view(request):
    if request.method == 'POST':
        form = DataEntryForm(request.POST)
        if form.is_valid():
            sheet = get_sheet()
            gender = form.cleaned_data['Gender']
            word = form.cleaned_data['Word']
            english_meaning = form.cleaned_data['English_Meaning']
            part_of_speech = form.cleaned_data['Part_of_Speech']
            other_comments = form.cleaned_data['Other_Comments']
            
            # Append the new row to the sheet
            sheet.append_row([gender, word, english_meaning, part_of_speech, other_comments])
            
            return redirect('success')
    else:
        form = DataEntryForm()
    
    return render(request, 'enter_data.html', {'form': form})

def quiz_view(request):
    if request.method == 'POST':
        num_questions = int(request.POST.get('num_questions', 0))
        data = get_sheet().get_all_records()
        quiz(data, num_questions)
        return redirect('success')
    return render(request, 'quiz.html')

def success_view(request):
    return HttpResponse("Operation was successful!")

def success_view(request):
    return render(request, 'success.html')


