import sqlite3
import json
import os

def guardar_en_sql(archivo_json="resultado_final.json", nombre_db="base_fiscal.db"):
    # 1. Verificamos que el archivo JSON exista
    if not os.path.exists(archivo_json):
        print(f"❌ Error: No se encontró el archivo '{archivo_json}'. Ejecuta primero el Extractor.")
        return

    # 2. Leemos los datos extraídos por la IA
    with open(archivo_json, 'r', encoding='utf-8') as f:
        datos = json.load(f)

    if not datos:
        print("⚠️ El archivo JSON está vacío.")
        return

    # 3. Nos conectamos a la base de datos (se creará automáticamente si no existe)
    conexion = sqlite3.connect(nombre_db)
    cursor = conexion.cursor()

    # 4. Creamos la tabla si no existe
    # Fíjate cómo definimos los tipos de datos exactos que pidió el reto
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS documentos_fiscales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_cliente TEXT NOT NULL,
            monto REAL,
            fecha DATE NOT NULL,
            tipo_solicitud TEXT NOT NULL,
            archivo_origen TEXT
        )
    ''')

    # 5. Insertamos cada registro del JSON en la tabla SQL
    registros_insertados = 0
    for registro in datos:
        # Usamos parámetros (?) para evitar inyecciones SQL (buenas prácticas)
        cursor.execute('''
            INSERT INTO documentos_fiscales (nombre_cliente, monto, fecha, tipo_solicitud, archivo_origen)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            registro.get("nombre_cliente"),
            registro.get("monto"), # Si es null en JSON, SQLite lo guarda como NULL
            registro.get("fecha"),
            registro.get("tipo_solicitud"),
            registro.get("archivo_origen")
        ))
        registros_insertados += 1

    # 6. Guardamos los cambios y cerramos la conexión
    conexion.commit()
    conexion.close()

    print(f"✅ ¡Éxito! Se han insertado {registros_insertados} registros en la base de datos '{nombre_db}'.")

# Ejecutamos la función
if __name__ == "__main__":
    print("🗄️  Iniciando migración a SQL...")
    guardar_en_sql()