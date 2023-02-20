# [The Astronauts Collective](https://www.hellotac.org/) Job Taster Lab
## Systems Reliability Engineer

### Quick Start
```shell
$ sed "s/YOUR_PAGERDUTY_SERVICE_KEY/REPLACE_ME_WITH_YOUR_ACTUAL_PAGERDUTY_SERVICE_KEY/g" .env.example > .env
$ docker-compose up --abort-on-container-exit # --build
```
[Click here to open Karma](http://127.0.0.1:8080/?q=%40state%3Dactive)

You can open DevTools to set the Karma coffee cup to a more interesting GIF (only works on Chrome):
```javascript
setInterval(() => document.querySelector("h1 > svg")?.parentElement?.setHTML("<img src='http://127.0.0.1:8000/references/assets/this-is-fine.gif'/>"), 100)
```

### Description
Simulating a simple Minecraft emerald bank alerting service that alerts when the balance reaches $0 (`EMERALDS_NO_ENOUGH`).

Everytime the bank is queried, it reads from balance.txt, minuses from expenses.txt and adds from income.txt.

A benign alert, `JARYL_IS_DUMB_DUMB`, pops up after 1 minute of the service being up.

### Services & Ports Used
Clear these ports if required

| Service        | Port   |
|----------------|--------|
| `mkdocs`       | `8000` |
| `karma`        | `8080` |
| `exporter`     | `8081` |
| `prometheus`   | `9090` |
| `alertmanager` | `9093` |
