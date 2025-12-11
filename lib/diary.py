# File: lib/diary.py

class Diary:
    def __init__(self):
        self._list_of_entries = []

    def add(self, entry):
        self.entry = entry
        self._list_of_entries.append(self.entry)

    def all(self):
        return [self.entry.title for self.entry in self._list_of_entries]

    def count_words(self):
        return sum(self.entry.count_words() for self.entry in self._list_of_entries)

    def reading_time(self, wpm):
        self.wpm = wpm
        return int(sum(self.entry.reading_time(self.wpm) for self.entry in self._list_of_entries))

    def find_best_entry_for_reading_time(self, wpm, minutes):
        self._total_words = wpm * minutes
        self._entry_dict = {}
        for self.entry in self._list_of_entries:
            if self.entry.count_words() > self._total_words:
                continue
            self._entry_dict[self.entry.reading_time(wpm)] = self.entry.title
        self._sorted_dict = dict(sorted(self._entry_dict.items(), key=lambda item: item[0], reverse=True)) 
        return self._sorted_dict[next(iter(self._sorted_dict))]


