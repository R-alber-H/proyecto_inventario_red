import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


def autenticar():
  print("\n=== INICIO DE SESIÓN ===")

  usuario_input = (input(f"Usuario: ").strip())
  password_input = (input("Contraseña: ").strip())

  url = f"{BASE_URL}/dna/system/api/v1/auth/token"
  try:
    response = requests.post(
        url, auth=(usuario_input, password_input), verify=False
    )
    response.raise_for_status()
    print("\n¡Autenticación exitosa!")
    return response.json().get("Token")
  except Exception as e:
    print(f"\nError de autenticación: Credenciales incorrectas o {e}")
    return None

def obtener_inventario(token):

  url = f"{BASE_URL}/dna/intent/api/v1/network-device"
  headers = {"X-Auth-Token": token, "Content-Type": "application/json"}
  try:
    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()
    return response.json().get("response", [])
  except Exception as e:
    print(f"Error al obtener inventario {e}")
    return []


def exportar_csv(dispositivos):
  import csv

  if not dispositivos:
    print("No hay datos para exportar")
    return

  nombre_archivo = "inventario_red.csv"
  try:
    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
      escritor = csv.writer(archivo)

      escritor.writerow([
          "Hostname",
          "IP",
          "Estado",
          "Versión",
          "Modelo",
          "SerialNumber",
          "Uptime",
      ])

      for d in dispositivos:
        escritor.writerow([
            d.get("hostname"),
            d.get("managementIpAddress"),
            d.get("reachabilityStatus"),
            d.get("softwareVersion"),
            d.get("platformId"),
            d.get("serialNumber"),
            d.get("upTime"),
        ])

    print(f"Inventario exportado correctamente a {nombre_archivo}")
  except Exception as e:
    print(f"Error al exportar CSV: {e}")