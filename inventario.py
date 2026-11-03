from api_cliente import autenticar, exportar_csv, obtener_inventario
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
  token = None
  dispositivos = []

  while True:
    print("\n========================================")
    print("      SISTEMA DE AUTOMATIZACIÓN DEVASC  ")
    print("========================================")
    print("1. Consultar inventario de dispositivos")
    print("2. Salir del programa")

    opcion = input("\nSeleccione una opción (1-2): ").strip()

    if opcion == "1":
      token = autenticar()

      if token:
        print("\nConsultando dispositivos de red...")
        dispositivos = obtener_inventario(token)

        if dispositivos:
          print(f"\nSe encontraron {len(dispositivos)} dispositivos")
          for d in dispositivos:
            print(f"=== Dispositivo: {d.get('hostname')} ===")
            print(f"    IP de Gestión:   {d.get('managementIpAddress')}")
            print(f"    Estado:          {d.get('reachabilityStatus')}")
            print(f"    Versión OS:      {d.get('softwareVersion')}")
            print(f"    Modelo:          {d.get('platformId')}")
            print(f"    Número de Serie: {d.get('serialNumber')}")
            print(f"    Tiempo activo:   {d.get('upTime')}\n")

          exportar = (
              input("\n¿Desea exportar estos datos a CSV? (s/n): ")
              .strip()
              .lower()
          )
          if exportar == "s":
            exportar_csv(dispositivos)

    elif opcion == "2":
      print("\nSaliendo del programa. ¡Hasta luego!")
      break
    else:
      print("\nOpción inválida: Por favor seleccione 1 o 2")


if __name__ == "__main__":
  main()