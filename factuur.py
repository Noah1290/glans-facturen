# Functie: berekent 21% btw over een bedrag
def bereken_btw(bedrag):
    return bedrag * 0.21

# NIEUW: vaste klanten van Glans & Co (in kleine letters)
vaste_klanten = ["bakkerij jansen", "tandartspraktijk smile", "kantoor van dijk", "sportschool fitlab"]
# Gegevens van de klus vragen
naam = input("Klantnaam: ")
print(f"Factuur voor {naam}")
uren = float(input("Aantal uren: "))
dag = input("Werkdag of weekend? ").lower()

# Tarief kiezen: weekend is duurder
if dag == "weekend":
    tarief = 40.00
else:
    tarief = 32.50

# Voorrijkosten: gratis vanaf 4 uur
if uren >= 4:
    voorrijkosten = 0.00
else:
    voorrijkosten = 17.50

# Bedragen berekenen
urenbedrag = uren * tarief

# NIEUW: 5% korting voor vaste klanten, alleen op de uren
if naam.lower() in vaste_klanten:
    korting = urenbedrag * 0.05
else:
    korting = 0.00

subtotaal = urenbedrag - korting + voorrijkosten
btw = bereken_btw(subtotaal)
totaal = subtotaal + btw

# Factuur tonen
print(f"Tarief: €{tarief:.2f} per uur")
print(f"Korting: -€{korting:.2f}")
print(f"Voorrijkosten: €{voorrijkosten:.2f}")
print(f"Subtotaal: €{subtotaal:.2f}")
print(f"Btw: €{btw:.2f}")
print(f"Totaal: €{totaal:.2f}")