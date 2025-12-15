*** Settings ***
Library  ../AppLibrary.py

*** Test Cases ***
Search by author works
    Input  lisaa article
    Input  FKS8R
    Input  Matti Meikäläinen, Seppo Taalasmaa
    Input  Kuka löi jouluna
    Input  Iltalehti
    Input  2012
    Input  10.1234/5678
    Input  tag
    Input  hae author Matti Meikäläinen
    Input  exit
    Run Application
    Output Should Contain  Matti Meikäläinen

Search by title works
    Input  lisaa article
    Input  FKS8R
    Input  Matti Meikäläinen, Seppo Taalasmaa
    Input  Kuka löi jouluna
    Input  Iltalehti
    Input  2012
    Input  10.1234/5678
    Input  tag
    Input  hae title Kuka lö
    Input  exit
    Run Application
    Output Should Contain  Kuka löi jouluna

Search by journal works
    Input  lisaa article
    Input  FKS8R
    Input  Matti Meikäläinen, Seppo Taalasmaa
    Input  Kuka löi jouluna
    Input  Iltalehti
    Input  2012
    Input  10.1234/5678
    Input  tag
    Input  hae journal iltalehti
    Input  exit
    Run Application
    Output Should Contain  Iltalehti

Search by doi works
    Input  lisaa article
    Input  FKS8R
    Input  Matti Meikäläinen, Seppo Taalasmaa
    Input  Kuka löi jouluna
    Input  Iltalehti
    Input  2012
    Input  10.1234/5678
    Input  tag
    Input  hae doi 10.1
    Input  exit
    Run Application
    Output Should Contain  10.1234/5678

Search by year works
    Input  lisaa article
    Input  FKS8R
    Input  Matti Meikäläinen, Seppo Taalasmaa
    Input  Kuka löi jouluna
    Input  Iltalehti
    Input  2012
    Input  10.1234/5678
    Input  tag
    Input  hae vuosi 2012
    Input  exit
    Run Application
    Output Should Contain  2012
    