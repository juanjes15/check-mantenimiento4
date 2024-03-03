from django.forms import (
    ModelForm,
    ImageField,
    TextInput,
    DateInput,
    RadioSelect,
    Textarea,
    FileInput,
)
from .models import Usuario, Equipo, Software, Driver, Revision


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        exclude = ["equipo"]
        widgets = {
            "nombre": TextInput(attrs={"class": "form-control"}),
            "fecha_intervencion": DateInput(
                format=("%Y-%m-%d"), attrs={"type": "date", "class": "form-control"}
            ),
            "ciudad": TextInput(attrs={"class": "form-control"}),
            "telefono": TextInput(attrs={"class": "form-control"}),
            "usuario_red": TextInput(attrs={"class": "form-control"}),
            "activo": TextInput(attrs={"class": "form-control"}),
        }


class EquipoForm(ModelForm):
    input_in_front = ImageField(
        required=False,
        widget=FileInput(attrs={"class": "form-control"}),
        label="Foto de entrada - Frente",
    )
    input_in_back = ImageField(
        required=False,
        widget=FileInput(attrs={"class": "form-control"}),
        label="Foto de entrada - Detrás",
    )
    input_in_right1 = ImageField(
        required=False,
        widget=FileInput(attrs={"class": "form-control"}),
        label="Foto de entrada - Derecha 1",
    )
    input_in_right2 = ImageField(
        required=False,
        widget=FileInput(attrs={"class": "form-control"}),
        label="Foto de entrada - Derecha 2",
    )
    input_in_left1 = ImageField(
        required=False,
        widget=FileInput(attrs={"class": "form-control"}),
        label="Foto de entrada - Izquierda 1",
    )
    input_in_left2 = ImageField(
        required=False,
        widget=FileInput(attrs={"class": "form-control"}),
        label="Foto de entrada - Izquierda 2",
    )

    class Meta:
        model = Equipo
        exclude = [
            "photo_in_front",
            "photo_in_back",
            "photo_in_right1",
            "photo_in_right2",
            "photo_in_left1",
            "photo_in_left2",
        ]
        widgets = {
            "tipo": TextInput(attrs={"class": "form-control"}),
            "marca": TextInput(attrs={"class": "form-control"}),
            "modelo": TextInput(attrs={"class": "form-control"}),
            "serial": TextInput(attrs={"class": "form-control"}),
            "estado": RadioSelect(),
            "sistema_operativo": TextInput(attrs={"class": "form-control"}),
            "estado_hdd": RadioSelect(),
            "ram": TextInput(attrs={"class": "form-control"}),
            "tipo_procesador": TextInput(attrs={"class": "form-control"}),
            "estado_fisico": Textarea(
                attrs={"class": "form-control", "style": "height: 100px"}
            ),
            "siniestro": RadioSelect(),
        }


class SoftwareForm(ModelForm):
    class Meta:
        model = Software
        exclude = ["equipo"]
        widgets = {
            "des_office": RadioSelect(),
            "des_chrome": RadioSelect(),
            "des_teams": RadioSelect(),
            "del_temp": RadioSelect(),
            "dfg_dd": RadioSelect(),
            "del_temp2": RadioSelect(),
            "del_prefetch": RadioSelect(),
            "conf_msconfig": RadioSelect(),
            "sfc_scannow": RadioSelect(),
            "win_22h2": RadioSelect(),
        }


class DriverForm(ModelForm):
    class Meta:
        model = Driver
        exclude = ["equipo"]
        widgets = {
            "diag_tool": RadioSelect(),
            "diag_tool_desc": Textarea(
                attrs={"class": "form-control", "style": "height: 100px"}
            ),
            "upd_bios": RadioSelect(),
            "upd_bios_ver": TextInput(attrs={"class": "form-control"}),
            "upd_bios_desc": Textarea(
                attrs={"class": "form-control", "style": "height: 100px"}
            ),
            "upd_all": RadioSelect(),
            "upd_all_desc": Textarea(
                attrs={"class": "form-control", "style": "height: 100px"}
            ),
            "upd_audio": RadioSelect(),
            "upd_video": RadioSelect(),
            "upd_wifi": RadioSelect(),
            "upd_ethernet": RadioSelect(),
            "upd_almacenamiento": RadioSelect(),
            "upd_chipset": RadioSelect(),
            "upd_camara": RadioSelect(),
            "upd_mouse": RadioSelect(),
            "exe_all": RadioSelect(),
            "observaciones": Textarea(
                attrs={"class": "form-control", "style": "height: 100px"}
            ),
        }


class RevisionForm(ModelForm):
    input_out_front = ImageField(
        required=False,
        widget=FileInput(attrs={"class": "form-control"}),
        label="Foto de salida - Frente",
    )
    input_out_back = ImageField(
        required=False,
        widget=FileInput(attrs={"class": "form-control"}),
        label="Foto de salida - Detrás",
    )
    input_out_right1 = ImageField(
        required=False,
        widget=FileInput(attrs={"class": "form-control"}),
        label="Foto de salida - Derecha 1",
    )
    input_out_right2 = ImageField(
        required=False,
        widget=FileInput(attrs={"class": "form-control"}),
        label="Foto de salida - Derecha 2",
    )
    input_out_left1 = ImageField(
        required=False,
        widget=FileInput(attrs={"class": "form-control"}),
        label="Foto de salida - Izquierda 1",
    )
    input_out_left2 = ImageField(
        required=False,
        widget=FileInput(attrs={"class": "form-control"}),
        label="Foto de salida - Izquierda 2",
    )

    class Meta:
        model = Revision
        exclude = [
            "photo_out_front",
            "photo_out_back",
            "photo_out_right1",
            "photo_out_right2",
            "photo_out_left1",
            "photo_out_left2",
            "equipo",
        ]
        widgets = {
            "teclado": RadioSelect(),
            "pantalla": RadioSelect(),
            "sonido": RadioSelect(),
            "camara": RadioSelect(),
            "touchpad": RadioSelect(),
            "wifi": RadioSelect(),
            "video_hdmi_vga": RadioSelect(),
            "internet": RadioSelect(),
            "apps_cliente": RadioSelect(),
            "headset": RadioSelect(),
            "limpieza": RadioSelect(),
            "funciona": RadioSelect(),
            "funciona_desc": Textarea(
                attrs={"class": "form-control", "style": "height: 100px"}
            ),
            "observaciones": Textarea(
                attrs={"class": "form-control", "style": "height: 300px"}
            ),
        }
