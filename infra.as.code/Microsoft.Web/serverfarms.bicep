param location string
param servicePlanName string 

// @allowed(['B1','S1','B2','B3','F1'])
// param skuName string 

// @allowed(['Premium','Standard','Basic'])
// param skuTier string 


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
