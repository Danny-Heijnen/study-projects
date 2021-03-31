import os
from PyPDF2 import PdfFileMerger

print("This program will take multiple PDF documents and merge them together into one document.\n\nStep 1. Create a folder and copy the PDF documents that you want to merge into that folder.\nStep 2. Change the file name of the documents to 1, 2, 3 ... in the required order.\nStep 3. Place this program (PDF_Merger.exe) in the same folder.\nStep 4. Start this program and enter 'y' to merge the PDF documents.\nThe new document will be placed in this folder with the name 'result.pdf'.")
print("\nIf you have not done step 1 to 3, please enter 'n' and restart the program when you're done with the preparation.")
print("\nNote: You will likely get a message saying 'PdfReadWarning'. This is not an error, the message can be ignored.")

answer = ""

while not (answer.lower() == "y" or answer.lower() == "n"):
    answer = input("\nDo you want to create a merged PDF right now? (y/n) ")

if answer.lower() == "n":
    quit()
else:
    list_of_pdfs = [input_pdf for input_pdf in os.listdir() if input_pdf.endswith(".pdf") and not input_pdf == "result.pdf"]

    list_of_pdfs.sort()

    merger = PdfFileMerger()

    for pdf in list_of_pdfs:
        merger.append(open(pdf, "rb"))

    try:
        with open("result.pdf", "wb") as output:
            merger.write(output)
    except:
        print("\nThe program has encountered an error, please check if the file 'result.pdf' contains the desired content.")
