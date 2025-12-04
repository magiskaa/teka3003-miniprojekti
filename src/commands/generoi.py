import os
from commands.hae import Hae

class Generoi:

    def __init__(self, db, io, output_dir="output"):
        self.db = db
        self.io = io
        self.output_dir = output_dir

    # Luo lähdetiedoston, hakee lähteelle ominaiset tiedot ja kirjoittaa ne tiedostoon.
    # Yliajaa aikaisemman luodun tiedoston.
    def kirjoita_tiedostoon(self, tulokset):
        os.makedirs(self.output_dir, exist_ok=True)
        path = os.path.join(self.output_dir, "lahteet.bib")

        with open(path, "w", encoding="utf-8") as f:
            for r in tulokset:
                if isinstance(r, dict):
                    # Muodostetaan BibTeX-tyyppinen merkintä
                    f.write(f"@{r.get('table')}{{{r.get('cite_key','unknown')},\n")

                    tietokentat = []
                    # Haetaan kunkin lähteen ominaiset tietokentät
                    for key in ('author', 'title', 'journal', 'year',
                                'doi', 'tag', 'publisher', 'booktitle'):
                        if key in r and r[key] is not None:
                            tietokentat.append((key, r[key]))

                    for i, (key, value) in enumerate(tietokentat):
                        # Viimeisen tietokentän perään ei saa tulla pilkkua
                        if i == len(tietokentat) - 1:
                            f.write(f"  {key}={{{value}}}\n")
                        else:
                            f.write(f"  {key}={{{value}}},\n")

                    f.write("}\n\n")

                else:
                    # r on virheviesti merkkijonona
                    f.write(str(r) + "\n")


    def run(self):
        try:
            hae = Hae(self.db, self.io)
            hae.run()
            tulokset = hae.hae_artikkelit()

            self.kirjoita_tiedostoon(tulokset)
            self.io.write("Bibtex-tiedosto generoitu")

        except Exception as e:
            self.io.write(f"Virhe tiedoston luomisessa: {e}")
