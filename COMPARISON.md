# WelshNormalizer vs. Whisper Text Normalizers: Comparison & Future Work

## Overview

This document compares `techiaith.speech_normalizer.WelshNormalizer` with OpenAI's Whisper text normalization classes: `BasicTextNormalizer` and `EnglishTextNormalizer`. The goal is to assess whether WelshNormalizer occupies the same role for Welsh that EnglishTextNormalizer does for English.

## Whisper's Normalizers

### BasicTextNormalizer (language-agnostic)

A minimal, language-agnostic normalizer that prepares text for WER (Word Error Rate) comparison. Its pipeline:

1. **Lowercasing**
2. **Annotation removal** — strips text within `<...>`, `[...]`, and `(...)`
3. **Unicode normalization** — NFKD (with diacritic removal) or NFKC (preserving diacritics)
4. **Symbol/punctuation stripping** — replaces all Unicode Mark, Symbol, and Punctuation characters with spaces
5. **Optional grapheme splitting** — splits into individual grapheme clusters
6. **Whitespace collapsing**

This normalizer performs no linguistic transformations — no contraction expansion, no spelling correction, no number handling. It is purely a text-cleaning pass.

### EnglishTextNormalizer (English-specific)

A linguistically-aware normalizer for English speech transcription. Its pipeline:

1. **Lowercasing**
2. **Annotation removal** — same as BasicTextNormalizer
3. **Filler word removal** — removes `hmm`, `mm`, `mhm`, `mmm`, `uh`, `um`
4. **Contraction expansion** — 40+ patterns (`won't` → `will not`, `gonna` → `going to`, `'re` → `are`, etc.)
5. **Abbreviation expansion** — titles and honorifics (`mr` → `mister`, `dr` → `doctor`, `prof` → `professor`, etc.)
6. **Number-to-digit conversion** — a complex stateful sliding-window parser handling:
   - Cardinal and ordinal numbers (`twenty million` → `20000000`, `third` → `3rd`)
   - Currency (`twenty dollars` → `$20`, combining dollars and cents)
   - Decimals (`three point five` → `3.5`)
   - Nominal sequences (`double oh seven` → `007`)
   - Percentage (`fifty percent` → `50%`)
7. **British → American spelling** — dictionary lookup from a JSON file
8. **Symbol cleanup and whitespace collapsing**

## Feature-by-Feature Comparison

| Capability | BasicText | EnglishText | WelshNormalizer |
|---|:---:|:---:|:---:|
| Lowercasing | Yes | Yes | Optional toggle |
| Remove annotations/tags | `<>` `[]` `()` | `<>` `[]` `()` | `<>` tags |
| Unicode normalization (NFKD/NFKC) | Yes | Yes | Yes (NFKC) |
| Strip all punctuation/symbols | Yes | Selective | Optional toggle |
| Hesitation/filler removal | No | Yes | Yes |
| Hesitation standardization | No | No | Yes |
| Contraction expansion | No | ~40 patterns | ~130+ patterns |
| Pronoun normalization | No | No | Yes |
| Dialect → standard spelling | No | British → American | Dialect → Standard Welsh |
| Number-to-digit parsing | No | Yes (complex) | Yes (decimal, vigesimal, mutated forms) |
| Currency normalization | No | Yes | Yes (punt/ceiniog) |
| Abbreviation expansion (titles) | No | Yes | No |
| Multi-word phrase correction | No | No | Yes |
| Context-aware transforms | No | Partial | Yes |
| Uncertainty flagging | No | No | Yes |
| Per-category toggles | Minimal | No | Yes (22 toggles) |
| SRT subtitle file support | No | No | Yes |
| Custom user corrections | No | No | Yes |
| False start removal | No | No | Yes |
| Hyphenated compound joining | No | No | Optional toggle |

## Where WelshNormalizer Matches or Exceeds

### Contraction and dialect handling

EnglishTextNormalizer handles approximately 40 contraction patterns. WelshNormalizer handles 130+ across multiple categories: pronouns, verb contractions, `mae` contractions, other contractions, dialectal plurals (North `-a` and South `-e` → standard `-au`), dialectal verbs, internal vowel reductions, and spelling corrections. This reflects the greater distance between spoken and written Welsh compared to English.

### Context-sensitive rules

Whisper's English normalizer uses ordered regex patterns to disambiguate contractions (e.g., matching `'d been` → `had been` before the generic `'d` → `would`). WelshNormalizer implements explicit contextual logic:

- **`'di` → `wedi`** only when preceded by a pronoun (`dwi 'di` → `dwi wedi`), left unchanged otherwise
- **`ma'` + follower** normalization using a lookup table that normalizes both `ma'` and its following word together

These are genuinely context-sensitive transformations that go beyond pattern ordering.

### Uncertainty flagging

WelshNormalizer flags ambiguous cases for human review rather than guessing. For example, `'di` without a preceding pronoun is flagged as `CONTEXT_UNCERTAIN`. Whisper's normalizers have no equivalent — they always produce a deterministic output with no indication of confidence.

