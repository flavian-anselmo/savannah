param webHookName string 
param location string 
param containerRegistryName string
param serviceUri string 
param action string 

resource containerRegistry 'Microsoft.ContainerRegistry/registries@2022-12-01' existing = {
  name: containerRegistryName

}
 
resource webHookForContainerRegistry 'Microsoft.ContainerRegistry/registries/webhooks@2022-12-01' = {
  name: webHookName
  location: location
  parent: containerRegistry
  properties: {
    actions: [
      action
    ]
    scope: ''
    serviceUri: serviceUri
    status: 'enabled'
  }
}
