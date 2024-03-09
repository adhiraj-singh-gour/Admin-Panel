from django.shortcuts import render
import requests

# Create your views here.
def adminpage(request):
    data=requests.get('http://127.0.0.1:8000/snippets/').json()
    return render(request,'admin.html',{"data":data})

def viewuser(request):
    # user = Signup.objects.all()
    return render(request,'viewuser.html',)

def viewproduct(request):
    data=requests.get('http://127.0.0.1:8000/snippets/').json()
    return render(request,'viewproduct.html',{"data":data})

def update(request,pk):
    data = requests.get('http://127.0.0.1:8000/SnippetDetail/').json()
    return render(request,'update.html',data)

def update_product(request,pk):
    # if request.method == "POST":
    #     data=Products.objects.get(id=pk)
    #     data.Name=request.POST['Name']
    #     data.Type=request.POST['Type']
    #     data.Price=request.POST['Price']
    #     data.Description=request.POST['Description']
    #     data.image=request.POST['image']
    #     data.save()
    #     data=Products.objects.all()

    return render(request, "admin.html")

def delete(request, pk):
    delete = requests.get('http://127.0.0.1:8000/SnippetDetail/').json()
    data=requests.get('http://127.0.0.1:8000/snippets/').json()
    return render(request,'admin.html',{'data':data})


def allorder(request):
    # data = ItemModel.objects.all()
    return render(request, "allorder.html")
