#-*-coding:utf-8 -*-
from pdf2docx import Converter
import colored
import glob
import subprocess
import pyfiglet
import os
class PdfConvert:
	@classmethod
	def showFile(cls):
		files = [f for f in glob.glob('*.pdf')]
		for file in files:
			print(file)
	@classmethod
	def convert(cls,pdfFile):
		try:
			converter = Converter("{}.pdf".format(pdfFile))
			converter.convert("{}.docx".format(pdfFile), start=0 , end=None)
			converter.close()
			return True
		except Exception as e:
			print("{}impossible de charge le fichier {}.pdf!".format(colored.fg(1),pdfFile))
		return False

def main():
	title = pyfiglet.figlet_format("PDF TO DOCX")
	print(f"{colored.fg(37)} {title}".center(20))
	choice = input("{}Voulez-vous lister les fichiers du  dossier courant? [O/N | entrer pour Oui] : ".format(colored.fg(6))).upper()
	if(choice == "O" or choice == "OUI" or choice == ""):
		PdfConvert.showFile()
	
	fileName = input("{}Entrez le nom du fichier pdf: ".format(colored.fg(6)))
	response = PdfConvert.convert(fileName)
	if(response):
		print('{}Conversion réussi!'.format(colored.fg(28)))
	else :
		print("Une erreur c'est produite! veuillez ressayer")


if __name__ == "__main__":
	subprocess.run("clear")
	main()
	print(f"{colored.fg(0)}")