#!/usr/bin/env python3
"""Read-only Terpedia GCP KB tabular-search helper."""
import argparse
import json
import os
import sys
import urllib.parse
import urllib.request

parser = argparse.ArgumentParser()
parser.add_argument("--search", required=True, help="compound or target label")
parser.add_argument("--source", default="all")
parser.add_argument("--base-url", default=os.getenv("TERPEDIA_KB_URL", "https://terpedia-knowledge-nanrsdlaoa-uc.a.run.app"))
args = parser.parse_args()

url = args.base_url.rstrip("/") + "/v1/tabular/search"
key = os.getenv("TERPEDIA_KB_KEY")
if not key:
    print("TERPEDIA_KB_KEY is required; retrieve it from Secret Manager at runtime.", file=sys.stderr)
    sys.exit(2)
body = json.dumps({"source": args.source, "query": args.search, "limit": 20}).encode()
request = urllib.request.Request(url, data=body, method="POST", headers={"Accept": "application/json", "Content-Type": "application/json", "x-knowledge-key": key, "User-Agent": "Terpedia-absinthe-research/0.1"})
try:
    with urllib.request.urlopen(request, timeout=20) as response:
        payload = json.load(response)
except Exception as exc:
    print(json.dumps({"query": args.search, "url": url, "status": "unreachable_or_error", "error": str(exc)}), file=sys.stderr)
    sys.exit(2)

print(json.dumps({"query": args.search, "source": args.source, "url": url, "status": "retrieved", "payload": payload}, indent=2, sort_keys=True))
