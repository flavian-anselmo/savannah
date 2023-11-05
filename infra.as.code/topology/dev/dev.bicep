param servicePlanName string 
param location string 
param sqlServerName string
param registryName string 
param webHookName string 
param serviceUri string = 'https://$savannah-api:Wl6jqwlh17vEhGtvbozsNXrstZuephsuTELZHo2WnneSkdaKyzh7ewKtXTg3@savannah-api.scm.azurewebsites.net/api/registry/webhook'
param action string = 'push'

module servicePlan '../../Microsoft.Web/serverfarms.bicep' = {
  name:'AppServicePlan'
  params:{
    location:location
    servicePlanName: servicePlanName
  }
}
module appservice '../../Microsoft.Web/site/sites.bicep' = {
  dependsOn:[
    servicePlan
  ]
  name:'appService'
  params:{
    location:location
    siteName:'savannah-api'
    planName:servicePlanName
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
    action:action
    serviceUri:serviceUri
  }
}
