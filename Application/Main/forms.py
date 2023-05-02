from django import forms

class CaesarForm(forms.Form):
    key = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "form-control",
        'placeholder' : "Secret Key",
        'autocomplete' : "off"
    }), required=True)
    pt = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "form-control",
        'placeholder' : "Plaintext",
        'autocomplete' : "off"
    }), required=False)
    ct = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "form-control",
        'placeholder' : "Ciphertext",
        'autocomplete' : "off"
    }), required=False)