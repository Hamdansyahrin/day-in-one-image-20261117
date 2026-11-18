# day-in-one-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/Hamdansyahrin/day-in-one-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/Hamdansyahrin/day-in-one-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

One picture that sums up the world's news of **Tuesday 17 November 2026**:
a broadsheet front page carrying **54 verified stories — 16 of them
illustrated** — every one of which happened, or was first reported, on
that Tuesday.

The three leads:

1. **Ukraine says a Crimean Bridge road span fell into the sea** — a
   second strike on the Kerch crossing in two days; President Zelensky
   hails an "unprecedented operation", the Kremlin vows to rebuild.
2. **Iran sends drones at a US radar in Bahrain; the US hits back** —
   US jets strike Qeshm, Tehran says tankers hit mines in Hormuz.
   The claims are marked as claims.
3. **Ebola cases in DR Congo top 11,000, WHO says** — more than doubled
   in three months, about 5,400 deaths, and no licensed vaccine for
   the Bundibugyo strain.

Around them: Trump's first Quad summit in Manila, Nvidia's sales
doubling to $115.8bn as the Dow fell 849 points, Mongolia's president
announcing he will resign, Serbia's student-led majority taking its
seats, Dhaka garment workers tear-gassed, the An-12 crash in Siberia,
Mondlane on trial in Mozambique, COP31 split over a fossil-fuel
phase-out, three countries losing measles-free status, Japan
scrambling jets, Cyclone Akvan, the Banda Sea quake, and the JPMorgan
outage — plus a "Where it happened" map and 38 further stories in the
"Also on Tuesday" index.

The page is drawn programmatically in full colour (no palette
quantization): masthead, stat strip, illustrated cards, world map with
numbered pins, and the day's index. Disputed claims are attributed in
the decks. Sources: Reuters, AP, AFP, BBC, Al Jazeera, WHO, UN.

## Run it

```sh
python3 main.py
```

`main.py` (Python 3.13, standard library only, no network) validates
`entry.png` — magic bytes, the 1 MiB whole-file cap, the 1024 px side
cap — and copies it byte for byte to `$MAKEFUN_OUTPUT_DIR/entry.png`
(default `/output/entry.png`). It writes the same bytes on every run.

---

<sub>Entered on [make.fun](https://make.fun/?ref=748tdgv2&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
