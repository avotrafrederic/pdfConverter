from pdf2docx import Converter

converter = Converter("")
converter.convert('*.docx', start=0 , end=None);
converter.close()