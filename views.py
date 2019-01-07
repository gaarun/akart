from django.shortcuts import render,HttpResponse,render_to_response,HttpResponseRedirect
from store.models import *
from Altmetric import settings
from store.forms import *

def home(request):
	#print(request.session.get("first_name","UnKnown"))
	if request.method == "POST":
		p=SearchForm(request.POST)
		if p.is_valid():
			q=p.cleaned_data
			name=q['search_str']
			p=Products.manager.product_name_startswith(name)
			return render(request,"product.html",{"product":p,"search":SearchForm(),"media":settings.MEDIA_URL,"media_root":settings.MEDIA_ROOT})
	else:
		p=Products.manager.all()
	return render(request,'product.html' , {"product":p,"search":SearchForm(),"media":settings.MEDIA_URL,"media_root":settings.MEDIA_ROOT})

def product(request):
	if request.method=="POST":
		p=SearchForm(request.POST)
		if p.is_valid():
			q=p.cleaned_data
			name=q['search_str']
			p=Products.manager.product_name_startswith(name)
			return render(request,"product.html",{"product":p,"search":SearchForm(),"media":settings.MEDIA_URL,"media_root":settings.MEDIA_ROOT})
	else:
		p=Products.manager.all()
	return render(request,'product.html' , {"product":p,"search":SearchForm(),"media":settings.MEDIA_URL,"media_root":settings.MEDIA_ROOT})

def stationary(request):
	name	=	"stationary"
	p=Products.manager.product_type_fullmatch(name)
	if request.method=="POST":
		p=SearchForm(request.POST)
		if p.is_valid():
			q=p.cleaned_data
			name=q['search_str']
			p=Products.manager.product_name_startswith(name)
			return render(request,"product.html",{"product":p,"search":SearchForm(),"media":settings.MEDIA_URL,"media_root":settings.MEDIA_ROOT})
	else:
		name	=	"stationary"
		p=Products.manager.product_type_fullmatch(name)
	return render(request,"product.html",{"product":p,"media":settings.MEDIA_URL,"media_root":settings.MEDIA_ROOT})

def electronic(request):
	p=Products.manager.product_type_fullmatch("electronic")
	if request.method=="POST":
		p=SearchForm(request.POST)
		if p.is_valid():
			q=p.cleaned_data
			name=q['search_str']
			p=Products.manager.product_name_startswith(name)
			return render(request,"product.html",{"product":p,"search":SearchForm(),"media":settings.MEDIA_URL,"media_root":settings.MEDIA_ROOT})
	else:
		p=Products.manager.product_type_fullmatch("electronic")
	return render(request,"product.html",{"product":p,"media":settings.MEDIA_URL,"media_root":settings.MEDIA_ROOT})

def kitchen(request):
	p=Products.manager.product_type_fullmatch("kitchenneeds")
	if request.method=="POST":
		p=SearchForm(request.POST)
		if p.is_valid():
			q=p.cleaned_data
			name=q['search_str']
			p=Products.manager.product_name_startswith(name)
			return render(request,"product.html",{"product":p,"search":SearchForm(),"media":settings.MEDIA_URL,"media_root":settings.MEDIA_ROOT})
	else:
		p=Products.manager.product_type_fullmatch("kitchenneeds")
	return render(request,"product.html",{"product":p,"media":settings.MEDIA_URL,"media_root":settings.MEDIA_ROOT})

def homeneeds(request):
	p=Products.manager.product_type_fullmatch("homeneeds")
	if request.method=="POST":
		p=SearchForm(request.POST)
		if p.is_valid():
			q=p.cleaned_data
			name=q['search_str']
			p=Products.manager.product_name_startswith(name)
			return render(request,"product.html",{"product":p,"search":SearchForm(),"media":settings.MEDIA_URL,"media_root":settings.MEDIA_ROOT})
	else:
		p=Products.manager.product_type_fullmatch("homeneeds")
	return render(request,"product.html",{"product":p,"media":settings.MEDIA_URL,"media_root":settings.MEDIA_ROOT})

def footwear(request):
	p=Products.manager.product_type_fullmatch("footwear")
	if request.method=="POST":
		p=SearchForm(request.POST)
		if p.is_valid():
			q=p.cleaned_data
			name=q['search_str']
			p=Products.manager.product_name_startswith(name)
			return render(request,"product.html",{"product":p,"search":SearchForm(),"media":settings.MEDIA_URL,"media_root":settings.MEDIA_ROOT})
	else:
		p=Products.manager.product_type_fullmatch("footwear")
	return render(request,"product.html",{"product":p,"media":settings.MEDIA_URL,"media_root":settings.MEDIA_ROOT})
def fashion(request):
	p=Products.manager.product_type_fullmatch("fashion")
	if request.method=="POST":
		p=SearchForm(request.POST)
		if p.is_valid():
			q=p.cleaned_data
			name=q['search_str']
			p=Products.manager.product_name_startswith(name)
			return render(request,"product.html",{"product":p,"search":SearchForm(),"media":settings.MEDIA_URL,"media_root":settings.MEDIA_ROOT})
	else:
		p=Products.manager.product_type_fullmatch("fashion")
	return render(request,"product.html",{"product":p,"media":settings.MEDIA_URL,"media_root":settings.MEDIA_ROOT})

def customer(request):
	first_name		=	""
	middle_name		=	""
	last_name		=	""
	gender			=	""
	mail_id			=	""
	mobile_number	=	""
	if request.method=='POST':
		c=CustomerForm(request.POST)
		if c.is_valid():
			z=c.cleaned_data
			Customer(first_name=z['first_name'],middle_name=z['middle_name'],last_name=z['last_name'],gender=z['gender'],mail_id=z['mail_id'],mobile_number=z['mobile_number'],address=z['address']).save()
			return HttpResponseRedirect("/home/")
	else:
		c=CustomerForm()
	return render_to_response("customerform.html",{ 'form':c})