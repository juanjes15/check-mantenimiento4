from django.db import models


class Equipo(models.Model):
    tipo = models.CharField(max_length=20, verbose_name="TIPO")
    marca = models.CharField(max_length=20, verbose_name="MARCA")
    modelo = models.CharField(max_length=15, verbose_name="MODELO")
    serial = models.CharField(max_length=15, verbose_name="SERIAL", unique=True)
    estado = models.BooleanField(null = True, verbose_name="ESTADO ACTUAL DEL EQUIPO", choices=((True, 'Bueno'), (False, 'Falla')))
    registro_entrada = models.BooleanField(null = True, verbose_name="Registro Fotografico Entrada", choices=((True, 'SI (WIP)'), (False, 'NO (WIP)')))
    registro_salida = models.BooleanField(null = True, verbose_name="Registro Fotografico Salida", choices=((True, 'SI (WIP)'), (False, 'NO (WIP)')))
    sistema_operativo = models.CharField(max_length=15, verbose_name="SISTEMA OPERATIVO INSTALADO")
    estado_hdd = models.BooleanField(null = True, verbose_name="ESTADO DISCO DURO", choices=((True, 'Bueno'), (False, 'Malo')))
    ram = models.CharField(max_length=10, verbose_name="RAM ACTUAL")
    tipo_procesador = models.CharField(max_length=15, verbose_name="TIPO PROCESADOR")
    estado_fisico = models.TextField(blank=True, verbose_name="ESTADO FISICO")
    siniestro = models.BooleanField(null = True, verbose_name="SINIESTRO", choices=((True, 'SI'), (False, 'NO')))


class Usuario(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="NOMBRE USUARIO FINAL")
    fecha_intervencion = models.DateField(null = True, verbose_name="FECHA INTERVENCIÓN")
    ciudad = models.CharField(max_length=50, verbose_name="CIUDAD")
    telefono = models.CharField(max_length=10, verbose_name="TELEFONO CONTACTO")
    usuario_red = models.CharField(max_length=50, verbose_name="USUARIO DE RED, CLAVE DE USUARIO")
    activo = models.CharField(max_length=20, verbose_name="ACTIVO")
    equipo = models.OneToOneField(Equipo, on_delete=models.CASCADE)


class Software(models.Model):
    des_office = models.BooleanField(null = True, verbose_name="VALIDAR DESACELERACION GRAFICA DE OFFICE 365", choices=((True, 'SI'), (False, 'NO')))
    des_chrome = models.BooleanField(null = True, verbose_name="VALIDAR DESACELERACION GRAFICA DE GOOGLE CHROME", choices=((True, 'SI'), (False, 'NO')))
    des_teams = models.BooleanField(null = True, verbose_name="VALIDAR DESACELERACION GRAFICA DE MICROSOFT TEAMS", choices=((True, 'SI'), (False, 'NO')))
    del_temp = models.BooleanField(null = True, verbose_name="ELIMINAR TEMPORALES DE WINDOWS (TEMP)", choices=((True, 'SI'), (False, 'NO')))
    dfg_dd = models.BooleanField(null = True, verbose_name="DESFRAGMENTAR EL DISCO (ANALIZAR - OPTIMIZAR) HDD-SSD", choices=((True, 'SI'), (False, 'NO')))
    del_temp2 = models.BooleanField(null = True, verbose_name="ELIMINAR TEMPORALES OCULTOS DE USUARIO (%TEMP%)", choices=((True, 'SI'), (False, 'NO')))
    del_prefetch = models.BooleanField(null = True, verbose_name="ELIMINAR ARCHIVOS CACHE DE WINDOWS EN CARPETA PREFETCH", choices=((True, 'SI'), (False, 'NO')))
    conf_msconfig = models.BooleanField(null = True, verbose_name="CONFIGURACION DEL MSCONFIG (15 segundos de Tiempo de Arranque)", choices=((True, 'SI'), (False, 'NO')))
    sfc_scannow = models.BooleanField(null = True, verbose_name="SFC / SCANNOW (ejecutar como administrador en Power Shell)", choices=((True, 'SI'), (False, 'NO')))
    win_22h2 = models.BooleanField(null = True, verbose_name="22H2 ULTIMA COMPILACION WINDOWS 10 (19045.3271-3374)", choices=((True, 'SI'), (False, 'NO')))
    equipo = models.OneToOneField(Equipo, on_delete=models.CASCADE)


