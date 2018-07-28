from django.shortcuts import render

# Create your views here.


def home(request):
    context = locals()
    template = "./profiles/index.html"
    return render(request, template, context)


def about(request):
    context = locals()
    template = "./profiles/about.html"
    return render(request, template, context)
