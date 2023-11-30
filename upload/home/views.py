from django.shortcuts import render, redirect
from django.views import View
from .forms import UploadImageForm
from .models import UploadImage
from django.utils.text import slugify
from django.contrib import messages


# Create your views here.


class HomeView(View):
    form_class = UploadImageForm

    def get(self, request):
        form = self.form_class()
        picture = UploadImage.objects.all()
        return render(request, 'home/index.html', {'form': form, 'picture': picture})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            UploadImage(title=cd['title'], image=request.FILES['image'],
                        slug=slugify(cd['title'][:50])).save()
            messages.success(request, "پست جدید آپلود شد", 'success')
            return redirect('home:home')



