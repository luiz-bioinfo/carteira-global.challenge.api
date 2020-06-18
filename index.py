# Imports

from flask import Flask
from flask_graphql import GraphQLView

from flask_cors import CORS

from mysql import connector
from graphene import *

import json

# Constants

DB_HOST = '127.0.0.1'
DB_USER = 'root'
DB_PASS = ''
DB_NAME = 'carteira-global.challenge.db'

# MySQL Connection

connection = connector.connect(
  host = DB_HOST,
  user = DB_USER,
  password = DB_PASS,
  database = DB_NAME
)

cursor = connection.cursor(prepared=True)

# Graphene Settings

class FII(ObjectType):
  id               = ID()
  ticker           = String()
  nome_fundo       = String()
  setor            = String()
  preco_atual      = Float()
  variacao_dia     = Float()
  ultimo_dividendo = Float()
  ultimo_dy        = Float()
  var_cota_ipo     = Float()
  var_cota_div_ipo = Float()
  p_vp             = Float()
  percent_em_caixa = Float()
  numero_cotistas  = Int()
  patrimonio       = Float()
  liquidez_diaria  = Float()
  favoritar        = Boolean()

class Query(ObjectType):
  fiis = List(FII)

  def resolve_fiis(parent, info):
    cursor.execute('select * from fii')
    rows = map(
      lambda row: FII(
        row[0],  row[1],  row[2],  row[3],
        row[4],  row[5],  row[6],  row[7],
        row[8],  row[9],  row[10], row[11],
        row[12], row[13], row[14], row[15]
      ),
      cursor.fetchall()
    )
    return rows

schema = Schema(
  query = Query
)

# App

app = Flask(__name__)
CORS(app)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))