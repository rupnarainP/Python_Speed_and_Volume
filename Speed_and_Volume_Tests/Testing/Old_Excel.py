import xlsxwriter
import concurrent.futures
import time

data = ''


class Excel:

    @staticmethod
    def get_data(json_data):
        global data
        data = json_data

    @staticmethod
    def average_speeds(speeds):
        answer = 0
        total = 0

        for speed in speeds:
            answer += float(speed)
            total += 1

        answer = answer / total

        return '{:.2f}'.format(answer)

    @staticmethod
    def average_volumes(volumes):
        answer = 0
        total = 0

        for volume in volumes:
            answer += (float(volume) * 100)
            total += 1

        answer = answer / total

        return '{:.2f}'.format(answer)

    def speed_test_weeks_threading(self, worksheet, row, col, year, duration, speed_volume, data):
        # Data
        for country in data:
            for i in range(len(country['d'])):
                fixed = self.average_speeds(country[speed_volume[0]])
                mobile = self.average_speeds(country[speed_volume[1]])

                worksheet.write(row, col, year)
                worksheet.write(row, col + 1, country['n'])
                worksheet.write(row, col + 2, duration)
                worksheet.write(row, col + 3, fixed)
                worksheet.write(row, col + 4, mobile)

                worksheet.write(row, i + 5, '{} | {}'.format(country[speed_volume[0]][i], country[speed_volume[1]][i]))

            row += 1

    def speed_test_worksheet(self, worksheet, excel_format):
        print('Creating speed test worksheet')

        global data

        year = "2019/2020"
        duration = '{} weeks'.format(len(data[0]['d']))
        weeks = data[0]['d']

        columns = ["Year", "Country", "Duration", "Performance average (fixed) (Mbps)",
                   "Performance average (mobile) (Mbps)"]

        for week in weeks:
            columns.append('{}  (Fixed | Mobile) (Mbps)'.format(week))

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

            col = 0
            row = 1

            self.speed_test_weeks_threading(worksheet, row, col, year, duration, data)

            # with concurrent.futures.ThreadPoolExecutor() as executor:
            #     executor.submit(self.speed_test_weeks_threading, worksheet, row, col, year, duration, ['fd', 'md']
            #                     , data)

    def volume_worksheet(self, worksheet, excel_format):
        print('Creating volume worksheet')

        global data

        year = "2019/2020"
        duration = '{} weeks'.format(len(data[0]['d']))
        weeks = data[0]['d']

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

            col = 0
            row = 1

            # Data
            for country in data:
                for i in range(len(country['d'])):
                    fixed = self.average_volumes(country['fvc'])
                    mobile = self.average_volumes(country['mvc'])

                    worksheet.write(row, col, year)
                    worksheet.write(row, col + 1, country['n'])
                    worksheet.write(row, col + 2, duration)
                    worksheet.write(row, col + 3, fixed)
                    worksheet.write(row, col + 4, mobile)

                    worksheet.write(row, i + 5, '{:.2f} | {:.2f}'.format(float(country['fvc'][i] * 100),
                                                                         float(country['mvc'][i] * 100)))

                row += 1

    def create_excel(self):
        print('Creating workbook')

        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook('../Results/Internet Performance Tests.xlsx')
        worksheet = workbook.add_worksheet('Speed Tests')
        worksheet2 = workbook.add_worksheet('Volume Tests')

        excel_format = workbook.add_format()
        excel_format.set_bold()
        excel_format.set_color('red')

        t1 = time.perf_counter()
        self.speed_test_worksheet(worksheet, excel_format)
        t2 = time.perf_counter()
        print('Speed Tests worksheet time taken: {:.2f}'.format(t2 - t1))

        t1 = time.perf_counter()
        self.volume_worksheet(worksheet2, excel_format)
        t2 = time.perf_counter()
        print('Volume Tests worksheet time taken: {:.2f}'.format(t2 - t1))

        workbook.close()
