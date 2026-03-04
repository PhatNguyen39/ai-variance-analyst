# Historical Variance Explanations — NovaTech Solutions Inc.

**Document Type:** FP&A Variance Commentary Archive  
**Purpose:** Reference for LLM context on how variances have been explained historically

---

## FY2023 Variance Commentary

### Q1 2023 — Marketing (Account 6003, Marketing Dept)
**Variance:** +$38K / +28% over budget  
**Explanation:** The digital demand generation agency retainer was renegotiated in February, resulting in a one-time catch-up invoice for January services being charged in February. Additionally, SEM spend was increased opportunistically when a competitor reduced their paid search presence, creating favorable CPC conditions. Total incremental spend approved by CMO as part of Q1 pipeline acceleration initiative.  
**Lesson:** One-time catch-up billings from agency retainer renegotiations can create artificial single-month spikes. Amortize over the contract period in future budgeting.

### Q2 2023 — Cloud Infrastructure (Account 5001, Engineering)
**Variance:** +$31K / +33% over budget  
**Explanation:** Onboarding of two new Enterprise customers in Q1 required dedicated infrastructure provisioning earlier than anticipated. The AWS data residency configuration for the healthcare customer required HIPAA-compliant dedicated RDS instances — a requirement not factored into the original budget. This was a scope change from the pre-sales technical assessment.  
**Lesson:** Enterprise deals with data residency requirements should trigger infrastructure cost review during the sales process. Pre-sales engineering must flag compliance infrastructure requirements to FP&A before deal close.

### Q3 2023 — SaaS Revenue (Account 4001, Sales)
**Variance:** -$67K / -8% under budget  
**Explanation:** Two contributing factors: (1) A mid-market customer downgraded from the Enterprise tier to Professional tier at renewal (July renewal), reducing MRR by $3.2K/month. (2) A new logo expected to close in June slipped to August due to extended procurement review, pushing recognition of the first month's revenue into Q3 rather than Q2 as planned.  
**Lesson:** Renewal downsell risk is difficult to forecast; model a 3-5% downsell assumption in future forecasts. New logo pipeline slippage should be modeled with 30-day buffer for enterprise deals.

### Q4 2023 — Salaries & Benefits (Account 6001, All Depts)
**Variance:** +$52K / +4.2% over budget  
**Explanation:** Two unplanned backfill hires in Engineering in November (Senior engineers resigned in October). While headcount targets weren't exceeded, the blended cost of replacement hires was higher than the departed employees (salary market inflation for senior engineers). Sign-on bonuses of $15K each also contributed.  
**Lesson:** Backfill hiring should include a market-rate adjustment buffer of 10-15% above the departed salary. Sign-on bonuses should be modeled at $10-15K for senior IC hires.

### Q4 2023 — Legal & Professional Fees (Account 6008, G&A)
**Variance:** +$44K / +52% over budget  
**Explanation:** Board-directed external counsel engagement for Series C preliminary materials. While the round ultimately did not proceed in Q4, the preparation work (diligence support, term sheet review, corporate restructuring analysis) required approximately 60 hours of external legal counsel at $450/hour average billing rate.  
**Lesson:** Fundraising-related legal expenses are inherently unpredictable. Consider maintaining a $25-30K unallocated legal reserve for board-directed activities.

---

## FY2022 Variance Commentary (Selected)

### Full Year 2022 — Cloud Infrastructure (Account 5001)
**Variance:** +$156K / +15.5% over budget  
**Explanation:** Customer growth exceeded plan by 18% in terms of data volume processed. The rapid onboarding of 3 enterprise customers in Q3 (originally planned for Q4) caused infrastructure provisioning to run ahead of plan. Reserved instance coverage was at 65% vs 80% target, resulting in higher on-demand pricing for the excess compute. This was a high-quality variance (revenue overperformance drove cost overperformance).  
**Lesson:** Infrastructure budget should include a variable component indexed to revenue. Reserve coverage ratio should be reviewed quarterly.

### Q2 2022 — Professional Services Revenue (Account 4002)
**Variance:** -$82K / -31% under budget  
**Explanation:** Implementation of the largest Q1 2022 new logo (Meridian Capital, $380K ACV) was delayed 6 weeks due to customer IT environment constraints — specifically, legacy SSO infrastructure required custom SAML integration work that extended the implementation timeline. Revenue recognition for the first milestone ($120K) pushed from Q2 to Q3.  
**Lesson:** Enterprise implementation timelines should include a 4-6 week IT integration buffer for financial services customers, who typically have legacy infrastructure. Milestone-based revenue recognition requires more conservative planning.

---

## Variance Patterns & Rules of Thumb

Based on historical analysis, the following patterns are consistent at NovaTech:

1. **Q3 Marketing always runs over budget** — The annual user conference and H2 brand campaign are intentionally front-loaded in Q3. Variances up to +40% in Q3 marketing have been approved and are consistent with the annual marketing plan.

2. **April T&E spikes are expected** — Sales Kickoff (SKO) occurs every April. T&E variances of +50-60% in April for the Sales department are normal and budgeted.

3. **Legal spikes in Q4 are common** — Year-end audit, contract renewals with enterprise customers, and board activities reliably push legal fees 30-50% over monthly budget in November/December.

4. **Infrastructure costs lag revenue by 60-90 days** — New customer onboarding triggers infrastructure provisioning 2-3 months before revenue recognition, creating temporary COGS overruns that normalize as revenue is recognized.

5. **Revenue misses are lagging indicators of pipeline issues** — A SaaS revenue miss in a given month was preceded by a pipeline warning in the CRM 60-90 days prior in 80% of historical cases.

6. **Commission overruns are positive signals** — Sales commission overruns indicate quota attainment above 100%, which correlates with SaaS revenue beats in subsequent quarters.
