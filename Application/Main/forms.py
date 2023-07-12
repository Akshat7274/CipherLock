from django import forms

class CaesarForm(forms.Form):
    key = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "col-lg-4 post-tester",
        'placeholder' : "Secret Shift Key",
        'autocomplete' : "off",
        'min' : 1,
        'max' : 25
    }), required=True)
    pt = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "col-lg-6",
        'id' : "enc-input",
        'placeholder' : "Plaintext",
        'autocomplete' : "off",
        'rows' : "3"
    }), required=False)
    ct = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "col-lg-6",
        'id' : "dec-input",
        'placeholder' : "Ciphertext",
        'autocomplete' : "off",
        'rows' : 3
    }), required=False)

class PlayfairForm(forms.Form):
    key = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "col-lg-4 post-tester",
        'placeholder' : "Secret Key",
        'autocomplete' : "off",
        'oninput' : "this.value=this.value.toLowerCase()",
        'pattern' : "[a-zA-Z]+",
        'oninvalid' : "setCustomValidity('Secret key can only contain alphabets')"
    }), required=True)
    pt = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "col-lg-6",
        'id' : "enc-input",
        'placeholder' : "Plaintext",
        'autocomplete' : "off",
        'oninput' : "this.value=this.value.toLowerCase()",
        'rows' : 3
    }), required=False)
    ct = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "col-lg-6",
        'id' : "dec-input",
        'placeholder' : "Ciphertext",
        'autocomplete' : "off",
        'rows' : 3
    }), required=False)

class HillForm(forms.Form):
    key = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "col-lg-4 post-tester",
        'placeholder' : "Secret Key",
        'autocomplete' : "off",
        'oninput' : "this.value=this.value.toLowerCase()",
        'pattern' : "[a-zA-Z]+",
        'oninvalid' : "setCustomValidity('Secret key can only contain alphabets')"
    }), required=True)
    pt = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "col-lg-6",
        'id' : "enc-input",
        'placeholder' : "Plaintext",
        'autocomplete' : "off",
        'oninput' : "this.value=this.value.toLowerCase()", 
        'rows' : 3
    }), required=False)
    ct = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "col-lg-6",
        'id' : "dec-input",
        'placeholder' : "Ciphertext",
        'autocomplete' : "off",
        'rows' : 3
    }), required=False)

class VigenereForm(forms.Form):
    key = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "col-lg-4 post-tester",
        'placeholder' : "Secret Key",
        'autocomplete' : "off",
        'oninput' : "this.value=this.value.toLowerCase()",
        'pattern' : "[a-zA-Z]+",
        'oninvalid' : "setCustomValidity('Secret key can only contain alphabets')"
    }), required=True)
    pt = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "col-lg-6",
        'id' : "enc-input",
        'placeholder' : "Plaintext",
        'autocomplete' : "off",
        'rows' : 3
    }), required=False)
    ct = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "col-lg-6",
        'id' : "dec-input",
        'placeholder' : "Ciphertext",
        'autocomplete' : "off", 
        'rows' : 3
    }), required=False)

class VernamForm(forms.Form):
    key = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "col-lg-4 post-tester",
        'placeholder' : "Secret Key",
        'autocomplete' : "off",
        'oninput' : "this.value=this.value.toLowerCase()",
        'pattern' : "[a-zA-Z]+",
        'oninvalid' : "setCustomValidity('Secret key can only contain alphabets')"
    }), required=True)
    pt = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "col-lg-6",
        'id' : "enc-input",
        'placeholder' : "Plaintext",
        'autocomplete' : "off",
        'oninput' : "this.value=this.value.toLowerCase()",
        'rows' : 3
    }), required=False)
    ct = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "col-lg-6",
        'id' : "dec-input",
        'placeholder' : "Ciphertext",
        'autocomplete' : "off",
        'rows' : 3
    }), required=False)

class RailfenceForm(forms.Form):
    key = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "col-lg-4 post-tester",
        'placeholder' : "Secret Key (No. of Rails)",
        'autocomplete' : "off",
        'min' : 1
    }), required=True)
    pt = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "col-lg-6",
        'id' : "enc-input",
        'placeholder' : "Plaintext",
        'autocomplete' : "off",
        'rows' : 3
    }), required=False)
    ct = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "col-lg-6",
        'id' : "dec-input",
        'placeholder' : "Ciphertext",
        'autocomplete' : "off",
        'rows' : 3
    }), required=False)

