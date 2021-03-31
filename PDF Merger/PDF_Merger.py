import os
from PyPDF2 import PdfFileMerger

print("This program will take multiple PDF files and merge them together into one document.\n\nIn order to do this, create a folder and place the separate PDF files into the folder.\nThen rename the files 1, 2, 3 ...  in the order you want to merge them.\nMake sure this program is in the same folder.")

print("\nIf you have already prepared the folder and filenames, enter 'y' to create the merged PDF.\nIf you have not prepared, please enter 'n' and restart the program when you're done.")

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