import datetime
import pandas as pd


"""CREACIÓN DE TABLA ÚNICA PRINCIPAL"""
filename = datetime.datetime.now().strftime("%d-%m-%Y")
filename = filename + '.csv'
dir = datetime.datetime.now().strftime('%Y-%m')

df_museos = pd.read_csv('museos/'+ dir + '/' + 'museos-' + filename)
df_cines = pd.read_csv('cines/'+ dir + '/' + 'cines-' + filename)
df_bibliotecas = pd.read_csv('bibliotecas/'+ dir + '/' + 'bibliotecas-' + filename)

tabla_unica = pd.DataFrame(columns=['cod_localidad', 'id_provincia', 'id_departamento', 'categoría', 'provincia', 'localidad', 'nombre', 'domicilio', 'código postal', 'número de teléfono', 'mail', 'web'])

df_museos2 = df_museos.drop(['Observaciones', 'subcategoria', 'piso', 'cod_area', 'Latitud', 'Longitud', 'TipoLatitudLongitud', 'Info_adicional', 'fuente', 'jurisdiccion', 'año_inauguracion', 'actualizacion'], axis=1)
df_cines2 = df_cines.drop(['Observaciones', 'Departamento','Piso', 'cod_area', 'Información adicional','Latitud', 'Longitud', 'TipoLatitudLongitud', 'Fuente', 'tipo_gestion',	'Pantallas',	'Butacas',	'espacio_INCAA', 'año_actualizacion'], axis=1)
df_bibliotecas2 = df_bibliotecas.drop(['Observacion', 'Subcategoria', 'Departamento','Piso', 'Cod_tel', 'Información adicional','Latitud', 'Longitud', 'TipoLatitudLongitud','Fuente', 'Tipo_gestion',	'año_inicio',	'Año_actualizacion'], axis=1)

df_museos2 = df_museos2.rename(columns={'Cod_Loc':'cod_localidad', 'IdProvincia':'id_provincia', 'IdDepartamento':'id_departamento', 'categoria':'categoría', 'direccion':'domicilio', 'CP':'código postal', 'telefono':'número de teléfono',  'Mail':'mail', 'Web':'web'})
df_cines2 = df_cines2.rename(columns={'Cod_Loc':'cod_localidad', 'IdProvincia':'id_provincia', 'IdDepartamento':'id_departamento', 'Categoría':'categoría', 'Provincia':'provincia','Dirección':'domicilio', 'CP':'código postal', 'Teléfono':'número de teléfono',  'Mail':'mail', 'Web':'web'})
df_bibliotecas2 = df_bibliotecas2.rename(columns={'Cod_Loc':'cod_localidad', 'IdProvincia':'id_provincia', 'IdDepartamento':'id_departamento', 'Categoría':'categoría', 'Provincia':'provincia', 'Localidad':'localidad', 'Nombre':'nombre', 'Domicilio':'domicilio', 'CP':'código postal', 'Teléfono':'número de teléfono',  'Mail':'mail', 'Web':'web'})

tabla_unica = pd.concat([tabla_unica, df_museos2], ignore_index=True)
tabla_unica = pd.concat([tabla_unica, df_cines2], ignore_index=True)
tabla_unica = pd.concat([tabla_unica, df_bibliotecas2], ignore_index=True)
tabla_unica['fecha_actualizacion'] =  pd.to_datetime('today').strftime('%Y-%m-%d')


