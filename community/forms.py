from django import forms
from .models import Post,Category

#cats= [('cosmetic','cosmetic'),('womens','womens'),('children','children'),('organic','organic')]
choices = Category.objects.all().values_list('name','name')
choice_list = []
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=('title','category','text','image',)

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','placeholder': "제목을 입력해 주세요", 'style':'width: 777px;'}),
            'category' : forms.Select(choices=choices,attrs={'class':'form-control','placeholder':'choose a category', 'style':'width: 112px;'},),
            'text': forms.Textarea(attrs={'class':'form-control', 'placeholder': "내용을 입력해 주세요", 'style':'width: 777px;',
            'rows': 15}),
        }