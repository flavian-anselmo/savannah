param servicePlanName string = 'savannah-plan'
param location string = 'eastus'
module servicePlan '../../Microsoft.Web/serverfarms.bicep' = {
  name:'AppServicePlan'
  params:{
    location:location
    servicePlanName: servicePlanName
  }
}
