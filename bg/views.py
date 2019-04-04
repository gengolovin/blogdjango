from django.shortcuts import render

def post_list(request):
    return render(request, 'bg/post_list.html', {})


