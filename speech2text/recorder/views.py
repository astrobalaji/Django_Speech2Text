from django.shortcuts import render

# Crea te your views here.
def recorder_view(request):
    return render(request,'recorder.html')
