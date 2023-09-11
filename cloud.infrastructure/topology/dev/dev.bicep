param servicePlanName string = 'savannah-plan'
param location string = 'eastus'
param sqlServerName string = 'savannah'
param registryName string = 'savannahregistry'
param webHookName string = 'webappsavannahapi'


// param appServiceName string = 'savannah-api'


module servicePlan '../../Microsoft.Web/serverfarms.bicep' = {
  name:'AppServicePlan'
  params:{
    location:location
    servicePlanName: servicePlanName
  }
}

// module appService '../../Microsoft.Web/site/sites.bicep' = {
//   name:'AppService'
//   params:{
//     location:location
//     planName:servicePlanName
//     siteName:appServiceName
//   }
// }


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
