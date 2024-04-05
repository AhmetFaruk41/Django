from datetime import date
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import redirect,render
from django.urls import reverse

data = {
    "programlama":"programlama kategorisine ait kurslar",
    "web-geliştirme":"web geliştirme kategorisine ait kurslarr",
    "mobil":"mobil kategorisine ait kurslar",
}
db ={
    "courses":[
        {
            "title":"javascript kursu",
            "description":"javascript kurs açıklaması",
            "imageUrl":"1.jpg",
            "slug":"javscript-kursu",
            "date": date(2022,10,10),
            "isActive":True,
            "isUpdated":True
        },
        {
            "title":"python kursu",
            "description":"python kurs açıklaması",
            "imageUrl":"2.jpg",
            "slug":"python-kursu",
            "date": date(2022,9,10),
            "isActive":False,
            "isUpdated":False
        },
        {
            "title":"web geliştirme kursu",
            "description":"web geliştirme kurs açıklaması",
            "imageUrl":"3.jpg",
            "slug":"web-gelistirme-kursu",
            "date": date(2022,8,10),
            "isActive":True,
            "isUpdated":True
        }
    ],
    "categories":[
                  {"id":1,"name":"programlama","slug":"programlama"},
                  {"id":2,"name":"web geliştirme","slug":"web-gelistirme"},
                  {"id":3,"name":"mobil uygulamalar","slug":"mobil-uygulamalar"},
                  ]
}

# isUpdated kısmında kaldım!!!!!!!!!!!!!!!!!!!!!!!

def index(request):
    #list comphension
    kurslar= [course for course in db["courses"] if course["isActive"]==True] #for döngüsü yerine kullanılan ifade 
    kategoriler= db["categories"]

    #for kurs in db["courses"]:
    #    if kurs["isActive"] == True:
    #        kurslar.append(kurs)

    return render(request,'courses/index.html',{
        'categories': kategoriler,
        'courses': kurslar
    })


def details(requst,kurs_adi):
    return HttpResponse(f"{kurs_adi} detay sayfası")

def getCoursesByCategory(request, category_name):
    try:
        category_text = data[category_name]
        return render(request,'courses/kurslar.html',{
            'category':category_name,
            'category_text':category_text
        })
    except:
        return HttpResponseNotFound("<h1>yanlış kategori seçimi</h1>")
    
def getCoursesByCategoryID(request,category_id):
    category_list = list(data.keys())
    if (category_id>len(category_list)):
        return HttpResponseNotFound("yanlış kategori seçimi")
    
    category_name = category_list[category_id - 1]

    redirect_url = reverse('courses_by_category',args=[category_name])
    
    return redirect(redirect_url)
