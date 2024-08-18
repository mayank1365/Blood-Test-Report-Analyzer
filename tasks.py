from crewai import Task
from textwrap import dedent
from agents import CustomAgents
import PyPDF2  

class CustomTasks:
    def __init__(self):
        self.agents = CustomAgents()

    def extract_text_from_pdf(self, pdf_path):
        """
        Extract text from a PDF file.
        """
        try:
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
            return text
        except Exception as e:
            return f"Error extracting text from PDF: {str(e)}"

    def research_health_info(self, blood_test_pdf):
        blood_test_summary = self.extract_text_from_pdf(blood_test_pdf)
        
        return Task(
            description=dedent(f'''
                **Task**: Comprehensive Health Information Research
                **Description**: 
                - Your task is to conduct thorough research based on the provided blood test summary.
                - Investigate multiple health parameters, including but not limited to:
                    - Nutritional deficiencies
                    - Metabolic markers
                    - Immune system indicators
                    - Cardiovascular health
                    - Hormonal balance
                - Search for articles that provide actionable insights to improve these health metrics and include links to these sources.

                **Blood Test Summary Extracted**:
                {blood_test_summary}

                **Note**: 
                - Ensure your research covers various aspects of health, offering practical advice on diet, exercise, and lifestyle changes.
                - Use `search_internet` to find the most up-to-date and relevant health information, and include links to the articles you find.

                {self.__tip_section()}
            '''),
            agent=self.agents.health_information_researcher(),
            parameters={"blood_test_pdf": blood_test_pdf}
        )

    def provide_health_feedback(self, research_findings):
        return Task(
            description=dedent(f'''
                **Task**: Provide Detailed Health Feedback
                **Description**: 
                - Your task is to analyze the research findings across multiple health parameters and provide detailed, personalized feedback.
                - Focus on creating a balanced health improvement plan covering:
                    - Dietary recommendations
                    - Exercise routines
                    - Supplements or medications
                    - Stress management techniques
                    - Lifestyle adjustments
                - Include links to relevant articles that support your recommendations.

                **Parameters**: 
                - research_findings: A document or data containing the findings from health research.

                **Note**: 
                - Ensure that the feedback is holistic and addresses the root causes of any health concerns identified in the research.
                - Use `search_internet` if additional information is required to provide comprehensive feedback, and include article links in your final feedback.

                {self.__tip_section()}
            '''),
            agent=self.agents.expert_health_analyst(),
            parameters={"research_findings": research_findings}
        )

    def __tip_section(self):
        return "Deliver high-quality results, and you might get featured in my health journal!"
