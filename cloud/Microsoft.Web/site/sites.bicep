param location string 
param siteName string 
param planName string 
resource servicePlan 'Microsoft.Web/serverfarms@2022-03-01' existing = {
  name: planName
}
resource site 'Microsoft.Web/sites@2022-03-01'  = {
  name:siteName
  location:location
  kind:'app,linux,container'
  dependsOn:[
    servicePlan
  ]
  properties:{

    serverFarmId: servicePlan.id  
  }
}
