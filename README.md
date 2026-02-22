kan vara bra att lägga till något om att väljer att inte transformera saker som jag personligen kan se är fel

bättre att flagga 

notera att inte har directories eftersom onödigt i denna upg på denna skala


# Hannah Zemack - Lab 1

## Setup
___

För att köra koden kör först i terminalen:

```uv sync```

## Teori

### Ingest -> Storage -> Transform -> Access
___

#### Ingest & Storage
Jag läser in CSV filen med hjälp av pandas read_csv och lagrar detta i en pandas DataFrame. 

#### Transform
Sedan städar jag datan från sådant som inte påverkar själva datan. Exempel på det är att allt ska vara i lowercase.
Men när jag städar datan görs inte sådant som kan ändra datan. 

Efter det flaggar jag de rader som aviker från den standardisering som har gjorts när jag städat.
Ett exempel är att jag flaggar när det saknas id eller om priset är onormalt högt jämfört med resterande. Programmet gör detta automatiskt
utifrån vad jag bestämt för regler.

Efter jag har flaggat går jag igenom flaggningarna manuellt och undersöker vad jag anser är "omöjlig data".
Alltså sådant som behöver fixas för att kunna användas i analyser. Jag tar sedan bort detta och genererar två nya dataframes.
Clean_df och rejected_df. Clean_df kan sedan användas för analyser.

#### Access
Jag genererar CSV filer som gör det enkelt att ta del av analysresultaten.

- analytics_summary.csv innehåller övergripande statistik som snittpris och medianpris
- price_analysis.csv innehåller de dyraste och mest avvikande produkterna
- rejected_products.csv innehåller alla produkter som ansetts omöjliga

CSV formatet gör datan lättillgänglig och kan enkelt öppnas i verktyg som Excel 
för vidare analys eller granskning.

### Teknologityper
___

#### Pandas
Pandas är det som jag använder mig av under hela detta projekt. Det kan användas för att
läsa in, städa, transformera och analyser data i DataFrames.

#### Psycopg3
Ett pythonbiliotek för att kunna komminucera med PostgreSQL





