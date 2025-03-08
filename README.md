# Chicken-Disease-Classification-Using-Fecal-Image

## Workflows

1. Update config.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/kunalmishravitb/Chicken-Disease-Classification-Using-Fecal-Image.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n venv python=3.10 -y
```

```bash
conda activate venv
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
localhost:8080
```




# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	# Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	# Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	# optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	# required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app






# 🐓 Chicken Disease Classification Using Fecal Image  

## 🚀 Workflows  

1⃣ Update `config.yaml`  
2⃣ Update `params.yaml`  
3⃣ Update the entity  
4⃣ Update the configuration manager in `src config`  
5⃣ Update the components  
6⃣ Update the pipeline  
7⃣ Update `main.py`  
8⃣ Update `app.py`  

---

# 🛠️ How to Run?  

### 🔹 **STEPS:**  

### 💕 **Step 01 - Clone the repository**  
```bash
git clone https://github.com/kunalmishravitb/Chicken-Disease-Classification-Using-Fecal-Image.git
```

### 🐍 **Step 02 - Create a Conda environment**  
```bash
conda create -n venv python=3.10 -y
conda activate venv
```

### 📦 **Step 03 - Install the requirements**  
```bash
pip install -r requirements.txt
```

### 🚀 **Step 04 - Run the application**  
```bash
python app.py
```

Now, open your browser and go to:  
```bash
localhost:8080
```

---

# ☁️ AWS CICD Deployment with GitHub Actions  

## 🔑 **1. Login to AWS Console**  

## 🔐 **2. Create IAM user for deployment**  
👉 **With specific access:**  
✅ **EC2 Access** - Virtual Machine  
✅ **ECR** - Elastic Container Registry to store Docker images  

### 📌 **Deployment Overview:**  
1⃣ Build a **Docker image** of the source code  
2⃣ Push the **Docker image** to **ECR**  
3⃣ Launch an **EC2 instance**  
4⃣ Pull the **Docker image** from **ECR** to EC2  
5⃣ Run the **Docker image** on EC2  

### 🔑 **Required AWS Policies:**  
✅ `AmazonEC2ContainerRegistryFullAccess`  
✅ `AmazonEC2FullAccess`  

---

## 📦 **3. Create an ECR Repository**  
👉 **Save the URI:**  
`566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken`  

---

## 💻 **4. Create an EC2 Machine (Ubuntu)**  

## 🐳 **5. Install Docker on EC2 Machine**  

### 🔹 (Optional) Update & Upgrade  
```bash
sudo apt-get update -y
sudo apt-get upgrade -y
```

### 🔹 (Required) Install Docker  
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

---

## ⚙️ **6. Configure EC2 as a Self-Hosted Runner**  
👉 **Go to:** `Settings > Actions > Runner > New Self Hosted Runner`  
👉 **Choose OS and run the provided commands one by one**  

---

## 🔒 **7. Setup GitHub Secrets**  

```
AWS_ACCESS_KEY_ID=xxxxxxxxxxxxxxxxxx
AWS_SECRET_ACCESS_KEY=xxxxxxxxxxxxxxxxxx
AWS_REGION=us-east-1
AWS_ECR_LOGIN_URI=566373416292.dkr.ecr.us-east-1.amazonaws.com
ECR_REPOSITORY_NAME=chicken
```
