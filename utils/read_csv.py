import pandas as pd


class Dataframe:
    def __init__(self, filename) -> None:
        self.df = pd.read_csv(filename, sep=",", low_memory=False)
        self.df['code_number'] = self.df.index
        self.conjunto_A = self.df[(self.df['automotor_origen'] == 'Nacional')& (self.df['registro_seccional_provincia'] == 'Formosa') & (self.df['automotor_anio_modelo'] > 2015)]
        self.conjunto_B = self.df [(self.df['registro_seccional_codigo'] == 1216) & (self.df['automotor_origen'] == 'Importado')]
    
    def process_data(self):
        raise NotImplementedError("Subclasses must implement process_data method.")

class CountriesData(Dataframe):
    def process_data(self):
        countries_A = self.conjunto_A[['titular_pais_nacimiento', 'titular_pais_nacimiento_id']].drop_duplicates()
        countries_B = self.conjunto_B[['titular_pais_nacimiento', 'titular_pais_nacimiento_id']].drop_duplicates()
        final_df = pd.concat([countries_A, countries_B], ignore_index=True, sort=False)
        countries_total = final_df[['titular_pais_nacimiento', 'titular_pais_nacimiento_id']].drop_duplicates()
        countries_total.columns = ['name', 'code']
        countries_clean = countries_total.drop(0) # fila 0 -> code: Nan, name: No aplica
        return countries_clean, True

class ProvincesData(Dataframe):
    def process_data(self):
        provinces_A = self.conjunto_A[['registro_seccional_provincia', 'titular_domicilio_provincia_id', 'titular_pais_nacimiento_id']].drop_duplicates()
        provinces_B = self.conjunto_B[['registro_seccional_provincia', 'titular_domicilio_provincia_id', 'titular_pais_nacimiento_id']].drop_duplicates()
        final_df_provinces = pd.concat([provinces_A, provinces_B], ignore_index=True, sort=False)
        provinces_total = final_df_provinces.drop_duplicates()
        provinces_total_Arg = provinces_total[(provinces_total['titular_pais_nacimiento_id'] == "ARG")] # Aplique este filtro ya que tenia un registro que el pais era Paraguay y la provincia Formosa por ende el codigo de la provincia no iba a ser UNIQUE
        provinces_total_Arg.columns = ['name', 'code', 'country_code']
        return provinces_total_Arg, True

class ProcedureData(Dataframe):
    def process_data(self):
        procedure_A = self.conjunto_A[['code_number', 'tramite_tipo', 'titular_domicilio_provincia_id']].drop_duplicates()
        procedure_B = self.conjunto_B[['code_number', 'tramite_tipo', 'titular_domicilio_provincia_id']].drop_duplicates()
        final_df_procedure = pd.concat([procedure_A, procedure_B], ignore_index=True, sort=False)
        procedure_total = final_df_procedure.drop_duplicates()
        procedure_total.columns=['code_number','type','province_code']
        return procedure_total, True

        
       
        



