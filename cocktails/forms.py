from django import forms

from cocktails.models import Cocktail


class CocktailForm(
    forms.ModelForm
):
    class Meta:
        model = Cocktail
        fields = "__all__"
