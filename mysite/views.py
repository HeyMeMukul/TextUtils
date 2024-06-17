
# Views.py
# I have created this file - Mukul
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")



def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    charcount = len(djtext)
    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    # usin POST method to make the URL clean  so that data will not be send by URL this is for safty purpose also
    fullcaps = request.POST.get('fullcaps', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

 
    # Perform analysis
    analyzed = djtext
    purpose = []

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = "".join(char for char in analyzed if char not in punctuations)
        purpose.append('Removed Punctuation')

    if fullcaps == "on":
        analyzed = analyzed.upper()
        purpose.append('Changed to Uppercase')

    if extraspaceremover == "on":
        analyzed = ' '.join(analyzed.split())
        purpose.append('Removed Extra Spaces')

   
    # If no option was selected
    if not (removepunc == "on" or fullcaps == "on"or extraspaceremover == "on"):
        return HttpResponse("Error: No option selected.")

    # Set params for rendering template
    params = {'purpose': ', '.join(purpose), 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)
