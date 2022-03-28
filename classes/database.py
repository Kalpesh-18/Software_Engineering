class Database(object):
    def __init__(self, username: str) -> None:
        self._username = username
        self._path = f'C:\Users\{self._username}\AppData\Local\Google\Chrome\User Data\Default\History'
        self._last_updated: int = None

        '''setting up sqlite connection is done here'''

    def update(self) -> None:
        '''To be overriden by children'''
        pass

    def chrome(self) -> bool:
        '''To check if Chrome is installed on the system'''
        pass

    def is_present(self) -> bool:
        '''To check if History is present in the system'''
        pass

    def get_path(self) -> str:
        return self._path

    def set_path(self, path: str) -> None:
        self._path = path

    def get_last_updated(self) -> int:
        return self._last_updated

    def set_last_updated(self) -> None:
        '''Assign current time in seconds since the epoch to last_updated\n
           Hint : Use gmtime() from datetime module'''
        pass

    
class Urls(Database):
    def __init__(self, username: str) -> None:
        super.__init__(username)
        self._urls = [str]

    def get_urls(self) -> list[str]:
        return self._urls

    def update(self) -> None:
        '''run an sqlite query to store urls visited in urls list'''
        pass

    def get_domain(self, url: str) -> str:
        '''string slicing to get only the domain from url\n
           e.g. https://docs.python.org/3/library/time.html to https://docs.python.org/'''
        pass

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