import webbrowser

from fpdf import FPDF
import os


class PdfReport:
    def __init__(self,filename):
        self.filename = filename

    def generate(self,flatmate1,flatmate2,bill):
        flatmate_1pay=str(round(flatmate1.pays(bill, flatmate2)))
        flatmate_2pay=str(round(flatmate2.pays(bill, flatmate1)))
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        pdf.image("files/house.png", w=80, h=80)
        pdf.set_font(family="Times", size=24, style='B')
        pdf.cell(w=0, h=80, txt="FLATMATE BILL", border=0, align='C', ln=1)
        #insert period and label value
        pdf.set_font(family="Courier", size=14,style='I')
        pdf.cell(w=100, h=40, txt="Period", border=0, align='C')
        pdf.cell(w=150, h=40, txt=bill.period, border=0, align='C', ln=1)
        #name and amount to be paid
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0, align='C')
        pdf.cell(w=150, h=25, txt=flatmate_1pay, border=0, align='C' , ln=1)
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0, align='C')
        pdf.cell(w=150, h=25, txt=flatmate_2pay, border=0, align='C')
        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)
