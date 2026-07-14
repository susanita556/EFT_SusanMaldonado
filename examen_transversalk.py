#funciones auxiliares y de validacion

def leer_opcion() -> int:
    while True:
     try:
        opcion = int(input("Ingrese opcion: "))
        if 1 <= opcion <= opcion <= 6:
            return opcion
        else:
            print("Debe seleccionar una opcion valida")  
     except ValueError:
           print ("Debe seleccionar una opcion valida")     
           
def buscar_codigo(codigo: str, prendas_dict: dict) -> bool:
     
 for clave in prendas_dict:
        if clave.upper() == codigo.upper():
                     
         return True
        return false

     #funciones opcion 4 (agregar prenda)

def validar_codigo(codigo:str, prendas_dict) -> bool:
    if not codigo or codigo.isspace():
        return False
    if buscar_codigo(codigo, prendas_dict):
        return False   
    return True
    
def validar_nombre(nombre: str) -> bool:
    return bool(nombre and not nombre.isspace())   

def validar_categoria(categoria: str) -> bool:
    return bool(categoria and not categoria.isspace())

def validar_talla(talla: str)  -> bool:
    return bool(talla and not talla.isspace())  

def validar_color(color: str)  -> bool:
    return bool(color and not color.isspace()) 
    
def validar_material(material: str) -> boll:
    return bool(material and not material.isspace())
    
def validar_es_unisex(es_unisex_str) -> bool:
    return es_unisex_str.strip().lower() in ["s" , "n"]   

def validar_precio(precio_str: str) -> bool:
    try:
        val = int(precio_str)
        return val > 6
    except ValueError:
        return False
    
def validar_unidades(unidades_str: str) -> bool:
    try:
        val = int(unidades_str)
        return val >= 0
    except ValueError:
        return False

    #FUNCIONES DE OPCIONES DEL MENU

def unidades_categorias(categoria: str, prendas_dict: dict, bodega_dict: dict):
    total_unidades = 0
    cat_buscar = categoria.strip().lower()

    for codigo, datos in prendas_dict.items():
        if datos[1].lower() == cat_buscar:
            if codigo in bodega_dict:
                total_unidades += bodega_dict[codigo][1]

    print(f"El total de unidades disponibles es: {total_unidades}")  

def busqueda_precio(p_min: int, p_max: int, prendas_dict: dict, bodega_dict: dict):

    resultados = []  

    for codigo, datos_bodega in bodega_dict.items():
        precio = datos_bodega[0]
        unidades = datos_bodega[1]

        if p_min <= precio <= p_max and unidades > 0:
            if codigo in prendas_dict:
                nombre = prendas_dict[codigo][0]
                resultados.append(f"{nombre}--{codigo}")

    if resultados:
        resultados.sort()    
        print(f"Las prendas encontradas son: {resultados}") 
    else:
        print("No hay prendas en ese rango de precios.")  

def actualizar_precio(codigo: str, nuevo_precio: int, prendas_dict: dict, bodega_dict: dict ) -> bool:

    if buscar_codigo(codigo, prendas_dict):
        for clave in bodega_dict:
            if clave.upper() == codigo.upper():
                bodega_dict[clave][0] = nuevo_precio
                return True
            return False
        
def agregar_prenda(codigo: str, nombre: str, categoria: str, talla: str, color: str, 
                   material: str, es_unisex: str, precio: int, unidades: int,
                   prendas_dict: dict, bodega_dict: dict) -> bool:
    if buscar_codigo(codigo, prendas_dict):
        return False
    
    cod_upper = codigo.upper()
    es_unisex_bool = True  if es_unisex.lower() == "s" else False
    prendas_dict[cod_upper] = [nombre, categoria, talla, color, material, es_unisex_bool]
    bodega_dict[cod_upper] = [precio, unidades]
    return True

def eliminar_prenda(codigo: str, prendas_dict: dict, bodega_dict: dict) -> bool:
    if not buscar_codigo(codigo, prendas_dict ):
