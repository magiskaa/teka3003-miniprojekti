# teka3003-miniprojekti
[Backlog](https://docs.google.com/spreadsheets/d/1iG8tZJiLOmtiUZvNDI_r38IGDxe9mPEwLc3JRLR8H6M/edit?usp=sharing)
[![CI](https://github.com/magiskaa/teka3003-miniprojekti/actions/workflows/main.yml/badge.svg)](https://github.com/magiskaa/teka3003-miniprojekti/actions/workflows/main.yml)

## Definition of done
- Testikattavuus kohtuullinen.
- pylintin mukainen koodityyli.

## Ohjeet projektin käyttöön
### 0. Cloonaa/pullaa repository

### 1. Lataa ja/tai käynnistä docker

### 2. Mene komentorivillä projektin juureen (hakemisto jossa run.sh ja run.bat)

### 3. Riippuen mitä haluat tehdä, aja jokin seuraavista:
!HUOM! 

Windows: run.bat 

MacOS/Linux: ./run.sh

Aja ohjelma:
```bash
run.bat
```
Käynnistys skripti ajaa main.py tiedoston. Tietokanta tulee tallentaa oletushakemistoon käynnistys skriptin luomaan data/ hakemistoon. Tynkä tekee tämän.

Aja robot testit:
```bash
run.bat test
```
Testien yhteenveto tulostuu komentoriville, sekä raportit tallentuvat host koneelle projektin juureen kansioon reports/

Avaa shell konttiin projektin työhakemistoon:
```bash
run.bat shell
```
Shellistä pääsee pois komennolla:
```bash
exit
```
Kontti sulkeutuu automaattisesti, kun ohjelman suoritus lakkaa.

### !!HUOM!!
Windows koneella käytä Komentokehotetta (CMD) tai PowerShelliä. 
Esim Git Bash rikkoo polut dockerin kanssa, eikä tietokanta ja testien tulokset tallennu oikein.

### 4. Riippuvuudet
Projektin riippuvuudet asentuvat automaattisesti Dockerin toimesta. Lisää vain tarvitsemasi kirjasto requirements.txt tiedostoon, joka sijaitsee projektin juuressa.
