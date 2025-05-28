from django.shortcuts import render , redirect
from django.views import View
from ShopApp.form import RegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *



def search(request ):
    cartitems = 0
    if request.user.is_authenticated:
        item = Cart.objects.filter(user = request.user)
        
        for i in item:
            cartitems = cartitems + 1 

    if request.method == "POST":
        search = request.POST.get( 'search')
        search_items = Product.objects.filter(  p_name__icontains = search )
        
        return render(request, 'search.html' , { 
                 'search_items' : search_items ,
            'search':search,
            'cartitems' : cartitems })


def Home(request):
    cat = Product.objects.all()
    mens = Product.objects.filter( category = 'M').order_by('-id')[ : 10]
    camera = Product.objects.filter( category = "C" ).order_by('-id')[:10]
    shoes = Product.objects.filter( category = "Sh" ).order_by('-id')[:10]
    all = Product.objects.all().order_by('-id')[:10]

    cartitems = 0
    if request.user.is_authenticated:
        item = Cart.objects.filter(user = request.user)
        
        for i in item:
            cartitems = cartitems + 1 

    context = { 
        'cat': cat , 
        'all': all , 
        'mens' : mens,
        "shoes": shoes,
        'camera' : camera,
        'cartitems' : cartitems
    }
    return render(request, 'index.html', context)


class ProductDetails(View):
    def get(self, request, id):
        product = Product.objects.get(pk=id)


        cartitems = 0
        if request.user.is_authenticated:
            item = Cart.objects.filter(user = request.user)
        
            for i in item:
                cartitems = cartitems + 1 

        return render(request, 'productDetails.html', {'product': product , 'cartitems':cartitems})


class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'registration.html', {'form': form})
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulation! Registered Successfully')
            form.save()
        return render(request, 'registration.html', {'form': form})
    

def profile(request):
    
    cartitems = 0
    if request.user.is_authenticated:
        item = Cart.objects.filter(user = request.user)
        
        for i in item:
            cartitems = cartitems + 1 
    return render(request, 'profile.html' ,{"cartitems":cartitems})

def carts(request):
    user = request.user
    cartitems = 0
    if request.user.is_authenticated:
        items = Cart.objects.filter(user = request.user)    
        for i in items:
            cartitems = cartitems + 1 
    total_price = 0
    for i in items:
        total_price += i.product.discounted_price * i.quantity
    return render(request, 'carts.html', {'items': items, 'cartitems':cartitems, 'total':total_price  })

def addToCart(request):
    if request.user.is_authenticated:
        user = request.user
        product_id = request.GET.get('pro_id')
        product = Product.objects.get(id = product_id)
    
        for user in User.objects.all():
            User.objects.get_or_create(username=user)
        Cart(user= request.user, product=product).save()
        return redirect('/')
    else:
        return redirect('login')
        
def RemoveCart_items(request, id):
    remove_item  = Cart.objects.get( id = id).delete()
    return redirect('carts')

def buynow(request):
    return render(request, 'buynow.html')


def checkout(request):
    return render(request, 'checkout.html')



def base(request):
    
    cartitems = 0
    if request.user.is_authenticated:
        item = Cart.objects.filter(user = request.user)
        
        for i in item:
            cartitems = cartitems + 1 
    cat = Product.objects.all().order_by('-id')
    shoes = Product.objects.filter(category ="Sh").order_by('-id')
    men = Product.objects.filter(category ="M").order_by('-id')
    sunglasses = Product.objects.filter(category ="SG").order_by('-id')
    women = Product.objects.filter(category ="W").order_by('-id')
    camera = Product.objects.filter(category ="C").order_by('-id')

    if request.method == 'POST':
        serarch = request.POST.get('search')
        redirect( 'search.html')

     
    return render(request, 'base.html' ,  {
        'cat': cat,
        'shoes': shoes,
        'mens': men,
        'women' : women,
        'camera':camera,
        'sunglasses':sunglasses,
        'cartitems': cartitems
    })

def shoes(request , x = None):
    cartitems = 0
    if request.user.is_authenticated:
        item = Cart.objects.filter(user = request.user)
        
        for i in item:
            cartitems = cartitems + 1 

    if x == 'all':
        shoes = Product.objects.filter(category ="Sh").order_by('-id')
    else:
        shoes = Product.objects.filter(category ="Sh").filter(barnd = x).order_by('-id')

    return render(request, 'shoes.html' , {'shoes': shoes , 'cartitems': cartitems})

def mens(request , x = None):
    cartitems = 0
    if request.user.is_authenticated:
        item = Cart.objects.filter(user = request.user)
        
        for i in item:
            cartitems = cartitems + 1 
    if x == 'all':
        men = Product.objects.filter(category ="M").order_by('-id')
    elif x == 'H-M':
        men = Product.objects.filter(category ="M").filter(barnd = 'H&M' ).order_by('-id')      
    else:
        men = Product.objects.filter(category ="M").filter(barnd = x).order_by('-id')      
    return render(request, 'mens.html' , {'men': men , 'cartitems':cartitems})

def camera(request , x = None):
    cartitems = 0
    if request.user.is_authenticated:
        item = Cart.objects.filter(user = request.user)
        
        for i in item:
            cartitems = cartitems + 1 
    if x == 'all':
        camera = Product.objects.filter(category ="C").order_by('-id')   
    else:
        camera = Product.objects.filter(category ="C").filter(barnd = x).order_by('-id')   
    return render(request, 'camera.html' , {'camera': camera , 'cartitems':cartitems})

def womens(request , x = None):
    cartitems = 0
    if request.user.is_authenticated:
        item = Cart.objects.filter(user = request.user)
        
        for i in item:
            cartitems = cartitems + 1 

    if  x == 'all':   
        women = Product.objects.filter(category ="W").order_by('-id')    
    else:  
        women = Product.objects.filter(category ="W").filter(barnd = x).order_by('-id')    
    return render(request, 'women.html' , {'women': women , 'cartitems':cartitems})



def sunglasses(request, x= None ): 
    
    cartitems = 0
    if request.user.is_authenticated:
        item = Cart.objects.filter(user = request.user)
        
        for i in item:
            cartitems = cartitems + 1 

    if x == 'all':
        sunglasses = Product.objects.filter(category ="SG").order_by('-id')
    else:
        sunglasses = Product.objects.filter(category ="SG").filter(barnd = x).order_by('-id')
    return render(request, 'sunglasses.html' , {'sunglasses': sunglasses , 'cartitems':cartitems})