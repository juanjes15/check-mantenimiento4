from django.db.models import (
    Model,
    URLField,
    CharField,
    BooleanField,
    TextField,
    OneToOneField,
    DateField,
    CASCADE,
)


class Equipo(Model):
    photo_in_front = URLField(max_length=150)
    photo_in_back = URLField(max_length=150)
    photo_in_right1 = URLField(max_length=150)
    photo_in_right2 = URLField(max_length=150)
    photo_in_left1 = URLField(max_length=150)
    photo_in_left2 = URLField(max_length=150)
    tipo = CharField(max_length=20, verbose_name="TIPO*")
    marca = CharField(max_length=20, verbose_name="MARCA*")
    modelo = CharField(max_length=15, verbose_name="MODELO*")
    serial = CharField(max_length=15, verbose_name="SERIAL*", unique=True)
    estado = BooleanField(
        null=True,
        verbose_name="ESTADO ACTUAL DEL EQUIPO*",
        choices=((True, "Bueno"), (False, "Falla")),
    )
    sistema_operativo = CharField(
        max_length=15, verbose_name="SISTEMA OPERATIVO INSTALADO*"
    )
    estado_hdd = BooleanField(
        null=True,
        verbose_name="ESTADO DISCO DURO*",
        choices=((True, "Bueno"), (False, "Malo")),
    )
    ram = CharField(max_length=10, verbose_name="RAM ACTUAL*")
    tipo_procesador = CharField(max_length=15, verbose_name="TIPO PROCESADOR*")
    estado_fisico = TextField(blank=True, verbose_name="ESTADO FISICO")
    siniestro = BooleanField(
        null=True, verbose_name="SINIESTRO*", choices=((True, "SI"), (False, "NO"))
    )

    class Meta:
        ordering = ["serial"]


class Usuario(Model):
    nombre = CharField(max_length=100, verbose_name="NOMBRE USUARIO FINAL*")
    fecha_intervencion = DateField(null=True, verbose_name="FECHA INTERVENCIÓN*")
    ciudad = CharField(max_length=50, verbose_name="CIUDAD*")
    telefono = CharField(max_length=10, verbose_name="TELEFONO CONTACTO*")
    usuario_red = CharField(
        max_length=50, verbose_name="USUARIO DE RED, CLAVE DE USUARIO*"
    )
    activo = CharField(max_length=20, verbose_name="ACTIVO*")
    equipo = OneToOneField(Equipo, on_delete=CASCADE)


class Software(Model):
    des_office = BooleanField(
        null=True,
        verbose_name="VALIDAR DESACELERACION GRAFICA DE OFFICE 365*",
        choices=((True, "SI"), (False, "NO")),
    )
    des_chrome = BooleanField(
        null=True,
        verbose_name="VALIDAR DESACELERACION GRAFICA DE GOOGLE CHROME*",
        choices=((True, "SI"), (False, "NO")),
    )
    des_teams = BooleanField(
        null=True,
        verbose_name="VALIDAR DESACELERACION GRAFICA DE MICROSOFT TEAMS*",
        choices=((True, "SI"), (False, "NO")),
    )
    del_temp = BooleanField(
        null=True,
        verbose_name="ELIMINAR TEMPORALES DE WINDOWS (TEMP)*",
        choices=((True, "SI"), (False, "NO")),
    )
    dfg_dd = BooleanField(
        null=True,
        verbose_name="DESFRAGMENTAR EL DISCO (ANALIZAR - OPTIMIZAR) HDD-SSD*",
        choices=((True, "SI"), (False, "NO")),
    )
    del_temp2 = BooleanField(
        null=True,
        verbose_name="ELIMINAR TEMPORALES OCULTOS DE USUARIO (%TEMP%)*",
        choices=((True, "SI"), (False, "NO")),
    )
    del_prefetch = BooleanField(
        null=True,
        verbose_name="ELIMINAR ARCHIVOS CACHE DE WINDOWS EN CARPETA PREFETCH*",
        choices=((True, "SI"), (False, "NO")),
    )
    conf_msconfig = BooleanField(
        null=True,
        verbose_name="CONFIGURACION DEL MSCONFIG (15 segundos de Tiempo de Arranque)*",
        choices=((True, "SI"), (False, "NO")),
    )
    sfc_scannow = BooleanField(
        null=True,
        verbose_name="SFC / SCANNOW (ejecutar como administrador en Power Shell)*",
        choices=((True, "SI"), (False, "NO")),
    )
    win_22h2 = BooleanField(
        null=True,
        verbose_name="22H2 ULTIMA COMPILACION WINDOWS 10 (19045.3271-3374)*",
        choices=((True, "SI"), (False, "NO")),
    )
    equipo = OneToOneField(Equipo, on_delete=CASCADE)


