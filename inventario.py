
def mostrar_banner():
  print("=" * 60)
  print("      SISTEMA AUTOMATIZADO DE GESTION DE INVENTARIO DE RED")
  print("=" * 60)

def ejecutar_consulta_api():
  print("=" * 60)
  print(f"            REPORTE DE EQUIPOS DE RED CONSULTADOS")
  print("=" * 60)

def main():
  mostrar_banner()

  opcion = input("\n¿Desea iniciar el programa? (Presione Enter para continuar / 'q' para salir): ")
    
  if opcion.lower() == 'q':
    print("\nSaliendo del programa...")
    return

  ejecutar_consulta_api()
    
  print("\nRevision Completada Exitosamente")

if __name__ == "__main__":
    main()