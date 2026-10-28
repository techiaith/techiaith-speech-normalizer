#!/usr/bin/env python3
"""
Welsh Number Normalizer

Converts Welsh number words to digit form for WER calculation.
Handles both the decimal and traditional vigesimal counting systems,
ordinals, currency, and common units.

Usage:
    from techiaith.speech_normalizer.welsh_number_normalizer import WelshNumberNormalizer

    num_norm = WelshNumberNormalizer()
    num_norm("tri deg pump")    # → "35"
    num_norm("pymtheg ar hugain")  # → "35"
    num_norm("mil naw cant pedwar deg tri")  # → "1943"
"""

import re
from typing import Optional


# ============================================================================
# CARDINAL NUMBER WORDS
# ============================================================================

# Base numbers (masculine forms are default; feminine used in context)
# Includes soft mutation (SM), aspirate mutation (AM), and nasal mutation (NM)
UNITS = {
    "dim": 0, "sero": 0,
    "un": 1,
    "dau": 2, "dwy": 2,
    "ddau": 2, "ddwy": 2,                          # SM of dau/dwy
    "tri": 3, "tair": 3,
    "dri": 3, "dair": 3,                            # SM of tri/tair
    "thri": 3, "thair": 3,                          # AM of tri/tair
    "pedwar": 4, "pedair": 4,
    "bedwar": 4, "bedair": 4,                        # SM of pedwar/pedair
    "phedwar": 4, "phedair": 4,                      # AM of pedwar/pedair
    "pump": 5, "pum": 5,
    "bum": 5, "bump": 5,                            # SM of pum/pump
    "phum": 5, "phump": 5,                           # AM of pum/pump
    "chwech": 6, "chwe": 6,
    "saith": 7,
    "wyth": 8,
    "naw": 9,
    "nau": 9,                                        # SM of naw (after o/yn)
    "deg": 10, "deng": 10,
    "ddeg": 10, "ddeng": 10,                         # SM of deg/deng
    "un ar ddeg": 11, "un deg un": 11,
    "deuddeg": 12, "un deg dau": 12, "un deg dwy": 12,
}

TEENS = {
    "un ar ddeg": 11,
    "deuddeg": 12, "deuddeng": 12,
    "tri ar ddeg": 13, "tair ar ddeg": 13,
    "dri ar ddeg": 13, "dair ar ddeg": 13,           # SM
    "pedwar ar ddeg": 14, "pedair ar ddeg": 14,
    "bedwar ar ddeg": 14, "bedair ar ddeg": 14,       # SM
    "pymtheg": 15, "pymtheng": 15,
    "bymtheg": 15, "bymtheng": 15,                    # SM of pymtheg
    "un ar bymtheg": 16,
    "dau ar bymtheg": 17, "dwy ar bymtheg": 17,
    "ddau ar bymtheg": 17, "ddwy ar bymtheg": 17,     # SM
    "deunaw": 18, "ddeunaw": 18,                       # SM of deunaw
    "pedwar ar bymtheg": 19, "pedair ar bymtheg": 19,
    "bedwar ar bymtheg": 19, "bedair ar bymtheg": 19,  # SM
}

# Decimal tens (includes common mutated forms)
DECIMAL_TENS = {
    "un deg": 10,
    "dau ddeg": 20, "dwy ddeg": 20,
    "ddau ddeg": 20, "ddwy ddeg": 20,                 # SM
    "tri deg": 30, "tair deg": 30,
    "dri deg": 30, "dair deg": 30,                     # SM
    "thri deg": 30, "thair deg": 30,                   # AM
    "pedwar deg": 40, "pedair deg": 40,
    "bedwar deg": 40, "bedair deg": 40,                 # SM
    "phedwar deg": 40, "phedair deg": 40,               # AM
    "pum deg": 50, "bum deg": 50,                       # SM
    "phum deg": 50,                                     # AM
    "chwe deg": 60,
    "saith deg": 70,
    "wyth deg": 80,
    "naw deg": 90,
}

# Vigesimal multiples of 20
VIGESIMAL_TWENTIES = {
    "ugain": 20, "hugain": 20,
    "deugain": 40, "ddeugain": 40,                     # SM of deugain
    "trigain": 60, "drigain": 60,                       # SM of trigain
    "pedwar ugain": 80, "pedair ugain": 80,
    "bedwar ugain": 80, "bedair ugain": 80,             # SM
}

# Multipliers (with mutated forms)
MULTIPLIERS = {
    "cant": 100, "gant": 100,                          # gant = SM of cant
    "can": 100, "gan": 100,                             # reduced forms
    "mil": 1000, "fil": 1000,                           # fil = SM of mil
    "miliwn": 1_000_000, "filiwn": 1_000_000,           # SM of miliwn
    "biliwn": 1_000_000_000,
}

