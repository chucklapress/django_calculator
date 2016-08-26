from django.shortcuts import render



# Create your views here.
def index_view(request):
    if request.POST:
        left = request.POST['left']
        right = request.POST['right']
        mathop =request.POST['operators']
        if mathop == 'add':
            value = int(left) + int(right)
        if mathop == 'subtract':
            value = int(left) - int(right)
        if mathop == 'multiply':
            value = int(left) * int(right)
        if mathop == 'divide':
            value = int(left) / int(right)


        context ={
            'total':value
        }
        print(request.POST)
        return render(request, 'index.html', context)

    print(request.POST)
    return render(request, 'index.html')



