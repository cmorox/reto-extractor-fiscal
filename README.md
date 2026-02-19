
# 📄 El Extractor Fiscal - Prueba Técnica

Este proyecto es un pipeline de procesamiento de datos en Python que extrae información clave de documentos desordenados (texto plano, Word y Excel) utilizando Inteligencia Artificial, y la almacena de forma estructurada en una base de datos relacional.

## 🚀 Características Principales
* **Soporte Multiformato:** Extrae texto crudo de archivos `.txt`, `.docx` y `.xlsx`.
* **Extracción Determinista con IA:** Utiliza la API de Gemini 2.5 Flash con *Structured Outputs* para forzar una respuesta en formato JSON estricto, evitando alucinaciones o texto libre.
* **Tolerancia a Fallos:** Implementa un sistema de reintentos automáticos (retry logic) en caso de que la API devuelva un formato inválido.
* **Persistencia de Datos:** Incluye un script secundario para migrar los datos extraídos en formato JSON hacia una base de datos local SQLite (`base_fiscal.db`).

## 🛠️ Tecnologías y Librerías Utilizadas
* `python 3.x`
* `google-generativeai` (Motor de LLM)
* `python-dotenv` (Manejo seguro de variables de entorno)
* `python-docx` y `openpyxl` (Lectura de documentos)
* `sqlite3` (Base de datos relacional)

## ⚙️ Instalación y Configuración
1. Clona este repositorio o descarga los archivos.
2. Instala las dependencias ejecutando:
   ```bash
   pip install google-generativeai python-dotenv python-docx openpyxl

```

3. Crea un archivo llamado `.env` en la raíz del proyecto y agrega tu clave de API:
```text
GEMINI_API_KEY="tu_clave_aqui"

```



## ▶️ Instrucciones de Uso

1. Coloca los documentos a analizar dentro de la carpeta `mis_archivos_sucios/`.
2. Ejecuta el motor de extracción:
```bash
python main.py

```


*(Esto generará un archivo `resultado_final.json`)*
3. Ejecuta el script de persistencia para guardar los datos en SQL:
```bash
python insertar_sql.py

```



```


¿Pudiste copiarlo y guardarlo bien esta vez? ¡Avísame si tienes cualquier otro detalle antes de tu gran día de mañana!

```
