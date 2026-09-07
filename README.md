# Kattegat Desk

Vikings-themed Grok Bot crew + live HUD for Polymarket BTC-USD and ETH-USD perps.

Same desk as Casa Perps. New masks. Same rules: paper first, human says row.

## Roster

| Code | Name | Job |
|---|---|---|
| RAGN | Ragnar | routes |
| LAGR | Lagertha | plans |
| BJOR | Bjorn | scouts |
| FLOK | Floki | ships tickets |
| ROLL | Rollo | risk |
| SEER | The Seer | vetoes |

## Open the HUD

Open `kattegat-desk.html` in a browser. Polls public Polymarket Perps API. No keys. No `/v1/trade`.

```bash
python3 server.py
# http://127.0.0.1:8765/kattegat-desk.html
```

Paper equity starts at $1,000. Ticket prefix `KG-YYYYMMDD-NN`.
Group chat: Kattegat. Folder: `/workspace/kattegat/`.

The fleet prepares. You say row.
