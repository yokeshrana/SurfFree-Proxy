import urllib

import httplib2
from  django.http import request
from django.shortcuts import render
from bs4 import BeautifulSoup as sp
import urllib
from django.http import HttpResponse
import re
# Create your views here.



def index(request,url):
    conn= urllib.urlopen(url)
    respose = conn.read()
    cleanSoup = sp(respose, "html.parser")
    for a in cleanSoup.findAll('a'):
        a['href'] ="/proxy/"+a['href']
    respose = str(cleanSoup)
    return HttpResponse(respose)


def process(request):
    html = "<body style='background:#222'>";
    html += "<br><hr><h1 style='text-align:center;color:#FFF'>Surf Free</h1><hr><br><br><br>"
    html += "<div style='font-size:2em; text-align:center;color:#FFF'>This is an Proxy Server  </div>"
    html += "<br><br> <br><br><br><div  style='text-align:center;color:#FFF;font-size:2em;'> " \
            "<a style='color:#FFF;text-decoration: none;'>Just add the website url like this http://127.0.0.1:8000/proxy/http://hmsonline.herokuapp.com</a> </div>"
    html += "<br><br> <br><br><br><hr><br><div  style='position:relative; margin-bottom:20px;text-align:center;color:#FFF;font-size:2em;'> " \
            "DEVELOPED BY YOKESH RANA CSE BIET JHANSI </div><hr>"
    return HttpResponse(html)