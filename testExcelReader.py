import ExcelReaderPub
import WebWriterTest


"""
test for the excel reader
excel reader works like normal, however, the output is to a fake webpage to prove the concept
"""


def main():
    # instantiate the reader
    reader = ExcelReaderPub.ExcelReader('Inventory.xlsx')
    # get the items into a dictionary
    items = reader.parse_sheet()
    # instantiate the writer
    writer = WebWriterTest.WebWriterTest(items)
    writer.write()


main()
