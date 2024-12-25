from django import forms

class AppointmentForm(forms.Form):
    name = forms.CharField(max_length=100, label="Имя")
    phone = forms.CharField(max_length=15, label="Номер телефона")
    date = forms.DateTimeField(
        label="Дата и время",
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )