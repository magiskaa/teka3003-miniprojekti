*** Settings ***
Library  ../LaskuriLibrary.py

*** Test Cases ***
Lisaa Laskuri yhdesti
    Laskuri Value Should Be  0
    Lisaa Laskuri
    Laskuri Value Should Be  1
