# Created by zhouwang on 2020/9/11.
from graphite_api.node import LeafNode, BranchNode
from .render import Reader
import configure
import elasticsearch


class Finder(object):
    def __init__(self, config=None):
        self.es = elasticsearch.Elasticsearch(**configure.elasticsearch)
        self.es_index = configure.elasticsearch['index']

    def find_nodes(self, query):
        res = self.es.search(
            index=self.es_index,
            doc_type='_doc',
            body={
                'query': {
                    'regexp': {
                        'name': query.pattern.replace('.', '\\.').replace('*', '[-a-z0-9_;:]*')
                    }
                }
            },
            _source=['name', 'leaf']
        )

        for hit in res.get('hits', {}).get('hits'):
            metric = hit.get('_source')
            if metric['leaf']:
                yield LeafNode(metric['name'], Reader(metric['name']))
            else:
                yield BranchNode(metric['name'])
