'''

### Regular Expressions (Regex) and Their Uses

Regular expressions are patterns used to match characters in a string. Below are some common regex sequences and their explanations with small examples:

1. **`\d`** → Matches any digit (0-9).
   - Example: `\d` in `"A3B"` → Matches `"3"`

2. **`\D`** → Matches any non-digit character.
   - Example: `\D` in `"7X9"` → Matches `"X"`

3. **`\s`** → Matches any whitespace character (space, tab, newline).
   - Example: `\s` in `"Hello World"` → Matches the space `" "`

4. **`\S`** → Matches any non-whitespace character.
   - Example: `\S` in `" "` (space) → No match
   - Example: `\S` in `"A B"` → Matches `"A"` and `"B"`

5. **`\w`** → Matches any alphanumeric character (letters and numbers).
   - Example: `\w` in `"Test_123"` → Matches `"T"`, `"e"`, `"s"`, `"t"`, `"1"`, `"2"`, `"3"`

6. **`\W`** → Matches any non-alphanumeric character.
   - Example: `\W` in `"Hello@World!"` → Matches `"@"` and `"!"`

7. **`\b`** → Matches a word boundary (position between a word and a non-word character).
   - Example: `\bHi\b` in `"Hi there"` → Matches `"Hi"`

8. **`\A`** → Matches the start of a string.
   - Example: `\AHello` in `"Hello World"` → Matches `"Hello"`

9. **`\Z`** → Matches the end of a string.
   - Example: `end\Z` in `"This is the end"` → Matches `"end"`

'''
