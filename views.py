from django.shortcuts import render, redirect,HttpResponse
from . import models


def addingstring(request):
    if request.method == 'POST':
        string1 = request.POST.get("message")

        if (string1.isalpha()):
            obj = models.Alphabet()
            obj.alphabets = string1
            obj.save()
            print(string1)
            print("All are alphabet")
        elif (string1.isnumeric()):
            obj1 = models.Numeric()
            obj1.numeric = string1
            obj1.save()
            print(string1)
            print("All are numeric")
        else:
            obj2 = models.Alphanumeric()
            obj2.alphanumeric = string1
            obj2.save()
            print(string1)
            print("all are alphanumeric")
        return redirect('viewstring/')
    return render(request, 'dashboard.html', {})


def viewingstring(request):
    obj1= models.Alphabet.objects.all()
    obj2 = models.Alphanumeric.objects.all()
    obj3 = models.Numeric.objects.all()
    if request.method == 'POST' and 'delete' in request.POST:
        idd = request.POST.get('delete')
        ob = models.Alphabet.objects.get(id=idd)
        ob.delete()
    else:
        print('hi')
    if request.method == 'POST' and 'delete1' in request.POST:
        idd = request.POST.get('delete1')
        ob = models.Alphanumeric.objects.get(id=idd)
        ob.delete()
    else:
        print('hi')
    if request.method == 'POST' and 'delete2' in request.POST:
        idd = request.POST.get('delete2')
        ob = models.Numeric.objects.get(id=idd)
        ob.delete()
    else:
        print('hi')
    return render(request, 'view.html', {'key':obj1,'key2':obj2,'key3':obj3})
