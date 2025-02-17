Hola chicos aquí esta el ejercicio,
para ejecutarlo creen un entorno virtual con:
paso 1:
python -m venv venv
paso 2:
venv\Scripts\activate

paso 3, si no les funciona paso 2 ejecutar para dar permisos:
Set-ExecutionPolicy Unrestricted -Scope Process
paso 4: ejecutar paso 2 otra ves.
paso 5:  pip install pandas openpyxl  ó pip install pandas y pip install openpyxl 
paso 6: ejecutar el proyecto python main.py

para ver el resultado de el ejecio c de extraer nobre creen archivos en 
la carpeta raiz o pongan una ruta en la lina 62
donde tengar archivos con extencion .txt o cambian el tipo de extencion

se genera un xlsx o excel automaticamente cuando se ejecuta python main.py en la ruta donde tiene el proyecto
para ver el resultado en visual o abrir arcivos de excel en visual studio code pueden instalar la 
extencion excel Viewer del marketplace de visual. 


cuando se ejecuta python main.py genera el excel si lo vuelven a ejecutar borren el excel generado anteriormente 


Ejercicios
1. Realizar un programa en Python para identificar a través de expresiones
regulares lo siguiente:
    a. Validar un formato de fecha corto y uno largo, por ejemplo corto: YYMM-DD; largo: “dia, DD" de "MM" de "YYYY”.
    
    b. Reemplazar palabras identificando otra palabra para cambiarla en
    una oracion/parrafo. Por ejemplo cambiar “el” por “en”.
    
    c. Extraer los nombres de archivos de un tipo de formato en una ruta de
    directorio, por ejemplo: C:\Documentos, archivos txt.
    
    d. Validar un nombre de usuario que debe tener entre 8 y 12 caracteres
    y solo puede contener letras, números, guiones bajos o guiones alto.
    
    e. Validar si una contraseña es segura. Una contraseña segura debe
    tener al menos 8 caracteres, una letra mayúscula, una letra
    minúscula, un número y un carácter especial.
    
    La salida debe mostrar un arreglo impreso de las ocurrencias encontradas o
    dar un mensaje que no encontró ninguna. De forma opcional puede mandar
    la salida en un txt o un archivo de Excel.