"""TABLA CANTIDAD DE PANTALLAS, BUTACAS Y ESPACIOS INCAA POR PROVINCIA"""
cines_info = pd.DataFrame(columns=['provincia', 'pantallas', 'butacas', 'espacio_INCAA'])
df_cines3 = df_cines.drop(['Cod_Loc', 'Nombre', 'Localidad', 'IdProvincia', 'IdDepartamento', 'Categoría', 'Dirección', 'CP', 'Teléfono', 'Mail', 'Web', 'Observaciones', 'Departamento','Piso', 'cod_area', 'Información adicional','Latitud', 'Longitud', 'TipoLatitudLongitud', 'Fuente', 'tipo_gestion', 'año_actualizacion'], axis=1)
df_cines3 = df_cines3.rename(columns={'Provincia': 'provincia', 'Pantallas': 'pantallas', 'Butacas': 'butacas'})
cines_info = pd.concat([cines_info, df_cines3], ignore_index=True)
cines_info['fecha_actualizacion'] =  pd.to_datetime('today').strftime('%Y-%m-%d')


"""TABLA DE FUENTES Y CATEGORÍAS POR PROVINCIA:"""

registros_tabla = pd.DataFrame(columns=['categoria', 'fuente', 'provincia'])

registros_cines = df_cines.drop(['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'Observaciones', 'Departamento', 'Localidad', 'Nombre', 'Dirección', 'Piso', 'CP', 'cod_area', 'Teléfono', 'Mail', 'Web', 'Información adicional','Latitud', 'Longitud', 'TipoLatitudLongitud', 'tipo_gestion', 'Pantallas', 'Butacas', 'espacio_INCAA', 'año_actualizacion'], axis=1)
registros_museos = df_museos.drop(['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'Observaciones', 'subcategoria', 'localidad', 'nombre', 'direccion', 'piso', 'CP', 'cod_area', 'telefono', 'Mail', 'Web', 'Latitud', 'Longitud', 'TipoLatitudLongitud', 'Info_adicional', 'jurisdiccion', 'año_inauguracion', 'actualizacion'], axis=1)
registros_bibliotecas = df_bibliotecas.drop(['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'Observacion', 'Subcategoria', 'Departamento', 'Localidad', 'Nombre', 'Domicilio', 'Piso', 'CP', 'Cod_tel', 'Teléfono', 'Mail', 'Web', 'Información adicional', 'Latitud', 'Longitud', 'TipoLatitudLongitud', 'Tipo_gestion', 'año_inicio', 'Año_actualizacion'], axis=1)

registros_cines = registros_cines.rename(columns={'Categoría':'categoria', 'Provincia':'provincia', 'Fuente':'fuente'})
registros_bibliotecas = registros_bibliotecas.rename(columns={'Categoría':'categoria', 'Provincia':'provincia', 'Fuente':'fuente'})

registros_tabla = pd.concat([registros_tabla, registros_cines], ignore_index=True)
registros_tabla = pd.concat([registros_tabla, registros_museos], ignore_index=True)
registros_tabla = pd.concat([registros_tabla, registros_bibliotecas], ignore_index=True)

registros_categoria = pd.pivot_table(registros_tabla, index='categoria', columns='categoria',  aggfunc='count', margins=True)
registros_fuente = pd.pivot_table(registros_tabla, index='categoria', columns='fuente',  aggfunc='count', margins=True)
registros_provincia = pd.pivot_table(registros_tabla, index='categoria', columns='provincia',  aggfunc='count', margins=True)

registros_categoria.columns = registros_categoria.columns.droplevel(0) 
registros_categoria.columns.name = None               
registros_categoria = registros_categoria.reset_index()               

registros_fuente.columns = registros_fuente.columns.droplevel(0)
registros_fuente.columns.name = None               
registros_fuente = registros_fuente.reset_index()                

registros_provincia.columns = registros_provincia.columns.droplevel(0) 
registros_provincia.columns.name = None              
registros_provincia = registros_provincia.reset_index()  

registros_categoria['fecha_actualizacion'] = pd.to_datetime('today').strftime('%Y-%m-%d')
registros_fuente['fecha_actualizacion'] =  pd.to_datetime('today').strftime('%Y-%m-%d')
registros_provincia['fecha_actualizacion'] =  pd.to_datetime('today').strftime('%Y-%m-%d')

   
print(registros_provincia)




