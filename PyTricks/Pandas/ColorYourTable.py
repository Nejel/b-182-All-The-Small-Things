import pandas as pd
from flask import Flask
import requests
from pandas.io.json import json_normalize

app = Flask(__name__)
app.debug = True

def highlight(row):
    text_field = 'rmq_id'
    val_field = 'rmq_stat_flag'

    colors = {0: 'gray',
              1: 'green',
              2: 'yellow'}
    if row[val_field] in colors:
        color = colors[row[val_field]]
    else:
        try:
            val = int(row[val_field])
            if val > 2:
                color = 'red'
            else:
                color = 'lightgray'
        except ValueError:
            color = 'gray'

    return ['background-color: %s' % color if name == text_field else '' for name in row.index]

def get_table():
    url = "http://worker1.datastream.center:9000/stat"
    r = requests.get(url)
    json = r.json()
    df0 = json_normalize(json['statistics'])
    df0 = pd.DataFrame(data=df0)
    df1 = json_normalize(json['stat'])
    df1 = pd.DataFrame(data=df1)
    df = pd.concat([df0, df1], axis=1, sort=False)
    df['last_check'] = df['last_check'].fillna(method='ffill')
    df = df[['last_check', 'rmq_id', 'project', 'host', 'un_mins', 'consumer', 'message', 'rmq_stat_flag']]
    return df.style.apply(highlight, axis=1).set_table_attributes('border="1"').hide_index().hide_columns('rmq_stat_flag').render() # разукрашиваем таблицу и применяем стили

@app.route('/')
def main_page():
    return get_table()

if __name__ == '__main__':
    app.run()
