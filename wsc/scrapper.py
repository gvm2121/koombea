from bs4 import BeautifulSoup as Bs
import requests
import time



def get_Links(URL):
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
    return (URL,total_links,links,titulo)
    

def get_Links_Details(tupla):
    try:
        res = []
        links = tupla[2]
        titulo = tupla[3]
        for link in links:
            if not link.get_text():
                res.append((link.get("href"),titulo))            
            else:
                res.append((link.get("href"),link.get_text()))
        return res
    except:
        return "no hay datos"

