from openai import OpenAI
from datetime import datetime
API_KEY = "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"

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY
)
def generate_next_tasks(all_tasks: list, job_title: str):

    if not all_tasks:
        prompt = f"""
        The employee's job title is: {job_title}.
        The employee has no assigned tasks yet.

        Generate 10 beginner-level tasks suitable for the first 10 days 
        for someone starting this role. Each task should include:
        - Title
        - Short Description
        - Priority (Low/Medium/High)

        Example:
        Title: Learn React Components
        Description: Understand how to create and reuse React components.
        Priority: High
        """
    else:
        tasks_text = ""
        for t in all_tasks:
            tasks_text += f"""
            Title: {t['title']}
            Description: {t['description']}
            Priority: {t['priority']}
            """

        prompt = f"""
        The employee's job title is: {job_title}.

        Current Tasks:
        {tasks_text}

        Based on the employee's role and current progress,
        suggest the next 3 suitable tasks for this employee.
        Each suggestion must include:
        - Title
        - Short Description
        - Priority (Low/Medium/High)
        """

    completion = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=800
    )

    return completion.choices[0].message.content
