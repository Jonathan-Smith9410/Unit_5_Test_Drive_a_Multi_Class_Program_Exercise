class Diary:
    # ... (rest of the Diary class code remains the same) ...

    def find_best_entry_for_reading_time(self, wpm, minutes):
        """
        Finds the single best entry that is readable within the given minutes at the given wpm.

        Returns:
            The title of the matching DiaryEntry instance, or None if no suitable entry is found.
        """
        max_words = wpm * minutes
        
        # 1. Filter entries to find those that are readable within the time limit.
        # 2. Sort the valid entries by word count in descending order.
        # 3. Return the title of the entry with the highest word count (longest one that fits).

        # Use a list comprehension to filter for valid entries first.
        # This prevents unnecessary sorting of invalid entries.
        valid_entries = [
            entry for entry in self._list_of_entries 
            if entry.count_words() <= max_words
        ]

        if not valid_entries:
            # Return None or raise an exception if no entries fit the criteria
            return None 

        # Sort the valid entries based on their word count in descending order.
        valid_entries.sort(key=lambda entry: entry.count_words(), reverse=True)

        # The first entry in the sorted list is the best fit.
        return valid_entries[0].title

    # ... (rest of the Diary class code remains the same) ...

    # with greentext removed

        max_words = wpm * minutes
        valid_entries = [
            entry for entry in self._list_of_entries 
            if entry.count_words() <= max_words
        ]
        if not valid_entries:
            return None 
        valid_entries.sort(key=lambda entry: entry.count_words(), reverse=True)
        return valid_entries[0].title