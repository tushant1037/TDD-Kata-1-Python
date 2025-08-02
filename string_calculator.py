import re

class StringCalculator:
    def Add(self, numbers: str) -> int:
        if not numbers:
            return 0
        parts = re.split(r'[,\n]', numbers)
        return sum(int(part) for part in parts if part)
