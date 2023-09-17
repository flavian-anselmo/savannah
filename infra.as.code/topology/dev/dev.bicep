param servicePlanName string 
param location string 
param sqlServerName string
param registryName string 
param webHookName string 

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
