.PHONY: lint security test performance pipeline run

# ── Quality Gates ────────────────────────────────────────────────────────────

lint:
	ruff check backend/ tests/

security:
	bandit -r backend/ -q -ll

test:
	python3 -m pytest tests/ -v

performance:
	PYTHONPATH=. python3 scripts/perf_check.py

# ── Full local pipeline (mirrors CI) ─────────────────────────────────────────

pipeline: lint security test performance
	@echo ""
	@echo "✓ All quality gates passed."

# ── Dev ───────────────────────────────────────────────────────────────────────

run:
	uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
