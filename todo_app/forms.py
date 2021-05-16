from django import forms

def first_symbol_must_be_D_validator(value):
    if not value or not value[0] == "D":
        raise forms.ValidationError(f"Description should start with 'D' now it starts with {value[0]}")

class TodoForm(forms.Form):
    name = forms.CharField(
        max_length=30,
        min_length=2,
        )
    description = forms.CharField(
        widget=forms.Textarea(),
        validators= (
            first_symbol_must_be_D_validator,
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for _,field in self.fields.items():
            if 'class' in field.widget.attrs:
                value = field.widget.attrs['class'] + 'form-control'
            else:
                value = 'form-control'
            field.widget.attrs['class'] = value

