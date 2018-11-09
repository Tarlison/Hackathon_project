from django.shortcuts import render

def post_news(request):
    return render(request, 'hackathon/post_news.html', {})
