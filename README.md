
# PythonFastAPICICDDemo

A demo project showcasing **CI/CD pipeline for a FastAPI application** using **GitHub Actions**, **Docker**, and **automated email notifications**. 

This project demonstrates: 
- Running tests automatically on push
- Sending email notifications if tests fail
- Building and pushing Docker images to Docker Hub if tests pass  

---

## 🧰 Tech Stack

- **Python 3.12**  
- **FastAPI**  
- **Pytest** (for testing)  
- **Docker & Docker Hub**  
- **GitHub Actions** (CI/CD pipeline)  
- **Gmail SMTP** (for email notifications)

---

## 📂 Project Structure

```
PythonFastAPICICDDemo/
├── main.py # FastAPI application
├── tests/
│ └── test_main.py # Test cases
├── Dockerfile_local_machine # Dockerfile for local machine
├── docker-compose_local_machine.yaml
├── requirements.txt # Python dependencies
└── .github/
└── workflows/
└── ci-cd.yaml # GitHub Actions CI/CD workflow
```



---

## ⚡ Features

1. **Automated Testing**  
   - Runs `pytest` automatically on every push to `main`.  
   - Pipeline marks status `success` or `failed`.

2. **Email Notification on Test Failure**  
   - Sends email via Gmail if tests fail.  
   - Includes repository name, commit SHA, branch, and author info.

3. **Docker Build & Push on Success**  
   - Builds Docker image using `Dockerfile_local_machine`.  
   - Pushes image to Docker Hub with Git commit SHA as the tag.

4. **Manual Trigger**  
   - You can manually trigger the pipeline from GitHub Actions UI.

---

## 🚀 Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/PythonFastAPICICDDemo.git
cd PythonFastAPICICDDemo

2️⃣ Install dependencies
python3.12 -m pip install -r requirements.txt

3️⃣ Run tests locally
pytest

4️⃣ Docker Setup (Optional)
Build Docker image locally:
docker build -t python-fastapi-ci-cd-demo:latest -f Dockerfile_local_machine .
Run Docker container:
docker run -p 8000:8000 python-fastapi-ci-cd-demo:latest