class RCTForm(forms.Form):
    key = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "col-lg-4 post-tester",
        'placeholder' : "Secret Key",
        'autocomplete' : "off"
    }), required=True)
    pt = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "col-lg-6",
        'id' : "enc-input",
        'placeholder' : "Plaintext",
        'autocomplete' : "off",
        'rows' : 3
    }), required=False)
    ct = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "col-lg-6",
        'id' : "dec-input",
        'placeholder' : "Ciphertext",
        'autocomplete' : "off",
        'rows' : 3
    }), required=False)

class DESForm(forms.Form):
    key = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "col-lg-4 post-tester",
        'placeholder' : "Secret Key",
        'autocomplete' : "off"
    }), required=True)
    pt = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "col-lg-6",
        'id' : "enc-input",
        'placeholder' : "Plaintext",
        'autocomplete' : "off",
        'rows' : 3
    }), required=False)
    ct = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "col-lg-6",
        'id' : "dec-input",
        'placeholder' : "Ciphertext",
        'autocomplete' : "off",
        'rows' : 3
    }), required=False)

class AESForm(forms.Form):
    key = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "col-lg-4 post-tester",
        'placeholder' : "Secret Key",
        'autocomplete' : "off"
    }), required=True)
    pt = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "col-lg-6",
        'id' : "enc-input",
        'placeholder' : "Plaintext",
        'autocomplete' : "off",
        'rows' : 3
    }), required=False)
    ct = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "col-lg-6",
        'id' : "dec-input",
        'placeholder' : "Ciphertext",
        'autocomplete' : "off",
        'rows' : 3
    }), required=False)

class DFForm(forms.Form):
    q = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "col-lg-4 post-tester",
        'id' : "prime",
        'placeholder' : "Prime Number",
        'autocomplete' : "off",
        'min' : 2,
        'max' : 500,
    }), required=True)
    a = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "col-lg-4",
        'placeholder' : "Primitive Root",
        'autocomplete' : "off"
    }), required=True)
    xa = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "col-lg-4",
        'id' : "a-priv",
        'placeholder' : "A's Private Key",
        'autocomplete' : "off"
    }), required=True)
    xb = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "col-lg-4",
        'id' : "b-priv",
        'placeholder' : "B's Private Key",
        'autocomplete' : "off"
    }), required=True)

class ElGamalForm(forms.Form):
    q = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "col-lg-4 post-tester",
        'id' : "prime",
        'placeholder' : "Prime Number",
        'autocomplete' : "off",
        'min' : 2,
        'max' : 500,
    }), required=True)
    a = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "col-lg-4",
        'placeholder' : "Primitive Root",
        'autocomplete' : "off"
    }), required=True)
    xa = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "col-lg-4",
        'id' : "s-priv",
        'placeholder' : "Sender's Private Key",
        'autocomplete' : "off"
    }), required=False)  
    k = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : "col-lg-4",
        'id' : "rnd",
        'placeholder' : "Random No.",
        'autocomplete' : "off"
    }), required=False)
    m = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "col-lg-4",
        'placeholder' : "Message",
        'autocomplete' : "off",
        'rows' : 3
    }), required=True)
    verify = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "col-lg-4",
        'placeholder' : "Signature",
        'autocomplete' : "off",
        'rows' : 1
    }), required=False)

bits = [(-1,"SELECT NO. OF BITS"),(4,"4"),(8,"8"),(16,"16"),(32,"32"),(64,"64"),(128,"128"),(256,"256"),(512,"512"),(1024,"1024"),(2048,"2048"),(4096,"4096")]

class RSAForm(forms.Form):
    b = forms.IntegerField(widget=forms.Select(attrs={
        'class' : "col-lg-3 post-tester",
        'placeholder' : "Bits",
        'autocomplete' : "off"
    }, choices = bits), 
    required = True,
    )
    m = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "col-lg-4",
        'id' : "enc-input",
        'placeholder' : "Message",
        'autocomplete' : "off",
        'rows' : 1
    }), required=False)
    p = forms.CharField(widget=forms.Textarea(attrs={
        'id' : "inp-p"
    }), required=False)
    q = forms.CharField(widget=forms.Textarea(attrs={
        'id' : "inp-q"
    }), required=False)
    gen = forms.IntegerField(widget=forms.NumberInput(attrs={
        'id' : "key-gen",
        'value' : 0
    }))
    e = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "col-lg-3",
        'id' : "priv-key",
        'placeholder' : "Public Key for Encryption (e)",
        'autocomplete' : "off",
        'rows' : 1
    }), required=False)
    enc = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "col-lg-4",
        'id' : "dec-input",
        'placeholder' : "Encrypted Text",
        'autocomplete' : "off",
        'rows' : 1
    }), required=False)