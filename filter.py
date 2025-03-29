class BadWordFilter:
    def __init__(self):
        """
        Initializes the BadWordFilter class with an empty list of bad words.
        """
        self.bad_words = []

    def configure_bad_words(self, file_path: str):
        """
        Reads a file containing bad words separated by colons and populates the bad_words list.

        Args:
            file_path (str): Path to the file containing bad words.
        """
        with open(file=file_path, mode="r") as text_file:
            bad_words_text = text_file.read().split(":")

            # Clean and strip each word, then add it to the bad_words list
            for word in bad_words_text:
                cleaned_word = word.strip()
                if cleaned_word:  # Avoid adding empty strings
                    self.bad_words.append(cleaned_word)

    def filter_text(
        self,
        text: str,
        remove_bad_word: bool = False,
        replace_with_star: bool = False,
        case_sensitive: bool = False,
    ) -> str:
        """
        Filters the given text by either removing bad words or replacing them with stars.

        Args:
            text (str): The input text to filter.
            remove_bad_word (bool): If True, removes bad words from the text.
            replace_with_star (bool): If True, replaces bad words with '***'.
            case_sensitive (bool): If False, the filtering will ignore case sensitivity.

        Returns:
            str: The filtered text.
        """
        # Ensure only one filtering option is active
        if remove_bad_word == replace_with_star:
            replace_with_star = True  # Default behavior

        filtered_text = text
        for bad_word in self.bad_words:
            if not case_sensitive:
                # Perform case-insensitive replacement
                filtered_text = self._replace_case_insensitive(
                    filtered_text, bad_word, "" if remove_bad_word else "***"
                )
            else:
                # Perform case-sensitive replacement
                if remove_bad_word:
                    filtered_text = filtered_text.replace(bad_word, "")
                else:
                    filtered_text = filtered_text.replace(bad_word, "***")

        return filtered_text

    def _replace_case_insensitive(
        self, text: str, bad_word: str, replacement: str
    ) -> str:
        """
        Helper method to replace bad words in a case-insensitive manner.

        Args:
            text (str): The input text.
            bad_word (str): The bad word to replace.
            replacement (str): The replacement string.

        Returns:
            str: The text with the bad word replaced.
        """
        import re

        # Use regex to perform case-insensitive replacement
        return re.sub(re.escape(bad_word), replacement, text, flags=re.IGNORECASE)
