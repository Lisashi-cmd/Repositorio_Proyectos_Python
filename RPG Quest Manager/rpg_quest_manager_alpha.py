# RPG Quest Manager (Alpha V1 - 24/10/26)

import csv
import os

from excepciones import ErrorLecturaArchivo


class Mision:

  def __init__(self, nombre: str, tipo: str, completada: bool = False):
    self.__nombre: str = nombre
    self.__tipo: str = tipo
    self.__completada: bool = completada

  @property
  def nombre(self) -> str:
    return self.__nombre

  @property
  def tipo(self) -> str:
    return self.__tipo

  @property
  def completada(self) -> bool:
    return self.__completada

  def marcar_completada(self):
    self.__completada = True
    print(f"✨ ¡Misión '{self.__nombre}' marcada como completada!")

  def __str__(self) -> str:
    estado = "X" if self.__completada else " "
    return f" | [{estado}] {self.__nombre} ({self.__tipo})"


class Gremio:

  def __init__(self, misiones: list[Mision] | None = None):
    self.__misiones: list[Mision] = misiones if misiones is not None else []

  def cargar_misiones_desde_archivo(self, nombre_archivo: str):
    try:
      # Obtenemos la ruta absoluta de la carpeta donde está este script en ejecución
      directorio_actual = os.path.dirname(os.path.abspath(__file__))
      # Unimos esa ruta con el nombre del archivo para que siempre lo encuentre sin importar la terminal
      ruta_completa = os.path.join(directorio_actual, nombre_archivo)

      with open(ruta_completa, "r", encoding="utf-8") as m:
        lector = csv.reader(m)

        try:
          next(lector)  # Salto de línea (encabezado)
        except StopIteration:
          print("⚠️ El archivo CSV está vacío.")
          return

        for fila in lector:
          if len(fila) >= 3:
            nombre = fila[0].strip()
            tipo = fila[1].strip()
            completada = fila[2].strip().lower() == "true"
            self.__misiones.append(Mision(nombre, tipo, completada))

      print(f"✅ Misiones cargadas exitosamente desde '{nombre_archivo}'.")

    except FileNotFoundError:
      print(
          f"❌ Error: No se encontró el archivo '{nombre_archivo}' en la"
          f" carpeta del proyecto."
      )
    except Exception as e:  # noqa: BLE001
      raise ErrorLecturaArchivo(nombre_archivo, f"❌ Ocurrió un error inesperado al leer el archivo: {e}")

  def agregar_mision(self, mision: Mision):
    # Aquí añadimos la misión directamente a la lista interna del gremio
    self.__misiones.append(mision)
    print(f"📜 Nueva misión '{mision.nombre}' agregada al Gremio.")

  def mostrar_tablero(self):
    if not self.__misiones:
      print("No hay misiones registradas en el tablero.")
      return
    print("\n================================")
    print("      TABLERO DE MISIONES       ")
    print("================================")
    for i, mision in enumerate(self.__misiones, 1):
      print(f"{i}. {mision}")
    print("================================\n")


# --- Bloque de Prueba / Main ---
if __name__ == "__main__":
  gremio = Gremio()

  gremio.cargar_misiones_desde_archivo("misiones.csv")

  nueva = Mision("Derrotar al Dragón de las Cavernas", "Principal", False)
  gremio.agregar_mision(nueva)

  gremio.mostrar_tablero()           