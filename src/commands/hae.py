
class Hae:

    def __init__(self, db, io, attribuutti=None, hakusana=""):
        self.hakuattribuutit = self.alusta_set()
        self.hakusana = hakusana
        self.attribuutti = attribuutti
        self.db = db
        self.io = io
        self.cursor = db.cursor()
        self.tulokset = []

    
    # TODO: Ehkä parempi tapa käsitellä virheet ja erikoistapausten tulostus.
    def run(self):

        # Haetaan kaikkien pöytien nimet
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [t[0] for t in self.cursor.fetchall()]
        query = ""

        if self.attribuutti is None:
            query = "SELECT * FROM {table}"
        elif self.tarkista_hakuattribuutti() and self.hakusana != "":
            query = "SELECT * FROM {table} WHERE LOWER ({attribuutti}) LIKE LOWER ('%{hakuehto}%')"
        else:
            self.tulokset = ["Virheellinen hakuattribuutti tai puuttuva hakusana!\n"]
            return

        for table in tables:
            try:
                if self.attribuutti is None:
                    self.cursor.execute(query.format(table=table))
                else:
                    self.cursor.execute(query.format(
                        table=table,
                        attribuutti=self.hakuattribuutit[self.attribuutti.lower()],
                        hakuehto=self.hakusana
                    ))

                hakutulos = self.cursor.fetchall()
                if hakutulos:
                    hakutulos = [dict(t) for t in hakutulos]
                    #lisätään tuloksiin tieto mistä taulusta se on peräisin
                    for r in hakutulos:
                        r['table'] = table
                    self.tulokset.extend(hakutulos)
            except Exception as e:
                #self.io.write(e)
                pass

        if not self.tulokset:
            self.tulokset = ["Hakuehdoilla ei löytynyt yhtään tulosta!"]

    # Lisää tarvittavat hakuattribuutit.
    def alusta_set(self):
        return {
            "year": "year",
            "vuosi": "year",
            "author": "author",
            "tekijä": "author",
            "journal": "journal",
            "julkaisu": "journal",
            "title": "title",
            "otsikko": "title",
            "tag": "tag",
            "cite": "cite_key",
            "doi": "doi"
        }

    def tarkista_hakuattribuutti(self):
        return self.attribuutti.replace(" ", "").lower() in self.hakuattribuutit

    # Tulostus
    def tulosta(self):
        for row in self.tulokset:
            if isinstance(row, dict):
                self.io.write("\n------------------------------")
                self.io.write(f"  Tyyppi:   {row.get('table','')}")
                self.io.write(f"  Cite key: {row.get('cite_key','')}")
                self.io.write(f"  Author:   {row.get('author','')}")
                self.io.write(f"  Title:    {row.get('title','')}")
                self.io.write(f"  Journal:  {row.get('journal','')}")
                self.io.write(f"  Year:     {row.get('year','')}")
                self.io.write(f"  DOI:      {row.get('doi','')}")
                self.io.write(f"  Tag:      {row.get('tag','')}")
                self.io.write("------------------------------\n")
            else:
                self.io.write(str(row))

    def hae_artikkelit(self):
        return self.tulokset
