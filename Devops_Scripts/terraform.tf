terraform{
    required_providers {
      azurerm = {
        source = "hashicorp/azurerm"
        version = ~>4.0""
      }
 }   
}

providers "azurerm" {
    features{}
}

terraform{
    backend "azurerm" {
        resource-group-name = 
        stotage-account-name = 
        container-name = 
        key = "terraform.tfstate"
    }    
}