from django.shortcuts import render

# Create your views here.
def isifaperta(request):
    judul = "Faperta Details"

    konteks = {
        'jdl': judul
    }
    return render(request, 'situsfaperta.html', konteks)
