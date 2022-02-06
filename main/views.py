from django.shortcuts import render

# Create your views here.

def get_base_context(request, pagename):
    return {
        'pagename': pagename,
    }


def index_page(request):
    context = get_base_context(request, 'PythonBin')
    return render(request, 'main/index.html', context)

