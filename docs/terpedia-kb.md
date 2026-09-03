# Terpedia KB connection

The paper's authoritative knowledge source is the Terpedia KB running in GCP project `terpedia-489015`. The current public API is:

```text
https://terpedia-knowledge-nanrsdlaoa-uc.a.run.app
```

The helper in `scripts/query_kb.py` accepts `TERPEDIA_KB_URL` and `TERPEDIA_KB_KEY` from the environment. The key must be retrieved at runtime from Secret Manager as described in `../kb-source/docs/TERPEDIA_DATA_REFERENCE.md`; it is never committed. A successful authenticated refresh for four absinthe-relevant terms is recorded in `data/gcp-kb-refresh-2026-09-03.json`.

## Refresh pattern

```bash
TERPEDIA_KB_URL=http://104.197.255.123:8010 \
  python3 scripts/query_kb.py --search thujone
```

Save returned JSON under a dated `data/kb-refresh/` directory after checking the response and recording the retrieval time. Never overwrite the curated inventory with an unreviewed refresh.
