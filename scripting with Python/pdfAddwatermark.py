
# from GEEKS for GEEKS .com
# https://www.geeksforgeeks.org/add-watermark-to-pdf-using-pypdf4-in-python/
import PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader


PyPDF2.PdfFileReader('super.pdf')


def put_watermark(input_pdf, output_pdf, watermark):

    # reads the watermark pdf file through
    # PdfFileReader
    watermark_instance = PdfFileReader(watermark)

    # fetches the respective page of
    # watermark(1st page)
    watermark_page = watermark_instance.getPage(0)

    # reads the input pdf file
    pdf_reader = PdfFileReader(input_pdf)

    # It creates a pdf writer object for the
    # output file
    pdf_writer = PdfFileWriter()

    # iterates through the original pdf to
    # merge watermarks
    for page in range(pdf_reader.getNumPages()):

        page = pdf_reader.getPage(page)

        # will overlay the watermark_page on top
        # of the current page.
        page.mergePage(watermark_page)

        # add that newly merged page to the
        # pdf_writer object.
        pdf_writer.addPage(page)

    with open(output_pdf, 'wb') as out:

        # writes to the respective output_pdf provided
        pdf_writer.write(out)


if __name__ == "__main__":
    put_watermark(
        input_pdf='super.pdf',  # the original pdf
        output_pdf='watermark_added1.pdf',  # the modified pdf with watermark
        watermark='wtr.pdf'  # the watermark to be provided
    )


#another solution - from ZTM 
#https://github.com/aneagoie/watermarker/blob/master/pdf.py
# import PyPDF2

# template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
# watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
# output = PyPDF2.PdfFileWriter()

# for i in range(template.getNumPages()):
#   page = template.getPage(i)
#   page.mergePage(watermark.getPage(0))
#   output.addPage(page)

#   with open('watermarked_output.pdf', 'wb') as file:
#     output.write(file)