# created by me video #4

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def ex1(request):
    return HttpResponse('''<nav class="navbar navbar-expand-lg navbar-dark bg-dark"> <a class="navbar-brand" 
    href="/">Textutils</a> <button class="navbar-toggler" type="button" data-toggle="collapse" 
    data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle 
    navigation"> <span class="navbar-toggler-icon"></span> </button> <div class="collapse navbar-collapse" 
    id="navbarNavAltMarkup"> <div class="navbar-nav"> <a class="nav-item nav-link" href="/ex1">About Us</a> <a 
    class="nav-item nav-link" href="#">Contact Us</a> </div> </div> <form class="form-inline"> <input 
    class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search"> <button class="btn 
    btn-outline-success my-2 my-sm-0" type="submit">Search</button> </form> </nav>                <h1>I'm doing 
    exercise of navigation to various links:</h1> <h2>Google</h2> <a href = "https://www.google.com"> navigate to 
    google </a> <h2>Facebook</h2> <a href = "https://www.fb.com"> navigate to facebook </a> <h2>YouTube</h2> <a href 
    = "https://www.youtube.com"> navigate to youtube </a> <h2>Flipkart</h2> <a href = "https://www.flipkart.com"> 
    navigate to flipkart </a>''')


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    purpose = ''

    # Checkbox values = ON / OFF
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # check which checkbox is ON
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"+\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed
        purpose += '|Removed Punctuations|'

    if fullcaps == 'on':
        analyzed = ''
        analyzed = analyzed.join(djtext.upper())
        djtext = analyzed
        purpose += '|UPPERCASE|'

    if newlineremover == 'on':
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        djtext = analyzed
        purpose += '|New Line Remover|'

    if charcount == 'on':
        analyzed = len(djtext)
        djtext = f'{djtext}\n\nCharacter Count: {str(analyzed)}'
        purpose += '|Character Count|'

    if charcount == 'off' and removepunc == 'off' and fullcaps == 'off' and newlineremover == 'off':
        return HttpResponse('Error')

    params = {'purpose': purpose, 'analyzed_text': djtext}
    return render(request, 'analyze.html', params)