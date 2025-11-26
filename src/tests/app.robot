*** Settings ***
Library  ../AppLibrary.py

*** Test Cases ***
Add article citation works
    Input  lisaa article
    Input  key
    Input  author
    Input  title
    Input  journal
    Input  year
    Input  doi
    Run Application
    Output Should Contain  Article citation added
