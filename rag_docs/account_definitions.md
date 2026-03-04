# GL Account Definitions & Variance Interpretation Guide

**Document Type:** Finance Reference  
**Purpose:** Grounding LLM in accounting definitions and normal account behavior

---

## Revenue Accounts

### Account 4001 — Product Revenue (SaaS)
**Nature:** Recurring monthly recognized revenue from active SaaS subscriptions. Recognized on a straight-line basis over contract term per ASC 606.  
**Normal Behavior:** Should grow month-over-month as net new ARR is added. Declines indicate churn exceeding new business or downsell.  
**Common Variance Drivers:** Customer churn, deal slippage, downsell at renewal, pricing changes.  
**Favorable Variance:** Revenue > budget (overperformance in new logos or lower churn)  
**Unfavorable Variance:** Revenue < budget (churn event, delayed deal close, downsell)

### Account 4002 — Professional Services Revenue
**Nature:** Revenue from time-and-materials or milestone-based implementation projects. Recognized as services are delivered.  
**Normal Behavior:** Lumpy; tied directly to implementation project timelines. Can vary significantly month-to-month.  
**Common Variance Drivers:** Implementation timeline delays, scope changes, new logo velocity, milestone completions.  
**Key Relationship:** Lags new SaaS logo closings by 30-90 days. PS revenue miss often follows a period of slow new logo closings.

### Account 4003 — Support & Maintenance Revenue
**Nature:** Recurring annual support contract fees, recognized monthly. Most predictable revenue line.  
**Normal Behavior:** Should be stable with gradual growth tied to SaaS ARR growth.  
**Common Variance Drivers:** Churn (customers who cancel SaaS also cancel support), upsells to Premium support tier.

---

## Cost of Goods Sold (COGS) Accounts

### Account 5001 — Cloud Infrastructure
**Nature:** Variable cost of operating the SaaS platform on cloud infrastructure (AWS). Includes compute, storage, data transfer, and managed services.  
**Normal Behavior:** Semi-variable — a baseline fixed component plus variable usage tied to customer activity.  
**Key Relationship:** Should scale proportionally with SaaS revenue (budget assumes ~11% of SaaS revenue). Spikes outside this ratio warrant investigation.  
**Common Variance Drivers:** New customer onboarding (temporary spike), architecture changes, reserved instance coverage gaps, unexpected batch processing jobs.

### Account 5002 — Third-Party Software Licenses
**Nature:** Licenses for software embedded in or required to deliver the platform. Primarily fixed contracts.  
**Normal Behavior:** Low variance; spikes indicate new tool additions or contract overages.

### Account 5003 — Professional Services COGS
**Nature:** Fully-loaded cost of delivering PS engagements (employee salaries + subcontractors).  
**Normal Behavior:** Moves directionally with PS revenue. Margins should be 48-55%.  
**Common Variance Drivers:** Subcontractor usage for overflow capacity, implementation overtime, travel for on-site work.

---

## Operating Expense (OpEx) Accounts

### Account 6001 — Salaries & Benefits
**Nature:** Largest cost line. Includes base salary, payroll taxes, health benefits, 401k match for all employees.  
**Normal Behavior:** Relatively fixed month-to-month; step changes occur with new hires. April shows slight uptick due to merit increases.  
**Common Variance Drivers:** Headcount timing (late hires = underspend), backfill hiring at higher market rates, unplanned sign-on bonuses.  
**Interpretation:** Underspend often indicates open headcount — which may be a capacity risk. Overspend may indicate unplanned hires or market rate pressure.

### Account 6002 — Sales Commissions
**Nature:** Variable compensation tied to sales quota attainment. Paid monthly based on bookings.  
**Normal Behavior:** Should correlate with bookings volume. Seasonal with Q2 and Q4 being highest.  
**Common Variance Drivers:** Above/below quota attainment, accelerators for overperformance, timing of deal closes.  
**Key Signal:** Commission overrun is a positive leading indicator for SaaS revenue (bookings precede revenue recognition).

### Account 6003 — Marketing & Advertising
**Nature:** External spend on demand generation, brand awareness, events, digital advertising.  
**Normal Behavior:** Highly seasonal. H2-heavy with major investment in Q3 (user conference, brand campaign).  
**Common Variance Drivers:** Campaign timing shifts, CPC fluctuations, event costs exceeding estimate.  
**Important Context:** Q3 marketing variances of up to +40% have been explicitly planned for the annual conference.

### Account 6004 — Travel & Entertainment
**Nature:** Employee travel (flights, hotels), customer entertainment, meals.  
**Normal Behavior:** Lumpy; peaks in April (SKO), Q2/Q4 (customer events), and whenever executive travel is elevated.  
**Common Variance Drivers:** Conference attendance, customer visits, SKO, team off-sites.

### Account 6005 — Software & Tools
**Nature:** SaaS subscriptions for internal tools (Salesforce, Slack, GitHub, etc.)  
**Normal Behavior:** Relatively fixed; annual contracts create lumpiness in renewal months.

### Account 6006 — Depreciation & Amortization
**Nature:** Non-cash expense. Depreciation of hardware and amortization of capitalized software.  
**Normal Behavior:** Fixed based on asset schedule. Changes only when new assets are added.

### Account 6007 — Rent & Facilities
**Nature:** Office lease payments and facilities operating costs.  
**Normal Behavior:** Fixed monthly payments per lease contracts. Highly predictable.

### Account 6008 — Legal & Professional Fees
**Nature:** External legal counsel, audit fees, accounting advisory, IP filings.  
**Normal Behavior:** Base retainer is relatively flat; spikes occur around audit, fundraising, or disputes.  
**Common Variance Drivers:** M&A activity, contract disputes, fundraising diligence, board-directed legal work, year-end audit.  
**Important Note:** Legal spikes are largely uncontrollable and unpredictable. Significant spikes (>50%) are not unusual in Q4 due to audit preparation.

---

## Variance Materiality Thresholds (Company Policy)

| Threshold | Action Required |
|---|---|
| < 5% and < $10K | No commentary required |
| 5-10% or $10-25K | Brief note in flash report |
| 10-20% or $25-50K | Full variance explanation required by department head |
| > 20% or > $50K | CFO review + corrective action plan |
| > 30% or > $100K | Board notification in next quarterly package |
