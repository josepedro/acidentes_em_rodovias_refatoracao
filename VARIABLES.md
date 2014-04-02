#Acidentes em Rodovias - Variables

##Python

####generico_dao.py

|Type     |Name        |Description        |
|:---------:|:------------|:-------------------|
|Class    |GenericoDAO | Creates Database connection, executes queries and transform queries results in objects |
|Method   |\_\_init\_\_ | Class constructor |
|Variable | usuario | Database's username |
|Variable | database | Database's schema name|
|Variable | senha | Database's password |
|Variable | host | Database's host |
|Variable | conexao | Receives a connection with the Database |
|Method   | get_conexao | Starts and returns a connection with the Database |
|Method   | executa_query | Executes a SQL query |
|Parameter| query | A SQL instruction |
|Parameter| get\_data\_frame | Determines the format of the query results. Sets False as default |
|Variable | dados | Receives the query result |
|Method | transforma\_dicionario\_em\_objetos| Transforms the query results in a model object |
|Parameter| classe | Determines the Class of the model object |
|Parameter| modulo | Indicates the name of the module that the class is |
|Variable | modulo\_classe | Receives the module inserted into __sys.modules__ |
|Variable | lista_objetos | A list of the objects that will be returned |
|Variable | chaves | Receives the keys of the query dictionary |
|Variable | instancia | Instance of a determined object |
