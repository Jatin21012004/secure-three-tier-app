# Secure Three-Tier Flask App

A secure, containerized three-tier application using **Flask**, **Redis**, and **Nginx** with Docker and Docker Compose.

---

## Project Structure

secure-three-tier-app/
├── app/
│ ├── Dockerfile
│ ├── requirements.txt
│ └── app.py
├── nginx/
│ └── nginx.conf
├── docker-compose.yml
├── screenshots/
│ ├── trivy-scan.png
│ ├── docker-ps.png
│ └── app-running.png
└── README.md


---

## Features

- Python 3.10 + Flask backend
- Redis caching
- Nginx as reverse proxy
- Multi-stage Docker builds for security
- Non-root container execution
- Vulnerability scanned with Trivy
- Minimal runtime image

---

## Setup & Run

1. Clone the repository:

```bash
git clone <your-repo-url>
cd secure-three-tier-app
Build and run containers:

docker-compose up --build
Visit http://localhost:5000 in your browser.

Security Measures
Multi-stage Docker build separates build and runtime dependencies

Removed pip, setuptools, and wheel from final image

App runs as non-root user

Image scanned with Trivy

Screenshots
App running: screenshots/app-running.png

Docker ps output: screenshots/docker-ps.png

Trivy scan results: screenshots/trivy-scan.png

Author
Jatin
Email: jatinjawa18@gmail.com
GitHub: https://github.com/Jatin21012004
