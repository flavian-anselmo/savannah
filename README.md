# Savannah.Backend.Test

Backend Engineer (Junior) Test 
# Read The Docs 
## Read Using Swagger (Read & Test)
[https://savannah-api.azurewebsites.net/docs](https://savannah-api.azurewebsites.net/docs)

## Read Uisng Redocs (Read)
[https://savannah-api.azurewebsites.net/redoc](https://savannah-api.azurewebsites.net/redoc)

# Cloud Infrastructure  & Deployment 
![deployment](assets/cloud_infra.png)

# DataBase Schema 
![deployment](assets/database_erd.png)

# Run Locally without Docker 
- create a virtual environement 
```bash 
python3 -m venv venv 
```
- Activate the virtual environment
```bash 
source venv/bin/activate
```

- Install required dependancies 
```bash 
pip install -r requirements.txt
```
- Then  run the command below 
```bash 
uvicorn app.main:app --reload 
```
# Run Locally with Docker 
```bash 
docker-compose -f docker-compose.dev.yaml up --build 
```






