*** Settings ***
Library  ../AppLibrary.py

*** Test Cases ***

Generoi produces valid bibtex-file
    Input  lisaa article
    Input  key1
    Input  Matti Meikäläinen
    Input  Kuka löi jouluna
    Input  Iltalehti
    Input  2012
    Input  10.1234/5678
    Input  tag
    Input  generoi
    Input  exit
    Run Application

    Output Should Contain  Bibtex-tiedosto generoitu

    ${content}=  Read Generated File

    File Should Contain  @article{key1,
    File Should Contain    author={Matti Meikäläinen},
    File Should Contain    title={Kuka löi jouluna},
    File Should Contain    journal={Iltalehti},
    File Should Contain    year={2012},
    File Should Contain    doi={10.1234/5678},
    File Should Contain    tag={tag}
    File Should Contain  }