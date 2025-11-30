*** Settings ***
Library  ../AppLibrary.py

*** Test Cases ***
Author validation works
    Input  lisaa article
    Input  FKS8R
    Input  Matti M31käläinen, Seppo T44lasmaa
    Input  Matti Meikäläinen, Seppo Taalasmaa
    Input  Kuka löi jouluna
    Input  Iltalehti
    Input  2012
    Input  10.1234/5678
    Input  exit
    Run Application
    Output Should Contain  Tekijä(t) ei kelpaa

Title validation works
    Input  lisaa article
    Input  FKS8R
    Input  Matti Meikäläinen, Seppo Taalasmaa
    Input  ${EMPTY}
    Input  Kuka löi jouluna
    Input  Iltalehti
    Input  2012
    Input  10.1234/5678
    Input  exit
    Run Application
    Output Should Contain  Otsikko ei kelpaa

Journal validation works
    Input  lisaa article
    Input  FKS8R
    Input  Matti Meikäläinen, Seppo Taalasmaa
    Input  Kuka löi jouluna
    Input  ${EMPTY}
    Input  Iltalehti
    Input  2012
    Input  10.1234/5678
    Input  exit
    Run Application
    Output Should Contain  Julkaisupaikka ei kelpaa

Year validation works
    Input  lisaa article
    Input  FKS8R
    Input  Matti Meikäläinen, Seppo Taalasmaa
    Input  Kuka löi jouluna
    Input  Iltalehti
    Input  Matti
    Input  2012
    Input  10.1234/5678
    Input  exit
    Run Application
    Output Should Contain  Vuosi ei kelpaa

DOI validation works
    Input  lisaa article
    Input  FKS8R
    Input  Matti M31käläinen, Seppo T44lasmaa
    Input  Matti Meikäläinen, Seppo Taalasmaa
    Input  Kuka löi jouluna
    Input  Iltalehti
    Input  2012
    Input  1234567890
    Input  10.1234/5678
    Input  exit
    Run Application
    Output Should Contain  DOI ei kelpaa
