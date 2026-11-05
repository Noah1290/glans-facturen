def bereken_btw(bedrag):
        return bedrag * 0.21

naam = input("Naam: ")
print(f"Hallo {naam}")
uren = float(input("Aantal uren: "))
tarief = float(input("Uurtarief: "))

subtotaal = uren * tarief
btw = bereken_btw(subtotaal)
totaal = subtotaal + btw

print(f"Subtotaal: €{subtotaal:.2f}")
print(f"Btw: €{btw:.2f}")
print(f"Totaal: €{totaal:.2f}")