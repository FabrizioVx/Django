"""POST VIEWS"""
#Django
from django.shortcuts import render
#UTILITIES
from datetime import datetime

posts = [
    {
        'name' : 'BLACK',
        'user': 'Fabrizio',
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036',
    },
    {
        'name' : 'BLACK',
        'user': 'Fabrizio',
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036',
    },
    {
        'name' : 'BLACK',
        'user': 'Fabrizio',
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036',
    }
]




def list_posts(request):
    return  render(request,'feed.html',{'posts':posts})



    #"""Listas posts"""
    
    #"""
    #content = []
    #for post in posts:
    #    content.append("""
        #<p><strong>{name}</strong> </p>
        #<p><small>{user} - <i>{timestamp}</i></small></p>
        #<figure><img src="{picture}"/></figure>
        #""".format(**post))

   # return HttpResponse('<br>'.join(content))
   # """

