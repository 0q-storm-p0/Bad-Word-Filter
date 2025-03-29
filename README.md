# Bad Word Filter

A simple Python library to filter out inappropriate language from text, with configurable sensitivity and replacement options.

## Features

- 🚫 Configurable list of bad words from a text file
- 🔤 Case-sensitive or case-insensitive filtering
- ✨ Option to replace bad words with stars (`***`) or remove them completely
- 🐍 Lightweight and easy to integrate

## Installation

Simply include the `filter.py` file in your project directory.

## Usage

1. Create a text file with bad words separated by colons (example: `badWords.txt`)
2. Use the filter in your Python code:

```python
from filter import BadWordFilter

# Initialize and configure
filter = BadWordFilter()
filter.configure_bad_words("badWords.txt")

# Filter text
clean_text = filter.filter_text("Some inappropriate content here", replace_with_star=True)
print(clean_text)
```

## Configuration Options

Customize the filtering behavior with these parameters:

| Parameter           | Description                                                                  | Default |
| ------------------- | ---------------------------------------------------------------------------- | ------- |
| `case_sensitive`    | Set to `True` for exact case matching                                        | `False` |
| `replace_with_star` | Replace bad words with `***`                                                 | `True`  |
| `remove_bad_word`   | Completely remove bad words (overrides `replace_with_star` if both are True) | `False` |

## Example

**badWords.txt:**

```
Fuck : Porn : Bitch
```

**Code:**

```python
text = "This text contains FUCK and bitch"
filtered = filter.filter_text(text, case_sensitive=False)
print(filtered)
```

**Output:**

```
This text contains *** and ***
```

## Edge Cases Handled

- Empty bad words in the list are automatically skipped
- Maintains original spacing when words are removed
- Properly handles special characters in bad words

## Contributing

Contributions are welcome! Here are some potential improvements:

- Add support for regular expressions in bad words
- Implement a whitelist feature
- Add multilingual support

## License

MIT License - free for personal and commercial use.

```

This README:
- Has a clean, professional look with emojis for visual appeal
- Includes all key sections (Features, Installation, Usage, Configuration, Example)
- Shows code examples with proper formatting
- Uses markdown tables for parameter documentation
- Mentions edge cases to show robustness
- Suggests contribution ideas to encourage collaboration
- Is concise but covers all important aspects

You can copy this exactly as-is into your `README.md` file. The markdown formatting will render nicely on GitHub/GitLab.
```
