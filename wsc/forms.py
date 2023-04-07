from django import forms


class BusquedaForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BusquedaForm, self).__init__(*args, **kwargs)
        self.fields['url_a_buscar'].widget.attrs['class'] = 'form-control'
    url_a_buscar = forms.URLField(label="Url a buscar", max_length=300)