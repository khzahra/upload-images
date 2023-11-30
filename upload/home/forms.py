from django import forms


class UploadImageForm(forms.Form):
    title = forms.CharField(label="عنوان")
    image = forms.ImageField(label="تصویر")
    body = forms.CharField(label="متن")

