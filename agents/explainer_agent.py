import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain_skill(skill, goal):
    """
    Explains why a skill is important for a given career goal.
    Falls back to static explanation if API fails.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a career mentor explaining skills simply."
                },
                {
                    "role": "user",
                    "content": f"Explain why {skill} is important for a {goal} in 2 sentences."
                }
            ]
        )

        return {
            "source": "AI",
            "explanation": response.choices[0].message.content
        }

    except Exception:
        # Safe fallback (VERY IMPORTANT)
        return {
            "source": "fallback",
            "explanation": f"{skill} is a core skill commonly required for success as a {goal}."
        }
