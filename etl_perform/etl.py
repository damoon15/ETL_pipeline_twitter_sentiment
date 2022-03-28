import pymongo
from sqlalchemy import create_engine
import time
import logging
import pandas as pd

time.sleep(10)
###############################connect to the Database in mongo####################
client = pymongo.MongoClient("mongodb")
#client = pymongo.MongoClient("0.0.0.0:27027")
db = client.twitter

##############################create table in postgres##############################
pg = create_engine('postgresql://postgres:libertfire@postgresdb:5432/melone', echo=True)

pg.execute("""
    CREATE TABLE IF NOT EXISTS tweet_pool (
        id VARCHAR(1000),
        text VARCHAR(1000)
    );
""")

#########################transfer data from mongo to postgres###########################
entries = db.tweet_pool.find()
for e in entries:
    logging.critical('\n {}'.format(e))
    text = e['text']
    id = e['id']

    query = "INSERT INTO tweet_pool VALUES (%s, %s);"
    pg.execute(query, (id,text))

'''
entries = db.tweet_pool.find()
text = []
id = []
for e in entries:
    logging.critical('\n {}'.format(e))
    text.append(e['text'])
    id.append(e['id'])
dic = {'text': text, 'id':id}
df = pd.DataFrame(dic)
df.to_sql(df, pg, if_exists='replace')
'''

