from Speed_Tests.Speed_Test import Speed_test
from Web_Scraping.Web_Scrape import Web_Scrape
from Enums import Enum
import time
from EXCEL.Excel import Excel
# from test import Excel


class Main:
    t1 = time.perf_counter()
    file = Speed_test()
    scrape = Web_Scrape()
    excel = Excel()

    # Set Ookla data source
    scrape.set_source(Enum.Urls.Ookla.value)

    # Get Ookla data
    json = scrape.speed_and_volume_data()
    # Transform data into a Json array
    json = file.translate_JSONArray2(json)
    # Convert data to Json
    jsonArray = file.convert_String_To_Json(json)

    # Set Json data to the Excel class
    excel.get_data(jsonArray)
    # Create the Excel spreadsheet
    excel.create_excel(Enum.FileName.SpeedAndVolume.value, Enum.FileType.Speed.value)

    # Set Remote work data source
    scrape.set_source(Enum.Urls.IpBuffer.value)
    # Get Remote work data and transform into a Json format
    remote = scrape.remote_work_data()
    jsonArray = file.remote_data_to_json(remote)

    # print(jsonArray['The Benefits and Struggles of Working Remotely'][0])

    # Set Json data to the Excel class
    excel.get_data(jsonArray)
    # Create the Excel spreadsheet
    excel.create_excel(Enum.FileName.Remote.value, Enum.FileType.Remote.value)

    t2 = time.perf_counter()
    print('Total time taken is: {:.2f}'.format(t2 - t1))

# Need to add a function to separate developed vs developing countries
