# Python Text Processor

![CI Status](https://github.com/bmeera/python-text-processor/actions/workflows/python-app.yml/badge.svg)

**CSCI-5400 Lab**: A simple Python application that works with text files.

This application reads text from a file, counts the number of words, converts the text to uppercase, and writes the result to a new file. It includes a full CI/CD pipeline using GitHub Actions and Docker for automated testing, releasing, and container deployment.

---

## 🛠️ Features

- ✅ Interactive user input (enter custom text)
- 📄 Word count & uppercase conversion
- 🔁 GitHub Actions CI for testing and linting
- 🚀 GitHub Releases with version tagging
- 🐳 Dockerized application published to GitHub Container Registry

---

## 💻 How to Run

### ▶️ Run locally:

```bash
python src/text_processor.py
```

### 🐳 Run in Docker:

```bash
docker run -it ghcr.io/bmeera/python-text-processor:main
```

---

## 📦 GitHub Actions Workflows

### 🔹 `python-app.yml`

- Triggered on push or pull request to the `main` branch
- Lints code, runs unit tests, and uploads `output.txt` as an artifact

### 🔹 `release.yml`

- Triggered when a version tag like `v0.1.0` is pushed
- Packages the app as a `.zip` file and creates a GitHub Release

### 🔹 `docker-deploy.yml`

- Triggered on push to `main` or any version tag
- Builds and publishes a Docker image to GitHub Container Registry (`ghcr.io`)

---

## 🧪 How to Run Tests

Run all unit tests using:

```bash
python -m unittest discover tests
```

---

## 🏁 Project Status

✔️ Fully working  
✔️ All workflows tested  
✔️ CI/CD pipeline complete  
✔️ Interactive and Dockerized
