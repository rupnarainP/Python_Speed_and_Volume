import xlsxwriter
import concurrent.futures
import time
from API import Calculation_API as calculationApi
from Enums import Enum
from Enums import Enum_Excel

data = ''
workbook = ''


class Excel:

    @staticmethod
    def get_data(json_data):
        global data
        data = json_data

    def create_rows_and_columns_speeds(self, worksheet, worksheet2, worksheet3, row, col, year, duration, data):
        row2 = row
        row3 = row

        for country in data:
            fixed = calculationApi.average_speeds(country['fd'])
            mobile = calculationApi.average_speeds(country['md'])

            worksheet.write(row, col, year)
            worksheet.write(row, col + 1, country['n'])
            worksheet.write(row, col + 2, duration)
            worksheet.write(row, col + 3, fixed)
            worksheet.write(row, col + 4, mobile)

            count = 0

            for i in range(0, len(country['d']), 2):
                worksheet.write(row, i + 5, '{}'.format(country['fd'][count]))
                worksheet.write(row, i + 6, '{}'.format(country['md'][count]))
                count += 1

            row += 1

            if country['n'] == 'Australia' or \
                    country['n'] == 'Austria' or \
                    country['n'] == 'Belgium' or \
                    country['n'] == 'Canada' or \
                    country['n'] == 'Cyprus' or \
                    country['n'] == 'Czechia' or \
                    country['n'] == 'Denmark' or \
                    country['n'] == 'Estonia' or \
                    country['n'] == 'Finland' or \
                    country['n'] == 'France' or \
                    country['n'] == 'Germany' or \
                    country['n'] == 'Greece' or \
                    country['n'] == 'Hungary' or \
                    country['n'] == 'Hong Kong (SAR)' or \
                    country['n'] == 'Ireland' or \
                    country['n'] == 'Israel' or \
                    country['n'] == 'Italy' or \
                    country['n'] == 'Japan' or \
                    country['n'] == 'Latvia' or \
                    country['n'] == 'Lithuania' or \
                    country['n'] == 'Luxembourg' or \
                    country['n'] == 'Macau (SAR)' or \
                    country['n'] == 'Netherlands' or \
                    country['n'] == 'New Zealand' or \
                    country['n'] == 'Norway' or \
                    country['n'] == 'Portugal' or \
                    country['n'] == 'Singapore' or \
                    country['n'] == 'Slovakia' or \
                    country['n'] == 'Slovenia' or \
                    country['n'] == 'Spain' or \
                    country['n'] == 'Sweden' or \
                    country['n'] == 'Switzerland' or \
                    country['n'] == 'Taiwan' or \
                    country['n'] == 'United Kingdom' or \
                    country['n'] == 'United States':
                worksheet2.write(row2, col, year)
                worksheet2.write(row2, col + 1, country['n'])
                worksheet2.write(row2, col + 2, duration)
                worksheet2.write(row2, col + 3, fixed)
                worksheet2.write(row2, col + 4, mobile)

                count = 0
                for j in range(0, len(country['d']), 2):
                    worksheet2.write(row2, j + 5, '{}'.format(country['fd'][count]))
                    worksheet2.write(row2, j + 6, '{}'.format(country['md'][count]))
                    count += 1

                row2 += 1

            else:
                worksheet3.write(row3, col, year)
                worksheet3.write(row3, col + 1, country['n'])
                worksheet3.write(row3, col + 2, duration)
                worksheet3.write(row3, col + 3, fixed)
                worksheet3.write(row3, col + 4, mobile)

                count = 0
                for g in range(0, len(country['d']), 2):
                    worksheet3.write(row3, g + 5, '{}'.format(country['fd'][count]))
                    worksheet3.write(row3, g + 6, '{}'.format(country['md'][count]))
                    count += 1

                row3 += 1

    def create_rows_and_columns_volume(self, worksheet, worksheet2, worksheet3, row, col, year, duration, data):
        row2 = row
        row3 = row

        for country in data:
            fixed = calculationApi.average_volumes(country['fvc'])
            mobile = calculationApi.average_volumes(country['mvc'])

            worksheet.write(row, col, year)
            worksheet.write(row, col + 1, country['n'])
            worksheet.write(row, col + 2, duration)
            worksheet.write(row, col + 3, fixed)
            worksheet.write(row, col + 4, mobile)

            count = 0
            for i in range(0, len(country['d']), 2):
                worksheet.write(row, i + 5, '{:.2f}'.format(float(country['fvc'][count] * 100)))
                worksheet.write(row, i + 6, '{:.2f}'.format(float(country['mvc'][count] * 100)))
                count += 1

            row += 1

            if country['n'] == 'Australia' or \
                    country['n'] == 'Austria' or \
                    country['n'] == 'Belgium' or \
                    country['n'] == 'Canada' or \
                    country['n'] == 'Cyprus' or \
                    country['n'] == 'Czechia' or \
                    country['n'] == 'Denmark' or \
                    country['n'] == 'Estonia' or \
                    country['n'] == 'Finland' or \
                    country['n'] == 'France' or \
                    country['n'] == 'Germany' or \
                    country['n'] == 'Greece' or \
                    country['n'] == 'Hungary' or \
                    country['n'] == 'Hong Kong (SAR)' or \
                    country['n'] == 'Ireland' or \
                    country['n'] == 'Israel' or \
                    country['n'] == 'Italy' or \
                    country['n'] == 'Japan' or \
                    country['n'] == 'Latvia' or \
                    country['n'] == 'Lithuania' or \
                    country['n'] == 'Luxembourg' or \
                    country['n'] == 'Macau (SAR)' or \
                    country['n'] == 'Netherlands' or \
                    country['n'] == 'New Zealand' or \
                    country['n'] == 'Norway' or \
                    country['n'] == 'Portugal' or \
                    country['n'] == 'Singapore' or \
                    country['n'] == 'Slovakia' or \
                    country['n'] == 'Slovenia' or \
                    country['n'] == 'Spain' or \
                    country['n'] == 'Sweden' or \
                    country['n'] == 'Switzerland' or \
                    country['n'] == 'Taiwan' or \
                    country['n'] == 'United Kingdom' or \
                    country['n'] == 'United States':
                worksheet2.write(row2, col, year)
                worksheet2.write(row2, col + 1, country['n'])
                worksheet2.write(row2, col + 2, duration)
                worksheet2.write(row2, col + 3, fixed)
                worksheet2.write(row2, col + 4, mobile)

                count = 0
                for p in range(0, len(country['d']), 2):
                    worksheet2.write(row2, p + 5, '{:.2f}'.format(float(country['fvc'][count] * 100)))
                    worksheet2.write(row2, p + 6, '{:.2f}'.format(float(country['mvc'][count] * 100)))
                    count += 1

                row2 += 1

            else:
                worksheet3.write(row3, col, year)
                worksheet3.write(row3, col + 1, country['n'])
                worksheet3.write(row3, col + 2, duration)
                worksheet3.write(row3, col + 3, fixed)
                worksheet3.write(row3, col + 4, mobile)

                count = 0
                for o in range(0, len(country['d']), 2):
                    worksheet3.write(row3, o + 5, '{:.2f}'.format(float(country['fvc'][count] * 100)))
                    worksheet3.write(row3, o + 6, '{:.2f}'.format(float(country['mvc'][count] * 100)))
                    count += 1

                row3 += 1

    def create_rows_and_columns(self, worksheet, worksheet2, worksheet3, row, col, year,
                                duration, name):
        global data

        # Data
        # Creating the speeds spreadsheets for global, developed and developing countries
        if name == Enum_Excel.Spreadsheet_name.SPEED_TEST_GLOBAL.value:
            self.create_rows_and_columns_speeds(worksheet, worksheet2, worksheet3, row, col, year, duration, data)

        # Creating the volume spreadsheets for global, developed and developing countries
        elif name == Enum_Excel.Spreadsheet_name.VOLUME_TEST_GLOBAL.value:
            self.create_rows_and_columns_volume(worksheet, worksheet2, worksheet3, row, col, year, duration, data)

    # Setting the column attributes for the Internet Performance spreadsheets
    @staticmethod
    def set_worksheet_attributes(worksheet, col):
        worksheet.set_column(0, 0, 10)
        worksheet.set_column(1, 1, 20)
        worksheet.set_column(3, col, 30)
        worksheet.freeze_panes(1, 0)  # Freeze the first row.

        return worksheet

    # init method to create the Internet Performance spreadsheets
    def create_worksheets(self, name, excel_format):
        global data, worksheet, worksheet2, worksheet3
        global workbook

        if name == Enum_Excel.Spreadsheet_name.SPEED_TEST_GLOBAL.value:
            print('Creating speed test worksheet ')
            worksheet = workbook.add_worksheet(name)
            worksheet2 = workbook.add_worksheet(Enum_Excel.Spreadsheet_name.SPEED_TEST_DEVELOPED.value)
            worksheet3 = workbook.add_worksheet(Enum_Excel.Spreadsheet_name.SPEED_TEST_DEVELOPING.value)

        elif name == Enum_Excel.Spreadsheet_name.VOLUME_TEST_GLOBAL.value:
            print('Creating volume test worksheet ')
            worksheet = workbook.add_worksheet(name)
            worksheet2 = workbook.add_worksheet(Enum_Excel.Spreadsheet_name.VOLUME_TEST_DEVELOPED.value)
            worksheet3 = workbook.add_worksheet(Enum_Excel.Spreadsheet_name.VOLUME_TEST_DEVELOPING.value)


        year = "2019/2020"
        duration = '{} weeks'.format(len(data[0]['d']))
        weeks = data[0]['d']
        columns = []

        if name == Enum_Excel.Spreadsheet_name.SPEED_TEST_GLOBAL.value:
            columns = ["Year", "Country", "Duration", "Performance average (fixed) (Mbps)",
                       "Performance average (mobile) (Mbps)"]

            for week in weeks:
                columns.append('{}  (Fixed) (Mbps)'.format(week))
                columns.append('{}  (Mobile) (Mbps)'.format(week))

        elif name == Enum_Excel.Spreadsheet_name.VOLUME_TEST_GLOBAL.value:
            columns = ["Year", "Country", "Duration", "Volume average (fixed) (%)",
                       "Volume average (mobile) (%)"]

            for week in weeks:
                columns.append('{}  (Fixed) (%)'.format(week))
                columns.append('{}  (Mobile) (%)'.format(week))

        # Start from the first cell. Rows and columns are zero indexed.
        row = 0
        col = 0

        # Header
        for column in columns:
            worksheet.write(row, col, column, excel_format)
            worksheet2.write(row, col, column, excel_format)
            worksheet3.write(row, col, column, excel_format)

            col += 1

        worksheet = self.set_worksheet_attributes(worksheet, col)
        worksheet2 = self.set_worksheet_attributes(worksheet2, col)
        worksheet3 = self.set_worksheet_attributes(worksheet3, col)

        col = 0
        row = 1

        self.create_rows_and_columns(worksheet, worksheet2, worksheet3, row, col, year,
                                     duration, name)

    # init method to create the Remote work spreadsheet
    def create_worksheets_remote(self, name, excel_format):
        if name == Enum_Excel.Spreadsheet_name.REMOTE_TEST.value:
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

    # Creating the Excel workbooks and start of the process
    def create_excel(self, name_of_file, test_type):
        print('Creating workbook')
        global workbook

        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook('Results/{}'.format(name_of_file))

        excel_format = workbook.add_format()
        excel_format.set_bold()
        excel_format.set_color('red')

        if test_type == Enum.FileType.Speed.value:
            # t1 = time.perf_counter()
            # self.create_worksheets('Speed Test', excel_format)
            # t2 = time.perf_counter()
            # print('Speed Tests worksheet time taken: {:.2f}'.format(t2 - t1))
            #
            # t1 = time.perf_counter()
            # self.create_worksheets('Volume Test', excel_format)
            # t2 = time.perf_counter()
            # print('Volume Tests worksheet time taken: {:.2f}'.format(t2 - t1))

            t1 = time.perf_counter()
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.submit(self.create_worksheets, Enum_Excel.Spreadsheet_name.SPEED_TEST_GLOBAL.value, excel_format)

            t2 = time.perf_counter()
            print('Speed Tests worksheet time taken: {:.2f}'.format(t2 - t1))

            t1 = time.perf_counter()
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.submit(self.create_worksheets, Enum_Excel.Spreadsheet_name.VOLUME_TEST_GLOBAL.value, excel_format)

            t2 = time.perf_counter()
            print('Volume Tests worksheet time taken: {:.2f}'.format(t2 - t1))

        elif test_type == Enum.FileType.Remote.value:
            t1 = time.perf_counter()
            self.create_worksheets_remote(Enum_Excel.Spreadsheet_name.REMOTE_TEST.value, excel_format)
            t2 = time.perf_counter()
            print('Remote Work worksheet time taken: {:.2f}'.format(t2 - t1))

        workbook.close()