# ============================================================================
# ORDINAL WORDS
# ============================================================================

ORDINALS = {
    "cyntaf": "1af", "cynta": "1af",
    "gyntaf": "1af", "gynta": "1af",                    # SM of cyntaf
    "ail": "2il",
    "trydydd": "3ydd", "trydedd": "3edd",
    "drydydd": "3ydd", "drydedd": "3edd",                # SM of trydydd/trydedd
    "pedwerydd": "4ydd", "pedwaredd": "4edd",
    "bedwerydd": "4ydd", "bedwaredd": "4edd",             # SM of pedwerydd/pedwaredd
    "pumed": "5ed", "bumed": "5ed",                       # SM of pumed
    "chweched": "6ed",
    "seithfed": "7fed",
    "wythfed": "8fed",
    "nawfed": "9fed",
    "degfed": "10fed", "ddegfed": "10fed",                # SM of degfed
    "unfed ar ddeg": "11eg",
    "deuddegfed": "12fed",
    "trydydd ar ddeg": "13eg", "trydedd ar ddeg": "13eg",
    "drydydd ar ddeg": "13eg", "drydedd ar ddeg": "13eg",  # SM
    "pedwerydd ar ddeg": "14eg", "pedwaredd ar ddeg": "14eg",
    "bedwerydd ar ddeg": "14eg", "bedwaredd ar ddeg": "14eg",  # SM
    "pymthegfed": "15fed",
    "unfed ar bymtheg": "16eg",
    "ail ar bymtheg": "17eg",
    "deunawfed": "18fed",
    "pedwerydd ar bymtheg": "19eg",
    "bedwerydd ar bymtheg": "19eg",                        # SM
    "ugeinfed": "20fed",
    "unfed ar hugain": "21ain",
}

# ============================================================================
# CURRENCY
# ============================================================================

CURRENCY_UNITS = {
    "punt": "£", "bunt": "£", "phunt": "£",
    "ceiniog": "c",
}

# ============================================================================
# CONNECTOR WORDS (ignored during parsing)
# ============================================================================

CONNECTORS = {"a", "ac", "ar", "o"}


