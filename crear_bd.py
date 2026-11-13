"""
Script de apoyo: crea la base de datos serie4_vehiculos_db si no existe.

Se ejecuta UNA sola vez, antes de las migraciones:
    .venv\\Scripts\\python.exe crear_bd.py

Se conecta al servidor MySQL/MariaDB sin seleccionar una base de datos,
porque todavía podría no existir.
"""

import MySQLdb

NOMBRE_BD = "serie4_vehiculos_db"

try:
    conexion = MySQLdb.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",
    )
    cursor = conexion.cursor()
    cursor.execute(
        f"CREATE DATABASE IF NOT EXISTS `{NOMBRE_BD}` "
        "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
    )
    conexion.commit()
    print(f"Base de datos '{NOMBRE_BD}' verificada/creada correctamente.")
except MySQLdb.Error as error:
    print(f"Error al conectar con MySQL: {error}")
    raise
finally:
    if "cursor" in locals():
        cursor.close()
    if "conexion" in locals():
        conexion.close()
