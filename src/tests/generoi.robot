*** Settings ***
Library  ../AppLibrary.py

*** Test Cases ***

Generoi produces valid bibtex-file
    Input  lisaa article
    Input  SusMart2018
    Input  Susanna Martikainen, Jaana Kotila, Johanna Kaipio, Tinja Lääveri
    Input  Lääkärit ja hoitajat parempien tietojärjestelmien kehittämistyössä: kyvykkäät ja innokkaat käyttäjät alihyödynnettyinä
    Input  Finnish Journal of eHealth and eWelfare
    Input  2018
    Input  10.23996/fjhw.70097
    Input  tag
    Input  generoi
    Input  exit
    Run Application

    Output Should Contain  Bibtex-tiedosto generoitu

    ${content}=  Read Generated File

    File Should Contain  @article{SusMart2018,
    File Should Contain    author={Susanna Martikainen, Jaana Kotila, Johanna Kaipio, Tinja Lääveri},
    File Should Contain    title={Lääkärit ja hoitajat parempien tietojärjestelmien kehittämistyössä: kyvykkäät ja innokkaat käyttäjät alihyödynnettyinä},
    File Should Contain    journal={Finnish Journal of eHealth and eWelfare},
    File Should Contain    year={2018},
    File Should Contain    doi={10.23996/fjhw.70097},
    File Should Contain    tag={tag}
    File Should Contain  }