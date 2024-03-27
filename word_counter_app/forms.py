from django import forms

CHOICES = [("old", "Old"), ("new", "New"), ]

BIRTH_YEAR_CHOICES = ["2023", "2024"]


class TextForm(forms.Form):
    text_input = forms.CharField(
        label='Enter your text',
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 50})
    )


class UserForm(forms.Form):
    name = forms.CharField(label="Your name")
    email = forms.EmailField(label="Your email", help_text="A valid email address, please.")
    comment = forms.CharField(label="Your comment", widget=forms.Textarea)
    invoice_date = forms.DateField(label="Invoice date",
                                   widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    choice_field = forms.ChoiceField(label="Your choice",
                                     widget=forms.RadioSelect, choices=CHOICES, help_text="Choose old or a new user")
