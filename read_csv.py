import pandas as pd
from app.database import engine
import numpy as np

def read_conjunto_A():
    df = pd.read_csv('dnrpa-transferencias-autos-202305.csv', sep = ',', low_memory=False)
    df['id'] = np.arange(1, len(df)+1)
    conjunto_A = df[(df['automotor_origen'] == 'Nacional')& (df['registro_seccional_provincia'] == 'Formosa') & (df['automotor_anio_modelo'] > 2015)]
    conjunto_A.to_csv('conjunto_A.csv')
    return conjunto_A

def read_conjunto_B():
    df = pd.read_csv('dnrpa-transferencias-autos-202305.csv', sep = ',', low_memory=False)
    df['id'] = np.arange(1, len(df)+1)
    conjunto_B = df [(df['registro_seccional_codigo'] == 1216) & (df['automotor_origen'] == 'Importado')]
    conjunto_B.to_csv('conjunto_B.csv')
    return conjunto_B

def conjunto_A_to_sql():
    conjunto_A = read_conjunto_A()
    
    conjunto_A_procedure = conjunto_A[['id','tramite_tipo','titular_domicilio_provincia_id']]
    conjunto_A_procedure.columns = ['id','Type', 'Povince_code']
    conjunto_A_procedure.to_sql(name='Procedure', con= engine, if_exists='append', index=False)

    conjunto_A_province = conjunto_A[['id','titular_domicilio_provincia','titular_domicilio_provincia_id','titular_pais_nacimiento_id']]
    conjunto_A_province.columns = ['id','Name','Code','Country_Code']
    conjunto_A_province.to_sql(name='Province', con= engine, if_exists='append', index=False)

    conjunto_A_country = conjunto_A[['id','titular_pais_nacimiento_id', 'titular_pais_nacimiento']]
    conjunto_A_country.columns = ['id','Code', 'Name']
    conjunto_A_country.to_sql(name='Country', con= engine, if_exists='append', index=False)
    

def conjunto_B_to_sql():
    conjunto_B = read_conjunto_B()
    
    conjunto_B_procedure = conjunto_B[['id','tramite_tipo','titular_domicilio_provincia_id']]
    conjunto_B_procedure.columns = ['id','Type', 'Povince_code'] 
    conjunto_B_procedure.to_sql(name='Procedure', con= engine, if_exists='append', index=False)

    conjunto_B_province = conjunto_B[['id','titular_domicilio_provincia','titular_domicilio_provincia_id','titular_pais_nacimiento_id']]
    conjunto_B_province.columns = ['id','Name','Code','Country_Code']
    conjunto_B_province.to_sql(name='Province', con= engine, if_exists='append', index=False)
    
    conjunto_B_country = conjunto_B[['id','titular_pais_nacimiento_id', 'titular_pais_nacimiento']]
    conjunto_B_country.columns = ['id','Code', 'Name']
    conjunto_B_country.to_sql(name='Country', con= engine, if_exists='append', index=False)



