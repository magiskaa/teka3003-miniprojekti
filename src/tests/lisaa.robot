*** Settings ***
Library  ../AppLibrary.py

*** Test Cases ***
Author validation works
    Input  lisaa article
    Input  SusMart2018
    Input  Susanna Martika1nen, J4ana Kotila, J0hanna Kaipio, T1nja Lääveri
    Input  Susanna Martikainen, Jaana Kotila, Johanna Kaipio, Tinja Lääveri
    Input  Lääkärit ja hoitajat parempien tietojärjestelmien kehittämistyössä: kyvykkäät ja innokkaat käyttäjät alihyödynnettyinä
    Input  Finnish Journal of eHealth and eWelfare
    Input  2018
    Input  10.23996/fjhw.70097
    Input  tag
    Run Application
    Output Should Contain  Tekijä(t) ei kelpaa

Title validation works
    Input  lisaa article
    Input  SusMart2018
    Input  Susanna Martikainen, Jaana Kotila, Johanna Kaipio, Tinja Lääveri
    Input  ${EMPTY}
    Input  Lääkärit ja hoitajat parempien tietojärjestelmien kehittämistyössä: kyvykkäät ja innokkaat käyttäjät alihyödynnettyinä
    Input  Finnish Journal of eHealth and eWelfare
    Input  2012
    Input  10.23996/fjhw.70097
    Input  tag
    Run Application
    Output Should Contain  Otsikko ei kelpaa

Journal validation works
    Input  lisaa article
    Input  SusMart2018
    Input  Susanna Martikainen, Jaana Kotila, Johanna Kaipio, Tinja Lääveri
    Input  Lääkärit ja hoitajat parempien tietojärjestelmien kehittämistyössä: kyvykkäät ja innokkaat käyttäjät alihyödynnettyinä
    Input  ${EMPTY}
    Input  Finnish Journal of eHealth and eWelfare
    Input  2018
    Input  10.23996/fjhw.70097
    Input  tag
    Run Application
    Output Should Contain  Julkaisupaikka ei kelpaa

Year validation works
    Input  lisaa article
    Input  SusMart2018
    Input  Susanna Martikainen, Jaana Kotila, Johanna Kaipio, Tinja Lääveri
    Input  Lääkärit ja hoitajat parempien tietojärjestelmien kehittämistyössä: kyvykkäät ja innokkaat käyttäjät alihyödynnettyinä
    Input  Finnish Journal of eHealth and eWelfare
    Input  KaksiTuhattaKahdeksanToista
    Input  2018
    Input  10.23996/fjhw.70097
    Input  tag
    Run Application
    Output Should Contain  Vuosi ei kelpaa

DOI validation works
    Input  lisaa article
    Input  SusMart2018
    Input  Matti M31käläinen, Seppo T44lasmaa
    Input  Susanna Martikainen, Jaana Kotila, Johanna Kaipio, Tinja Lääveri
    Input  Kuka löi jouluna
    Input  Iltalehti
    Input  2012
    Input  1234567890
    Input  10.23996/fjhw.70097
    Input  tag
    Run Application
    Output Should Contain  DOI ei kelpaa

Tag validation works
    Input  lisaa article
    Input  FKS8R
    Input  Susanna Martika1nen, J4ana Kotila, J0hanna Kaipio, T1nja Lääveri
    Input  Matti Meikäläinen, Seppo Taalasmaa
    Input  Lääkärit ja hoitajat parempien tietojärjestelmien kehittämistyössä: kyvykkäät ja innokkaat käyttäjät alihyödynnettyinä
    Input  Finnish Journal of eHealth and eWelfare
    Input  2018
    Input  1234567890
    Input  10.23996/fjhw.70097
    Input  a¨'´cä
    Input  tag
    Run Application
    Output Should Contain  Tag ei kelpaa

Add from DOI works
    Input  lisaa 10.1109/ICISCE.2018.00127
    Input  DOIREF1
    Input  tag
    Run Application
    Output Should Contain  Artikkeli lisätty tietokantaan

Add from URL works
    Input  lisaa https://doi.org/10.1109/ICISCE.2018.00127
    Input  URLREF1
    Input  tag
    Run Application
    Output Should Contain  Artikkeli lisätty tietokantaan