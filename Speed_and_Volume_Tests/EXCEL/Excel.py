import xlsxwriter
import concurrent.futures
import time
from API import Calculation_API as calc

data = ''
workbook = ''


class Excel:

    @staticmethod
    def get_data(json_data):
        global data
        data = json_data

    def create_rows_and_columns(self, worksheet, row, col, year, duration, name):
        global data

        # Data

        if name == 'Speed Test':
            for country in data:
                for i in range(len(country['d'])):
                    fixed = calc.average_speeds(country['fd'])
                    mobile = calc.average_speeds(country['md'])

                    worksheet.write(row, col, year)
                    worksheet.write(row, col + 1, country['n'])
                    worksheet.write(row, col + 2, duration)
                    worksheet.write(row, col + 3, fixed)
                    worksheet.write(row, col + 4, mobile)

                    worksheet.write(row, i + 5, '{} | {}'.format(country['fd'][i], country['md'][i]))

                row += 1

        else:
            for country in data:
                for i in range(len(country['d'])):
                    fixed = calc.average_volumes(country['fvc'])
                    mobile = calc.average_volumes(country['mvc'])

                    worksheet.write(row, col, year)
                    worksheet.write(row, col + 1, country['n'])
                    worksheet.write(row, col + 2, duration)
                    worksheet.write(row, col + 3, fixed)
                    worksheet.write(row, col + 4, mobile)

                    worksheet.write(row, i + 5, '{:.2f} | {:.2f}'.format(float(country['fvc'][i] * 100),
                                                                         float(country['mvc'][i] * 100)))

                row += 1

    def create_worksheets(self, name, excel_format):
        if name == 'Speed Test':
            print('Creating speed test worksheet ')

        else:
            print('Creating volume test worksheet ')

        global data
        global workbook

        worksheet = workbook.add_worksheet(name)

        year = "2019/2020"
        duration = '{} weeks'.format(len(data[0]['d']))
        weeks = data[0]['d']
        columns = []

        if name == 'Speed Test':
            columns = ["Year", "Country", "Duration", "Performance average (fixed) (Mbps)",
                       "Performance average (mobile) (Mbps)"]

            for week in weeks:
                columns.append('{}  (Fixed | Mobile) (Mbps)'.format(week))

        else:
            columns = ["Year", "Country", "Duration", "Volume average (fixed) (%)",
                       "Volume average (mobile) (%)"]

            for week in weeks:
                columns.append('{}  (Fixed | Mobile) (%)'.format(week))

        # Start from the first cell. Rows and columns are zero indexed.
        row = 0
        col = 0

        # Header
        for column in columns:
            worksheet.write(row, col, column, excel_format)
            col += 1

        worksheet.set_column(0, 0, 10)
        worksheet.set_column(1, 1, 20)
        worksheet.set_column(3, col, 30)
        worksheet.freeze_panes(1, 0)  # Freeze the first row.

        col = 0
        row = 1

        self.create_rows_and_columns(worksheet, row, col, year, duration, name)

    def create_worksheets_remote(self, name, excel_format):
        if name == 'Remote Test':
            print('Creating remote worksheet ')

        else:
            print('Incorrect name ')

        global data
        global workbook

        worksheet = workbook.add_worksheet(name)

        # for key in data:
        #     print(key)
        #     print(data[key])

        # Start from the first cell. Rows and columns are zero indexed.
        row = 0
        col = 0
        count = 0

        # Header
        for key in data:
            worksheet.write(row, col, key, excel_format)
            # print(key)
            row += 1

            for item in data[key]:
                for line in item:
                    # if count == 0:
                    #     worksheet.write(row, col, line, excel_format)
                    #     # print(line)
                    #     row += 1
                    #     count += 1

                    worksheet.write(row, col, line)
                    # print(line)
                    col += 1

                row += 1
                col = 0

            row += 1
            col = 0
            count = 0

        worksheet.set_column('A:A', 60)
        worksheet.set_column('B:K', 30)
        # worksheet.set_column(1, 1, 20)
        # worksheet.set_column()
        # worksheet.set_column(3, col, 30)
        # worksheet.freeze_panes(1, 0)  # Freeze the first row.

        col = 0
        row = 1
        #
        # self.create_rows_and_columns(worksheet, row, col, year, duration, name)

    def create_excel(self, name_of_file, test_type):
        print('Creating workbook')
        global workbook

        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook('Results/{}'.format(name_of_file))

        excel_format = workbook.add_format()
        excel_format.set_bold()
        excel_format.set_color('red')

        if test_type == 'Speeds':
            # t1 = time.perf_counter()
            # self.create_worksheets('Speed Test', excel_format)
            # t2 = time.perf_counter()
            # print('Speed Tests worksheet time taken: {:.2f}'.format(t2 - t1))
            #
            # t1 = time.perf_counter()
            # self.create_worksheets('Volume Test', excel_format)
            # t2 = time.perf_counter()
            # print('Volume Tests worksheet time taken: {:.2f}'.format(t2 - t1))

            with concurrent.futures.ThreadPoolExecutor() as executor:
                t1 = time.perf_counter()
                executor.submit(self.create_worksheets, 'Speed Test', excel_format)
                t2 = time.perf_counter()
                print('Speed Tests worksheet time taken: {:.2f}'.format(t2 - t1))

                t1 = time.perf_counter()
                executor.submit(self.create_worksheets, 'Volume Test', excel_format)
                t2 = time.perf_counter()
                print('Volume Tests worksheet time taken: {:.2f}'.format(t2 - t1))

        elif test_type == 'Remote':
            t1 = time.perf_counter()
            self.create_worksheets_remote('Remote Test', excel_format)
            t2 = time.perf_counter()
            print('Remote Work worksheet time taken: {:.2f}'.format(t2 - t1))

        workbook.close()
