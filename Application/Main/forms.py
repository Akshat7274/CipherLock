from django import forms

class CaesarForm(forms.Form):
    key = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "form-control",
        'placeholder' : "Secret Key",
        'autocomplete' : "off",
        'min' : 1,
        'max' : 25
    }), required=True)
    pt = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "form-control",
        'placeholder' : "Plaintext",
        'autocomplete' : "off"
    }), required=False)
    ct = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "form-control",
        'placeholder' : "Ciphertext",
        'autocomplete' : "off"
    }), required=False)

class PlayfairForm(forms.Form):
    key = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "form-control",
        'placeholder' : "Secret Key",
        'autocomplete' : "off",
        'oninput' : "this.value=this.value.toLowerCase()"
    }), required=True)
    pt = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "form-control",
        'placeholder' : "Plaintext",
        'autocomplete' : "off",
        'oninput' : "this.value=this.value.toLowerCase()"
    }), required=False)
    ct = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "form-control",
        'placeholder' : "Ciphertext",
        'autocomplete' : "off"
    }), required=False)

class HillForm(forms.Form):
    key = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "form-control",
        'placeholder' : "Secret Key",
        'autocomplete' : "off",
        'oninput' : "this.value=this.value.toLowerCase()"
    }), required=True)
    pt = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "form-control",
        'placeholder' : "Plaintext",
        'autocomplete' : "off",
        'oninput' : "this.value=this.value.toLowerCase()"
    }), required=False)
    ct = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "form-control",
        'placeholder' : "Ciphertext",
        'autocomplete' : "off"
    }), required=False)

class VigenereForm(forms.Form):
    key = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "form-control",
        'placeholder' : "Secret Key",
        'autocomplete' : "off",
        'oninput' : "this.value=this.value.toLowerCase()"
    }), required=True)
    pt = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "form-control",
        'placeholder' : "Plaintext",
        'autocomplete' : "off",
    }), required=False)
    ct = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "form-control",
        'placeholder' : "Ciphertext",
        'autocomplete' : "off"
    }), required=False)

class VernamForm(forms.Form):
    key = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "form-control",
        'placeholder' : "Secret Key",
        'autocomplete' : "off",
        'oninput' : "this.value=this.value.toLowerCase()"
    }), required=True)
    pt = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "form-control",
        'placeholder' : "Plaintext",
        'autocomplete' : "off",
        'oninput' : "this.value=this.value.toLowerCase()"
    }), required=False)
    ct = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "form-control",
        'placeholder' : "Ciphertext",
        'autocomplete' : "off"
    }), required=False)

class RailfenceForm(forms.Form):
    key = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "form-control",
        'placeholder' : "Secret Key",
        'autocomplete' : "off",
        'min' : 1
    }), required=True)
    pt = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "form-control",
        'placeholder' : "Plaintext",
        'autocomplete' : "off"
    }), required=False)
    ct = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "form-control",
        'placeholder' : "Ciphertext",
        'autocomplete' : "off"
    }), required=False)