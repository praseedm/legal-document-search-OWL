from SPARQLWrapper import SPARQLWrapper2


class SPARQL_Model:
    def get_document_info(self):
        sparql = SPARQLWrapper2("http://localhost:3030/legal_document_search/")
        query = """
                PREFIX lds: <http://www.semanticweb.org/master/ontologies/2023/1/legal_document_search#>
                    SELECT ?document_id ?term_length ?status_value ?effective_date ?termination_date
                        ?notice_period WHERE {
                        ?LegalDocument lds:document_id ?document_id.
                        ?LegalDocument lds:term_length ?term_length.
                        ?LegalDocument lds:effective_date ?effective_date.
                        ?LegalDocument lds:termination_date ?termination_date.
                        ?LegalDocument lds:notice_period ?notice_period.
                        
                        ?LegalDocument lds:hasStatus ?Status.
                        ?Status lds:status_value ?status_value.
                    }
        """
        sparql.setQuery(query)
        results = sparql.query().bindings
        return results

    def filter_document_bystatus(self, status="pending"):
        sparql = SPARQLWrapper2("http://localhost:3030/legal_document_search/")
        query = (
            """
                PREFIX lds: <http://www.semanticweb.org/master/ontologies/2023/1/legal_document_search#>
                    SELECT ?document_id ?term_length ?status_value ?effective_date ?termination_date
                        ?notice_period WHERE {
                        ?LegalDocument lds:document_id ?document_id.
                        ?LegalDocument lds:term_length ?term_length.
                        ?LegalDocument lds:effective_date ?effective_date.
                        ?LegalDocument lds:termination_date ?termination_date.
                        ?LegalDocument lds:notice_period ?notice_period.
                        
                        ?LegalDocument lds:hasStatus ?Status.
                        ?Status lds:status_value ?status_value.
                    
        """
            + f'?Status lds:status_value "{status}"'
            + " }"
        )
        sparql.setQuery(query)
        results = sparql.query().bindings
        return results

    def get_parties_info(self):
        sparql = SPARQLWrapper2("http://localhost:3030/legal_document_search/")
        query = """
                PREFIX lds: <http://www.semanticweb.org/master/ontologies/2023/1/legal_document_search#>
                SELECT ?document_id ?employer_name ?employee_name ?employer_address ?employee_address WHERE {
                    ?LegalDocument lds:document_id ?document_id.
                    
                    ?LegalDocument lds:hasEmployee ?Employee.
                    ?Employee lds:party_name ?employee_name.
                    ?Employee lds:party_address ?employee_address.
                    
                    ?LegalDocument lds:hasEmployer ?Employer.
                    ?Employer lds:party_name ?employer_name.
                    ?Employer lds:party_address ?employer_address.
                }
        """
        sparql.setQuery(query)
        results = sparql.query().bindings
        return results

    def get_remuneratoin_info(self):
        sparql = SPARQLWrapper2("http://localhost:3030/legal_document_search/")
        query = """
                PREFIX lds: <http://www.semanticweb.org/master/ontologies/2023/1/legal_document_search#>
                SELECT ?document_id ?remuneration_amount ?currency WHERE {
                    ?LegalDocument lds:document_id ?document_id.
                    
                    ?LegalDocument lds:hasRemuneration ?Remuneration.
                    ?Remuneration lds:amount_value ?remuneration_amount.
                    ?Remuneration lds:amount_currency ?currency.
                }
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
