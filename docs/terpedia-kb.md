# Terpedia KB connection

The paper's authoritative knowledge source is the Terpedia KB running on GCP/GCE. The endpoint below is taken from Terpedia's API proxy configuration (`../api.terpedia.com/api/v1/chat/completions.ts`):

```text
http://104.197.255.123:8010
```

The helper in `scripts/query_kb.py` accepts `TERPEDIA_KB_URL` to override it. The older KB documentation also describes entity search on port 8001 and Fuseki on port 3030; those ports were not reachable from the current session. Do not interpret an unreachable endpoint as absence of a molecule or target in the KB.

## Refresh pattern

```bash
TERPEDIA_KB_URL=http://104.197.255.123:8010 \
  python3 scripts/query_kb.py --search thujone
```

Save returned JSON under a dated `data/kb-refresh/` directory after checking the response and recording the retrieval time. Never overwrite the curated inventory with an unreviewed refresh.

