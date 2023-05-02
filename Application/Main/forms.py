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

class RCTForm(forms.Form):
    key = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "form-control",
        'placeholder' : "Secret Key",
        'autocomplete' : "off"
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

class DESForm(forms.Form):
    key = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "form-control",
        'placeholder' : "Secret Key",
        'autocomplete' : "off"
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

class AESForm(forms.Form):
    key = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "form-control",
        'placeholder' : "Secret Key",
        'autocomplete' : "off"
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

class DFForm(forms.Form):
    q = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "form-control",
        'placeholder' : "Prime Number",
        'autocomplete' : "off",
        'min' : 2,
        'max' : 500,
    }), required=True)
    a = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "form-control",
        'placeholder' : "Primitive Root",
        'autocomplete' : "off"
    }), required=True)
    xa = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "form-control",
        'placeholder' : "A's Private Key",
        'autocomplete' : "off"
    }), required=False)
    xb = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "form-control",
        'placeholder' : "B's Private Key",
        'autocomplete' : "off"
    }), required=False)
    ya = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "form-control",
        'placeholder' : "A's Public Key",
        'autocomplete' : "off"
    }), required=False)
    yb = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "form-control",
        'placeholder' : "B's Public Key",
        'autocomplete' : "off"
    }), required=False)
    key = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "form-control",
        'placeholder' : "Generated Key",
        'autocomplete' : "off"
    }), required=False)