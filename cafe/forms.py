from django import forms
from .models import Inquiry


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ('name', 'email', 'message')

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '이름'}),
            'email': forms.EmailInput(attrs={'placeholder': '이메일'}),
            'message': forms.Textarea(attrs={'placeholder': '문의할 내용을 입력하세요.'})
        }

        labels = {
            'name': '',
            'email': '',
            'message': ''
        }
