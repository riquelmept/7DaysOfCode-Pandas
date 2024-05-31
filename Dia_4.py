import pandas as pd
import seaborn as sns
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt

#Importando dados pelo acervo do Franciscono GitHub

dados_2010_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20101.csv?raw=true')
dados_2010_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20102.csv?raw=true')
dados_2011_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20111.csv?raw=true')
dados_2011_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20112.csv?raw=true')
dados_2012_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20121.csv?raw=true')
dados_2012_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20122.csv?raw=true')
dados_2013_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20131.csv?raw=true')
dados_2013_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20132.csv?raw=true')
dados_2014_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20141.csv?raw=true')
dados_2014_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20142.csv?raw=true')
dados_2015_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20151.csv?raw=true')
dados_2015_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20152.csv?raw=true')
dados_2016_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20161.csv?raw=true')
dados_2016_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20162.csv?raw=true')
dados_2017_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20171.csv?raw=true')
dados_2017_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20172.csv?raw=true')
dados_2018_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20181.csv?raw=true')
dados_2018_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20182.csv?raw=true')
dados_2019_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20191.csv?raw=true')
dados_2019_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20192.csv?raw=true')
dados_2020_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20201.csv?raw=true')

#Concatenando todos os DataFrame
emprestimos_biblioteca = pd.concat([dados_2010_1,dados_2010_2,dados_2011_1,dados_2011_2,dados_2012_1,dados_2012_2,dados_2013_1,dados_2013_2,dados_2014_1,
                                    dados_2014_2,dados_2015_1,dados_2015_2,dados_2016_1,dados_2016_2,dados_2017_1,dados_2017_2,dados_2018_1,dados_2018_2,
                                    dados_2019_1,dados_2019_2,dados_2020_1],ignore_index=True)

emprestimos_biblioteca

#Verificando e excluindo dados duplciados
emprestimos_biblioteca.value_counts()
emprestimos_biblioteca = emprestimos_biblioteca.drop_duplicates()
emprestimos_biblioteca.value_counts()

#Verificando estrutura inicial dos dados
emprestimos_biblioteca.head()

#Importando Dados Exemplares
dados_exemplares = pd.read_parquet('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/raw/main/Dia_1-Importando_dados/Datasets/dados_exemplares.parquet')
dados_exemplares

#Concatenando junto ao DF atualizado
emprestimos_completo = emprestimos_biblioteca.merge(dados_exemplares)
emprestimos_completo

#Primeiras Manipulações
emprestimos_completo.head()

"""
Proposta de incluir coluna com nomenclatura da CDU(Classificação Decimal Universal):
000 a 099: Generalidades. Ciência e conhecimento.
100 a 199: Filosofia e psicologia.
200 a 299: Religião.
300 a 399: Ciências sociais.
400 a 499: Classe vaga. Provisoriamente não ocupada.
500 a 599: Matemática e ciências naturais.
600 a 699: Ciências aplicadas.
700 a 799: Belas artes.
800 a 899: Linguagem. Língua. Linguística.
900 a 999: Geografia. Biografia. História.
"""

CDU_lista = []
for CDU in emprestimos_completo['localizacao']:
  if(CDU < 100):
    CDU_lista.append('Generalidades')
  elif(CDU < 200):
    CDU_lista.append('Filosofia e psicologia')
  elif(CDU < 300):
    CDU_lista.append('Religião')
  elif(CDU < 400):
    CDU_lista.append('Ciências sociais')
  elif(CDU < 500):
    CDU_lista.append('Classe vaga')
  elif(CDU < 600):
    CDU_lista.append('Matemática e ciências naturais')
  elif(CDU < 700):
    CDU_lista.append('Ciências aplicadas')
  elif(CDU < 800):
    CDU_lista.append('Belas artes')
  elif(CDU < 900):
    CDU_lista.append('Linguagem')
  else:
    CDU_lista.append('Geografia. Biografia. História.')

emprestimos_completo['CDU_geral'] = CDU_lista

emprestimos_completo.head()

#Excluindo coluna "registro_sistema" e alterando type de matrícula

emprestimos_completo.drop(columns=['registro_sistema'],inplace=True)

emprestimos_completo['matricula_ou_siape'] = emprestimos_completo['matricula_ou_siape'].astype('string')

emprestimos_completo.info()

emprestimos_completo.head()

emprestimos_completo['id_emprestimo'].value_counts()

