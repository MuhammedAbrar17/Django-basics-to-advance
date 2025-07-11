from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,HttpResponseNotFound,HttpResponseRedirect

# Create your views here.
Posts = [
    {
    'id':0,
    'title':'Hello wrold',
    "discription":"hey this world's most beautiful country is switzerlend"
},
{
    'id':1,
    'title':"Prophet Muhammed (s.a)",
    'discription':'''muhammed (s.a) he is the last phrophet in our world,
    The most Hand some and good guy in the world is prophet muhammed (s.a)'''
},
{
    'id':2,
    'title':" jebreel (a.s)",
    'discription':"jebreel (a.s) he is the messenger of allah, and he is the leader of all malaikath"
},

]


    
def home(request):
    html = "" 
    for post in Posts:
        html += f''' 
            <div> 
            <a href = "/post/{post['id']}/"
                <h1> {post['id']} - {post['title']} </h1> </a>
                <p> {post['discription']} </p>            
            </div>
    
''' 
    return render(request,"home.html",{"posts":Posts,'username':'abu'})

def post(request, id):
    valid_id = False
    for post in Posts:
        if post['id'] == id:
            post_dict = post
            valid_id = True
    if valid_id:

        html = f'''
            <h1> {post_dict['title']}</h1>
            <p> {post_dict['discription']}</p>
    '''
        return HttpResponse(html)
    
    else:
        return HttpResponseNotFound("Post Not avalibale")
    

def google(request):
    return HttpResponseRedirect('https://www.google.com')