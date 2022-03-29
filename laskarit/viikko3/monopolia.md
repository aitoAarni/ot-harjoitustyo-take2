
Sovelluksen loogisen tietomallin muodostavat luokat User ja Todo, jotka kuvaavat käyttäjiä ja käyttäjien tehtäviä:

```mermaid
 classDiagram
      peli "1" --> "*" pelaaja
      ruutu "1" <.. "*" pelaaja
      class pelaaja{
          ruutu
          heitä_noppaa()
      }
      class peli{
          pelaajat
          vuoro
      }
      class ruutu{
          seuraava_ruutu
      }
```
