from elasticsearch import Elasticsearch
import logging


def initialize_mappings(hosts: str, index_name: str, mappings):
    es = Elasticsearch(hosts=hosts)
    try:
        exists = es.indices.exists(index=index_name)
        if not exists:
            es.indices.create(index=index_name, body={"mappings": mappings})
    except Exception as e:
        pass
    finally:
        es.close()
