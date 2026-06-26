import os
from typing import Iterable, List
from collections.abc import Iterator
import pdfplumber 
from pathlib import Path
import csv
import re

from pdfplumber.pdf import PDF

sciezka = Path("./data")


def main():
    a = Path("./data/Sample-Pdf-invoices/PDF")
    docs_list = retrive_documents(a)
    for i in docs_list:
        with pdfplumber.open(i) as pdf:
            first = pdf.pages[0]
            print(first.chars[0])

        


def retrive_documents(directory: Path) -> list[str] : 
    """Retrive all documents"""
    return [str(p) for p in directory.glob("**/*.pdf")]




# def create_pdf_obj(filepath: Path) -> PDF:
#     with pdfplumber.open(filepath) as pdf:
 
    
 




if __name__ == "__main__":
    main()
1