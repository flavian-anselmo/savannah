param servicePlanName string = 'savannah-plan'
param location string = 'eastus'
param sqlServerName string ='savannah'
param registryName string ='savannahregistry'
param webHookName string ='webappsavannahapi'

module servicePlan '../../Microsoft.Web/serverfarms.bicep' = {
  name:'AppServicePlan'
  params:{
    location:location
    servicePlanName: servicePlanName
  }
}

module containerRegistry '../../Microsoft.ContainerRegistry/registries.bicep' = {
  name:'registry'
  dependsOn:[
    servicePlan
  ]
  params:{
    location:location
    registryName: registryName
  }
}

module postgreSQLFlexibleServer '../../Microsoft.DBforPostgreSQL/flexibleServers.bicep' ={
  name:'postgresServer'
  params:{
    location:location
    sqlServerName:sqlServerName
  }
}

module webHookForContainerRegistry '../../Microsoft.ContainerRegistry/registries/webhooks.bicep'= {
  name:'webHook'
  dependsOn:[
    containerRegistry
  ]
  params:{
    containerRegistryName: registryName
    location:location
    webHookName:webHookName
  }
}
