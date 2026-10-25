class ErrorLecturaArchivo(Exception):
    """Excepción para errores al leer archivos CSV."""
    def __init__(self, archivo: str, mensaje: str | None = None):
        self.archivo = archivo
        if mensaje is None:
            mensaje = f"No se pudo leer el archivo '{archivo}'"
        super().__init__(mensaje)   