from django import forms

class RollNumberForm(forms.Form):
    roll_no = forms.CharField(
        label="",
        max_length=10,
        widget=forms.TextInput(attrs={"placeholder": "e.g : 1,2,."})
    )
