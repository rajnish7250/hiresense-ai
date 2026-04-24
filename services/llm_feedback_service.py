import os

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except:
    OPENAI_AVAILABLE = False


class LLMFeedbackService:

    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")

        self.use_llm = OPENAI_AVAILABLE and api_key is not None

        if self.use_llm:
            self.client = OpenAI(api_key=api_key)

    def generate_feedback(
        self,
        resume_text: str,
        job_desc: str,
        match_score: float,
        missing_keywords: list,
        matched_keywords=None
    ) -> str:

        #  Fallback (no API)
        if not self.use_llm:
            return self._rule_based_feedback(match_score, missing_keywords)

        try:
            prompt = f"""
You are an expert ATS resume evaluator.

Analyze the resume against the job description and give clear feedback.

Match Score: {match_score}%

Missing Skills: {missing_keywords}

Instructions:
- Be concise (3-5 bullet points)
- Focus on improvements
- Be professional

Output:
"""

            response = self.client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            return response.choices[0].message.content.strip()

        except Exception:
            return self._rule_based_feedback(match_score, missing_keywords)

    # Rule-based fallback (IMPORTANT)
    def _rule_based_feedback(self, score, missing_keywords, matched_keywords=None):

        strengths = []
        gaps = []
        suggestions = []

        # Strengths (USE MATCHED KEYWORDS)
        if matched_keywords:
            strengths.append(
                f"Strong alignment with: {', '.join(matched_keywords[:3])}"
            )
        else:
            strengths.append("Good alignment with job requirements")

        # Gaps
        if missing_keywords:
            gaps.extend(missing_keywords)

        # Suggestions
        if "deployment" in missing_keywords:
            suggestions.append(
                "Add experience with model deployment (Flask, FastAPI, or cloud)"
            )

        suggestions.append(
            "Include measurable achievements (e.g., improved performance by X%)"
        )

        # Format Feedback
        feedback = "Strengths:\n"
        for s in strengths:
            feedback += f"- {s}\n"

        feedback += "\nGaps:\n"
        for g in gaps:
            feedback += f"- {g}\n"

        feedback += "\nSuggestions:\n"
        for s in suggestions:
            feedback += f"- {s}\n"

        return feedback