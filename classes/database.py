import sqlite3
import time
from os.path import exists
import datetime


class Database(object):
    def __init__(self, username: str) -> None:
        self._username = username
        self._path = f'C:\\Users\\{self._username}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History'
        self._last_updated: int = None
        self.date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.set_last_updated()

        '''setting up sqlite connection to be done here'''
        c = sqlite3.connect(self._path, timeout=10)
        self.cursor = c.cursor()

    def get_date(self):
        return self.date

    def get_cursor(self):
        return self.cursor

    def update(self) -> None:
        '''To be overriden by children'''
        pass

    def chrome(self) -> bool:
        '''To check if Chrome is installed on the system'''
        return exists("C:\Program Files\Google\Chrome\Application\chrome.exe")

    def is_present(self) -> bool:
        '''To check if History is present in the system'''
        return exists(self._path)

    def get_path(self) -> str:
        return self._path

    def set_path(self, path: str) -> None:
        self._path = path

    def get_last_updated(self) -> int:
        return self._last_updated

    def set_last_updated(self) -> None:
        '''Assign current time in seconds since the epoch to last_updated\n
           Hint : Use gmtime() from datetime module'''
        self._last_updated = time.gmtime()
        with open('lu.txt', 'w') as lu:
            lu.write(self.date)
        

        
class Urls(Database):
    def __init__(self, username: str) -> None:
        self.db = Database(username)
        self._urls = [str]

    def get_urls(self) -> list[str]:
        return self._urls

    def update(self) -> None:
        '''run an sqlite query to store urls visited in urls list'''
        self._urls = [str]
        self._urls.clear()
        query = f"SELECT urls.url \
                    FROM visits, urls \
                    WHERE visits.url = urls.id \
                    AND datetime(visits.visit_time / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch') \
                    LIKE '{self.db.get_date()}%'"
        self.db.get_cursor().execute(query)
        for i in self.db.get_cursor().fetchall():
            if i[0].startswith('http'):
                self._urls.append(i[0])

    def get_domain(self, url: str) -> str:
        '''string slicing to get only the domain from url\n
           e.g. https://docs.python.org/3/library/time.html to https://docs.python.org/'''
        occurance = 0
        for pos, char in enumerate(url):
            if(char == '/'):
                occurance += 1
            if occurance == 3:
                break
        return url[:pos + 1]    

    def get_website_count(self) -> int:
        '''get total number of unique domains visited in a day'''
        return len(self.get_total_websites())

    def get_total_websites(self) -> list[str]:
        '''get a list of unique domains visited in a day'''
        for i, url in enumerate(self._urls):
            self._urls[i] = self.get_domain(url)
        return list(set(self._urls))


class Visits(Database):
    def __init__(self, username: str) -> None:
        self.db = Database(username)
        self._visits = {}

    def get_visits(self) -> dict():
        return self._visits

    def update(self) -> None:
        '''run an sqlite query to get number of visits on each domain in a day in a form of a dictionary'''
        self._visits = {}
        query = f"SELECT url, visit_count FROM urls where \
            datetime(last_visit_time / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch') \
                LIKE '{self.db.get_date()}%';"
        self.db.get_cursor().execute(query)
        count = 0
        for i in self.db.get_cursor().fetchall():
            if i[0].startswith('http'):
                self._visits[i[0]] = i[1]
            count += 1
            if count == 10:
                break


class Downloads(Database):
    def __init__(self, username: str) -> None:
        self.db = Database(username)
        self._downloads: list[str] = None

    def get_downloads(self) -> list[str]:
        return self._downloads

    def update(self) -> None:
        '''run an sqlite query to get a list of downloaded files in a day'''
        query = f"SELECT current_path \
                    FROM downloads \
                    WHERE datetime(end_time / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch') \
                    LIKE '{self.get_date()}%'"
        self.db.get_cursor().execute(query)
        for i in self.db.get_cursor().fetchall():
            self._downloads.append(i[0])


class Terms(Database):
    def __init__(self, username: str) -> None:
        self.db = Database(username)
        self._terms = list[str]

    def get_terms(self) -> list[str]:
        return list(set(self._terms))

    def update(self) -> None:
        '''run an sqlite query to get a list of terms searched in a day'''
        query = f"SELECT keyword_search_terms.term FROM keyword_search_terms, urls WHERE\
                        keyword_search_terms.url_id = urls.id \
                        AND datetime(urls.last_visit_time / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch') \
                        LIKE '{self.db.get_date()}%'"
        self.db.get_cursor().execute(query)
        self._terms = []
        for i in self.db.get_cursor().fetchall():
            self._terms.append(i[0])