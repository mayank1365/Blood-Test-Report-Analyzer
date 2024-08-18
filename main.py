import os
from crewai import Crew
from agents import CustomAgents
from tasks import CustomTasks
from textwrap import dedent

class CustomCrew:
    def __init__(self, blood_test_pdf):
        self.blood_test_pdf = blood_test_pdf

    def run(self):
        agents = CustomAgents()
        tasks = CustomTasks()

        research_task = tasks.research_health_info(self.blood_test_pdf)
        feedback_task = tasks.provide_health_feedback(research_task)

        crew = Crew(
            agents=[agents.expert_health_analyst(), agents.medical_report_interpreter(), agents.health_information_researcher()],
            tasks=[research_task, feedback_task],
            verbose=True,
        )

        result = crew.kickoff()
        return result

if __name__ == "__main__":
    print("## Welcome to Blood Test Analysis")
    print("-------------------------------")
    blood_test_pdf = input(dedent("Enter the path to the blood test PDF file: "))

    custom_crew = CustomCrew(blood_test_pdf)
    result = custom_crew.run()
    
    print("\n\n########################")
    print("## Here is a summarized feedback for your Blood Test:")
    print("########################\n")
    print(result)
    
