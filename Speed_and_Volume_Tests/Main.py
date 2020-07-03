from Speed_Tests.Speed_Test import Speed_test
from Web_Scraping.Web_Scrape import Web_Scrape
import time
from EXCEL.Excel import Excel
# from test import Excel


class Main:
    t1 = time.perf_counter()
    file = Speed_test()
    scrape = Web_Scrape()
    excel = Excel()

    scrape.set_source('https://www.speedtest.net/insights/blog/tracking-covid-19-impact-global-internet-performance'
                          '/#/South%20Africa')

    json = scrape.speed_and_volume_data()
    json = file.translate_JSONArray2(json)
    jsonArray = file.convert_String_To_Json(json)

    excel.get_data(jsonArray)
    excel.create_excel('Internet Performance Tests.xlsx', 'Speeds')

    scrape.set_source('https://lp.buffer.com/state-of-remote-work-2020')

    remote = scrape.remote_work_data()
    jsonArray = file.remote_data_to_json(remote)

    # print(jsonArray['The Benefits and Struggles of Working Remotely'][0])

    excel.get_data(jsonArray)
    excel.create_excel('State of Remote Work.xlsx', 'Remote')
    t2 = time.perf_counter()
    print('Total time taken is: {:.2f}'.format(t2 - t1))

