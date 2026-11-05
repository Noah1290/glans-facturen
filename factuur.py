# Functie: berekent 21% btw over een bedrag
def bereken_btw(bedrag):
    return bedrag * 0.21

# Gegevens van de klus vragen
naam = input("Klantnaam: ")
print(f"Hallo {naam}")
uren = float(input("Aantal uren: "))
dag = input("Werkdag of weekend? ").lower()

# Tarief kiezen: weekend is duurder
if dag == "weekend":
    tarief = 40.00
else:
    tarief = 32.50

# Bedragen berekenen
subtotaal = uren * tarief
btw = bereken_btw(subtotaal)
totaal = subtotaal + btw

# Factuur tonen
print(f"Tarief: €{tarief:.2f} per uur")
print(f"Subtotaal: €{subtotaal:.2f}")
print(f"Btw: €{btw:.2f}")
print(f"Totaal: €{totaal:.2f}")