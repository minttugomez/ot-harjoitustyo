# Määrittelydokumentti

Toteutin perinteisen muistipelin tietokoneversiona. Muistipelissä on 72 korttia, joissa on jonkinlainen kuva. Jokaista kuvaa löytyy pelistä kaksi kappaletta. Pelaajia on 2-4, ja jokainen vuorollaan avaa kaksi korttia, jolloin kaikki näkevät korteissa esiintyneet kuvat. Mikäli näissä kahdessa avatussa kortissa on sama kuva, nämä kortit poistuvat pelistä ja kyseinen pelaaja saa pisteen sekä ylimääräisen vuoron. Peli päättyy, kun kortteja ei ole enää jäljellä. Voittaja on se, jolla on eniten pisteitä.

Koska web-komponentit eivät kuulu tämän kurssin laajuuteen, toteutan muistipelin niin, että pelaajat pelaavat sitä samalta koneelta. Kaikki 2-4 pelaajaa ovat siten teknisesti vain yksi käyttäjä. Perustoiminnallisuuksia sovelluksessa on pelin aloitus (jossa mahdollisuus valita pelaajien määrä), pelin eteneminen vuorotellen pelaajien välillä, pisteiden lasku ja pelin päättyminen.

Pelin alkaessa sovellus arpoo kuvien sijainnit muttei näytä niitä pelaajille. Sovellus ylläpitää tietoa kuvien sijainnista pelin päättymiseen asti. Tarvetta itse tietokannalle ei pelissä oikeastaan ole.