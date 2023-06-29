import pandas as pd

def read():
    df = pd.read_csv('dnrpa-transferencias-autos-202305.csv', sep = ',', low_memory=False)

    conjunto_A = df[(df['automotor_origen'] == 'Nacional')& (df['registro_seccional_provincia'] == 'Formosa') & (df['automotor_anio_modelo'] > 2015)]
    conjunto_A.to_csv('conjunto_A.csv')
    
    conjunto_B = df [(df['registro_seccional_codigo'] == 1216) & (df['automotor_origen'] == 'Importado')]
    conjunto_B.to_csv('conjunto_B.csv')

    

read()
