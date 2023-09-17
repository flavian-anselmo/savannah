param webHookName string 
param location string 
param containerRegistryName string

resource containerRegistry 'Microsoft.ContainerRegistry/registries@2022-12-01' existing = {
  name: containerRegistryName

}
 
resource webHookForContainerRegistry 'Microsoft.ContainerRegistry/registries/webhooks@2022-12-01' = {
  name: webHookName
  location: location
  parent: containerRegistry
  properties: {
    actions: [
      'push'
    ]
    scope: ''
    serviceUri: 'https://$savannah-api:Wl6jqwlh17vEhGtvbozsNXrstZuephsuTELZHo2WnneSkdaKyzh7ewKtXTg3@savannah-api.scm.azurewebsites.net/api/registry/webhook'
    status: 'enabled'
  }
}
