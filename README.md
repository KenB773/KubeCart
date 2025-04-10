# 🚀 KubeCart – Flask Microservice on ~~AWS EKS~~ Google Cloud Run

KubeCart is a minimal Python Flask microservice originally deployed to AWS using Kubernetes (EKS), but moved to Google Cloud Run for cost management (read: free tier). It returns JSON responses and includes a health check endpoint, making it perfect for demonstrating cloud-native deployment, containerization, and infrastructure orchestration.

## ~~🌐 Live Deployment~~ (Moved from AWS to Google Cloud's Cloud Run for cost management reasons!)

~~**App:**  [http://a2a513d41c3964ed9aa41c0269d14c62-1950382880.us-east-1.elb.amazonaws.com/](http://a2a513d41c3964ed9aa41c0269d14c62-1950382880.us-east-1.elb.amazonaws.com/)~~

~~**Swagger UI:**  [http://a2a513d41c3964ed9aa41c0269d14c62-1950382880.us-east-1.elb.amazonaws.com/swagger](http://a2a513d41c3964ed9aa41c0269d14c62-1950382880.us-east-1.elb.amazonaws.com/swagger)~~

## 🌐 Live Deployment (Google Cloud Run)

**App:** [https://kubecart-812353429065.us-east1.run.app/)](https://kubecart-812353429065.us-east1.run.app/)  

**Swagger UI:** [https://kubecart-812353429065.us-east1.run.app/swagger](https://kubecart-812353429065.us-east1.run.app/swagger)   

**Health Check:** [https://kubecart-812353429065.us-east1.run.app/health](https://kubecart-812353429065.us-east1.run.app/health)


- `/` → Main endpoint  
- `/health` → Health check
  
- Test endpoints like:
- `GET /cart?user_id=guest`
- `POST /cart/add`
- `DELETE /cart/remove`
- `POST /cart/checkout`

**Cloud Deployments**
- **Google Cloud Run** – Final production deployment (serverless, HTTPS, scalable)
- **AWS EKS (Elastic Kubernetes Service)** – Initial cluster-based deployment (retired)

## 🧱 Tech Stack (entire project)

- **Flask + Flask-RESTX (formerly Gunicorn)** – Python microservice + Swagger docs
- **Docker** – Containerized image
- **Amazon EKS (Kubernetes)** – Managed cluster with EC2 node group
- **AWS CloudFormation + IAM** – Infra as code via `eksctl`
- **Load Balancer** – Auto-provisioned for public access
- **kubectl** – Manual deployment and rollout control
- **Cloud Build / GCloud CLI** – Deployed images to Cloud Run
- **Cloud Run Logs** – Debugged application behavior and routing issues

## 📦 Project Structure

```text
kube-flask-eks/
├── app/                        # Flask app code + Docker config
│   ├── app.py                  # Flask + RESTX app
│   ├── requirements.txt        # Python dependencies
│   └── Dockerfile              # Builds container image
├── k8s/                        # Kubernetes manifests
│   ├── deployment.yaml         # Deployment for kubecart pods
│   ├── service.yaml            # LoadBalancer service config
│   └── ingress.yaml (optional) # Placeholder for future ingress setup
├── eks/                        # EKS provisioning config
│   └── eksctl-cluster.yaml     # eksctl config file (IAM, networking, etc.)
├── .gitignore
├── README.md
├── index.md (optional)         # GitHub Pages project site
└── LICENSE

```

## 🗺️ Architecture Diagram (retired)

```text
┌──────────────────────────────────────┐
│        👨‍💻 Local Development         │
│  - Windows 11 + Git Bash             │
│  - Python + Flask                    │
│  - Docker Desktop                    │
│  - AWS CLI, eksctl, kubectl          │
└────────────────────────┬─────────────┘
                         │
                         ▼
┌────────────────────────────────────────────┐
│    Docker Image Build & Push (Local → Hub) │
│    Image: kenb773/kubecart:swaggerfix      │
└────────────────────────┬───────────────────┘
                         │
                         ▼
       ┌────────────────────────────────┐
       │  AWS Elastic Kubernetes Service│
       │  (Amazon EKS - Managed K8s CP) │
       └────────┬──────────────┬────────┘
                │              │
                ▼              ▼
    ┌────────────────┐   ┌────────────────┐
    │  EC2 Node (t3) │   │  EC2 Node (t3) │   <- (EKS Worker Nodes)
    └──────┬─────────┘   └────────┬───────┘
           │                     │
           ▼                     ▼
 ┌─────────────────┐   ┌─────────────────┐
 │ Pod 1           │   | Pod 2           │
 │ Flask           |   | Flask           |
 │ RESTX           │   | RESTX           │
 └─────────────────┘   └─────────────────┘

        └────┬────────────────────┬────┘
             ▼                    ▼
     ┌────────────────────────────────────┐
     │ Kubernetes Service (LoadBalancer)  │
     │ - Maps port 80 → 5000              │
     └────────────────────────────────────┘
                        │
                        ▼
       ┌─────────────────────────────────────┐
       │ AWS Elastic Load Balancer (ELB)     │
       │ - Public IP: a2a5...elb.amazonaws...│
       └─────────────────────────────────────┘
                        │
                        ▼
               ┌────────────────┐
               │  Web Browser   │
               │ (User Accesses │
               │  Public URL)   │
               └────────────────┘
```

## 📐 Architecture Diagram (active)

```text
     ┌──────────────────────────────┐
     │   Local Development          │
     │   - Flask + RESTX            │
     │   - Docker Desktop           │
     └────────────┬────────────────┘
                  ▼
     ┌──────────────────────────────┐
     │ Docker Hub (Image Hosting)   │
     └────────────┬────────────────┘
                  ▼
     ┌──────────────────────────────┐
     │ Google Cloud Run             │
     │ - HTTPS endpoint             │
     │ - Serverless Flask API       │
     └────────────┬────────────────┘
                  ▼
     ┌──────────────────────────────┐
     │ User Browser / API Client    │
     │ - Calls /swagger, /cart, etc │
     └──────────────────────────────┘

## 📌 Highlights

- Built a Dockerized Python app and hosted it via Kubernetes
- Provisioned a production-ready EKS cluster using `eksctl`
- Configured public access using LoadBalancer service
- Demonstrated health checks and container orchestration
- Real-time Swagger UI at `/swagger` for testing endpoints
- Simulated cart logic using in-memory store per user

## 🧠 Lessons Learned

- IAM policies must be carefully configured for eksctl + EKS
- Kubernetes services expose pods via a load balancer or cluster IP
- Debugging `InvalidImageName` and `403` errors is part of real dev life...
- ...But the manual `kubectl set image` rollout used to troubleshoot stale container caching - I don't think I've ever been quite so frustrated during a debug 🙃
- Migrating from EC2-based EKS to serverless Cloud Run for simplified hosting
- Debugging persistent 404 issues using route isolation (Blueprints)
- Working with multiple cloud providers and container registries
