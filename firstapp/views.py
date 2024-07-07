from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import enter_data, quiz
import gspread
from google.oauth2.service_account import Credentials

# Path to your credentials JSON file
CREDS_FILE = 'path/to/your/credentials.json'

# Define the scope
SCOPE = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

def get_sheet():
    creds = Credentials.from_service_account_file(CREDS_FILE, scopes=SCOPE)
    client = gspread.authorize(creds)
    sheet = client.open('German words and meanings').sheet1
    return sheet

def enter_data_view(request):
    if request.method == 'POST':
        sheet = get_sheet()
        enter_data(sheet)
        return redirect('success')
    return render(request, 'enter_data.html')

def quiz_view(request):
    if request.method == 'POST':
        num_questions = int(request.POST.get('num_questions', 0))
        data = get_sheet().get_all_records()
        quiz(data, num_questions)
        return redirect('success')
    return render(request, 'quiz.html')

def success_view(request):
    return HttpResponse("Operation was successful!")
