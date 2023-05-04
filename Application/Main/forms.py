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
    key = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "form-control",
        'placeholder' : "Generated Key",
        'autocomplete' : "off"
    }), required=False)

class ElGamalForm(forms.Form):
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
        'placeholder' : "Sender's Private Key",
        'autocomplete' : "off"
    }), required=False)
    ya = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "form-control",
        'placeholder' : "Sender's Public Key",
        'autocomplete' : "off"
    }), required=False)
    m = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "form-control",
        'placeholder' : "Hash Value",
        'autocomplete' : "off"
    }), required=False)
    k = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "form-control",
        'placeholder' : "Random No.",
        'autocomplete' : "off"
    }), required=False)
    ki = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "form-control",
        'placeholder' : "Random No. Inverse",
        'autocomplete' : "off"
    }), required=False)
    s1 = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "form-control",
        'placeholder' : "Sign Part 1",
        'autocomplete' : "off"
    }), required=False)
    s2 = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "form-control",
        'placeholder' : "Sign Part 2",
        'autocomplete' : "off"
    }), required=False)
    v1 = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "form-control",
        'placeholder' : "Verification 1",
        'autocomplete' : "off"
    }), required=False)
    v2 = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "form-control",
        'placeholder' : "Verification 2",
        'autocomplete' : "off"
    }), required=False)
    verify = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "form-control",
        'placeholder' : "Verification Status",
        'autocomplete' : "off"
    }), required=False)

bits = [(4,"4"),(8,"8"),(16,"16"),(32,"32"),(64,"64"),(128,"128"),(256,"256"),(512,"512"),(1024,"1024"),(2048,"2048"),(4096,"4096")]

class RSAForm(forms.Form):
    b = forms.IntegerField(widget=forms.Select(attrs={
        'class' : "form-control",
        'placeholder' : "Bits",
        'autocomplete' : "off"
    }, choices = bits), 
    required = True,
    )
    m = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "form-control",
        'placeholder' : "Message",
        'autocomplete' : "off"
    }), required=True)
    p = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "form-control",
        'placeholder' : "Prime Number 1",
        'autocomplete' : "off",
        'rows' : 2
    }), required=False)
    q = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "form-control",
        'placeholder' : "Prime Number 2",
        'autocomplete' : "off",
        'rows' : 2
    }), required=False)
    n = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "form-control",
        'placeholder' : "n = p * q",
        'autocomplete' : "off",
        'rows' : 2
    }), required=False)
    phi = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "form-control",
        'placeholder' : "φ(n) = (p-1) * (q-1)",
        'autocomplete' : "off",
        'rows' : 2
    }), required=False)
    e = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "form-control",
        'placeholder' : "Public Key for Encryption (e)",
        'autocomplete' : "off",
        'rows' : 2
    }), required=False)
    d = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "form-control",
        'placeholder' : "Private Key for Encryption (d)",
        'autocomplete' : "off",
        'rows' : 2
    }), required=False)
    enc = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "form-control",
        'placeholder' : "Encrypted Message",
        'autocomplete' : "off",
        'rows' : 2
    }), required=False)
    dec = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "form-control",
        'placeholder' : "Decrypted Message",
        'autocomplete' : "off",
        'rows' : 2
    }), required=False)