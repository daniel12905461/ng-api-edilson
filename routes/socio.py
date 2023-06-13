from fastapi import APIRouter
from config.db import conectar_db
from schemas.socio import Socio
import json
import mysql.connector

socios = APIRouter()

@socios.get("/socios")
async def getall():
  cnx = conectar_db()

  cursor = cnx.cursor()

  consulta = ("SELECT nombres, apellidos, ci, foto, celular, fecha_nac, id, user, password, id_rols FROM socios")
  cursor.execute(consulta)
  resultados = cursor.fetchall()

  json_resultados = {"data": []}

  for fila in resultados:
    json_resultados["data"].append({
      "nombres": fila[0],
      "apellidos": fila[1],
      "ci": fila[2],
      "foto": fila[3],
      "celular": fila[4],
      "fecha_nac": fila[5],
      "id": fila[6],
      "user": fila[7],
      "password": fila[8],
      "id_rols": fila[9]
    })
    json_resultados["ok"] = True

  if len(json_resultados["data"]) == 0:
    json_resultados["mensaje"] = "No se encontraron resultados para la consulta."
    json_resultados["ok"] = False

  cursor.close()
  cnx.close()

  return json_resultados

@socios.get("/socios/{id}")
async def getbyid(id: int):
  cnx = conectar_db()

  cursor = cnx.cursor()

  consulta = ("SELECT nombres, apellidos, ci, foto, celular, fecha_nac, id, user, password, id_rols FROM socios WHERE id = "+str(id))
  # valores = (id)
  cursor.execute(consulta)
  resultados = cursor.fetchall()

  json_resultados = {"data": []}

  for fila in resultados:
    json_resultados["data"] = {
      "nombres": fila[0],
      "apellidos": fila[1],
      "ci": fila[2],
      "foto": fila[3],
      "celular": fila[4],
      "fecha_nac": fila[5],
      "id": fila[6],
      "user": fila[7],
      "password": fila[8],
      "id_rols": fila[9]
    }
    json_resultados["ok"] = True

  if len(json_resultados["data"]) == 0:
    json_resultados["mensaje"] = "No se encontraron resultados para la consulta."
    json_resultados["ok"] = False

  cursor.close()
  cnx.close()

  return json_resultados

@socios.post("/socios")
async def create(socio: Socio):
  cnx = conectar_db()
  cursor = cnx.cursor()

  sentencia = "INSERT INTO socios (nombres, apellidos, ci, foto, celular, fecha_nac, user, password, id_rols) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
  valores = (socio.nombres, socio.apellidos, socio.ci, socio.foto, socio.celular, socio.fecha_nac, socio.user, socio.password, socio.id_rols)

  try:
    cursor.execute(sentencia, valores)
    cnx.commit()

    num_filas_afectadas = cursor.rowcount

    json_respuesta = {"mensaje": "Inserción exitosa.", "filas_afectadas": num_filas_afectadas}

  except mysql.connector.Error as error:
    json_respuesta = {"mensaje": "Error al insertar en la base de datos: {}".format(error.msg)}

  finally:
    cursor.close()
    cnx.close()

  return json_respuesta

@socios.put("/socios/{id}")
async def update(id: int, socio: Socio):
  cnx = conectar_db()
  cursor = cnx.cursor()

  sentencia = "UPDATE socios SET nombres = '"+socio.nombres+"', apellidos = '"+socio.apellidos+"', ci = '"+socio.ci+"', foto = '"+socio.foto+"', celular = '"+socio.celular+"', fecha_nac = '"+socio.fecha_nac+"', user = '"+socio.user+"', password = '"+socio.password+"', id_rols = '"+socio.id_rols+"' WHERE id = "+str(id)

  cursor.execute(sentencia)
  cnx.commit()

  cursor.close()
  cnx.close()

  return cursor

@socios.delete("/socios/{id}")
async def delete(id: int):
  cnx = conectar_db()
  cursor = cnx.cursor()

  sentencia = "DELETE FROM socios WHERE id = "+str(id)

  cursor.execute(sentencia)
  cnx.commit()

  cursor.close()
  cnx.close()

  return cursor