emprestimos_completo.loc[emprestimos_completo['id_emprestimo']==2560028]

emprestimos = len(emprestimos_completo['id_emprestimo'].drop_duplicates())
emprestimos

exemplares = len(emprestimos_completo)
exemplares

emprestimos_data = pd.DataFrame(emprestimos_completo['data_emprestimo'].value_counts()).reset_index()
emprestimos_data.columns = ['data','quantidade']
emprestimos_data['data'] = pd.to_datetime(emprestimos_data['data'])
emprestimos_data

emprestimos_por_ano = emprestimos_data.groupby(by=emprestimos_data.data.dt.year).count()
emprestimos_por_ano.index = emprestimos_por_ano.index.set_names('ano')
emprestimos_por_ano

sns.set_theme(context='notebook', 
              style='darkgrid', 
              palette='deep', 
              font_scale=1.3, 
              rc={"figure.figsize":(15,8)})

ax = sns.lineplot(data=emprestimos_por_ano,x='ano',y='quantidade')
ax.set(xlabel=None,ylabel=None)
ax.tick_params(axis='x', rotation=30)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',').replace(',','.')))   

ax.set_title('Quantidade de exemplares emprestados do SISBI por ano'+'\n',size=20,loc='left',weight='bold')

ax=ax

emprestimos_por_mes = emprestimos_data.groupby(by=emprestimos_data.data.dt.month).count()
emprestimos_por_mes.index.name = 'mes'
emprestimos_por_mes

dict_meses = {1:'Jan',2:'Fev',3:'Mar',4:'Abr',
                    5:'Mai',6:'Jun',7:'Jul',8:'Ago',
                    9:'Set',10:'Out',11:'Nov',12:'Dez'}

emprestimos_por_mes.index = emprestimos_por_mes.index.map(dict_meses)

emprestimos_por_mes

ax = sns.lineplot(data=emprestimos_por_mes,x='mes',y='quantidade')
ax.set(xlabel=None,ylabel=None)
ax.tick_params(axis='x',rotation=30)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',').replace(',','.')))                

ax.set_title("Quantidade de exemplares emprestados do SISBI por mês"+"\n",size=20,loc='left',weight='bold')
ax.text(s='Período de 2010 a 2020',x=-0.5,y=265000,fontsize=18, ha='left',color='gray')

emprestimos_data.data

emprestimos_por_hora = emprestimos_data.groupby(by=emprestimos_data.data.dt.hour).count()
emprestimos_por_hora.index.name = 'horas'
emprestimos_por_hora = emprestimos_por_hora.reset_index()
emprestimos_por_hora

emprestimos_por_hora = emprestimos_por_hora.sort_values(ascending=True,by='quantidade')

ax = sns.barplot(data=emprestimos_por_hora,y='quantidade',x='horas',
                 palette='Blues',hue='quantidade',dodge=False)                  #Ordenar pela quantidade de exemplares emprestados
plt.legend([],[], frameon=False)                                                #Excluir a legenda do gráfico

ax.set(xlabel='Horário',ylabel=None)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',').replace(',','.')))           
ax.set_title("Quantidade de exemplares emprestados do SISBI por faixa horária"+"\n",size=20,loc='left',weight='bold')
ax.text(s='Período de 2010 a 2020',x=-0.5,y=225000,fontsize=18, ha='left',color='gray')
ax=ax

emprestimos_completo.head()

#Modificando para data o tipo de dado do DF

emprestimos_completo['data_emprestimo'] = pd.to_datetime(emprestimos_completo['data_emprestimo'])

#Verificando valores únicos das variáveis

emprestimos_completo.tipo_vinculo_usuario.unique()

emprestimos_completo.colecao.unique()

emprestimos_completo.biblioteca.unique()

emprestimos_completo.CDU_geral.unique()

def calcula_freq(variavel):
  '''
  Esta função irá gerar uma tabela de frequência com percentuais de acordo 
  com a variável passada. 

  variavel = variável categórica escolhida de dentro do conjunto de dados 
  emprestimos_completo
  '''

  dataframe = pd.DataFrame(emprestimos_completo[variavel].value_counts())                      
  dataframe.columns = ['quantidade']
  dataframe['percentual'] = round((dataframe.quantidade / dataframe.quantidade.sum())*100,1)

  return dataframe

calcula_freq('tipo_vinculo_usuario')

calcula_freq('colecao')

calcula_freq('biblioteca')

calcula_freq('CDU_geral')