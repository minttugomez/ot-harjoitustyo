# Memory game

Perinteinen muistipeli tietokoneversiona. Muistipelissä on 72 korttia, joissa on jonkinlainen kuva. Jokaista kuvaa löytyy pelistä kaksi kappaletta. Pelaajia on 2-4, ja jokainen vuorollaan avaa kaksi korttia, jolloin kaikki näkevät korteissa esiintyneet kuvat. Mikäli näissä kahdessa avatussa kortissa on sama kuva, nämä kortit poistuvat pelistä ja kyseinen pelaaja saa pisteen sekä ylimääräisen vuoron. Peli päättyy, kun kortteja ei ole enää jäljellä. Voittaja on se, jolla on eniten pisteitä.

## Dokumentaatio

- [määrittelydokumentti](https://github.com/minttugomez/ot-harjoitustyo/tree/master/memory-game/dokumentaatio/maarittelydokumentti.md)

- [työaikakirjanpito](https://github.com/minttugomez/ot-harjoitustyo/tree/master/memory-game/dokumentaatio/tyoaikakirjanpito.md)

- [changelog](https://github.com/minttugomez/ot-harjoitustyo/tree/master/memory-game/dokumentaatio/changelog.md)

- [arkkitehtuuri](https://github.com/minttugomez/ot-harjoitustyo/tree/master/memory-game/dokumentaatio/arkkitehtuuri.md)

## Release

- [Viikko 5](https://github.com/minttugomez/ot-harjoitustyo/releases/tag/viikko5)

## Asennus

Asenna riippuvuudet komennolla:

```bash
poetry install
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman voi suorittaa komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit voi suorittaa komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Laatutarkastus

Pylint-tarkastuksen voi suorittaa komennolla:

```bash
poetry run invoke lint
```

### Automaattinen formatointi

Automaattisen formatoinnin voi suorittaa komennolla:

```bash
poetry run invoke format
```
