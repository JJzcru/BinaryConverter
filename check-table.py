#!/usr/bin/env python
if __name__ == "__main__":
   archivo="alteraciones.php"
   inic = """<?php
   include_once 'session.class.php';
   include_once 'modulos.php';
   $sesion = new session();
   $modulos = new modulos();
   $dbcon=connect();\n"""
   final= inic
   molino = int(input ('Inserte el numero del molino: '))
   puntos = int(input ('Inserte la cantidad de puntos del molino: '))
   #X indica en que punto estan
   for x in range(1,puntos+1):
      checks = int(input ('\nCuantos checks tiene el punto ' + str(x) + ": "))
      #Y indica en que check estan
      for y in range(1,checks+1):
   		final=final + "$sql=\"" 
         final = final + "INSERT INTO dcheck (nombre,molino,punto,checks) VALUES ("
         final = final + input('Inserte el nombre del punto') + ", " + str(molino) + ", " + str(x) + ", " + str(y) 

   		final = final + "CREATE TABLE \u0060punto2." + str(x) + "\u0060 ( "
   		final = final + "id int NOT NULL AUTO_INCREMENT, "
   		for y in range(1,checks+1):
   			final = final + "check" + str(y) + " TINYINT(1), "
   			observaciones = int(input ('El check ' + str(y) + ' tiene observacion 1/0: '))
   			if observaciones==1:
   				final = final + "obs" + str(y) + " int, "
   		final = final + "comentario varchar(1000) DEFAULT NULL, checks TINYINT(1) DEFAULT NULL, obss int DEFAULT NULL, checka TINYINT(1) DEFAULT NULL, obsa int DEFAULT NULL, PRIMARY KEY (id)); "









   		final=final + "\";\nmysql_query($sql,$dbcon);\n"







   final=final + "\necho \"Insersiones/Alteraciones/Borrados Exitosos\";\n?>"
   g = open(archivo,"w")
   g.write(final)
   g.close() 
print ("Repeticion exitosa")
input()
