from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect, response,Http404
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

chal_dict = {'January': "Walk 10 miles",
             'February': "Walk 20 miles",
             'March': "Walk 30 miles",
             'April': "Walk 40 miles",
             'May': "Walk 50 miles",
             'June': "Walk 60 miles",
             'July': "Walk 70 miles",
             'August':"Walk 80 miles",
             'September':"Walk 90 miles",
             'October':"Walk 100 miles",
             'November':"Walk 110 miles",
             'December':None,#"Walk 120 miles"#,
             'Wwmember':'Hello'
             }


def index(request):
    welcome_msg=""
    month_array1=list(chal_dict.keys())
    
    for i in month_array1:
        redirect_path1=reverse('month_string',args=[i])
        welcome_msg=welcome_msg+("<li><a href=\"{}\">{}</a></li>".format(redirect_path1,i))

    
   # return HttpResponse(welcome_msg)
    return render(request,'challenges/index.html',{"month_array1":month_array1})

'''
def month_response_number(request, month_selected):
    str1=""
    try:
        str1=list(chal_dict.values())[month_selected-1]
    
    except:
        return HttpResponseNotFound("Not a valid Number")
    return HttpResponse(str1)
'''
def month_response_number(request, month_selected):
    month_array=list(chal_dict.keys())
    forward_month=''
    try:
      forward_month=month_array[month_selected-1]
      redirect_path=reverse('month_string',args=[forward_month]) #it will set path as challenges/January
      return HttpResponseRedirect(redirect_path)
      #return HttpResponse(forward_month)
     # return  HttpResponseRedirect('/challenges/'+ forward_month)


    except:
        return HttpResponseNotFound('Not a valid number')
    

 
def month_response(request, month_selected):

    str = ''
    month_selected = month_selected.title()
    response_data=render_to_string("404.html")
    try:
        str = '<h1>{}</h1>'.format(chal_dict[month_selected])
    except:
        #raise Http404()
        return HttpResponseNotFound(response_data)

    #return HttpResponse(response_data) "challenges/challenge.html"
    return render(request,"challenges/challenge.html",{"text":chal_dict[month_selected],"month_name":month_selected.title()})
