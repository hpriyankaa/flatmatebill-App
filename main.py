from flat import Bill, Flatmate
from report import PdfReport

amount=float(input("enter the total bill amount: " ))
period=input("enter the period: ")
name1=input("enter your name : ")
name2=input("enter room mate name: ")
days_in_house1=int(input("enter the number of days you stayed: "))
days_in_house2=int(input(f"enter the number of days {name2} stayed :"))
thebill= Bill(amount, period)
flatmate1= Flatmate(name1, days_in_house1)
flatmate2= Flatmate(name2, days_in_house2)
print(f"{flatmate1.name} pays",flatmate1.pays(thebill,flatmate2))
print(f"{flatmate2.name} pays",flatmate2.pays(thebill,flatmate1))

pdf_report= PdfReport(filename=f"{thebill.period}.pdf")
pdf_report.generate(flatmate1,flatmate2,thebill)
        
        

