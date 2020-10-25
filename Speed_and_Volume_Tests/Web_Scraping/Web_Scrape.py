from bs4 import BeautifulSoup
import requests
import time
from _collections import defaultdict

source = ''


class Web_Scrape:

    # Setting the URL link
    @staticmethod
    def set_source(url):
        global source
        source = url

    # Getting the URL link
    @staticmethod
    def get_source():
        global source

        return source

    # Getting data from Ookla
    def speed_and_volume_data(self):
        print('Getting data from Ookla', end=' ')
        t1 = time.perf_counter()

        soup = self.get_data()

        java_script = soup.find_all('script', type='text/javascript')

        script = java_script[3]
        script = str(script)
        # print(script)
        # print(script[script.index('Afghanistan'): script.index('"PW5Z"') - 5])

        script = script[script.index('Afghanistan'): script.index('"PW5Z"') - 9]
        # script = json.dumps(script, sort_keys=True, indent=4)
        t2 = time.perf_counter()
        print('Time take to get data: {:.2f}'.format(t2 - t1))

        return script

    # Getting data from Ip Buffer and converting it to a JSON format
    def remote_work_data(self):
        print('Getting data from Ip.buffer')
        t1 = time.perf_counter()

        soup = self.get_data()

        count = 0
        partitioned_results = []
        names = defaultdict(list)
        key = ''

        for result in soup.find_all('div', class_='rich-text-block w-richtext'):
            count += 1

            if count == 2:
                for con in result:
                    con_string = str(con)

                    if con_string.__contains__('<p>'):
                        if con_string.__contains__('<strong>'):
                            key = str(con.strong.text)
                            key = key.strip()

                        elif con_string.__contains__('<p>'):
                            if key == '':
                                continue

                            partitioned_results.append(str(con.text).strip())

                            if key == 'Location by country':
                                names[key].append(partitioned_results)
                                partitioned_results = []

                            elif key == 'Industry breakdown':
                                names[key].append(partitioned_results)
                                partitioned_results = []

                            elif key == 'Work experience':
                                names[key].append(partitioned_results)
                                partitioned_results = []

                            elif key == 'Remote work experience':
                                names[key].append(partitioned_results)
                                partitioned_results = []

                    if con_string.__contains__('<ul role="list">'):
                        for li in con.find_all('li'):
                            if li:
                                partitioned_results.append(str(li.next).strip())

                        if len(partitioned_results) > 0:
                            names[key].append(partitioned_results)
                            partitioned_results = []

        t2 = time.perf_counter()
        print('Time take to get data: {:.2f}'.format(t2 - t1))

        return names

    # Web scraping component
    def get_data(self):

        try:
            link = requests.get(self.get_source())
            soup = BeautifulSoup(link.content.decode('utf-8'), 'lxml')

        except ConnectionError as error:
            print(error)

        return soup


