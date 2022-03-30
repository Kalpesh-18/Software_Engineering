import sqlite3
import time
from os.path import exists


class Database(object):
    def __init__(self, username: str) -> None:
        self._username = username
        self._path = f'C:\Users\{self._username}\AppData\Local\Google\Chrome\User Data\Default\History'
        self._last_updated: int = None

        '''setting up sqlite connection to be done here'''
        c = sqlite3.connect(self._path, timeout=10)
        self._cursor = c.cursor()

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

        
class Urls(Database):
    def __init__(self, username: str) -> None:
        super.__init__(username)
        self._urls = [str]

    def get_urls(self) -> list[str]:
        return self._urls

    def update(self) -> None:
        '''run an sqlite query to store urls visited in urls list'''
        self._urls.clear()
        query = "SELECT DISTINCT url FROM urls;"
        self._cursor.execute(query)
        for i in self._cursor.fetchall():
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
        pass

    def get_total_websites(self) -> list[str]:
        '''get a list of unique domains visited in a day'''
        pass


class Visits(Database):
    def __init__(self, username: str) -> None:
        super().__init__(username)
        self._visits: dict() = None

    def get_visits(self) -> dict():
        return self._visits

    def update(self) -> None:
        '''run an sqlite query to get number of visits on each domain in a day in a form of a dictionary'''
        pass


class Downloads(Database):
    def __init__(self, username: str) -> None:
        super().__init__(username)
        self._downloads: list[str] = None

    def get_downloads(self) -> list[str]:
        return self._downloads

    def update(self) -> None:
        '''run an sqlite query to get a list of downloaded files in a day'''
        pass


class Terms(Database):
    def __init__(self, username: str) -> None:
        super().__init__(username)
        self._terms: list[str] = None

    def get_terms(self) -> list[str]:
        return self._terms

    def update(self) -> None:
        '''run an sqlite query to get a list of terms searched in a day'''
        pass
