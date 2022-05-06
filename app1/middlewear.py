from django.http import HttpResponse
# def mymiddlewear(get_response):
#     print("Inital state of middlewear....")
#     def innermiddlewear(request):
#
#         print("Befor exexcustion...")
#         response = get_response(request)
#         print("After exexcustion...")
#         return response
#     return innermiddlewear


class mymiddlewear:
    def __init__(self,get_response):
        self.get_response = get_response
        print("INIT methind")

    def __call__(self,request):
        print("Befor view  ")
        response = self.get_response(request)
        print("after view")
        #print(response)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("In process view")
        print(view_func.__name__)
        #return HttpResponse("<h1>You can not call view fumction</h1>")      #view function call nahi honae direct hech disel
        return None

    def process_exception(self,request,exception):
        print(exception)
        raise ValueError

    def process_template_response(self,request,response):
        response.contax_data['name'] = 'pratik'
        response.contax_data['marks'] = 90

        print("in template process view")
        return response