class WelshNumberNormalizer:
    """
    Converts Welsh number words to digit form.

    Supports:
    - Decimal system: tri deg pump → 35
    - Vigesimal system: pymtheg ar hugain → 35
    - Ordinals: trydydd → 3ydd
    - Currency: pum punt a deg ceiniog → £5.10
    - Multipliers: mil naw cant → 1900
    """

    def __init__(self):
        self._build_patterns()

    def __call__(self, text: str) -> str:
        return self.normalize(text)

    def normalize(self, text: str) -> str:
        """Convert Welsh number words in text to digits."""
        result = text
        result = self._normalize_currency(result)
        result = self._normalize_ordinals(result)
        result = self._normalize_cardinals(result)
        return result

    # ------------------------------------------------------------------ build
    def _build_patterns(self):
        # Build a combined vocabulary of all number-related words
        self._number_words = set()
        for d in [UNITS, TEENS, DECIMAL_TENS, VIGESIMAL_TWENTIES, MULTIPLIERS]:
            for phrase in d:
                for w in phrase.split():
                    self._number_words.add(w)
        self._number_words.update(CONNECTORS)

        # Ordinal patterns — sort longest first for greedy matching
        self._ordinal_keys = sorted(ORDINALS.keys(), key=len, reverse=True)
        self._ordinal_pattern = re.compile(
            r'\b(' + '|'.join(re.escape(k) for k in self._ordinal_keys) + r')\b',
            re.IGNORECASE,
        )

        # Currency pattern: e.g. "pum punt a deg ceiniog"
        currency_words = '|'.join(re.escape(w) for w in CURRENCY_UNITS)
        self._currency_pattern = re.compile(
            r'((?:[\w\s]+?)\s+(?:' + currency_words + r')(?:\s+(?:a|ac)\s+(?:[\w\s]+?)\s+(?:' + currency_words + r'))?)',
            re.IGNORECASE,
        )

    # -------------------------------------------------------------- currency
    def _normalize_currency(self, text: str) -> str:
        """Convert currency expressions like 'pum punt a deg ceiniog' → '£5.10'."""
        currency_words = {"punt", "bunt", "phunt", "ceiniog"}
        tokens = text.split()
        result_tokens = list(tokens)  # copy for modification
        i = 0

        while i < len(result_tokens):
            word = result_tokens[i].lower()
            if word not in currency_words or word == "ceiniog":
                i += 1
                continue

            # Found punt/bunt/phunt — look backwards for number phrase
            num_start = self._find_number_span_reverse(result_tokens, i)
            if num_start == i:
                i += 1
                continue

            num_phrase = ' '.join(result_tokens[num_start:i])
            pounds = self._words_to_number(num_phrase)
            if pounds is None:
                i += 1
                continue

            # Check for "a/ac X ceiniog" after
            pence = None
            pence_end = i + 1
            if (i + 1 < len(result_tokens) and
                    result_tokens[i + 1].lower() in ("a", "ac") and
                    i + 2 < len(result_tokens)):
                # Find ceiniog
                for j in range(i + 2, min(i + 9, len(result_tokens))):
                    if result_tokens[j].lower() == "ceiniog":
                        pence_phrase = ' '.join(result_tokens[i + 2:j])
                        pence = self._words_to_number(pence_phrase)
                        if pence is not None:
                            pence_end = j + 1
                        break

            if pence is not None:
                replacement = f"£{pounds}.{pence:02d}"
            else:
                replacement = f"£{pounds}"

            result_tokens[num_start:pence_end] = [replacement]
            i = num_start + 1

        return ' '.join(result_tokens)

    def _find_number_span_reverse(self, tokens: list, end: int) -> int:
        """Find the start of a number word span looking backwards from end."""
        i = end - 1
        has_number = False
        while i >= 0:
            word = tokens[i].lower()
            if word in self._number_words:
                if word not in CONNECTORS:
                    has_number = True
                i -= 1
            else:
                break
        start = i + 1
        # Don't start on a connector
        while start < end and tokens[start].lower() in CONNECTORS:
            start += 1
        return start if has_number else end

    # -------------------------------------------------------------- ordinals
    def _normalize_ordinals(self, text: str) -> str:
        """Convert ordinal words to digit form."""
        def replace_ordinal(m):
            key = m.group(1).lower()
            return ORDINALS.get(key, m.group(0))

        return self._ordinal_pattern.sub(replace_ordinal, text)

    # ------------------------------------------------------------- cardinals
    def _normalize_cardinals(self, text: str) -> str:
        """Find and replace sequences of number words with digits."""
        tokens = text.split()
        result = []
        i = 0

        while i < len(tokens):
            # Try to find the longest span of number words starting at i
            span_end = self._find_number_span(tokens, i)

            if span_end > i:
                number_phrase = ' '.join(tokens[i:span_end])
                value = self._words_to_number(number_phrase)
                if value is not None:
                    result.append(str(value))
                    i = span_end
                    continue

            result.append(tokens[i])
            i += 1

        return ' '.join(result)

    def _find_number_span(self, tokens: list, start: int) -> int:
        """Find the end index of a contiguous number word span."""
        i = start
        has_number_word = False

        while i < len(tokens):
            word = tokens[i].lower().rstrip('.,;:!?')
            if word in self._number_words:
                if word not in CONNECTORS:
                    has_number_word = True
                elif not has_number_word:
                    # Don't start a span with a connector
                    break
                i += 1
            else:
                break

        # Don't end on a connector
        while i > start and tokens[i - 1].lower().rstrip('.,;:!?') in CONNECTORS:
            i -= 1

        return i if has_number_word else start

    def _words_to_number(self, text: str) -> Optional[int]:
        """
        Parse a Welsh number phrase into an integer.

        Handles both decimal (tri deg pump = 35) and vigesimal
        (pymtheg ar hugain = 35) systems, plus multipliers
        (mil naw cant pedwar deg tri = 1943).
        """
        text = text.lower().strip()
        if not text:
            return None

        # Try direct lookups first (single tokens or known phrases)
        if text in UNITS:
            return UNITS[text]
        if text in TEENS:
            return TEENS[text]

        # Try vigesimal pattern: X ar hugain/deugain/trigain/pedwar ugain
        value = self._try_vigesimal(text)
        if value is not None:
            return value

        # Try decimal pattern: tri deg pump
        value = self._try_decimal(text)
        if value is not None:
            return value

        # Try with multipliers: mil naw cant pedwar deg tri
        value = self._try_with_multipliers(text)
        if value is not None:
            return value

        return None

    def _try_vigesimal(self, text: str) -> Optional[int]:
        """Parse vigesimal expressions like 'pymtheg ar hugain' (15+20=35)."""
        for vig_word, vig_value in VIGESIMAL_TWENTIES.items():
            # Pattern: "X ar hugain/deugain/etc"
            for connector in ["ar ", "a "]:
                suffix = connector + vig_word
                if text.endswith(suffix):
                    prefix = text[:-len(suffix)].strip()
                    if not prefix:
                        return vig_value
                    base = self._words_to_number(prefix)
                    if base is not None:
                        return base + vig_value

            # Pattern: just "ugain", "deugain", etc.
            if text == vig_word:
                return vig_value

        return None

    def _try_decimal(self, text: str) -> Optional[int]:
        """Parse decimal expressions like 'tri deg pump' (30+5=35)."""
        for dec_phrase, dec_value in DECIMAL_TENS.items():
            if text.startswith(dec_phrase):
                rest = text[len(dec_phrase):].strip()
                if not rest:
                    return dec_value
                unit = self._words_to_number(rest)
                if unit is not None and unit < 10:
                    return dec_value + unit

        return None

    def _try_with_multipliers(self, text: str) -> Optional[int]:
        """Parse expressions with multipliers: mil, cant, miliwn, biliwn."""
        words = text.split()
        total = 0
        current = 0
        i = 0

        while i < len(words):
            word = words[i]

            # Skip connectors
            if word in CONNECTORS:
                i += 1
                continue

            # Check for multi-word tens (e.g. "tri deg", "pedwar deg")
            if i + 1 < len(words):
                two_word = word + ' ' + words[i + 1]
                if two_word in DECIMAL_TENS:
                    current += DECIMAL_TENS[two_word]
                    i += 2
                    # Check for following unit
                    if i < len(words) and words[i] in UNITS and UNITS[words[i]] < 10:
                        current += UNITS[words[i]]
                        i += 1
                    continue
                if two_word in VIGESIMAL_TWENTIES:
                    current += VIGESIMAL_TWENTIES[two_word]
                    i += 2
                    continue

            # Check for teens (multi-word)
            matched_teen = False
            for teen_phrase, teen_val in sorted(TEENS.items(), key=lambda x: len(x[0]), reverse=True):
                teen_words = teen_phrase.split()
                if words[i:i + len(teen_words)] == teen_words:
                    current += teen_val
                    i += len(teen_words)
                    matched_teen = True
                    break
            if matched_teen:
                continue

            # Check for multipliers
            if word in MULTIPLIERS:
                mult = MULTIPLIERS[word]
                if current == 0:
                    current = 1
                if mult >= 1000:
                    total += current * mult
                    current = 0
                else:
                    current *= mult
                i += 1
                continue

            # Check for units
            if word in UNITS:
                current += UNITS[word]
                i += 1
                continue

            # Unrecognised word — bail
            return None

        total += current
        return total if total > 0 or text.strip() in ("dim", "sero") else None