class Driver(models.Model):
    diag_tool = models.BooleanField(null = True, verbose_name="En Laptops LENOVO Ejecutar Lenovo Diagnostics Tool sobre todos los componentes", choices=((True, 'Bueno'), (False, 'Falla')))
    diag_tool_desc = models.TextField(blank=True, verbose_name="¿Que esta fallando?")
    upd_bios = models.BooleanField(null = True, verbose_name="Actualizacion de BIOS", choices=((True, 'SI'), (False, 'NO')))
    upd_bios_ver = models.CharField(max_length=15, verbose_name="Version BIOS")
    upd_bios_desc = models.TextField(blank=True, verbose_name="Observaciones actualizacion BIOS")
    upd_all = models.BooleanField(null = True, verbose_name="Actualizacion Drivers al dia", choices=((True, 'SI'), (False, 'NO')))
    upd_all_desc = models.TextField(blank=True, verbose_name="¿Por que?")
    upd_audio = models.BooleanField(null = True, verbose_name="Audio", choices=((True, 'Aplica'), (False, 'No Aplica')))
    upd_video = models.BooleanField(null = True, verbose_name="Video", choices=((True, 'Aplica'), (False, 'No Aplica')))
    upd_wifi = models.BooleanField(null = True, verbose_name="Red WIFI", choices=((True, 'Aplica'), (False, 'No Aplica')))
    upd_ethernet = models.BooleanField(null = True, verbose_name="Red Ethernet", choices=((True, 'Aplica'), (False, 'No Aplica')))
    upd_almacenamiento = models.BooleanField(null = True, verbose_name="Dispositivos almacenamiento", choices=((True, 'Aplica'), (False, 'No Aplica')))
    upd_chipset = models.BooleanField(null = True, verbose_name="Chipset", choices=((True, 'Aplica'), (False, 'No Aplica')))
    upd_camara = models.BooleanField(null = True, verbose_name="Camara", choices=((True, 'Aplica'), (False, 'No Aplica')))
    upd_mouse = models.BooleanField(null = True, verbose_name="Mouse", choices=((True, 'Aplica'), (False, 'No Aplica')))
    exe_all = models.BooleanField(null = True, verbose_name="¿Se ejecutaron todos los Drivers?", choices=((True, 'SI'), (False, 'NO')))
    observaciones = models.TextField(blank=True, verbose_name="Observaciones actualizacion Drivers")
    equipo = models.OneToOneField(Equipo, on_delete=models.CASCADE)


class Revision(models.Model):
    teclado = models.BooleanField(null = True, verbose_name="Teclado", choices=((True, 'Funciona'), (False, 'No Funciona')))
    pantalla = models.BooleanField(null = True, verbose_name="Pantalla (Brillo)", choices=((True, 'Funciona'), (False, 'No Funciona')))
    sonido = models.BooleanField(null = True, verbose_name="Sonido (Altavoz)", choices=((True, 'Funciona'), (False, 'No Funciona')))
    camara = models.BooleanField(null = True, verbose_name="Camara", choices=((True, 'Funciona'), (False, 'No Funciona')))
    touchpad = models.BooleanField(null = True, verbose_name="TouchPad", choices=((True, 'Funciona'), (False, 'No Funciona')))
    wifi = models.BooleanField(null = True, verbose_name="Interfaz de red WIFI/RJ45", choices=((True, 'Funciona'), (False, 'No Funciona')))
    video_hdmi_vga = models.BooleanField(null = True, verbose_name="Video/HDMI/VGA", choices=((True, 'Funciona'), (False, 'No Funciona')))
    internet = models.BooleanField(null = True, verbose_name="Acceso a Internet", choices=((True, 'Funciona'), (False, 'No Funciona')))
    apps_cliente = models.BooleanField(null = True, verbose_name="Acceso aplicativos cliente", choices=((True, 'Funciona'), (False, 'No Funciona')))
    headset = models.BooleanField(null = True, verbose_name="HeadSet (Diadema)/Microfono", choices=((True, 'Funciona'), (False, 'No Funciona')))
    limpieza = models.BooleanField(null = True, verbose_name="Limpieza fisica interna y externa", choices=((True, 'SI'), (False, 'NO')))
    funciona = models.BooleanField(null = True, verbose_name="¿Funcionamiento correcto despues de la intervencion?", choices=((True, 'SI'), (False, 'NO')))
    funciona_desc = models.TextField(blank=True, verbose_name="¿Por que?")
    observaciones = models.TextField(blank=True, verbose_name="Observaciones Generales")
    equipo = models.OneToOneField(Equipo, on_delete=models.CASCADE)
