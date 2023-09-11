param servicePlanName string = 'savannah-plan'
param location string = 'eastus'
// param appServiceName string = 'savannah-api'

param registryName string = 'savannahregistry'

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
  params:{
    location:location
    registryName: registryName
  }
}

