import os
from openai import OpenAI

client = OpenAI()

def weekly_study_agent(skill_plan):
    """
    Generates a 7-day study plan.
    Uses AI if available, otherwise rule-based fallback.
    """

    # ---------- RULE-BASED FALLBACK ----------
    def fallback_plan():
        week_days = [
            "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"
        ]
        week_plan = []

        for i, skill in enumerate(skill_plan):
            if i >= 7:
                break
            week_plan.append({
                "day": week_days[i],
                "skill": skill["skill"],
                "task": f"Learn basics of {skill['skill']} and practice examples",
                "hours": 2
            })

        return {
            "source": "Rule-based",
            "week_plan": week_plan
        }

    # ---------- TRY AI ----------
    try:
        if not os.getenv("OPENAI_API_KEY"):
            return fallback_plan()

        prompt = f"""
        Create a 7-day study plan based on this learning roadmap:
        {skill_plan}

        Output ONLY a Python list of dictionaries with keys:
        day, skill, task, hours
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a learning planner AI."},
                {"role": "user", "content": prompt}
            ]
        )

        week_plan = eval(response.choices[0].message.content)

        return {
            "source": "AI",
            "week_plan": week_plan
        }

    # ---------- FALLBACK ON ANY ERROR (quota, network, parse, etc.) ----------
    except Exception:
        return fallback_plan()
