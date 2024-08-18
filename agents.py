from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
from tools.search_tools import SearchTools
from tools.interpreter_tools import InterpreterTools

class CustomAgents:
    def __init__(self):
        # self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)

    def expert_health_analyst(self):
        return Agent(
            role="Expert Health Analyst",
            backstory=dedent(f"""
                                Expert in summarizing medical reports, particularly blood test results,
                                with a focus on making complex data understandable for better health decisions.
                            """),
            goal=dedent(f"""
                            Provide feedback on how to improve health based on the research findings.
                        """),
            tools=[SearchTools.search_internet ],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
        )

    def medical_report_interpreter(self):
        return Agent(
            role="Medical Report Interpreter",
            backstory=dedent(f"""
                                Over a decade of experience in gathering and analyzing credible medical information online,
                                transforming complex data into actionable health insights.
                            """),
            goal=dedent(f"""
                            Summarize the blood test report and search the internet for related information.                            
                        """),
            tools=[SearchTools.search_internet , InterpreterTools.pdf_to_text_tool],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
        )
    
    def health_information_researcher(self):
        return Agent(
            role="Health Information Researcher",
            backstory=dedent(f"""
                                Specialist in nutrition and lifestyle, 
                                offering tailored advice to enhance health based on precise analysis and research findings.
                             """),
            goal=dedent(f"""
                            Conduct in-depth research on medical conditions, health metrics, and lifestyle improvements.                            
                        """),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
        )

