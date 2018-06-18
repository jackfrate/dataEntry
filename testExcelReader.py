import ExcelReaderPub
import WebWriterTest


def main():

    reader = ExcelReaderPub.ExcelReader('Inventory.xlsx')
    items = reader.parse_sheet()
    writer = WebWriterTest.WebWriterTest(items)
    writer.write()


main()
