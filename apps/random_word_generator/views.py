from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
# Create your views here.

def index(req):
    
    return render(req, "random_word_generator/index.html")

def random_generator(req):
    if 'counter' not in req.session:
        req.session['counter'] = 0
    req.session['counter'] += 1

    random_word = get_random_string(length=14)
    context = {
        'randon_word': random_word,
        'counter': req.session['counter']
    }
    return render(req, "random_word_generator/index.html", context)

def reset(request):
    request.session.clear()
    return redirect('/')