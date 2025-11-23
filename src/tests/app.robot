*** Settings ***
Library  ../AppLibrary.py

*** Test Cases ***
Add citation command works
    Input  lisaa article
    Run Application
    Output Should Contain  Komento: lisaa
    Output Should Contain  Argumentti: article
