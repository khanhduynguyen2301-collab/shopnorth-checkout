# shopnorth-checkout

Pricing code for **ShopNorth**, a fictional example online shop used by
[Incident Lab](https://github.com/hoang-luan-le/we_are_cooked) (Hack the Change 2026).
It is a teaching repo: one real bug, real tests, real GitHub Actions CI.

## The incident

`v2.14.0` (tagged) added loyalty-tier discounts. At 2:04 a.m. checkout errors jumped.
The night pair rolled production back to `v2.13.9`; the morning pair fixes it here.

## Fix it (morning pair)

```
pip install -r requirements-dev.txt
python -m pytest tests -q         # unit tests
python -m pytest ci/guards -q     # guard tests; CI runs these on every pull request
```

1. Reproduce the bug with a failing test in `tests/`.
2. Fix it in `checkout/`.
3. Open a pull request. CI must pass, including the guard tests.
4. Get a real review from a teammate (and the mentor, if one is assigned).

Learner code runs only in GitHub Actions, never on Incident Lab's servers.
