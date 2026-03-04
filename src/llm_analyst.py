"""
LLM Analyst — Generates executive reports using Claude API with RAG context.
"""

import os
import json
import anthropic
from typing import Optional

CLAUDE_MODEL = "claude-sonnet-4-20250514"


SYSTEM_PROMPT = """You are a senior FP&A (Financial Planning & Analysis) analyst at NovaTech Solutions Inc.
Your role is to analyze budget vs. actual financial variances and produce clear, actionable reports for the CFO and executive team.

STRICT RULES:
1. Use ONLY the variance data and context documents provided. Do not invent numbers or events not in the data.
2. Cite specific dollar amounts and percentages from the variance data.
3. When context explains a variance (e.g., planned marketing campaign, SKO), say it is "consistent with plan" or "expected per budget assumptions."
4. When context does NOT explain a variance, flag it as requiring investigation.
5. Maintain a professional, CFO-level communication style: concise, direct, no jargon.
6. If you are uncertain about a driver, say so explicitly rather than speculating.
7. Always distinguish between favorable variances (good news) and unfavorable variances (risk/concern).
"""


def build_executive_summary_prompt(variance_data: list[dict], summary_metrics: dict,
                                    rag_context: str) -> str:
    return f"""
COMPANY CONTEXT & REFERENCE DOCUMENTS:
{rag_context}

===

SUMMARY FINANCIAL METRICS (YTD):
{json.dumps(summary_metrics, indent=2)}

TOP FLAGGED VARIANCES:
{json.dumps(variance_data, indent=2)}

===

Please generate a comprehensive variance analysis report with these exact sections:

## EXECUTIVE SUMMARY
Write 4-5 sentences suitable for a CFO briefing. Lead with the most material finding. Mention total variance direction and magnitude. Reference specific accounts by name (not GL number).

## DRIVER ATTRIBUTION
For each of the top 5-7 flagged variances, provide:
- Account and Department
- Variance amount and percentage  
- Likely driver (based on provided context)
- Whether this is EXPECTED (per plan/seasonality) or UNEXPECTED (requires investigation)

## RISK FLAGS
List 3-5 forward-looking risks based on the current variance patterns. Focus on risks that could impact the remainder of the fiscal year. Be specific.

## RECOMMENDED ACTIONS
List 3-4 concrete actions for the finance team or department heads to take.

Format your response as clean, professional text. Use clear headers. Keep the Executive Summary under 150 words.
"""


def build_drill_down_prompt(account: str, department: str, period: str,
                             budget: float, actual: float, rag_context: str) -> str:
    variance = actual - budget
    variance_pct = variance / budget if budget != 0 else 0
    direction = "over budget" if variance > 0 else "under budget"

    return f"""
CONTEXT DOCUMENTS:
{rag_context}

===

VARIANCE DETAIL:
- Account: {account}
- Department: {department}  
- Period: {period}
- Budget: ${budget:,.0f}
- Actual: ${actual:,.0f}
- Variance: ${variance:+,.0f} ({variance_pct:+.1%}) — {direction}

===

Please provide a focused variance explanation (150-200 words) covering:
1. What likely drove this variance (cite context if available)
2. Whether this is consistent with plan, expected seasonality, or a surprise
3. Any actions or follow-up required
4. Forecast implication (will this reverse next month or persist?)

Be specific and cite dollar amounts.
"""


class VarianceAnalyst:
    """LLM-powered variance analyst."""

    def __init__(self, api_key: Optional[str] = None):
        key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not key:
            raise ValueError("ANTHROPIC_API_KEY not set. Export it or pass api_key parameter.")
        self.client = anthropic.Anthropic(api_key=key)

    def generate_full_report(self, variance_data: list[dict], summary_metrics: dict,
                              rag_context: str) -> str:
        """Generate full executive variance report."""
        prompt = build_executive_summary_prompt(variance_data, summary_metrics, rag_context)

        message = self.client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=2000,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text

    def explain_single_variance(self, account: str, department: str, period: str,
                                 budget: float, actual: float, rag_context: str) -> str:
        """Generate drill-down explanation for a single variance."""
        prompt = build_drill_down_prompt(account, department, period, budget, actual, rag_context)

        message = self.client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=600,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text

    def answer_question(self, question: str, variance_context: str, rag_context: str) -> str:
        """Answer a free-form FP&A question."""
        prompt = f"""
CONTEXT DOCUMENTS:
{rag_context}

CURRENT VARIANCE DATA SUMMARY:
{variance_context}

USER QUESTION:
{question}

Please answer concisely and factually, citing specific data where available.
"""
        message = self.client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=800,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text


if __name__ == "__main__":
    # Quick test
    analyst = VarianceAnalyst()
    result = analyst.explain_single_variance(
        account="Marketing & Advertising",
        department="Marketing",
        period="2024-07",
        budget=95000,
        actual=134900,
        rag_context="Q3 marketing is elevated due to the annual NovaSummit user conference and H2 brand campaign."
    )
    print(result)
