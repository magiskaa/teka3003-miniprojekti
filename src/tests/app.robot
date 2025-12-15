*** Settings ***
Library  ../AppLibrary.py

*** Test Cases ***
Add article citation works
    Input  lisaa article
    Input  SusMart2018
    Input  Susanna Martikainen, Jaana Kotila, Johanna Kaipio, Tinja Lääveri
    Input  Lääkärit ja hoitajat parempien tietojärjestelmien kehittämistyössä: kyvykkäät ja innokkaat käyttäjät alihyödynnettyinä
    Input  Finnish Journal of eHealth and eWelfare
    Input  2018
    Input  10.23996/fjhw.70097
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
    
