from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.
posts = [
    {
    'id':1,
    'title':'Hello wrold',
    "discription":"hey this world's most beautiful country is switzerlend"
},
{
    'id':2,
    'title':"Prophet Muhammed (s.a)",
    'discription':'''muhammed (s.a) he is the last phrophet in our world,
    The most Hand some and good guy in the world is prophet muhammed (s.a)'''
},
{
    'id':3,
    'title':" jebreel (a.s)",
    'discription':"jebreel (a.s) he is the messenger of allah, and he is the leader of all malaikath"
},

]

    


def helloworld(request):
    html = "" 
    for post in posts:
        html += f''' 
            <div> 
                <h1> {post['id']} - {post['title']} </h1>
                <p> {post['discription']} </p>            
            </div>
    
'''
    return HttpResponse(html)