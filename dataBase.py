import sqlalchemy 
import procesamientoDatos


engine = sqlalchemy.create_engine('postgresql://postgres:1234@localhost:5432/Alkemy')

procesamientoDatos.tabla_unica.to_sql('tabla_unificada', con=engine, if_exists='replace')
procesamientoDatos.cines_info.to_sql('cantidades_cines', con=engine, if_exists='replace')
procesamientoDatos.registros_categoria.to_sql('registros_categoria', con=engine, if_exists='replace', index_label='index')
procesamientoDatos.registros_fuente.to_sql('registros_fuente', con=engine, if_exists='replace', index_label='index')
procesamientoDatos.registros_provincia.to_sql('registros_provincia', con=engine, if_exists='replace', index_label='index')


