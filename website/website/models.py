from SPARQLWrapper import SPARQLWrapper2


class SPARQL_Model:
    def get_statuses(self):
        sparql = SPARQLWrapper2("http://localhost:3030/legal_document_search/")
        query = """
                PREFIX lds: <http://www.semanticweb.org/master/ontologies/2023/1/legal_document_search#>
                SELECT ?Status ?status_value ?LegalDocument WHERE {
  
                    ?LegalDocument lds:hasStatus ?Status.
                    ?Status lds:status_value ?status_value.
                } LIMIT 10
        """
        sparql.setQuery(query)
        results = sparql.query().bindings
        return results

    def test_db_pedia(self):
        sparql = SPARQLWrapper2("http://dbpedia.org/sparql")
        sparql.setQuery(
            """
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            SELECT ?label
            WHERE { <http://dbpedia.org/resource/Asturias> rdfs:label ?label }"""
        )
        results = sparql.query().bindings

        # import pdb

        # pdb.set_trace()
        for result in results:
            print("%s: %s" % (result["label"].lang, result["label"].value))
        return results
