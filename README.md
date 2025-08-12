# Customer Acquisition Cost (CAC) Analysis — 2024 Quarterly Data

**Author / Contact:** 23f3000880@ds.study.iitm.ac.in

## Summary
The company-wide average Customer Acquisition Cost (CAC) for 2024 is **230.42** (computed from Q1–Q4). The industry benchmark target is **150**, which means our current CAC is **80.42** higher than the target.

## Quarterly Data
- Q1: 229.04
- Q2: 225.25
- Q3: 233.99
- Q4: 233.39
- **Average (reported): 230.42**

## Key findings
1. The CAC remained consistently high across all four quarters (range: 225.25 — 233.99), with a small increase in Q3 and Q4.
2. The average CAC (230.42) is **~53.6%** above the industry target of 150, indicating structural inefficiency in customer acquisition.
3. The stability of CAC suggests the issue is persistent across channels rather than a one-off campaign spike.

## Business implications
- Sustained higher CAC reduces marketing ROI and compresses margins. If Customer Lifetime Value (LTV) is not proportionally higher, profitability will decline.
- Continued allocation of budget to underperforming channels will perpetuate the gap versus the industry benchmark and could endanger growth targets.
- Executive attention should shift from simply increasing spend to optimizing channel mix, improving targeting, and reducing waste.

## Recommendations — Optimize digital marketing channels (actionable)
### 1. Measure & attribute precisely
- Implement or refine multi-touch attribution and time-decay models to understand true channel contribution.
- Run incremental lift tests (holdout experiments) for major channels to measure causal impact.

### 2. Channel-level diagnosis and reallocation
- Break down CAC by channel (paid search, social, display, affiliates, email, organic).
- Identify high-CAC, low-LTV channels and reduce spend; move budget to lower-CAC but high-conversion channels (e.g., remarketing, branded search).
- Prioritize channels that deliver high conversion rates at lower CPAs (e.g., organic, referrals, email nurture).

### 3. Improve conversion efficiency
- Run CRO experiments on landing pages (A/B test messaging, forms, page speed).
- Shorten conversion funnels and reduce friction (fewer fields, clearer CTAs).
- Align creative with audience intent and tailor landing pages per campaign.

### 4. Optimize acquisition cost via smarter bidding & targeting
- Use CPA/ROAS-based automated bidding in programmatic and search platforms targeting conversion-ready audiences.
- Audience segmentation: exclude low-intent cohorts and focus on lookalike or high-intent segments.

### 5. Increase Customer Lifetime Value (LTV)
- Improve onboarding, cross-sell, and retention to increase LTV so that higher CACs become sustainable.
- Launch referral and loyalty programs that lower marginal CAC.

### 6. Tactical experiments (30–90 day sprints)
- Rapid experiments: reduce spend on worst-performing ad sets and reallocate to top 20% performers.
- Test lower-funnel creatives and offers to increase conversion rates.
- Pilot partnerships/affiliate channels with performance-based payment.

## Suggested KPI targets & metrics
- Short term (quarter): reduce CAC by 10–15% via reallocation and CRO.
- Medium term (3–6 months): achieve CAC ≤ 180 through attribution + automated bidding.
- Long term (6–12 months): target CAC 150 by combining channel optimization and LTV initiatives.

## What’s included in this PR
- `analysis.py` — Python analysis and visualization script (saves `figures/cac_trend.png`).
- `requirements.txt` — Python dependencies to run the analysis.
- `run_analysis.sh` — convenience script to run the analysis.
- `README.md` — this file (includes author email and the correct average 230.42).

## How to reproduce
1. Clone the repository.
2. Create a Python 3.9+ virtual environment and install requirements:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Run the analysis:
   ```bash
   python analysis.py
   ```
4. The plot will be saved to `figures/cac_trend.png`.

## Next steps (if this were a real PR)
- Provide channel-level CAC data and LTV per cohort for deeper modeling.
- Run incrementality tests and document results in follow-up PRs.
- Track experiment results and update projections.

## Notes
- Average computed from quarterly values: (229.04 + 225.25 + 233.99 + 233.39) / 4 = **230.4175**, reported in README as **230.42**.

