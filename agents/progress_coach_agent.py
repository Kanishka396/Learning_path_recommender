import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def progress_coach_agent(goal, completed_skills, all_skills):
    progress = int((len(completed_skills) / len(all_skills)) * 100)

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a friendly AI learning coach."
                },
                {
                    "role": "user",
                    "content": (
                        f"My career goal is {goal}. "
                        f"I have completed these skills: {completed_skills}. "
                        f"My overall progress is {progress}%. "
                        "Give short motivational feedback and what I should focus on next."
                    )
                }
            ]
        )

        return {
            "source": "AI",
            "message": response.choices[0].message.content,
            "progress": progress
        }

    except Exception:
        # Fallback (no API / quota safe)
        if progress < 30:
            msg = "You're just getting started. Stay consistent and focus on core fundamentals."
        elif progress < 70:
            msg = "Good progress! Keep going—you're building strong momentum."
        else:
            msg = "Excellent work! You're close to mastering this learning path."

        return {
            "source": "fallback",
            "message": msg,
            "progress": progress
        }
