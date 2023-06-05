from fpdf import FPDF
import os 

pdf = FPDF()
pdf.set_auto_page_break(0)

files = next(os.walk('./images'))[2] 
print(len(files))

for idx in range(len(files)):
    pdf.add_page()
    img= './images/img'+str(idx+1)+'.jpg'
    pdf.image(img,0,0,210,297)

pdf.output('output.pdf', 'F')
