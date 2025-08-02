import re

class StringCalculator:
    def Add(self, numbers: str) -> int:
        if not numbers:
            return 0
        delimiter_pattern = r"[,\n]"

        if numbers.startswith("//"):
            delimiter_section, numbers = numbers.split('\n', 1)

            custom_delimiters = re.findall(r"\[(.*?)\]", delimiter_section)
            if custom_delimiters:
                escaped = [re.escape(d) for d in custom_delimiters]
                delimiter_pattern = '|'.join(escaped)
            else:
                delimiter = delimiter_section[2:]
                delimiter_pattern = re.escape(delimiter)

        parts = re.split(delimiter_pattern, numbers)
        nums = [int(part) for part in parts if part]

        negatives = [n for n in nums if n < 0]
        if negatives:
            raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")

        return sum(n for n in nums if n <= 1000)
