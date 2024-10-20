
import math


class PaginationManager:
    _pageIndex = 0

    def __init__(self, items: list, pageSize: int, repeating=True):
        self._options = items
        self._pageSize = pageSize
        self.pageCount = math.ceil(len(items) / pageSize)
        self._repeating = repeating

    def __resolveNextIndex(self, times: int):
        rawNext = self._pageIndex + times
        if self._repeating:
            return rawNext % self.pageCount

        return min(rawNext, len(self.pageCount) - 1)

    def move(self, times=1):
        nextIndex = self.__resolveNextIndex(times)
        self._pageIndex = nextIndex

    @property
    def currentPage(self):
        start = self._pageIndex * self._pageSize
        end = start + self._pageSize
        return self._options[start:end]
