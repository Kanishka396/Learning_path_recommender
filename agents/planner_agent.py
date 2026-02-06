import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def learning_planner_agent(goal, all_skills, completed_skills):
    remaining_skills = [s for s in all_skills if s not in completed_skills]

    if not remaining_skills:
        return {
            "status": "complete",
            "plan": []
        }

    prompt = f"""
You are an AI career coach.

Career goal: {goal}
Completed skills: {completed_skills}
Remaining skills: {remaining_skills}

Return ONLY valid JSON in this format:
{{
  "plan": [
    {{
      "priority": 1,
      "skill": "Skill name",
      "reason": "Why this skill matters"
    }}
  ]
}}
"""

    try:
        # 🔹 Try AI first
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        raw_output = response.choices[0].message.content.strip()
        data = json.loads(raw_output)
        data["status"] = "in_progress"
        data["source"] = "AI"
        return data

    except Exception:
        # 🔁 FALLBACK (no quota / error)
        plan = []
        for idx, skill in enumerate(remaining_skills, start=1):
            plan.append({
                "priority": idx,
                "skill": skill,
                "reason": f"Core requirement for becoming a {goal}"
            })

        return {
            "status": "in_progress",
            "source": "Rule-based fallback",
            "plan": plan
        }
