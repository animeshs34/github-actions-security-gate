# 🛡️ CI/CD Security Gate POC

[![Security Gate](https://github.com/animeshs34/github-actions-security-gate/actions/workflows/security.yml/badge.svg)](https://github.com/animeshs34/github-actions-security-gate/actions/workflows/security.yml)
![License](https://img.shields.io/github/license/animeshs34/github-actions-security-gate)
![Topics](https://img.shields.io/github/topics/animeshs34/github-actions-security-gate)

A robust "Security Gate" implementation for CI/CD pipelines. This project demonstrates how to "Shift Left" by integrating automated security checks directly into the development workflow using GitHub Actions.

## 🚀 The Core Idea
Most security breaches happen because of small mistakes: a hardcoded key, an outdated library, or a common code flaw. This project blocks these mistakes **before** they can be merged into the main codebase.

## 🛠️ Security Stack
The pipeline runs three essential security stages on every push and PR:

| Stage                | Tool                                             | Description                                                                  |
| :------------------- | :----------------------------------------------- | :--------------------------------------------------------------------------- |
| **Secret Scanning**  | [Gitleaks](https://github.com/gitleaks/gitleaks) | Scans for hardcoded API keys, tokens, and credentials.                       |
| **Dependency Audit** | [pip-audit](https://github.com/pypa/pip-audit)   | Checks Python dependencies for known CVEs.                                   |
| **SAST**             | [Semgrep](https://semgrep.dev/)                  | Performs Static Application Security Testing using the OWASP Top 10 ruleset. |

## 📁 Repository Structure
*   `.github/workflows/security.yml`: The 💜 heart of the project. A multi-stage YAML pipeline that fails if any security issue is found.
*   `app.py`: Contains intentional SQL Injection and Command Injection for testing SAST.
*   `secrets_test.py`: Contains intentional (fake) secrets to test secret scanning.
*   `requirements.txt`: Uses an outdated `requests` version to trigger dependency audits.
*   `.gitleaksignore`: Demonstrates how to manage false positives in a production environment.

## 🔍 Intentional Vulnerability Guide
This repo is **deliberately insecure** for demonstration purposes:
1.  **SQL Injection**: Located in `app.py:get_user_data()` using f-strings for queries.
2.  **Command Injection**: Located in `app.py:run_system_command()` using `os.system`.
3.  **Hardcoded Secrets**: AWS and Stripe keys located in `secrets_test.py`.
4.  **Vulnerable Dependency**: `requests==2.20.0` has documented HIGH severity vulnerabilities.

## 📊 Pipeline Reports
This project is configured to export **SARIF** (Static Analysis Results Interchange Format) reports. Detailed findings are natively integrated into the **GitHub Security tab**, providing a professional dashboard for vulnerability management.

## 🔧 How to Use
1.  **Fork** this repository.
2.  **Push a change** or open a Pull Request.
3.  Observe the pipeline block the merge under the **Actions** tab.

---
*Created as a Proof of Concept for DevSecOps best practices.*
