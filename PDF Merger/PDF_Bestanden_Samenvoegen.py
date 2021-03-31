import os
from PyPDF2 import PdfFileMerger

print("Dit programma voegt meerdere PDF-documenten samen tot één PDF-document.\n\nStap 1. Maak een bestandsmap aan en kopieer de PDF-documenten die u wilt samenvoegen naar deze map.\nStap 2. Verander de bestandsnaam van de documenten naar 1, 2, 3 ... in de volgorde waarin u ze wilt samenvoegen.\nStap 3. Plaats dit programma (PDF_Bestanden_Samenvoegen.exe) in dezelfde bestandsmap.\nStap 4. Start dit programma en voer 'j' in om de PDF-documenten samen te voegen.\nHet nieuwe document wordt in deze map geplaats met de naam 'resultaat.pdf'.")
print("\nZijn de stappen 1 tot en met 3 nog niet uitgevoerd? Voer hieronder 'n' in en start het programma opnieuw nadat de bestanden zijn voorbereid.")
print("\nOpmerking: Waarschijnlijk komt de melding 'PdfReadWarning' in beeld. Dit is geen foutmelding, u kunt de melding negeren.")

answer = ""

while not (answer.lower() == "j" or answer.lower() == "n"):
    answer = input("\nWilt u nu de PDF-bestanden samenvoegen? (j/n) ")

if answer.lower() == "n":
    quit()
else:
    list_of_pdfs = [input_pdf for input_pdf in os.listdir() if input_pdf.endswith(".pdf") and not input_pdf == "resultaat.pdf"]

    list_of_pdfs.sort()

    merger = PdfFileMerger()

    for pdf in list_of_pdfs:
        merger.append(open(pdf, "rb"))

    try:
        with open("resultaat.pdf", "wb") as output:
            merger.write(output)
    except:
        print("\nEr is een fout opgetreden, controleer of het bestand 'resultaat.pdf' juist is gecreëerd.")
