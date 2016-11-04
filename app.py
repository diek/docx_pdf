# -*- coding: utf-8 -*-
import os.path
from datetime import datetime

from docxtpl import DocxTemplate
import pypandoc


def generate_invoice(tudoring_template):
    if os.path.isfile(tudoring_template):
        tpl = DocxTemplate(tudoring_template)
        invoice_date = datetime.now().strftime('%d.%m.%Y')
        context = {
            'STUDENT_NAME': 'Jerry Seinfeld',
            'STUDENT_NUMBER': 225,
            'SCHOOL_SUBJECT': [
                {'date': '19.05.2016', 'subject': 'ice cream'},
                {'date': '31.09.2016', 'subject': 'best breakfast cereal'},
                {'date': '03.10.2016', 'subject': 'stuff'},
            ],
            'TUTORING_TEACHER': "Kramer",
            'CREATION_DATE': invoice_date
        }
        context['NUMBER_OF_INVOICED_LESSONS'] = len(context['SCHOOL_SUBJECT'])
        tpl.render(context)
        filename = "student_tutoring {}".format(invoice_date)
        tpl.save(filename + '.docx')
        return(filename)
    else:
        print("Template does not exist")


def generate_pdf(invoice):
    # With an input file: it will infer the input format from the filename
    in_file = invoice + '.docx'
    out_file = invoice + '.pdf'
    pypandoc.convert_file(in_file, 'pdf', outputfile=out_file)


def main():
    invoice = generate_invoice("kramerica_tpl.docx")
    if invoice:
        generate_pdf(invoice)
    else:
        print("something went wrong")


if __name__ == '__main__':
    main()
