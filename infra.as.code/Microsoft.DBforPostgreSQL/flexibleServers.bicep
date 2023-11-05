param location string 
param sqlServerName string 
resource  sqlFlexibleServer 'Microsoft.DBforPostgreSQL/flexibleServers@2021-06-01' = {
  location:location
  name: sqlServerName
  sku:{
    name:'Standard_B1ms'
    tier:'Burstable'
  }
  properties:{
    administratorLogin:'anselmo'
    administratorLoginPassword:'savannahtest123/'
    version: '14'
    storage:{
      storageSizeGB:32
    }
    backup:{
      backupRetentionDays:7
      geoRedundantBackup:'Disabled'
    }
    highAvailability:{
      mode:'Disabled'
    }
    maintenanceWindow:{
      customWindow:'Disabled'
      dayOfWeek:0
      startHour:0
      startMinute:0
    }
  }
}
