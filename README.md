AI Learning Path Recommender

PathFinder is an AI-powered educational platform designed to help learners create a clear, structured, 
and personalized roadmap toward their career goals. Instead of leaving users confused about where to start or what to
learn next, the platform analyzes their target role, existing skills, and learning preferences to generate a guided path tailored specifically to them.

It combines agentic AI, intelligent skill tracking, and curated course recommendations to provide step-by-step guidance throughout the learning journey. 
The system not only suggests what topics to study but also explains why each skill matters, how it connects to the overall career path, and when it should be learned.
By continuously organizing learning priorities and monitoring progress, PathFinder transforms scattered online resources into a focused, goal-driven learning experience.

Project Overview

PathFinder is an AI-powered learning guidance system designed to help students and professionals navigate the often confusing process of skill development. 
Many learners struggle with questions like where to begin, which topics to prioritize, and how individual skills connect to their long-term career goals.
Instead of relying on random online resources or unstructured learning, PathFinder provides a clear, personalized roadmap that adapts to the user’s background and objectives.

PathFinder solves a common problem:

Learners don’t know what to learn first, what comes next, or why a skill matters for their target career.
To address this, the system collects and analyzes key inputs from the user, including:

User career goal (for example: Data Scientist, Web Developer, AI Engineer)
Skills already known or previously learned
Required skill roadmap based on industry expectations

Using this information, the platform intelligently generates:
Prioritized learning paths arranged in a logical sequence
AI-generated explanations that clarify the purpose and importance of each skill
Recommended courses and resources aligned with the roadmap
A progress tracking dashboard to help users stay motivated and monitor growth
Overall, PathFinder transforms scattered learning into a structured, goal-oriented journey, making it easier for users to learn efficiently and confidently.

Key Features
1. Learning Planner Agent
The Learning Planner Agent is responsible for creating a structured and personalized roadmap based on the user’s selected career goal and existing skills. Instead of showing a random list of topics, it organizes skills in a logical sequence so learners know exactly what to study first and what to learn next.
Generates an ordered learning roadmap tailored to user goals
Assigns skill priorities based on relevance and dependency
Explains the reasoning behind each recommendation to improve clarity
Helps users avoid confusion by breaking large goals into manageable steps

2. Skill Explainer Agent
The Skill Explainer Agent acts like an AI mentor that provides clear, beginner-friendly explanations for each skill in the roadmap. Its purpose is to reduce learning anxiety by helping users understand the importance and real-world application of every topic.
Provides AI-generated explanations for every skill
Helps beginners understand why a topic is important before learning it
Connects skills to practical use cases and career outcomes
Makes learning paths more understandable and less overwhelming

3. Progress Tracking Dashboard
The Progress Tracking Dashboard allows users to monitor their learning journey visually. As users complete skills, the dashboard updates in real time, giving them a sense of achievement and helping them stay motivated.
Tracks completed and pending skills
Shows dynamic progress percentage and visual indicators
Updates automatically as users mark skills as completed
Encourages consistency by making progress easy to measure

4. Course Recommendation Engine
Suggests curated online courses
Maps courses directly to required skills
Allows quick access to learning resources

5. Modern UI / UX
Streamlit-based responsive layout
Custom CSS styling
AI insight sections
Background image support
Clean dashboard design

6. Login System
Basic authentication flow
Session state handling
Separate login and home pages

Agent Architecture (Agentic AI)

PathFinder follows a multi-agent design, meaning the system is divided into smaller AI components (agents),
where each agent is responsible for a specific task instead of one large monolithic logic block. This approach improves modularity, readability, and scalability, 
making it easier to extend the system with new capabilities in the future.

The overall flow works like this:

User Input
     ↓
Learning Planner Agent
     ↓
Skill Explainer Agent
     ↓
UI Rendering + Course Recommendations

How the architecture works step-by-step

User Input Layer
The process begins when the user provides information such as career goal, current skills, or learning preferences. This input acts as the context shared across agents.

Learning Planner Agent
This agent analyzes the user’s goal and generates a structured learning roadmap. It decides:
which skills are required,
the correct learning order,
and the priority level of each skill.
Its main responsibility is planning and decision-making.

Skill Explainer Agent
Once the roadmap is created, this agent enriches it by generating clear AI explanations for each skill. It helps users understand:
why a skill matters,
where it is used in real-world scenarios,
and how it connects to the overall career path.
UI Rendering + Course Recommendation Layer
The final stage presents results to the user through the Streamlit interface. It displays:
the generated roadmap,
AI explanations,
progress tracking, and recommended learning resources.
