# Break My Code — Engineering Rules

This document defines how this project is built. Every rule here is mandatory.
Refer to [minimumcd.org](https://minimumcd.org) as the reference for CD discipline.

---

## Feature 0: The Pipeline Comes First

Before any feature is built, the CD pipeline must exist and be green.
Feature 0 = a "Hello World" deployed to a live URL via the automated pipeline.
No feature work begins until Feature 0 is complete and stable.

---

## Development Process: ATDD Cycle

Every feature follows this exact cycle, in order. No shortcuts.

```
RED → GREEN → REFACTOR → COMMIT → DEPLOY
```

### RED
Write the acceptance test that represents the requirement.
The test must fail before any implementation exists.
No code is written until there is a failing test that describes the expected behavior.

### GREEN
Write the minimum code required to make the failing test pass.
Do not over-engineer. Do not add features not covered by a test.

### REFACTOR
Clean up the code. Improve structure, naming, clarity.
Run the full test suite. All tests must remain green.
Do not change behavior during refactor.

### COMMIT
Commit to the main branch (trunk-based development).
No long-lived feature branches. Short-lived branches only (< 1 day).
The commit triggers the pipeline automatically.

### DEPLOY
The pipeline deploys automatically on green.
No manual deployments. Only the pipeline deploys to any environment.
If the pipeline fails, stop all feature work and fix it immediately.

---

## Quality Gates (Pipeline Stages)

The pipeline runs these gates in order. All must pass before deploy.

### 1. Acceptance Tests
- Represent real user requirements
- Written before implementation (RED phase)
- Scope: end-to-end behavior from user perspective

### 2. Linting & Code Analysis
- `ruff` for Python style and correctness
- `mypy` or `pyright` for type checking
- Zero warnings tolerated on new code

### 3. Security Scan
- `bandit` for Python security issues
- Dependency vulnerability scan (`pip-audit` or `safety`)
- No high-severity issues allowed to pass

### 4. Performance Tests
- Baseline response time assertions
- Regression detection: new code must not be slower than the baseline
- Lightweight — must complete in under 2 minutes

---

## Minimum CD Requirements (from minimumcd.org)

- **Trunk-based development**: all changes integrate into `main`. Short-lived branches only.
- **Single deployment pathway**: only the automated pipeline deploys. Never manually.
- **Pipeline verdict is final**: if the pipeline is red, the build does not ship. Period.
- **Immutable artifacts**: once built and tested, the artifact is not modified.
- **Stop the line**: when `main` is broken, feature work stops until it is fixed.
- **Production-like environments**: tests run in environments that mirror production.
- **On-demand rollback**: the previous version can be redeployed at any time.

---

## Project-Specific Rules

- The app is "Break My Code" — a Python playground that progressively stress-tests pasted code.
- Backend: FastAPI + Python 3.12
- Frontend: Single HTML file, Monaco editor from CDN, no build step
- Levels run as subprocesses with timeouts for isolation
- Default example code in the editor must demonstrate failures at multiple levels
- All level implementations stream results via Server-Sent Events (SSE)
