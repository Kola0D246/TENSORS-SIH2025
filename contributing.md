# 🧩 Contributing Guidelines

This document defines how **Team TENSORS** collaborates and manages code for the SIH 2025 project.  
External contributions are **not accepted** — this is an internal team repository.

---

## 👥 Team Collaboration Rules

- Each member works on their assigned module or feature branch.
- Always **sync with the `dev` branch** before starting new work.
- Avoid direct commits to `main` — it should only contain stable, reviewed code.

---

## 🌿 Branching Structure

We follow a simple branching model:

| Branch | Purpose |
|---------|----------|
| `main` | Stable, production-ready code |
| `dev` | Integration branch for team development |
| `feature/<name>` | New features or modules (e.g., `feature/login-system`) |
| `fix/<name>` | Bug fixes or patches |

Example:

```bash
git checkout -b feature/add-auth-module
```

Make changes. After finishing,

```bash
git add .
git commit -m "Add: login API endpoint"
git push origin feature/add-login-api
```

Then open a Pull Request (PR) to merge into dev.

---

## 🐛 Reporting Issues

- Check existing issues first to avoid duplicates.
- Include clear steps to reproduce the issue.
- Add screenshots or error logs if possible.

### 💡 Suggesting Features

- Open a new issue with the label `enhancement`.
- Describe your idea, its purpose, and possible implementation.

---

## 💬 Code Style

1. Follow PEP8 for Python code.
2. Use meaningful variable and function names.
3. Write docstrings for functions and classes.
4. Run linters before committing if possible.

---

## 🧪 Testing

1. Ensure your code passes all tests.
2. Ensure any major change does not break existing modules.
3. Add test data or mock inputs if needed.

---

## ✅ Pull Request Process

1. Ensure your code passes all tests.
2. Write clear commit messages.
3. Update documentation if needed (README.md, CHANGELOG.md).
4. Request review from a team member.

---

## 🧾 License and Access

This is a proprietary project under Team TENSORS.
All code, designs, and documentation are owned by the team.
Unauthorized sharing or external use is prohibited.
