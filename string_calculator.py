import re

class StringCalculator:
    def Add(self, numbers: str) -> int:
        if not numbers:
            return 0
        delimiter_pattern = r"[,\n]"

        if numbers.startswith("//"):
            delimiter_section, numbers = numbers.split('\n', 1)
            custom_delimiter = delimiter_section[2:]
            delimiter_pattern = re.escape(custom_delimiter)

        parts = re.split(delimiter_pattern, numbers)
        nums = [int(part) for part in parts if part]

        negatives = [n for n in nums if n < 0]
        if negatives:
            raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")

        return sum(nums)