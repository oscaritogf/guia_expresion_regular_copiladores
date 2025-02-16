import re
import os
import pandas as pd

# Función para validar fecha
def validar_fecha(fecha):
    regex_corto = r"^\d{2}-\d{1,2}-\d{1,2}$"
    regex_largo = r"^[A-Za-z]{3,9},?\s\d{1,2}\sde\s\d{1,2}\sde\s\d{4}$"
    if re.match(regex_corto, fecha):
        return "La fecha es válida en formato corto (YY-MM-DD)."
    elif re.match(regex_largo, fecha, re.IGNORECASE):
        return "La fecha es válida en formato largo (día, DD de MM de YYYY)."
    else:
        return "Formato de fecha no válido."

# Función para reemplazar palabras
def reemplazar_palabra(texto, palabra_original, palabra_nueva):
    patron = rf'\b{re.escape(palabra_original)}\b'
    texto_modificado = re.sub(patron, palabra_nueva, texto)
    return texto_modificado

# Función para extraer archivos por extensión
def extraer_archivos(ruta, extension):
    try:
        patron_archivo = fr'.+\.{extension}$'
        archivos = [f for f in os.listdir(ruta) if re.fullmatch(patron_archivo, f)]
        return archivos
    except FileNotFoundError:
        return "La ruta especificada no existe."

# Función para validar nombre de usuario
def validar_nombre_usuario(usuario):
    expresion_regular_nombre_usuario = r"^[A-Za-z0-9-_]{8,12}$"
    if re.match(expresion_regular_nombre_usuario, usuario):
        return "Nombre de usuario válido."
    else:
        return "Nombre de usuario no válido."

# Función para validar contraseña
def validar_contraseña(contraseña):
    patron_contraseña = r"^(?!.*(012|123|234|345|456|567|678|789|890|abc))(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    if re.match(patron_contraseña, contraseña):
        return "Contraseña segura."
    else:
        return "Contraseña no segura."

# Función principal para ejecutar las pruebas y generar la salida
def main():
    # Datos de prueba
    fechas = [
        "24-02-14",  # Válida formato corto
        "miércoles, 14 de febrero de 2024",  # Inválida
        "2024-02-14",  # Inválida
        "lunes, 30 de 1 de 2023",  # Válida formato largo
        "mar, 10 de 03 de 2022"  # Válida formato largo
    ]
    
    texto = "El perro corre en el parque y el gato duerme."
    palabra_a_cambiar = "perro"
    nueva_palabra = "caballo"
    
    ruta = "."  # Ruta actual del script
    extension = "txt"
    
    
    usuarios = ["Luis_Carlos4", "usuario_invalido!", "Ana_123"]
    
    contraseñas = ["Carmen@254", "contraseña", "Segura123!"]

    # Resultados
    resultados_fechas = [(fecha, validar_fecha(fecha)) for fecha in fechas]
    texto_modificado = reemplazar_palabra(texto, palabra_a_cambiar, nueva_palabra)
    archivos_extraidos = extraer_archivos(ruta, extension)
    resultados_usuarios = [(usuario, validar_nombre_usuario(usuario)) for usuario in usuarios]
    resultados_contraseñas = [(contraseña, validar_contraseña(contraseña)) for contraseña in contraseñas]

    # Crear DataFrame para exportar a Excel
    df_fechas = pd.DataFrame(resultados_fechas, columns=["Fecha", "Resultado"])
    df_texto = pd.DataFrame([{"Texto Original": texto, "Texto Modificado": texto_modificado}])
    df_archivos = pd.DataFrame({"Archivos Extraídos": archivos_extraidos})
    df_usuarios = pd.DataFrame(resultados_usuarios, columns=["Usuario", "Resultado"])
    df_contraseñas = pd.DataFrame(resultados_contraseñas, columns=["Contraseña", "Resultado"])

    # Exportar a Excel
    with pd.ExcelWriter("resultados.xlsx", engine="openpyxl") as writer:
        df_fechas.to_excel(writer, sheet_name="Fechas", index=False)
        df_texto.to_excel(writer, sheet_name="Reemplazo Palabras", index=False)
        df_archivos.to_excel(writer, sheet_name="Archivos Extraídos", index=False)
        df_usuarios.to_excel(writer, sheet_name="Usuarios", index=False)
        df_contraseñas.to_excel(writer, sheet_name="Contraseñas", index=False)

    print("Resultados exportados a 'resultados.xlsx'.")

# Ejecutar el programa
if __name__ == "__main__":
    main()