class Driver(Model):
    diag_tool = BooleanField(
        null=True,
        verbose_name="En Laptops LENOVO Ejecutar Lenovo Diagnostics Tool sobre todos los componentes*",
        choices=((True, "Bueno"), (False, "Falla")),
    )
    diag_tool_desc = TextField(blank=True, verbose_name="¿Que esta fallando?")
    upd_bios = BooleanField(
        null=True,
        verbose_name="Actualizacion de BIOS*",
        choices=((True, "SI"), (False, "NO")),
    )
    upd_bios_ver = CharField(max_length=15, verbose_name="Version BIOS*")
    upd_bios_desc = TextField(
        blank=True, verbose_name="Observaciones actualizacion BIOS"
    )
    upd_all = BooleanField(
        null=True,
        verbose_name="Actualizacion Drivers al dia*",
        choices=((True, "SI"), (False, "NO")),
    )
    upd_all_desc = TextField(blank=True, verbose_name="¿Por que?")
    upd_audio = BooleanField(
        null=True,
        verbose_name="Audio*",
        choices=((True, "Aplica"), (False, "No Aplica")),
    )
    upd_video = BooleanField(
        null=True,
        verbose_name="Video*",
        choices=((True, "Aplica"), (False, "No Aplica")),
    )
    upd_wifi = BooleanField(
        null=True,
        verbose_name="Red WIFI*",
        choices=((True, "Aplica"), (False, "No Aplica")),
    )
    upd_ethernet = BooleanField(
        null=True,
        verbose_name="Red Ethernet*",
        choices=((True, "Aplica"), (False, "No Aplica")),
    )
    upd_almacenamiento = BooleanField(
        null=True,
        verbose_name="Dispositivos almacenamiento*",
        choices=((True, "Aplica"), (False, "No Aplica")),
    )
    upd_chipset = BooleanField(
        null=True,
        verbose_name="Chipset*",
        choices=((True, "Aplica"), (False, "No Aplica")),
    )
    upd_camara = BooleanField(
        null=True,
        verbose_name="Camara*",
        choices=((True, "Aplica"), (False, "No Aplica")),
    )
    upd_mouse = BooleanField(
        null=True,
        verbose_name="Mouse*",
        choices=((True, "Aplica"), (False, "No Aplica")),
    )
    exe_all = BooleanField(
        null=True,
        verbose_name="¿Se ejecutaron todos los Drivers?*",
        choices=((True, "SI"), (False, "NO")),
    )
    observaciones = TextField(
        blank=True, verbose_name="Observaciones actualizacion Drivers"
    )
    equipo = OneToOneField(Equipo, on_delete=CASCADE)


class Revision(Model):
    teclado = BooleanField(
        null=True,
        verbose_name="Teclado*",
        choices=((True, "Funciona"), (False, "No Funciona")),
    )
    pantalla = BooleanField(
        null=True,
        verbose_name="Pantalla (Brillo)*",
        choices=((True, "Funciona"), (False, "No Funciona")),
    )
    sonido = BooleanField(
        null=True,
        verbose_name="Sonido (Altavoz)*",
        choices=((True, "Funciona"), (False, "No Funciona")),
    )
    camara = BooleanField(
        null=True,
        verbose_name="Camara*",
        choices=((True, "Funciona"), (False, "No Funciona")),
    )
    touchpad = BooleanField(
        null=True,
        verbose_name="TouchPad*",
        choices=((True, "Funciona"), (False, "No Funciona")),
    )
    wifi = BooleanField(
        null=True,
        verbose_name="Interfaz de red WIFI/RJ45*",
        choices=((True, "Funciona"), (False, "No Funciona")),
    )
    video_hdmi_vga = BooleanField(
        null=True,
        verbose_name="Video/HDMI/VGA*",
        choices=((True, "Funciona"), (False, "No Funciona")),
    )
    internet = BooleanField(
        null=True,
        verbose_name="Acceso a Internet*",
        choices=((True, "Funciona"), (False, "No Funciona")),
    )
    apps_cliente = BooleanField(
        null=True,
        verbose_name="Acceso aplicativos cliente*",
        choices=((True, "Funciona"), (False, "No Funciona")),
    )
    headset = BooleanField(
        null=True,
        verbose_name="HeadSet (Diadema)/Microfono*",
        choices=((True, "Funciona"), (False, "No Funciona")),
    )
    limpieza = BooleanField(
        null=True,
        verbose_name="Limpieza fisica interna y externa*",
        choices=((True, "SI"), (False, "NO")),
    )
    funciona = BooleanField(
        null=True,
        verbose_name="¿Funcionamiento correcto despues de la intervencion?*",
        choices=((True, "SI"), (False, "NO")),
    )
    funciona_desc = TextField(blank=True, verbose_name="¿Por que?")
    observaciones = TextField(blank=True, verbose_name="Observaciones Generales")
    photo_out_front = URLField(max_length=150)
    photo_out_back = URLField(max_length=150)
    photo_out_right1 = URLField(max_length=150)
    photo_out_right2 = URLField(max_length=150)
    photo_out_left1 = URLField(max_length=150)
    photo_out_left2 = URLField(max_length=150)
    equipo = OneToOneField(Equipo, on_delete=CASCADE)