### Configurability

Whisper's normalizers are essentially all-or-nothing (`BasicTextNormalizer` has two boolean options; `EnglishTextNormalizer` has none). WelshNormalizer offers 18 independent toggles, allowing researchers to measure the impact of each normalization category on downstream tasks like WER calculation.

### Additional features

- **SRT file processing** — direct support for normalizing subtitle files
- **Custom corrections** — users can supply their own single-word and multi-word replacements
- **False start removal** — removes truncated words (`m-`, `o-`) common in spontaneous speech

## Where WelshNormalizer Falls Short

### ~~1. Unicode normalization~~ (DONE)

NFKC normalization is now applied as the first step in the pipeline, ensuring circumflexed vowels (`ŵ`, `â`, etc.) match lookup tables regardless of encoding.

### ~~2. Number handling~~ (DONE)

A separate `WelshNumberNormalizer` class now handles:

- **Decimal system**: `tri deg pump` → `35`
- **Vigesimal system**: `pymtheg ar hugain` → `35`
- **Teens**: `un ar ddeg` → `11`, `deunaw` → `18`
- **Multipliers**: `mil naw cant pedwar deg tri` → `1943`
- **Ordinals**: `trydydd` → `3ydd`, `cyntaf` → `1af`
- **Currency**: `pum punt a deg ceiniog` → `£5.10`
- **Feminine forms**: `dwy`, `tair`, `pedair`, `trydedd`, etc.
- **Mutated forms**: soft mutation (`ddau`, `dri`, `fil`, `gyntaf`, etc.), aspirate mutation (`thri`, `phum`, `phedwar`, etc.)

Integrated into WelshNormalizer via an optional `normalize_numbers` toggle (off by default), following Whisper's compositional sub-normalizer pattern.

### 3. Abbreviation and title expansion

**Gap:** No expansion of titles or common abbreviations.

**Impact:** Transcriptions may contain `Mr`, `Mrs`, `Dr`, `St` (sant/stryd), `Prif`, etc. These are not expanded.

**Recommendation:** Lower priority than number handling. Could be added as an additional lookup table in `welsh_data.py` if needed. Note that some Welsh abbreviations are more complex due to mutation (`Dr` → `Doctor`/`Ddoctor` depending on context).

### ~~4. Lowercasing~~ (DONE)

Optional `lowercase` toggle added (off by default). When enabled, converts output to lowercase for WER calculation.

### ~~5. Punctuation and symbol handling~~ (DONE)

Optional `strip_punctuation` toggle added (off by default). When enabled, strips all punctuation and symbols for WER calculation.

## Architectural Comparison

| Aspect | Whisper normalizers | WelshNormalizer |
|---|---|---|
| Callable pattern | `__call__` (normalizer as function) | `__call__` + `.normalize()` |
| Composition | Composes sub-normalizers as classes | Composed `WelshNumberNormalizer` sub-normalizer |
| Data storage | Inline dictionaries + JSON file | Separate `welsh_data.py` module |
| Configuration | Constructor booleans (2-3) | Constructor booleans (18) |
| Return type | `str` | `str` or `Tuple[str, List[Flag]]` |
| Tokenization | Regex-based inline | Separate tokenizer module |

### Architectural alignment (DONE)

1. **`__call__`** — `WelshNormalizer` is now callable: `normalizer(text)` works alongside `normalizer.normalize(text)`.
2. **Sub-normalizer composition** — `WelshNumberNormalizer` is a separate class composed into `WelshNormalizer`, following Whisper's pattern.

## Summary

WelshNormalizer is a **WelshTextNormalizer** in the same sense that Whisper's `EnglishTextNormalizer` is an English-specific speech normalization layer. It occupies the same architectural role, handles the same category of problem (spoken-form → written-form normalization), and in several areas (contraction coverage, context sensitivity, configurability, uncertainty handling) exceeds what Whisper provides for English.

With NFKC Unicode normalization, number-to-digit conversion (including vigesimal and mutated forms), `__call__` API alignment, lowercasing, and punctuation stripping now implemented, **WelshNormalizer has reached effective parity with EnglishTextNormalizer**. The only remaining gap is title/abbreviation expansion, which is a minor completeness improvement.

## Priority Roadmap

| Priority | Task | Effort | Impact | Status |
|---|---|---|---|---|
| 1 | Add NFKC Unicode normalization pass | Small | Robustness against encoding variation | Done |
| 2 | Add `__call__` method | Trivial | API consistency with Whisper | Done |
| 3 | Welsh number normalizer (decimal, vigesimal, mutations) | Large | Feature parity for number handling | Done |
| 4 | Optional lowercasing toggle | Small | WER calculation support | Done |
| 5 | Optional punctuation stripping | Small | WER calculation support | Done |
| 6 | Title/abbreviation expansion | Small | Minor completeness improvement | Pending |
