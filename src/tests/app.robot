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

Add DOI citation works
    Input  lisaa 10.123456/abcd.1234
    Input  DOITest2015 
    Input  Tag
    Run Application    
    Output Should Contain  Artikkeli lisätty tietokantaan

Add URL citation works
    Input  lisaa https://link.springer.com/article/10.123456/abcd.1234
    Input  UrlTest2015
    Input  Tag
    Run Application    
    Output Should Contain  Artikkeli lisätty tietokantaan

Shutting down app works
    Input  exit
    Run Application
    Output Should Contain  Ohjelma suljetaan...

Connecting to database works
    Check Database Connection
    Output Should Contain  Yhdistetty tietokantaan
    
