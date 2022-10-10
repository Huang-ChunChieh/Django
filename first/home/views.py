# from django.shortcuts import render, HttpResponse
# from bs4 import BeautifulSoup
# import requests


# def simple_crawl(request):
#     url = "https://www.maxlist.xyz/"
#     res = requests.get(url)
#     soup = BeautifulSoup(res.text, "html.parser")
#     title = soup.select('title')
#     return render(request, 'home/simple_crawl.html', locals())


from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from bs4 import BeautifulSoup
import requests


def simple_crawl(request):
    return render(request, 'home/simple_crawl.html')


def POST_crawl(request):
    url = request.POST["title"]
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    post = []
    H_tag = soup.find_all('h2')
    for h in H_tag:
        post.append(h.text)

    return render(request, 'home/simple_crawl_result.html', locals())
