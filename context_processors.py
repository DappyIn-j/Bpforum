from myapp.models import Post

def searchFunction(request):
    search_context={}
    posts = Post.objects.all()
    if "search" in request.GET:
        query = request.GET.get('q')
    
        #start Filters
        search_box = request.GET.get("search-box")
        if search_box == "Descriptions" :
            objects = posts.filter(content__icontains=query)
        else:
            objects = posts.filter(title__icontains=query)
        #end Filters
        search_context= {
            "objects":objects,
            "query":query,
        }

    return search_context