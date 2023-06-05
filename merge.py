from pypdf import PdfMerger



merger = PdfMerger()

merger.append('file.pdf', pages=(0, 7))
merger.append('removedfooter.pdf')  
merger.append('file.pdf', pages=(161, 320))

merger.write("result.pdf")
merger.close()