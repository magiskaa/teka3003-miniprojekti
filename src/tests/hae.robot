*** Settings ***
Library  ../AppLibrary.py

*** Test Cases ***
Search by author works
    Input  lisaa article
    Input  SusMart2018
    Input  Susanna Martikainen, Jaana Kotila, Johanna Kaipio, Tinja Lääveri
    Input  Lääkärit ja hoitajat parempien tietojärjestelmien kehittämistyössä: kyvykkäät ja innokkaat käyttäjät alihyödynnettyinä
    Input  Finnish Journal of eHealth and eWelfare
    Input  2018
    Input  10.23996/fjhw.70097
    Input  tag
    Input  hae author Susanna Martikainen
    Input  exit
    Run Application
    Output Should Contain  Susanna Martikainen, Jaana Kotila, Johanna Kaipio, Tinja Lääveri

Search by title works
    Input  lisaa article
    Input  SusMart2018
    Input  Susanna Martikainen, Jaana Kotila, Johanna Kaipio, Tinja Lääveri
    Input  Lääkärit ja hoitajat parempien tietojärjestelmien kehittämistyössä: kyvykkäät ja innokkaat käyttäjät alihyödynnettyinä
    Input  Finnish Journal of eHealth and eWelfare
    Input  2018
    Input  10.23996/fjhw.70097
    Input  tag
    Input  hae title Lääkärit ja
    Input  exit
    Run Application
    Output Should Contain  Lääkärit ja hoitajat parempien tietojärjestelmien kehittämistyössä: kyvykkäät ja innokkaat käyttäjät alihyödynnettyinä

Search by journal works
    Input  lisaa article
    Input  SusMart2018
    Input  Susanna Martikainen, Jaana Kotila, Johanna Kaipio, Tinja Lääveri
    Input  Lääkärit ja hoitajat parempien tietojärjestelmien kehittämistyössä: kyvykkäät ja innokkaat käyttäjät alihyödynnettyinä
    Input  Finnish Journal of eHealth and eWelfare
    Input  2018
    Input  10.23996/fjhw.70097
    Input  tag
    Input  hae journal Finnish Journal of eHealth and eWelfare
    Input  exit
    Run Application
    Output Should Contain  Finnish Journal of eHealth and eWelfare

Search by doi works
   Input  lisaa article
    Input  SusMart2018
    Input  Susanna Martikainen, Jaana Kotila, Johanna Kaipio, Tinja Lääveri
    Input  Lääkärit ja hoitajat parempien tietojärjestelmien kehittämistyössä: kyvykkäät ja innokkaat käyttäjät alihyödynnettyinä
    Input  Finnish Journal of eHealth and eWelfare
    Input  2018
    Input  10.23996/fjhw.70097
    Input  tag
    Input  hae doi 10.2
    Input  exit
    Run Application
    Output Should Contain  10.23996/fjhw.70097

Search by year works
    Input  lisaa article
    Input  SusMart2018
    Input  Susanna Martikainen, Jaana Kotila, Johanna Kaipio, Tinja Lääveri
    Input  Lääkärit ja hoitajat parempien tietojärjestelmien kehittämistyössä: kyvykkäät ja innokkaat käyttäjät alihyödynnettyinä
    Input  Finnish Journal of eHealth and eWelfare
    Input  2018
    Input  10.23996/fjhw.70097
    Input  tag
    Input  hae vuosi 2018
    Input  exit
    Run Application
    Output Should Contain  2018
    