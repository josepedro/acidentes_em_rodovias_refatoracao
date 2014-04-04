#Acidentes em Rodovias - Variables

##Python

####generico_dao.py

#####__Class__ GenericoDAO: Creates Database connection, executes queries and transform queries results in objects

|Type     |Name        |Description        |
|:---------:|:------------|:-------------------|
|Method   |\_\_init\_\_ | Class constructor |
|Variable | usuario | Database's username |
|Variable | database | Database's schema name|
|Variable | senha | Database's password |
|Variable | host | Database's host |
|Variable | conexao | Receives a connection with the Database |

|Type     |Name        |Description        |
|:---------:|:------------|:-------------------|
|Method   | get_conexao | Starts and returns a connection with the Database |

|Type     |Name        |Description        |
|:---------:|:------------|:-------------------|
|Method   | executa_query | Executes a SQL query |
|Parameter| query | A SQL instruction |
|Parameter| get\_data\_frame | Determines the format of the query results. Sets False as default |
|Variable | dados | Receives the query result |

|Type     |Name        |Description        |
|:---------:|:------------|:-------------------|
|Method | transforma\_dicionario\_em\_objetos| Transforms the query results in a model object |
|Parameter| classe | Determines the Class of the model object |
|Parameter| modulo | Indicates the name of the module that the class is |
|Variable | modulo\_classe | Receives the module inserted into __sys.modules__ |
|Variable | lista_objetos | A list of the objects that will be returned |
|Variable | chaves | Receives the keys of the query dictionary |
|Variable | instancia | Instance of a determined object |

####envolvidos\_acidentes\_dao.py


#####__Class__ EnvolvidosAcidentesDAO Obtains data on those involved in accidents

|Type     |Name        |Description        |
|:---------:|:------------|:-------------------|
|Method | envolvidos\_acidentes | Returns the amount involved and the number of accidents per year |
|Variable | query | In method envolvidos\_acidentes, queries the amount involved and the number of accidents per year |

|Type     |Name        |Description        |
|:---------:|:------------|:-------------------|
|Method | media\_desvio\_envolvidos | Returns the average involved in accidents and it's standard deviation |
|Variable | lista\_envolvidos | List of involved in accidents per year |
|Variable | lista\_medias | List of averages involved in accidents |
|Variable | envolvidos | Number of involved |
|Variable | acidentes | Number of accidents |
|Variable | media | Average of involved in accidents |
|Variable | desvio | Standard deviation |

####municipio_dao.py

#####__Class__ MunicipioDAO: Obtains the list of brazilian municipalities

|Type     |Name        |Description        |
|:---------:|:------------|:-------------------|
| Method | lista\_municipios | Returns the list of brazilian municipalities of a state |
| Parameter | uf | Abreviation of the state's name |
| Parameter | limite | Limits the query |
| Variable | query | Queries the municipalities of a state |

