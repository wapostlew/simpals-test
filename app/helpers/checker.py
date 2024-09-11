from elasticsearch import Elasticsearch


def initialize_mappings(hosts: str, index_name: str, mappings):
    es = Elasticsearch(hosts=hosts)
    try:
        exists = es.indices.exists(index=index_name)
        if not exists:
            es.indices.create(index=index_name, body={"mappings": mappings})
            print(f"Index {index_name} created.")
    except Exception as e:
        print(f"Error updating mappings: {e}")
    finally:
        es.close()
