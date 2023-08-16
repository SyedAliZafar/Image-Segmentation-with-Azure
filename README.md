# Image-Segmentation-with-AWS
Defect detection and segmention using VGG 16 with AWS  deployment



# WorkFlow


1. Update config.yaml 
2. Update the entity
3. Update the configuration manager in src config
4. Update the components
5. Update the pipeline 
6. Update the main.py
7. Update the dvc.yaml
8. Update params.yaml
9. Update secrets.yaml [Optional]



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/entbappy/Chicken-Disease-Classification--Project
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n cnncls python=3.8 -y
```

```bash
conda activate cnncls
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```


### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag


# AZURE-CICD-Deployment-with-Github-Actions

##### Step 1
*  In Azure, go to container registries
	- Create new registry
	- Create new resource group (chicken_disease)
	- Create Registry name (chickendisease) 
	- Select Location
	- Press review and create

##### Step 2
## Save pass:

dUJzKfm9SqHhQy4G8KMxUUUFFqQ9aTeo6DDw18clM/+ACRDrKqPn




######## Step 3

## Run from terminal:
# Replace the login server from your current login server in Azure Registry


docker build -t azuredeployment.azurecr.io/azuretesting:latest .
docker login azuredeployment.azurecr.io
docker push azuredeployment.azurecr.io/azuretesting:latest

Note: Region should be Europe, US region might not be able to deploy properly
########### Step 4
* Search for webapp for container



## Deployment Steps:

1. Build the Docker image of the Source Code
2. Push the Docker image to Container Registry
3. Launch the Web App Server in Azure 
4. Pull the Docker image from the container registry to Web App server and run 

