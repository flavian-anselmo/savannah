param location string
param servicePlanName string 
resource servicePlan 'Microsoft.Web/serverfarms@2022-09-01' = {
  location:location
  name:servicePlanName
  kind:'linux'
  sku:{
    name:'S1'
    tier:'Standard'
    family:'S'
    capacity:1
  }
  properties:{
    zoneRedundant:false
  }
}
