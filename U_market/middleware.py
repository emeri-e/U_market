from business.models import Service, Product


class ObjectViewsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        
        response = self.get_response(request, *args, **kwargs)
        if request.path.startswith('/business/products/detail/') or request.path.startswith('/business/services/detail/'):
            pk = kwargs.get('pk')            
            if request.path.startswith('/business/products/detail/'):
                model = Product
                print(pk)

                
            else:                
                model = Service
            try:
                obj = model.objects.get(id=pk)
                obj.views += 1
                obj.save()
                print("reached here 1")
            except model.DoesNotExist:
                print("reached here 2")
                pass
        return response
