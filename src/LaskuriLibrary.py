from laskuri import Laskuri

class LaskuriLibrary:
    def __init__(self):
        self._laskuri = Laskuri()

    def lisaa_laskuri(self):
        self._laskuri.lisaa()

    def laskuri_value_should_be(self, odotus):
        int_odotus = int(odotus)
        if self._laskuri.value != int_odotus:
            raise AssertionError(f"{self._laskuri.value} != {int_odotus}")