#!/usr/bin/env python
import optparse
from PyPDF2 import PdfFileMerger

def main():
    p = optparse.OptionParser()
    p.add_option('--output', '-o', default="merged_document.pdf")
    options, arguments = p.parse_args()

    pdfs = arguments
    result_name = options.output

    outfile = PdfFileMerger()
    for f in pdfs:
        outfile.append(open(f, 'rb'))

    outfile.write(open(result_name, 'wb'))


if __name__ == '__main__':
    main()