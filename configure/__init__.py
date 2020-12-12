# Created by zhouwang on 2020/9/23.
import os
import configparser

path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'env')

try:
    env = open(path, 'r+').read().strip()
except Exception as e:
    print(e)
    env = 'development'


cf = configparser.ConfigParser()
cf.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), '%s.ini' % env))


elasticsearch = {
    'hosts': [{'host': hp.split(':')[0], 'port': hp.split(':')[1]}
              for hp in cf.get('elasticsearch', 'hosts').split(',')],
    'index': cf.get('elasticsearch', 'index')
}


tdengine = {
    'host': cf.get('tdengine', 'host'),
    'user': cf.get('tdengine', 'user'),
    'password': cf.get('tdengine', 'password'),
    'database': cf.get('tdengine', 'database')
}

