from commands.hae import Hae

class Generoi:
    
    def __init__(self, db, io):
        self.db = db
        self.io = io
    
            
    def kirjoita_tiedostoon(self, tulokset):
        with open("lahteet.bib", "w", encoding="utf-8") as f:
            for r in tulokset:
                if isinstance(r, dict):
                    # Muodostetaan BibTeX-tyyppinen merkintä
                    f.write(f"@{r.get('table')}{{{r.get('cite_key','unknown')}\n")
                    f.write(f"  auther={{{r.get('author','')}}},\n")
                    f.write(f"  title={{{r.get('title','')}}},\n")
                    f.write(f"  journal={{{r.get('journal','')}}},\n")
                    f.write(f"  year={{{r.get('year','')}}},\n")
                    f.write(f"  doi={{{r.get('doi','')}}},\n")
                    f.write(f"  tag={{{r.get('tag','')}}}\n")
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
            print("Bibtex-tiedosto generoitu")
        
        except:
            print("Virhe tiedoston luomisessa")