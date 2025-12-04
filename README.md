# teka3003-miniprojekti

[Backlog](https://docs.google.com/spreadsheets/d/1iG8tZJiLOmtiUZvNDI_r38IGDxe9mPEwLc3JRLR8H6M/edit?usp=sharing)

[![CI](https://github.com/magiskaa/teka3003-miniprojekti/actions/workflows/main.yml/badge.svg)](https://github.com/magiskaa/teka3003-miniprojekti/actions/workflows/main.yml)

## Sisältö
- [Definition of done](#definition-of-done)
- [Projektin käyttöohjeet](#ohjeet-projektin-käyttöön)
- [Sovelluksen käyttöohjeet](#ohjeet-sovelluksen-käyttöön)

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

Mikäli saat virheilmoituksen tyyliin "exec ./entrypoint.sh: no such file or directory" on ongelma kyseisen käynnistysscriptin rivinvaihdoista. Joskus windows kone sekottaa ne. Lokaali fixi on ajaa seuraava jossain unix shellissä:
```bash
dos2unix entrypoint.sh
```

### 4. Riippuvuudet
Projektin riippuvuudet asentuvat automaattisesti Dockerin toimesta. Lisää vain tarvitsemasi kirjasto requirements.txt tiedostoon, joka sijaitsee projektin juuressa.

## Ohjeet sovelluksen käyttöön

### 1. Kirjoita komento ja sen perään argumentit.

Käytettävissä olevat komennot: lisaa, hae, generoi, quit/exit.

#### 1.1 Lisää-komento
```bash
lisaa <referenssityyppi>
```
Käytettävissä olevat referenssityypit: `article`, `inproceedings`, `book`.

#### 1.2 Hae-komento
```bash
hae <attribuutti> <hakusana> 
```
Käytettävissä olevat attribuutit: `cite_key`, `author`, `title`,  `journal`, `tag`, `year`, `doi`.

#### 1.3 Generoi-komento
```bash
generoi
```
Tekee BibTex-tiedoston host-koneelle.

#### 1.4 Exit-komento
```bash
quit
```
tai
```bash
exit
```
Sulkee ohjelman.

### 2. Esimerkki viitteen lisäämisestä

Kun lisäät uuden viitteen (esim. artikkeli), ohjelma kysyy tarvittavat tiedot yksi kerrallaan.

1. Kirjoita komento: `lisaa article`.
2. Ohjelma kysyy `Cite key`: Anna lyhyt tunniste viitteelle (esim. VPL11).
3. Ohjelma kysyy muut tiedot (Author, Title, Journal, Year, DOI, Tag).
   - Jos tieto on vapaaehtoinen tai haluat jättää sen tyhjäksi (esim. Tag), paina vain Enter.
   - Jos syöte on virheellinen (esim. vuosiluku väärässä muodossa), ohjelma pyytää syöttämään sen uudelleen.
4. Kun kaikki tiedot on annettu onnistuneesti, ohjelma ilmoittaa: `Artikkeli lisätty tietokantaan`.

### 3. Esimerkkejä viitteen hakemisesta

Voit hakea viitteitä tietyn kentän (esim. tekijä tai vuosi) perusteella.

**Haku tekijän nimellä:**
Kirjoita komento: `hae author Matti`.
Ohjelma listaa kaikki viitteet, joiden tekijä-kenttä sisältää sanan "Matti".

**Haku vuosiluvulla:**
Kirjoita komento: `hae year 2023`.
Ohjelma listaa kaikki vuonna 2023 julkaistut viitteet.

### 4. BibTeX-tiedoston generointi
Voit luoda kaikista tietokannassa olevista viitteistä BibTeX-muotoisen tiedoston.

1. Kirjoita komento: `generoi`.
2. Ohjelma luo tiedoston `lahteet.bib` kansioon `output/`. 
3. Jos tiedosto on luotu onnistuneesti, ohjelma ilmoittaa: `Bibtex-tiedosto generoitu`.

Tiedosto sisältää viitteet seuraavassa muodossa:

```bibtex
@article{VPL11,
  author={Virtanen, Pekka},
  title={Uusi tutkimus},
  journal={Tiede-lehti},
  year={2023},
  doi={10.1234/5678},
  tag={tärkeä}
}
``` 
