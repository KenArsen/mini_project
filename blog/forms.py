from django import forms
from .models import Post, Category


class CreatePostForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.none(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        required=True,
        label="Категории",
        help_text="Выберите одну или несколько категорий"
    )

    class Meta:
        model = Post
        fields = ['category', 'title', 'description', 'content', 'art_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Введите контент'}),
            'art_image': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()
