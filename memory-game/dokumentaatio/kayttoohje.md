# Käyttöohje
Lataa projektin viimeisimmän releasen lähdekoodi valitsemalla Assets-osion alta Source code
## Ohjelman käynnistäminen
#### Asennus
Asennus tulee tehdä memorygame-kansion sisällä.
Asenna riippuvuudet komennolla:
```bash
poetry install
```
#### Komentorivitoiminnot
Komentorivitoiminnot tulee suorittaa memorygame-kansion sisällä.
### Ohjelman suorittaminen
Ohjelman voi suorittaa komennolla:
```bash
poetry run invoke start
```
#### Pelin aloittaminen
Sovellus käynnistyy menu-näkymään:

![image](https://github.com/minttugomez/ot-harjoitustyo/assets/116456153/187433cc-c700-4ba2-a583-aada36595a8c)

Pelin aloittamiseksi vaaditaan pelaajamäärän valinta ja sitten peli aloitetaan "START"-napista.
#### Pelivuoron toteuttaminen
Vuorossa oleva pelaaja on ympyröity:

![image](https://github.com/minttugomez/ot-harjoitustyo/assets/116456153/95f88b34-fcdd-4902-bcb4-940edaf074b8)

Omalla vuorollaan pelaaja klikkaa kahta eri korttia yrittäen saada parit.
Mikäli kortit eivät ole pari, vuoro siirtyy seuraavalle pelaajalle. Jos kortit ovat pari, pelaaja saa uuden vuoron.
Peli jatkuu kunnes kortit loppuvat
#### Pelin päättyminen
Pelin päättyessä pistetilanne näkyy näytöllä. Painamalla "CONTINUE"-nappia, pääsee takaisin menu-näkymään.
