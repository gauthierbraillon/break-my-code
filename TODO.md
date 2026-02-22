# What Remains To Be Done

## Current State

Feature 0 ATDD cycle is complete up to REFACTOR:

| Step      | Status |
|-----------|--------|
| RED       | ✓ Done — 3 acceptance tests written and confirmed failing |
| GREEN     | ✓ Done — Hello World FastAPI app passes all 3 tests |
| REFACTOR  | ✓ Done — Makefile, Dockerfile, GitHub Actions, quality gates all green locally |
| COMMIT    | ✗ Blocked — see below |
| DEPLOY    | ✗ Not started |

---

## Remaining Steps

### 1. Create GitHub repo (you need to approve this)

```bash
gh repo create break-my-code --public \
  --description "Python playground that stress-tests your code through progressive adversarial levels"
```

Then push:

```bash
git add .
git commit -m "Feature 0: Hello World with full CD pipeline"
git remote add origin https://github.com/gauthierbraillon/break-my-code.git
git push -u origin main
```

---

### 2. Create a Railway project

Go to https://railway.app → sign up / log in → New Project → Deploy from GitHub repo → select `break-my-code`.

Railway will auto-detect the Dockerfile.

---

### 3. Generate a Railway service token

In your Railway project → Settings → Tokens → Create Token (type: **Project** token).

Copy the token.

---

### 4. Add RAILWAY_TOKEN to GitHub secrets

Go to:
`https://github.com/gauthierbraillon/break-my-code/settings/secrets/actions`

Add secret:
- Name: `RAILWAY_TOKEN`
- Value: the token from step 3

---

### 5. Trigger the first deploy

Push any change to `main` (or re-push) — GitHub Actions will:
1. Lint (ruff)
2. Security scan (bandit)
3. Acceptance tests (pytest)
4. Performance gate (100ms threshold)
5. Deploy to Railway → live URL

---

## After Feature 0 is Live

Start Feature 1 following the ATDD cycle (RED → GREEN → REFACTOR → COMMIT → DEPLOY):

**Feature 1 — Level 1: Static Analysis**
- RED: Write acceptance test — POST /break with code returns a Level 1 result with ruff findings
- GREEN: Implement `/break` SSE endpoint + Level 1 runner (ruff subprocess)
- REFACTOR → COMMIT → DEPLOY

**Feature 2 — Level 2: Naive Runtime**
**Feature 3 — Level 3: Edge Case Fuzzing (Hypothesis)**
**Feature 4 — Level 4: Behavioral Analysis**
**Feature 5 — Level 5: Deep Adversarial**
