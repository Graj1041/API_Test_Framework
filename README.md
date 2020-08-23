# API_Test_Framework
API Testing Framework

# Clone API_Test_Framework repo
    Clone the repository to your local system

# Installation

      Step 1 :  Install Python 3.7.X or greater

      Step 2 :  Create virtual Environment
              2.1 : pip install virtualenv
              2.2 : In API_Test_Framework repo, open command prompt and type -"virtualenv env"
              2.3 : Activate virtual environment, type : .\env\Scripts\activate
              2.4 : Install required python module, type : pip install -r requirement.txt
        
# Run
    pytest -v -s --html=./Reports/report.html TestCases/
