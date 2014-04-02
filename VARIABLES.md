#Acidentes em Rodovias - Variables

##Python

####generico_dao.py

|Type     |Name        |Description        |
|:---------:|:------------|:-------------------|
|Class    |GenericoDAO | Create Database connection, execute querys and transform query results in objects |
|Method   |\_\_init\_\_ | Class constructor |
|Variable | usuario | Databse username |
|Variable | database | Database schema name|
|Variable | senha | Database password |
|Variable | host | Database host |
|Variable | conexao | Receives a connection with the Database |
|Method   | get_conexao | Start and returns a connection to the Database |
|Method   | executa_query | Executes a sql query |
|Parameter| query | A SQL instruction |
|Parameter| get\_data\_frame | Determines the format of the query results. False as default |
|Variable | dados | Receives the query result |
|Method | transforma\_dicionario\_em\_objetos| Transform the query results in a model object |
|Parameter| classe | Determines the Class of the model object |
|Parameter| modulo | Indicates the name of the module that the class is |
|Variable | modulo\_classe | Receives the module inserted into __sys.modules__ |
|Variable | lista_objetos | A list of objects that will be returned |
|Variable | chaves | Receives the keys of the query dictionary |
|Variable | instancia | Instance of a determined object |
