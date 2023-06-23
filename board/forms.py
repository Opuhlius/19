from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'post_text']

    CATEGORY_CHOICES = [
        ('TK', 'Tanks'),
        ('HL', 'Hils'),
        ('DD', 'DD'),
        ('TD', 'Trades'),
        ('GM', 'Gildmasters'),
        ('QG', 'Quaestgilders'),
        ('SM', 'Smitses'),
        ('TN', 'Tanners'),
        ('HM', 'Herbmakers'),
        ('WZ', 'Wizards'),
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES)