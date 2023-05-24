from django import forms 


class ContatoForm(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea)
    