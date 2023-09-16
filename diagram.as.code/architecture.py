from diagrams import Diagram, Cluster
from diagrams.azure.compute import ACR
from diagrams.azure.web import AppServices, AppServicePlans
from diagrams.azure.database import DatabaseForPostgresqlServers
from diagrams.azure.database import SQLDatabases
from diagrams.c4 import Container


with Diagram('assets/cloud_infra', show=False):
    with Cluster('Resource.Group (savannah.test)') as resource_group:
        with Cluster('Web') as web:
            app_service =[
                AppServices('app.service') >> AppServicePlans('app.service.plan')
            ] 
    
        with Cluster('PostgreSQL Flexible Server') as flexible_server:
            postgres_server = DatabaseForPostgresqlServers('Flexible.Server')
            with Cluster('Databases'):
                databases = [
                    SQLDatabases('db.production'),
                    SQLDatabases('db.testing'),
                    SQLDatabases('db.development')
                ]
                postgres_server >> databases
        postgres_server >> app_service
        app_service >> postgres_server

        with Cluster('Container.Registry'):
            azure_container_registry = ACR('ACR')
            web_hook = Container(
                name="Web.Hook",
                technology="registries",
                description="watch out for any image push to ACR",
            )
            azure_container_registry >> web_hook
            web_hook >> azure_container_registry
        app_service >> web_hook
        web_hook >> app_service



        



        





                


