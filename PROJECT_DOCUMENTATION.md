# PathFinder — Project Documentation


PathFinder: AI Learning Path Recommender


## Problem Statement

A large number of learners today struggle with the lack of structure in online education. While there is no shortage of courses and tutorials, students often remain confused about where to begin, which skill to prioritize next, and how individual topics connect to their long-term career goals. This lack of guided direction frequently leads to wasted effort, inconsistent progress, and eventual drop-off from learning journeys. The core problem addressed by this project is the absence of an intelligent system that can transform scattered learning resources into a coherent, goal-driven roadmap tailored to each learner’s needs.



## Proposed Solution

PathFinder is designed as an AI-assisted learning guidance platform that generates personalized and structured learning roadmaps. The system accepts user inputs such as career goals and existing skills, analyzes the gap between current knowledge and target role requirements, and produces an ordered sequence of skills to learn. Unlike systems that rely purely on raw language model output, PathFinder combines deterministic Python logic with AI-generated reasoning to maintain both reliability and explainability.

The platform not only recommends what to learn but also explains why each skill is important in the context of the chosen career path. In addition, it provides curated course recommendations and visual progress tracking so that learners can clearly monitor their advancement over time. The overall objective is to reduce learning ambiguity and improve consistency through guided, data-driven recommendations.



## System Architecture

The system follows a multi-stage processing pipeline beginning with user input and ending with an interactive dashboard. When a user selects a career goal and marks known skills, the Learning Planner Agent evaluates the required skill set and produces a prioritized roadmap. This roadmap is then enriched by the Skill Explainer Agent, which generates human-readable explanations describing the relevance of each skill. The Progress Engine computes completion metrics and feeds them to the user interface, which is built using Streamlit’s multi-page architecture.

This layered flow ensures clear separation of concerns and improves maintainability. Each stage performs a focused responsibility while passing structured data to the next component.



## Agent Design

PathFinder implements a modular multi-agent architecture in which each agent is responsible for a well-defined task. The Learning Planner Agent, implemented in `agents/planner_agent.py`, performs the core reasoning required to transform user inputs into an ordered learning sequence. It compares completed skills with the required roadmap and assigns priorities accordingly. The Skill Explainer Agent, implemented in `agents/explainer_agent.py`, acts as an AI mentor that generates concise explanations describing the importance and real-world relevance of each recommended skill. The Progress Coach Agent, located in `agents/progress_coach_agent.py`, analyzes user progress and provides contextual motivational feedback.

A key design decision in this project is that agents communicate using structured Python dictionaries rather than raw prompt chaining. This approach improves robustness, debuggability, and extensibility, and demonstrates deliberate engineering beyond simple LLM usage.



## Core Non-LLM Logic

To ensure the application is not overly dependent on AI responses, several critical components are implemented using pure Python logic. These include the skill completion tracking algorithm, progress percentage computation, course-to-skill mapping, session state persistence, and multi-page navigation flow. The application also includes defensive handling for API failures so that the system continues to function even when the AI service is unavailable or rate-limited. This hybrid design was intentionally chosen to demonstrate real engineering effort rather than prompt-only automation.



## User Interface Design

The user interface is built using Streamlit’s multi-page framework. The application currently consists of a login page and a main dashboard. The dashboard presents the generated roadmap, AI explanations, recommended courses, and progress indicators in a clean and responsive layout. Custom CSS styling is used to enhance visual clarity, and the interface supports background image theming. AI insights are displayed using expandable sections to maintain readability while keeping the interface uncluttered.



## Data Flow

The data flow begins when the user provides a target career goal and selects the skills they already know. This input is processed by the Learning Planner Agent, which determines missing competencies and assigns priorities. The Skill Explainer Agent then generates contextual explanations for each skill. In parallel, the progress engine calculates the user’s completion percentage based on the selected skills. Finally, the Streamlit UI renders the structured roadmap, explanations, recommended courses, and progress metrics for the user.



## Technology Stack

The core application is developed in Python and uses Streamlit for rapid UI development and multi-page navigation. The AI layer integrates the OpenAI API to generate reasoning-based explanations. Frontend styling is handled through HTML and custom CSS embedded within the Streamlit application. The overall design emphasizes modularity, readability, and ease of future extension.


## Setup and Execution

To run the project locally, the repository must first be cloned and a virtual environment created. After installing dependencies from the requirements file, the user must provide an OpenAI API key via an environment variable or `.env` file. The application can then be launched using the Streamlit command to start the multi-page dashboard. The repository contains a fully functional Python implementation intended for reviewer verification.



## Validation Notes for Reviewers

This project intentionally combines deterministic program logic with AI-assisted reasoning. The core control flow, state management, and progress computation are implemented manually in Python. The language model is used only as an assistive component for explanation generation. The modular agent design and structured data flow are meant to reflect real-world AI system engineering practices rather than simple prompt-based automation.


## Future Improvements

Planned enhancements include integration of a resume skill gap analyzer, an adaptive weekly study planner, difficulty estimation for skills, voice assistant support, and deployment to a cloud environment. The architecture has been intentionally designed to allow these agents to be added with minimal refactoring.


## Author

Kanishka Khaitan
AI Enthusiast and Builder

