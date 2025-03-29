from filter import BadWordFilter

# Initialize the BadWordFilter class
filter_instance = BadWordFilter()

# Configure the bad words list by providing a file
filter_instance.configure_bad_words("badWords.txt")

# Example text to filter
text_to_filter = "This text is for testing: FUck you"

# Case-insensitive filtering (default behavior)
filtered_text = filter_instance.filter_text(
    text=text_to_filter, case_sensitive=False, replace_with_star=True
)
print(filtered_text)  # Output: This text is for testing: *** you

# Case-sensitive filtering
filtered_text_case_sensitive = filter_instance.filter_text(
    text=text_to_filter, case_sensitive=True
)
print(filtered_text_case_sensitive)  # Output: This text is for testing: FUck you
