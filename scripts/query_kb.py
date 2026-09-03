#!/usr/bin/env python3
"""Read-only Terpedia KB entity-search helper.

The URL is configurable because Terpedia's GCP deployment and public proxy
ports have changed over time. This script never treats a failed request as a
negative biological result.
"""
import argparse
import json
import os
import sys
import urllib.parse
import urllib.request

parser = argparse.ArgumentParser()
parser.add_argument("--search", required=True, help="compound or target label")
parser.add_argument("--base-url", default=os.getenv("TERPEDIA_KB_URL", "http://104.197.255.123:8010"))
args = parser.parse_args()

url = args.base_url.rstrip("/") + "/entities/search?" + urllib.parse.urlencode({"q": args.search})
request = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "Terpedia-absinthe-research/0.1"})
try:
    with urllib.request.urlopen(request, timeout=20) as response:
        payload = json.load(response)
except Exception as exc:
    print(json.dumps({"query": args.search, "url": url, "status": "unreachable_or_error", "error": str(exc)}), file=sys.stderr)
    sys.exit(2)

print(json.dumps({"query": args.search, "url": url, "status": "retrieved", "payload": payload}, indent=2, sort_keys=True))
