from diagrams import Diagram, Cluster
from diagrams.azure.compute import ACR
from diagrams.azure.web import AppServices, AppServicePlans
from diagrams.azure.database import DatabaseForPostgresqlServers
from diagrams.azure.database import SQLDatabases
from diagrams.c4 import Container
from diagrams.azure.general import Resourcegroups
from diagrams.onprem.vcs import Git, Github
from diagrams.onprem.ci import GithubActions
from diagrams.azure.general import Usericon


with Diagram('assets/cloud_infra', show=False):
    '''
    Cloud Infrastructure
    '''
    with Cluster('Resource.Group (savannah.test)'):
        resource_group = Resourcegroups('Resource.Group')
        with Cluster('Web'):
            app_service =[
                
                AppServices('app.service') >> AppServicePlans('app.service.plan')
            ] 
    
        with Cluster('PostgreSQL Flexible Server'):
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


    '''
    Deployment Strategy
    '''
    with Cluster('Deployment'):
        git = Git('git')
        git_hub = Github('git.hub')
        with Cluster('GithubActions'):
            cloud = GithubActions('Cloud.Infra')
            image = GithubActions('Image.Build')
            actions = [
                cloud,
                image
            ]
            image >> azure_container_registry
            cloud >> resource_group
        git >> git_hub >> cloud
        git >> git_hub >> image
    
    with Cluster('client'):
        url = Usericon('https://savannah-api.azurewebsites.net')
        url >> app_service








        





                


