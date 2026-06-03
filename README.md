Filmrekommendationssystem:
Detta program är ett filmrekommendationssystem skrivet i Python. Programmet använder en lista med filmer där varje film innehåller information om titel, genre, åldersgräns, speltid, utgivningsår, IMDb-betyg, språk och om filmen är animerad eller inte. Användaren får svara på frågor om vilken typ av film som önskas. Programmet jämför sedan användarens svar med informationen i filmlistan och räknar ut vilka filmer som passar bäst. Därefter visas de tre högst rankade filmerna. Programmet innehåller även en feedback-funktion som gör att användaren kan välja en film som rekommenderades. Genren från den filmen sparas och påverkar framtida rekommendationer.

Funktioner: 
Filtrerar filmer efter genre, filtrerar filmer efter åldersgräns, filtrerar filmer efter språk, filtrerar filmer efter om de är animerade eller inte, filtrerar bort filmer med för lågt IMDb-betyg, visar de tre bästa rekommendationerna, tar emot feedback från användaren, anpassar framtida rekommendationer baserat på tidigare feedback.


Det som var lätt:
Det var ganska enkelt att skapa listan med filmer eftersom varje film kunde sparas som en dictionary. Då blev det lätt att organisera information som titel, genre, betyg och språk.

När filmerna hade sorterats var det ganska enkelt att använda en for-loop för att skriva ut informationen om de tre bästa rekommendationerna.


Det som var svårt:
Det svåraste var att bestämma hur filmerna skulle få poäng. Jag behövde fundera på hur mycket varje matchning skulle vara värd. Till exempel får en film: 2 poäng om genren matchar, 1 poäng om åldersgränsen matchar, 1 poäng om språket matchar, 1 poäng om filmen är animerad eller inte enligt användarens önskemål. Dessutom får filmen en bonus baserad på sitt IMDb-betyg. Detta var svårt eftersom jag behövde få rekommendationerna att kännas rimliga.

Efter att alla filmer fått poäng behövde de sorteras från högst till lägst poäng. Den här delen var svår eftersom jag behövde förstå hur: "scored_movies.sort(reverse=True, key=lambda x: x[0])" fungerar. Jag behövde lära mig att lambda används för att välja vilket värde som ska användas vid sorteringen, för att jag lärde mig detta innan så använde jag mig av extern hjälp för att fixa problemet.

Det var också svårt att hantera situationer där användaren skriver något annat än ett nummer på frågan om IMDb-betyg. Därför använde jag:

try:
    rating = float(input("Minimum IMDb rating?\n"))
except ValueError:
    print("Please enter a valid number.")

Denna del fick jag hjälp av AI med eftersom jag inte tidigare hade arbetat med try och except.

Feedback-funktionen var också utmanande. Programmet behövde komma ihåg vilken typ av film användaren gillade även efter att loopen startade om. För att lösa detta skapade jag variabeln: "preferred_genre = None". När användaren väljer en film sparas filmens genre i variabeln. Nästa gång rekommendationer räknas ut får filmer från samma genre extra poäng. Detta gjorde  rekommendationerna mer personliga men krävde att jag förstod hur information kan sparas mellan flera varv i en loop.


Vad jag lärde mig:
Genom projektet har jag lärt mig att använda: listor, dictionaries, typ vad lambda är, felhantering med try och except, variabler som sparar information mellan loopar, hur feedback från användaren kan användas för att förbättra rekommendationer. Jag har också blivit bättre på att kommentera min kod så att den blir lättare att förstå och underhålla.
