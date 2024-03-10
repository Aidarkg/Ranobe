from django import forms
from book import models


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = models.Book2
        fields = ['file', 'photo', 'years_of_release']
        widgets = {
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'years_of_release': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if models.Book2.objects.filter(file=file).exists():
            raise forms.ValidationError('Такая книга уже существует')
        return file