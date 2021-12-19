from django.shortcuts import render
import sqlite3
from sqlite3 import Error
# Create your views here.
from django.shortcuts import render
from django.template import loader
import pandas as pd
import json
from sqlalchemy import create_engine
# Create your views here.
def createTableImmobilier():
    df = pd.read_csv('hello//static//file_uploaded//promoteur_immo_V2.csv', delimiter=',')
    tf = df[df.balcony == True]
    engine = create_engine('postgresql://manuel:jw8s0F4@localhost:5432/myimmo')
    tf.to_sql('immobilier', engine)

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect('C:\\Users\\Joe\\Desktop\\py\\brief14\\myapp\\db.sqlite3')
    except Error as e:
        print(e)
    return conn

def index(request):
    conn = sqlite3.connect('/tmp/8d9c3248c81cf5e/db.sqlite3')
    df = pd.read_sql_query("SELECT * FROM data_view_data_view", conn)
    total_rows = len(df.index)
    bien = total_rows + 1
    s = df.groupby('ville')['prix_m2_ttc'].mean()
    mean_records = s.reset_index().to_json(orient ='records')
    mean = []
    mean = json.loads(mean_records)
    st = df.groupby('ville')['prix_m2_ttc'].std()
    std_records = st.reset_index().to_json(orient ='records')
    std = []
    std = json.loads(std_records)
    return render(request, 'data/view.html',{'bien':bien, 'mean':mean, 'std':std})
