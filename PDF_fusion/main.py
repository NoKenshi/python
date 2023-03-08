import os
import PyPDF2
import datetime

# Récupérez le chemin du répertoire où se trouve votre fichier Python
path = os.path.dirname(os.path.abspath(__file__))

# Nom du dossier que vous souhaitez créer
folder_name = "result"

# Vérifiez si le dossier existe déjà
if not os.path.exists(os.path.join(path, folder_name)):
    # Créer le dossier
    os.mkdir(os.path.join(path, folder_name))
    print("Dossier créé avec succès !")
else:
    print("Le dossier existe déjà.")

# Chemin du dossier contenant les fichiers PDF à fusionner
dossier = "./files"

# Créer un objet PdfFileWriter pour écrire le PDF fusionné
pdf_writer = PyPDF2.PdfWriter()

# Boucle à travers tous les fichiers PDF dans le dossier
for filename in os.listdir(dossier):
    if filename.endswith('.pdf'):
        # Ouvrir le fichier PDF et créer un objet PdfFileReader
        with open(os.path.join(dossier, filename), 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Ajouter les pages du fichier PDF à l'objet PdfFileWriter
            for page in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page])

# Créer un nom unique pour le fichier fusionné
timestamp = datetime.datetime.now().strftime("%Y_%m_%d__%H_%M_%S")
fusion_filename = f"fusion_{timestamp}.pdf"

# Enregistrer le PDF fusionné dans un nouveau fichier
with open(os.path.join(path, folder_name, fusion_filename), 'wb') as fichier_fusionne:
    pdf_writer.write(fichier_fusionne)

print(f"Le fichier fusionné a été enregistré sous {os.path.join(path, folder_name, fusion_filename)}")
