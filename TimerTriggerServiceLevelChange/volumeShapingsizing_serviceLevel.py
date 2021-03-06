import json
import time
import requests
# the idea is to get the bearer token and pass the token to call the functions to list, create and other operations.

#Azure base authentication URL
AzureAuthURL = "https://login.microsoftonline.com/c9f32fcb-4ab7-40fe-af1b-1850d46cfbbe/oauth2/token"
AuthorizationURL = "https://login.microsoftonline.com/common/oauth2/authorize"
AzureAccountBaseURL = "https://management.azure.com/subscriptions/5ad8e8ac-cdb7-40bf-a1c1-ff707c86c9ea/resourceGroups/westus2.rg/providers/Microsoft.NetApp/netAppAccounts"
AzureVolumeBaseURL = "https://management.azure.com/subscriptions/5ad8e8ac-cdb7-40bf-a1c1-ff707c86c9ea/resourceGroups/westus2.rg/providers/Microsoft.NetApp/netAppAccounts/westus2/capacityPools/poolstandard/volumes"
AzureGetSpecificVolURL = "https://management.azure.com/subscriptions/5ad8e8ac-cdb7-40bf-a1c1-ff707c86c9ea/resourceGroups/westus2.rg/providers/Microsoft.NetApp/netAppAccounts/westus2/capacityPools/poolstandard/volumes"
AzureUpdateVolURL = "https://management.azure.com/subscriptions/5ad8e8ac-cdb7-40bf-a1c1-ff707c86c9ea/resourceGroups/westus2.rg/providers/Microsoft.NetApp/netAppAccounts/westus2/capacityPools/poolstandard/volumes/testVol"
AzureUpdateCapacityPool = "https://management.azure.com/subscriptions/5ad8e8ac-cdb7-40bf-a1c1-ff707c86c9ea/resourceGroups/westus2.rg/providers/Microsoft.NetApp/netAppAccounts/westus2/capacityPools/testpooltoDelete"
# header for the post function
headers1 = {
        'cache-control': "no-cache",
    }

#Payload for the get token
payload = "grant_type=client_credentials&client_id=EnterYourClentIDHere&client_secret=EnterYourSecretHere&resource=https%3A%2F%2Fmanagement.azure.com%2F&undefined="

    # get the bearer token
def get_token():
    response = requests.request("POST", AzureAuthURL, data=payload, headers=headers1)
    #print("The response code : ", response.status_code, response.text)
    getToken = response.json()
    accessToken = getToken['access_token']
    print("access token : ", getToken['access_token'])
    #self.test = accessToken
    return accessToken
def list_Volumes():
    token = get_token()
    #token = self.get_token()
    bearertoken = "Bearer " + token
    querystring = {"api-version": "2019-08-01"}
    HEADERS = {
        'Authorization': bearertoken,
        'Content-Type': "application/json",
        'cache-control': "no-cache",
    }
    getResult = requests.get(url=AzureVolumeBaseURL, headers=HEADERS, params=querystring)
    print("The response code : ", getResult.status_code, getResult.text)
    data = getResult.json()
    for i in data['value']:
        name = i['tags']
        print("name : ", name)
def get_Volume():
    token = get_token()
    #token = self.get_token()
    bearertoken = "Bearer " + token
    querystring = {"api-version": "2019-11-01"}
    HEADERS = {
        'Authorization': bearertoken,
        'Content-Type': "application/json",
        'cache-control': "no-cache",
    }
    getResult = requests.get(url=AzureGetSpecificVolURL, headers=HEADERS, params=querystring)
    print("The response code : ", getResult.status_code, getResult.text)
    data = getResult.json()
    for i in data['value']:
        name = i['tags']
        print("name : ", name)
def update_volume():
    #token = self.get_token()
    token=get_token()
    bearertoken = "Bearer " + token
    querystring = {"api-version": "2019-11-01"}
    HEADERS = {
        'Authorization': bearertoken,
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "bf720790-dc80-4f34-a64e-d70d042857c1"
    }
    payload1 = "{\n  \"location\": \"westus2\",\n  \"properties\": {\n    \"creationToken\": \"testVol\",\n    \"serviceLevel\": \"Standard\",\n    \"subnetId\": \"/subscriptions/5ad8e8ac-cdb7-40bf-a1c1-ff707c86c9ea/resourceGroups/westus2.rg/providers/Microsoft.Network/virtualNetworks/westus2-01.vnet/subnets/ANF.sn\",\n    \"usageThreshold\": 107374182400\n  }\n}"
    updateResult = requests.put(url=AzureUpdateVolURL, data=payload1, headers=HEADERS, params=querystring)
    print("The response code : ", updateResult.status_code, updateResult.text)
    data1 = updateResult.json()
    print(data1)

def update_CapacityPool():
    #token = self.get_token()
    token=get_token()
    bearertoken = "Bearer " + token
    querystring = {"api-version":"2020-06-01"}
    HEADERS = {
        'Authorization': bearertoken,
        'Content-Type': "application/json",
        'cache-control': "no-cache",
    }
    payload2 = "{\n  \"location\": \"westus2\",\n  \"properties\": {\n    \"size\": 4398046511104,\n    \"serviceLevel\": \"Premium\"\n  }\n}"
    updateCapacityPool = requests.put(url=AzureUpdateCapacityPool, data=payload2, headers=HEADERS, params=querystring)
    print("The response code : ", updateCapacityPool.status_code, updateCapacityPool.text)
    data2 = updateCapacityPool.json()
    print(data2)
