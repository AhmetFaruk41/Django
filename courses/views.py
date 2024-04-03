from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import redirect,render
from django.urls import reverse
data = {
    "programlama":"programlama kategorisine ait kurslar",
    "web-geliştirme":"web geliştirme kategorisine ait kurslarr",
    "mobil":"mobil kategorisine ait kurslar",
}

def kurslar(request):
    category_list = list(data.keys())
    list_items=''
    for category in category_list:
        redirect_url = reverse('courses_by_category',args=[category])
        list_items += f"<li><a href='{redirect_url}>{category}</a></li>"
    htmt= f"<h1>kurs listesi</h1><br><ul>{list_items}</ul>"

    return HttpResponse(htmt)

def index(request):
    return render(request,'index.html')

def details(requst,kurs_adi):
    return HttpResponse(f"{kurs_adi} detay sayfası")

def getCoursesByCategory(request,category_name):
    try:
        category_text = data[category_name]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("<h1>yanlış kategori seçimi</h1>")
    
def getCoursesByCategoryID(request,category_id):
    category_list = list(data.keys())
    if category_id>len(category_list):
        return HttpResponseNotFound("yanlış kategori seçimi")
    
    category_name = category_list[category_id - 1]
    redirect_url = reverse('courses_by_category',args=[category_name])
    
    return redirect(redirect_url)
