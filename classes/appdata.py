from classes.database import Downloads, Terms, Urls, Visits


class AppData(object):
    def __init__(self) -> None:
        pass

    def download(self) -> None:
        '''to be overriden by children'''
        pass

    def get_data(self) -> None:
        '''to be overriden by children'''
        pass


class NoOfWebsites(AppData, Urls):
    def __init__(self, username: str) -> None:
        super().__init__(username)
        self._no_of_websites: int = None

    def download(self) -> None:
        '''save the data into a file'''
        pass

    def get_data(self) -> None:
        '''call Urls.get_website_count() an store in no_of_websites'''
        pass


class MostVisitedWebsites(AppData. Visits):
    def __init__(self, username: str) -> None:
        super().__init__(username)
        self._most_visited_websites: list[str] = None

    def download(self) -> None:
        '''save the data into a file and save as a pie chart'''
        pass

    def get_data(self) -> None:
        '''call Visits.get_visits() and store top 5 in most_visited_websites\n
           create a pie chart\n
           update visits in week file(where number of visits in last 7 days is stored)'''
        pass


class VisitsInWeek(AppData):
    def __init__(self, username: str) -> None:
        super().__init__(username)
        self._visits_in_week: dict() = None

    def download(self) -> None:
        '''save the data into a file and save as a line plot'''
        pass

    def get_data(self) -> None:
        '''access visits in week file(where number of visits in last 7 days is stored) and store its data in visits_in_week\n
           create a line plot'''
        pass


class WebsiteVisits(AppData, Visits):
    def __init__(self, username: str) -> None:
        super().__init__(username)
        self._website_visits: dict() = None

    def download(self) -> None:
        '''save the data into a file and save as a bar plot'''
        pass

    def get_data(self) -> None:
        '''call Visits.get_visits() and store it in website_visits\n
           create a bar plot'''
        pass


class NoOfDownloads(AppData, Downloads):
    def __init__(self, username: str) -> None:
        super().__init__(username)
        self._no_of_downloads: int = None

    def download(self) -> None:
        '''save the data into a file'''
        pass

    def get_data(self) -> None:
        '''call Downloads.get_downloads() and store it in no_of_downloads'''
        pass


class TermsOfDay(AppData, Terms):
    def __init__(self, username: str) -> None:
        super().__init__(username)
        self._terms_of_day: list[str] = None

    def download(self) -> None:
        '''save the data into a file'''
        pass

    def get_data(self) -> None:
        '''call Terms.get_terms(), perform some stemming and store it in terms_of_day(max 10)'''
        pass