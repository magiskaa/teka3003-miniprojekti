*** Settings ***
Library  ../AppLibrary.py

*** Test Cases ***
Add article citation works
    Input  lisaa article
    Input  FKS8R
    Input  Matti Meikäläinen, Seppo Taalasmaa
    Input  Kuka löi jouluna
    Input  Iltalehti
    Input  2012
    Input  10.1234/5678
    Input  tag
    Input  exit
    Run Application
    Output Should Contain  Artikkeli lisätty tietokantaan

Shutting down app works
    Input  exit
    Run Application
    Output Should Contain  Ohjelma suljetaan...

Connecting to database works
    Check Database Connection
    Output Should Contain  Yhdistetty tietokantaan
    
