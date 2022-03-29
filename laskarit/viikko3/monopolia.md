
Sovelluksen loogisen tietomallin muodostavat luokat User ja Todo, jotka kuvaavat käyttäjiä ja käyttäjien tehtäviä:

```mermaid
 classDiagram
      Todo "*" --> "1" User
      class pelaaja{
          ruutu
      }
      class peli{
          pelaajat
          vuoro
      }
      class ruutu{
          seuraava_ruutu
      }
      class Noppa{
          heitä_noppaa
      }
```
