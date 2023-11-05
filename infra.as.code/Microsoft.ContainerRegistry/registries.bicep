param registryName string 
param location string 
param skuName string 

resource containerRegistry 'Microsoft.ContainerRegistry/registries@2022-12-01' = {
  name:registryName
  location:location
  sku:{
    name:skuName
  }
  properties:{
    adminUserEnabled:true
    policies:{
      quarantinePolicy:{
        status:'disabled'
      }
      trustPolicy:{
        type:'Notary'
        status:'disabled'
      }
      retentionPolicy:{
        days:7
        status:'disabled'
      }
    }

  }
}
