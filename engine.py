import dataclasses
import logging
from typing import Optional

from googleapiclient.discovery import build


class GoogleEngine:
    SERVICE_NAME = "customsearch"

    SERVICE_VERSION = "v1"

    def __init__(self, api_key, cse_id, limit, exact_search):
        self._service = build(self.SERVICE_NAME, self.SERVICE_VERSION, developerKey=api_key)
        self._cse_id = cse_id
        self._limit = limit
        self._exact_search = exact_search

    def search_keywords(self, keywords, sites):
        search_results = []
        for keyword in keywords:
            for result in self.__site_search__(keyword, sites):
                search_results.append(result)
        return search_results

    def __site_search__(self, keyword, sites):
        for site in sites:
            logging.info(f'Search "{keyword}" in site: {site}')
            service_response = self._service.cse().list(
                q=f'site:{site} {keyword}',
                cx=self._cse_id,
                num=self._limit,
                exactTerms=keyword if self._exact_search else None
            ).execute()
            logging.debug(f"Google Custom Search Service Response:\n {service_response}")
            try:
                for item in service_response["items"]:
                    yield SearchResult(keyword, site,
                                       result=Result(item["title"], item["link"]))
            except KeyError:
                logging.warning(f'No Result found for {keyword} in site: {site}')
                yield SearchResult(keyword, site)


@dataclasses.dataclass
class SearchResult:
    keyword: str
    site: str
    result: Optional['Result'] = None


@dataclasses.dataclass
class Result:
    title: str
    link: str
