import pandas as pd



def get_countries():
    df = pd.read_csv('dnrpa-transferencias-autos-202305.csv', sep = ',', low_memory=False)
    conjunto_A = df[(df['automotor_origen'] == 'Nacional')& (df['registro_seccional_provincia'] == 'Formosa') & (df['automotor_anio_modelo'] > 2015)]
    conjunto_B = df [(df['registro_seccional_codigo'] == 1216) & (df['automotor_origen'] == 'Importado')]
    countries_A = conjunto_A[['titular_pais_nacimiento_id','titular_pais_nacimiento']].drop_duplicates()
    countries_B = conjunto_B[['titular_pais_nacimiento_id','titular_pais_nacimiento']].drop_duplicates()
    final_df = pd.concat([countries_A,countries_B], ignore_index=True, sort=False)
    countries_total = final_df[['titular_pais_nacimiento_id','titular_pais_nacimiento']].drop_duplicates()
    countries_total.columns = ['code','name']
    countries_clean = countries_total.drop(0) # fila 0 -> code: Nan, name: No aplica
    return countries_clean
    

def get_province():
    df = pd.read_csv('dnrpa-transferencias-autos-202305.csv', sep = ',', low_memory=False)
    conjunto_A = df[(df['automotor_origen'] == 'Nacional')& (df['registro_seccional_provincia'] == 'Formosa') & (df['automotor_anio_modelo'] > 2015)]
    conjunto_B = df [(df['registro_seccional_codigo'] == 1216) & (df['automotor_origen'] == 'Importado')]
    provinces_A = conjunto_A[['registro_seccional_provincia','titular_domicilio_provincia_id','titular_pais_nacimiento_id']].drop_duplicates()
    provinces_B = conjunto_B[['registro_seccional_provincia','titular_domicilio_provincia_id','titular_pais_nacimiento_id']].drop_duplicates()
    final_df_provinces = pd.concat([provinces_A,provinces_B], ignore_index=True, sort=False)
    provinces_total = final_df_provinces.drop_duplicates()
    provinces_total_Arg = provinces_total[(provinces_total['titular_pais_nacimiento_id'] == "ARG")] # Aplique este filtro ya que tenia un registro que el pais era Paraguay y la provincia Formosa por ende el codigo de la provincia no iba a ser UNIQUE
    provinces_total_Arg.columns = ['name','code','country_code']
    print (provinces_total_Arg)
    return provinces_total_Arg


def get_procedure():
    df = pd.read_csv('dnrpa-transferencias-autos-202305.csv', sep = ',', low_memory=False)
    df['code_number'] = df.index
    conjunto_A = df[(df['automotor_origen'] == 'Nacional')& (df['registro_seccional_provincia'] == 'Formosa') & (df['automotor_anio_modelo'] > 2015)]
    conjunto_B = df [(df['registro_seccional_codigo'] == 1216) & (df['automotor_origen'] == 'Importado')]
    procedure_A = conjunto_A[['code_number','tramite_tipo','titular_domicilio_provincia_id']].drop_duplicates()
    procedure_B = conjunto_B[['code_number','tramite_tipo','titular_domicilio_provincia_id']].drop_duplicates()
    final_df_procedure = pd.concat([procedure_A,procedure_B], ignore_index=True, sort=False)
    procedure_total = final_df_procedure.drop_duplicates()
    procedure_total.columns=['code_number','type','province_code']
    return procedure_total





        
       
        


