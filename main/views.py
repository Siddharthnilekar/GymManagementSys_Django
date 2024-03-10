from django.shortcuts import render
from . import models
from . import forms

#home
def home(request):
    banners=models.Banners.objects.all()
    services=models.Service.objects.all()[:3]
    gimgs=models.GalleryImage.objects.all().order_by('-id')[:9]
    return render(request, 'home.html',{'banners':banners, 'services':services,'gimgs':gimgs})

# PageDetail
def page_detail(request,id):
    page=models.Page.objects.get(id=id)
    return render(request, 'page.html',{'page':page})

# FAQ
def faq_list(request):
    faq=models.Faq.objects.all()
    return render(request, 'faq.html',{'faqs':faq})

# Enquiry
def enquiry(request):
    msg=''
    if request.method=='POST':
        form=forms.EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            msg='Data has been saved'
    form=forms.EnquiryForm
    return render(request, 'enquiry.html',{'form':form,'msg':msg})

# Show galleries
def gallery(request):
	gallery=models.Gallery.objects.all().order_by('-id')
	return render(request, 'gallery.html',{'gallerys':gallery})

# Show gallery photos
def gallery_detail(request,id):
	gallery=models.Gallery.objects.get(id=id)
	gallery_imgs=models.GalleryImage.objects.filter(gallery=gallery).order_by('-id')
	return render(request, 'gallery_imgs.html',{'gallery_imgs':gallery_imgs,'gallery':gallery})

# Subscription Plans
def pricing(request):
    #  annotate(total_members=Count('subscription__id'))..order_by('price')
	pricing=models.SubPlan.objects.all()
	dfeatures=models.SubPlanFeature.objects.all()
	return render(request, 'pricing.html',{'plans':pricing,'dfeatures':dfeatures})


