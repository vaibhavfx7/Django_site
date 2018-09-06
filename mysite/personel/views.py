from django.shortcuts import render

def index(request):
	return render(request,'personel/home.html')
def contact(request):
	return render(request,'personel/basic.html',{'content':['If you like to contact me ,please email me','kvaibhavs077@gmail.com']})

