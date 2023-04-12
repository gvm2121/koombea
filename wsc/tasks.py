from bs4 import BeautifulSoup as Bs
import requests
from wsc.models import *
from celery import shared_task

@shared_task
def get_Links(URL,user):
    q1 = MainWebs.objects.get(url=URL,user = User.objects.get(pk = user))
    try:
        r = requests.get(URL)        
    except requests.exceptions.RequestException as e:
        return "La url ingresada no es correcta, podrías revisarla bien?, está mal escrita o necesita de autorizacion",e    
    s = Bs(r.text,"html.parser")        
    links = [link for link in s.find_all("a")]
    total_links = len(links)
    titulo = s.title.string if s.title.string else "Sin Titulo"

    if len(links)==0:
        return "Es probable que el sitio web esté renderizado con javascript, necesita ser tratado de forma particular, no se puede scrappear"
        total_links = 0
    q1.name = titulo
    q1.total_links = total_links
    q1.save()
    
    for link in links:
        if not link.get_text():
            DetailsWeb.objects.create(web_parent=q1,name_detail=str(titulo),link_detail=str(link))
        else:
            DetailsWeb.objects.create(web_parent=q1,name_detail=str(link.get_text()),link_detail=str(link))

