# Hannah Zemack - Lab 1

## Setup
___

För att använda koden kör först i terminalen:

```uv sync```

Alternativt använd egen virtual environment och installera pandas.

## Run
___

För att köra koden kör endas main.py filen

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
Ett pythonbiliotek för att kunna komminucera med PostgreSQL. Kan användas när man istället
för CSV filer har en databas. I en ETL används det ofta i load när man vill spara den transformerade datan
till databasen.

#### Pydantic
Ett pythonbbliotek för validering av data.

### ETL
___

#### Extract
Hämta data från någon källa. Kan vara en databas, en fil eller något liknande.

#### Transform
Bearbeta och städa datan så att den sedan går att använda. Kan vara att ta bort felaktig data
eller standardisera format.

#### Load
Innebär att spara den bearbetade och rena datan någonstans. Som i extract kan det vara en databas, en fil etc.

### Noteringar
___

I denna labb har jag valt att inte dela upp allt i olika directories. Även om det är bättre praxis.
Detta eftersom det inte kändes nödvändigt i denna skala på projekt. 






