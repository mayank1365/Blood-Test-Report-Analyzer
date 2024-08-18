# Blood Test Report Feedback

This tool analyzes blood report PDFs, extracts the text, and provides constructive feedback to improve the user's health based on the analyzed data. It leverages various tools and agents to process the report and offer actionable insights.

## Features
- **PDF to Text Conversion:** Automatically extracts text from blood report PDFs for detailed analysis.
- **Health Feedback Generation:** Provides tailored health recommendations based on the analyzed data.
- **User-Friendly Output:** Presents results in a clear, easy-to-understand format, focusing on key health indicators.
- **Background Processing:** Efficiently processes and analyzes data using specialized tools and agents.
- **Scalable Design:** Capable of handling various types of blood reports with different formats, ensuring broad compatibility.

## Prerequisites
- **Python 3.10+**
- **Poetry Package Manager**
- **PyPDF2**
- **SERPER API KEY**
- **OPENAI API KEY**
- **pyowm**
  

## Setup and Installation
1. ** Seting up the project on local system**
   ```
    git clone https://github.com/mayank1365/blood-test-report-feedback.git
    cd blood-test-report-feedback
   ```   
3. **Install Dependencies:**
   ```
   poetry install --no-root
   ```
4. **Running the project**
   ```
   python main.py
   ```
   or
   ```
   python run
   ```
   
## Key Components 
  - ```./main.py```: The main script file responsible for initiating the PDF analysis and generating health feedback.
  - ```./tasks.py```: Contains tasks and functions for handling PDF extraction, data processing, and generating feedback.
  - ```./agents.py```: Manages the creation and orchestration of agents that handle different aspects of the report analysis.
  - ```./tools```: Contains utility classes and functions for PDF text extraction and search operations.
    - ```./tools/interpreter_tools.py```: Provides functions to interpret and process the extracted text from the blood reports.
    - ```./tools/search_tools.py```: Implements search functionalities for identifying and searching relevant information on google.
      
## How It Works
- PDF Upload: Users provide the blood report PDF path as input.
- Text Extraction: The tool converts the PDF content into text.
- Data Parsing: The extracted text is processed to identify relevant health metrics like Hemoglobin, Cholesterol, etc.
- Health Analysis: The tool compares the parsed data against standard health ranges and generates feedback.
- Result Output: Users receive a comprehensive summary of health recommendations along with links to the relevant articles referenced.

## Sample Output

########################
### Here is a summarized feedback for your Blood Test:
########################

The health improvement plan based on the research findings are as follows:

1. **HbA1c Levels**: To lower HbA1c levels, a balanced diet consisting of whole foods rich in protein and low in processed carbs and sugary drinks is recommended. Regular physical activity and consistent blood glucose monitoring can also contribute to better HbA1c control. More details can be found [here](https://www.everlywell.com/blog/hba1c/how-to-lower-hba1c/).

2. **Metabolic Markers**: To improve metabolic health, opt for a diet rich in fruits and vegetables, which can reduce inflammatory markers and help prevent metabolic syndrome. Regular exercise and maintaining a healthy weight can also contribute to better metabolic health. Additional information can be found [here](https://www.levels.com/blog/the-ultimate-guide-to-metabolic-health).

3. **Immune System Indicators**: Strengthening the immune system involves consuming a balanced diet with plenty of fruits and vegetables, regular exercise, and ensuring adequate sleep. Vitamins C and D, in particular, support the immune system and can be found in a variety of foods. More information can be found [here](https://www.webmd.com/diet/ss/slideshow-strengthen-immunity).

4. **Cardiovascular Health**: For a healthier heart, it's recommended to consume nutrient-rich foods like fruits and vegetables, control portion sizes, and engage in daily physical activity. Avoiding smoking and consuming a high-fiber diet can also contribute to improved cardiovascular health. More information can be found [here](https://www.mayoclinic.org/diseases-conditions/heart-disease/in-depth/heart-disease-prevention/art-20046502).

5. **Hormonal Balance**: Hormonal balance can be achieved by consuming adequate protein at each meal, regular exercise, maintaining a healthy weight, and taking care of gut health through a balanced diet. Consuming healthy fats, anti-inflammatory foods, cruciferous vegetables, high-quality protein, and prebiotics can also aid in hormonal balance. More information can be found [here](https://www.healthline.com/nutrition/balance-hormones).

Remember, it's always best to consult a healthcare provider before making any major changes to your diet or lifestyle. These suggestions are based on general research and individual needs may vary.
