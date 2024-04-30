# Changelog

## Viikko 3

- Projekti alustettu
- Luotu MemoryGame-luokka, joka mm. ylläpitää tietoa korttien sijainnista ja pelitilanteesta
- Lisätty MemoryGame-luokkaan funktiot korttimäärän validoinnille, korttien sekoittamiselle sekä korttien asettamiselle ruudukoksi
- Luotu testit yllämainituille

## Viikko 4

- MemoryGame-luokan start-funktiota täydennetty
- Start-funktiolle lisätty testi
- MemoryGame-luokkaan lisätty change_players-funktio pelaajamäärän muuttamiselle
- Change_players-funktiolle lisätty testi
- MemoryGame-luokkaan lisätty duplicate_cards funktio korttien parien luomiselle
- Duplicate_cards-funktiolle lisätty testi
- Luotu UI-luokka käyttöliittymän toteuttamiselle sekä siihen liittyvät setup, start ja draw_grid -funktiot

## Viikko 5

- MemoryGame-luokkaan lisätty funktio pisteiden laskulle
- Käyttöliittymään laitettu näkymään pistetilanne
- Lisätty pisteytykseen liittyvät testit
- Lisätty menutaulu käyttöliittymään

## Viikko 6

- Dokumentaatioon päivitetty neuvo komentojen suorittamisesta memorygame-kansion sisällä
- Luotu logiikka nappien painallukselle
- Toteutettu napin tummentuminen hetkellisesti klikattaessa
- Toteutettu pelaajamäärän muuttuminen pelaajanappia klikatessa
- Toteutettu pelin alkaminen "start"-nappia klikatessa
- Lisätty ominaisuus, joka näyttää, mikä pelaajamäärä on valittuna
- Päivitetty testit muokattuihin funktioihin
- Luotu testit end- ja setup-funktioille
- Lisätty teksti "choose players first" mikäli peliä yritetään aloittaa valitsematta pelaajamäärä
- Lisätty vuorokierto memorygame-luokkaan
- Lisätty logiikka korttien kääntymiselle
- Estetty enemmän kuin kahden kortin klikkaaminen vuorolla
- Päivitetty memorygame-luokan testit ja lisätty testit uusille funktioille