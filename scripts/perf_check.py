"""
Performance gate: the homepage must respond in under 100ms on average (10 requests).
"""

import sys
import time
from fastapi.testclient import TestClient
from backend.main import app

THRESHOLD_MS = 100
RUNS = 10

client = TestClient(app)

times = []
for _ in range(RUNS):
    start = time.perf_counter()
    r = client.get("/")
    elapsed = (time.perf_counter() - start) * 1000
    assert r.status_code == 200, f"Unexpected status {r.status_code}"
    times.append(elapsed)

avg_ms = sum(times) / len(times)
print(f"Average response time: {avg_ms:.1f}ms (threshold: {THRESHOLD_MS}ms)")

if avg_ms > THRESHOLD_MS:
    print(f"FAIL: {avg_ms:.1f}ms exceeds {THRESHOLD_MS}ms threshold")
    sys.exit(1)

print("PASS")
