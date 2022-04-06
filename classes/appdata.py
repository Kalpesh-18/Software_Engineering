from database import Downloads, Terms, Urls, Visits
import pandas as pd
import os
import datetime


class AppData(object):
    def __init__(self) -> None:
        if not os.path.exists('viw.csv'):
            viw = {'viw': [0, 0, 0, 0, 0, 0, 0]}
            pd.DataFrame(viw).to_csv('viw.csv')

    def download(self) -> None:
        '''to be overriden by children'''
        pass

    def get_data(self) -> None:
        '''to be overriden by children'''
        pass


class NoOfWebsites(AppData, Urls):
    def __init__(self, username: str) -> None:
        Urls.__init__(self, username)
        AppData.__init__(self)
        self._no_of_websites: int = None

    def download(self) -> None:
        '''save the data into a file'''
        pass

    def get_data(self) -> None:
        '''call Urls.get_website_count() and store in no_of_websites'''
        self.update()
        self._no_of_websites = self.get_website_count()
        with open('lu.txt', 'r') as lu:
            if lu.readline() != datetime.datetime.now().strftime("%Y-%m-%d"):
                df = pd.read_csv('viw.csv')
                viw = {'viw':df['viw'].tolist()}
                viw['viw'] = viw['viw'][1:]
                viw['viw'].append(self._no_of_websites)
                pd.DataFrame(viw).to_csv('viw.csv')
        return self._no_of_websites


class MostVisitedWebsites(AppData, Visits):
    def __init__(self, username: str) -> None:
        Visits.__init__(self, username)
        AppData.__init__(self)
        self._most_visited_websites: list[str] = None

    def download(self) -> None:
        '''save the data into a file and save as a pie chart'''
        pass

    def get_data(self) -> None:
        '''call Visits.get_visits() and store top 5 in most_visited_websites\n
           create a pie chart\n
           update visits in week file(where number of visits in last 7 days is stored)'''
        self.update()
        self._most_visited_websites = self.get_visits()
        return self._most_visited_websites


class VisitsInWeek(AppData):
    def __init__(self, username: str) -> None:
        AppData.__init__(self)
        self._visits_in_week: dict() = None

    def download(self) -> None:
        '''save the data into a file and save as a line plot'''
        pass

    def get_data(self) -> None:
        '''access visits in week file(where number of visits in last 7 days is stored) and store its data in visits_in_week\n
           create a line plot'''
        df = pd.read_csv('viw.csv')
        return df['viw'].tolist()


class WebsiteVisits(AppData, Visits):
    def __init__(self, username: str) -> None:
        Visits.__init__(self, username)
        AppData.__init__(self)
        self._website_visits: dict() = None

    def download(self) -> None:
        '''save the data into a file and save as a bar plot'''
        pass

    def get_data(self) -> None:
        '''call Visits.get_visits() and store it in website_visits\n
           create a bar plot'''
        self.update()
        self._website_visits = self.get_visits()
        return self._website_visits


class NoOfDownloads(AppData, Downloads):
    def __init__(self, username: str) -> None:
        Downloads.__init__(self, username)
        AppData.__init__(self)
        self._no_of_downloads: int = None

    def download(self) -> None:
        '''save the data into a file'''
        pass

    def get_data(self) -> None:
        '''call Downloads.get_downloads() and store it in no_of_downloads'''
        self.update()
        self._no_of_downloads = len(self.get_downloads())
        return self._no_of_downloads


class TermsOfDay(AppData, Terms):
    def __init__(self, username: str) -> None:
        Terms.__init__(self, username)
        AppData.__init__(self)
        self._terms_of_day: list[str] = None

    def download(self) -> None:
        '''save the data into a file'''
        pass

    def get_data(self) -> None:
        '''call Terms.get_terms(), perform some stemming and store it in terms_of_day(max 10)'''
        self.update()
        self._terms_of_day = self.get_terms()
        return self._terms_of_day[:10]


if __name__ == '__main__':
    now = NoOfWebsites('Chitrang')
    print(now.get_data())

    mvw = MostVisitedWebsites('Chitrang')
    print(mvw.get_data())

    viw = VisitsInWeek('Chitrang')
    print(viw.get_data())

    wv = WebsiteVisits('Chitrang')
    print(wv.get_data())

    nod = NoOfDownloads('Chitrang')
    print(wv.get_data())

    tod = TermsOfDay('Chitrang')
    print(tod.get_data())