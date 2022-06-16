from django.shortcuts import render
# Create your views here.


def index(request):
    dict_ = {
        'key': 'Hello World',
        'color': 'yellow',
        'list_': ['Abylai', "Salima", "Sanjar", 'Janat']
    }
    return render(request, 'index.html', context=dict_)


def main(req):
    return render(req, 'main.html')


def dt(r):
    return render(r, 'dtime.html')


def info(a):
    return render(a, 'info.html')

