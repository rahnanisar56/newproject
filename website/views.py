from django.shortcuts import render
def homepagee(request):
    return render(request,'homepage.html')

def aboutt(request):
    return render(request, 'about.html')
