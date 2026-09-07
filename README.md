# Casa Perps Desk HUD

Live ops dashboard for the Casa Perps Grok Bot crew (Polymarket BTC-USD + ETH-USD perps).

Looks like the GPTHEIST DESK chrome. Does not invent PnL.

## Open

Just open `casa-perps-hud.html` in a browser. It polls:

- `GET https://api.perpetuals.polymarket.com/v1/info/tickers`
- `GET https://api.perpetuals.polymarket.com/v1/info/book?instrument_id=6` (BTC)
- `GET https://api.perpetuals.polymarket.com/v1/info/book?instrument_id=7` (ETH)

CORS is `*`. No backend required. Paper ledger lives in `localStorage`.

Or from the Grok Bot computer:

```bash
python3 server.py
# then open http://127.0.0.1:8765/casa-perps-hud.html
```

## What is real

- BTC/ETH mark, index, basis, funding/hr, OI, spread, $1k impact
- LIVE pill only if last poll < 15s
- Paper equity starts at $1,000. Day stop −2%
- Ticket pipeline DRAFT → STOCKHOLM → PALERMO → YOU → PAPER FILL
- Six agents only: Professor, Berlin, Tokyo, Rio, Stockholm, Palermo

## What is not

- No live `/v1/trade` calls
- No $52 → $11k seed
- No 5D lattice / tail ridge / fake confidence

Crew prepares. You pull the trigger.
