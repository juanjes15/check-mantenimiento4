from django import forms
from .models import Usuario, Equipo, Software, Driver, Revision


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        exclude = ["equipo"]


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = "__all__"


class SoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        exclude = ["equipo"]


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        exclude = ["equipo"]


class RevisionForm(forms.ModelForm):
    class Meta:
        model = Revision
        exclude = ["equipo"]
