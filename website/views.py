from django.shortcuts import render
def homepage(request):
    return render(request,'website/homepage.html')

def about(request):
    return render(request, 'website/about.html')
