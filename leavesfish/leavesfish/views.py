from django.shortcuts import render

def home(request):
    return render(request,'leavesfish/home.html')
    
def profile(request):
    return render(request,'leavesfish/profile.html',{'users':request.user})