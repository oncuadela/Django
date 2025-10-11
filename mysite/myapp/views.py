from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

def main(request: HttpRequest) -> HttpResponse:
    jmeno = "Karel"
    barva = "Cervena"
    return render(request, "index.html", {
        "jmeno":jmeno,
        "barva":barva,
    })

def second(request: HttpRequest) -> HttpResponse:  
    return HttpResponse("He")
    
def article_main(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Tohle je hlavni article.")


def article(request: HttpRequest,article_id: int,name: str = '') -> HttpResponse:
    return HttpResponse(
        "Tohle je clanek c.{}. {}".format(article_id, "Nazev tohoto clanku je: {}".format(
            name) if name else "Tenhle clanek nema nazev."
        ))


def article_uniq(request):
    return HttpResponse("Tohle je unikatni clanek")