from django import forms

from cinema.models import Country, Actor


class MovieForm(forms.ModelForm):
    GENRE_CHOICES = (
        ('драма', 'драма'),
        ('історичний', 'історичний'),
        ('комедія', 'комедія'),
        ('романтичний', 'романтичний'),
        ('трилер', 'трилер'),
        ('кримінальний', 'кримінальний'),
        ('мюзикл', 'мюзикл'),
        ('анімація', 'анімація'),
    )
    title = forms.CharField(max_length=200)
    description = forms.CharField(max_length=600)
    contrives = forms.ModelMultipleChoiceField(queryset=Country.objects)
    actors = forms.ModelMultipleChoiceField(queryset=Actor.objects)
    genre = forms.MultipleChoiceField(choices=GENRE_CHOICES)
    duration = forms.IntegerField(min_value=15, max_value=180)  # in minutes
    poster = forms.ImageField()

