# CI/CD Security Gate POC

This repository demonstrates a "Security Gate" in a CI/CD pipeline using GitHub Actions. It is designed to catch security issues early in the development lifecycle (Shift-Left).

## Included Security Checks

1.  **Secret Scanning**: Uses `Gitleaks` to find hardcoded credentials and secrets.
2.  **Dependency Audit**: Uses `pip-audit` to scan project dependencies for known CVEs.
3.  **SAST (Static Application Security Testing)**: Uses `Semgrep` with the `p/owasp-top-ten` ruleset to find insecure code patterns.

## Repository Structure

*   `.github/workflows/security.yml`: The GitHub Actions workflow file.
*   `app.py`: Deliberately vulnerable Python code (SQLi, Command Injection).
*   `secrets_test.py`: Contains fake hardcoded secrets for testing.
*   `requirements.txt`: Includes a vulnerable version of the `requests` library.

## How to Test

1.  Push this code to a new GitHub repository or open a Pull Request.
2.  Observe the "Actions" tab.
3.  The pipeline **should fail** because of the intentional vulnerabilities provided in this POC.

## Best Practices Explored

*   **Failure Thresholds**: In this POC, the pipeline is configured to fail on *any* finding. In a real project, you might set thresholds (e.g., fail only on `CRITICAL` or `HIGH` severity).
*   **False Positives**: Secret scanners can sometimes flag test keys. Use `.gitleaksignore` to manage these.
*   **Reporting**: GitHub Actions provides a summary of scan results in the workflow run logs.