def main():
    import sys
    import argparse

    parser = argparse.ArgumentParser(
        description='Welsh number normalizer - convert Welsh number words to digits',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Normalize number words in text
  python welsh_number_normalizer.py --text "tri deg pump"

  # Normalize an SRT file
  python welsh_number_normalizer.py --srt input.srt

  # Normalize an SRT file and save to output file
  python welsh_number_normalizer.py --srt input.srt --output output.srt

  # Normalize an SRT file keeping original text above normalized text
  python welsh_number_normalizer.py --srt input.srt --output output.srt --include-original
        '''
    )

    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument(
        '--text',
        type=str,
        help='Text containing Welsh number words to normalize'
    )
    input_group.add_argument(
        '--srt',
        type=str,
        help='Path to SRT file to normalize'
    )

    parser.add_argument(
        '--output', '-o',
        type=str,
        help='Output file path (only for SRT files)'
    )

    parser.add_argument(
        '--include-original',
        action='store_true',
        help='Include original text above normalized text in SRT output'
    )

    args = parser.parse_args()

    normalizer = WelshNumberNormalizer()

    if args.text:
        if args.output:
            print("Warning: --output is ignored for text input")

        normalized = normalizer.normalize(args.text)
        print("Original:")
        print(args.text)
        print("\nNormalized:")
        print(normalized)

    elif args.srt:
        try:
            with open(args.srt, 'r', encoding='utf-8') as f:
                content = f.read()

            normalized_lines = []
            lines = content.split('\n')
            i = 0

            while i < len(lines):
                line = lines[i].strip()

                if line.isdigit():
                    normalized_lines.append(line)
                    i += 1

                    if i < len(lines):
                        normalized_lines.append(lines[i].strip())
                        i += 1

                        subtitle_lines = []
                        while i < len(lines) and lines[i].strip():
                            subtitle_lines.append(lines[i])
                            i += 1

                        subtitle_text = '\n'.join(subtitle_lines)
                        normalized_text = normalizer.normalize(subtitle_text)

                        if args.include_original:
                            normalized_lines.append(subtitle_text)
                            normalized_lines.append(normalized_text)
                        else:
                            normalized_lines.append(normalized_text)

                        normalized_lines.append('')
                else:
                    i += 1

            result = '\n'.join(normalized_lines)

            if args.output:
                with open(args.output, 'w', encoding='utf-8') as f:
                    f.write(result)
                print(f"Normalized SRT file saved to: {args.output}")
            else:
                print("Normalized SRT content:")
                print(result)

        except FileNotFoundError:
            print(f"Error: File not found: {args.srt}")
            sys.exit(1)
        except Exception as e:
            print(f"Error processing SRT file: {e}")
            sys.exit(1)


if __name__ == '__main__':
    main()
