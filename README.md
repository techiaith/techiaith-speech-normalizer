# Normaleiddiwr Lleferydd Cymraeg / Welsh Speech Normalizer

## Gosod / Installation

```bash
pip install techiaith-speech-normalizer
```

Neu o'r ffynhonnell / Or from source:

```bash
git clone https://github.com/techiaith/techiaith-speech-normalizer.git
cd techiaith-speech-normalizer
pip install .
```

---

## Cymraeg

### Trosolwg

Mae'r modiwl hwn yn normaleiddio trawsgrifiadau lleferydd Cymraeg air-am-air
(verbatim) i ffurfiau mwy darllenadwy. Pan fydd modelau adnabod lleferydd
(fel Whisper) yn trawsgrifio Cymraeg llafar, maen nhw'n aml yn cynhyrchu
ffurfiau tafodiaith, byrfoddau, a sillafu ansafonol. Mae'r normaleiddiwr yn
trosi'r ffurfiau hyn i'r Gymraeg ysgrifenedig safonol, tra'n cadw ystyr y
testun gwreiddiol.

### Enghreifftiau

Mae'r enghreifftiau isod yn defnyddio `WelshNormalizer(remove_tags=True, remove_asterisks=True)`.

| Verbatim (gwreiddiol) | Normalaidd (canlyniad) | Esboniad |
|------------------------|------------------------|----------|
| `bo' nw'n gwbod` | `bod nhw'n gwybod` | Ehangu byrfoddau berfol a rhagenwol, adfer llafariaid mewnol |
| `ma' nw 'di ca'l` | `mae nhw wedi cael` | Normaleiddio `ma'`→`mae`, `'di`→`wedi` (cyd-destunol), `ca'l`→`cael` |
| `petha <anadlu> dechre` | `pethau dechrau` | Safoni lluosogion tafodieithol, dileu tagiau di-leferydd |
| `rwbeth *actually* gwbod` | `rhywbeth actually gwybod` | Cywiro sillafu, dileu sêr o eiriau Saesneg |
| `yy dwi'm isio` | `yym dw i ddim eisiau` | Safoni petruster, ehangu negyddion, safoni sillafu |

### Categorïau Normaleiddio

Mae'r normaleiddiwr yn trin y categorïau canlynol, a phob un yn gallu cael
ei droi ymlaen neu i ffwrdd yn annibynnol:

#### Normaleiddio trawsgrifiad (gwella'r testun ar gyfer isdeitlau / cynnyrch terfynol)

- **Tagiau di-leferydd**: Dileu marcwyr fel `<anadlu>`, `<chwerthin>`, `<aneglur>` (i ffwrdd yn ddiofyn; trowch ymlaen gyda `remove_tags=True`)
- **Sêr (cod-newid)**: Dileu `*...*` o gwmpas geiriau Saesneg (i ffwrdd yn ddiofyn; trowch ymlaen gyda `remove_asterisks=True`)
- **Rhagenwau**: `nw`→`nhw`, `'u`→`eu`, `'ych`→`eich`
- **Byrfoddau berfol**: `ca'l`→`cael`, `bo'`→`bod`, `neud`→`gwneud`, `nath`→`gwnaeth`
- **Byrfoddau `mae`**: `ma'`→`mae` gyda normaleiddio dilynwyr cyd-destunol
- **`'di` cyd-destunol**: `'di`→`wedi` dim ond pan fo rhagenw yn dod o'i flaen (e.e. `dwi 'di`→`dwi wedi`)
- **Byrfoddau eraill**: `'na`→`yna`, `'ma`→`yma`, `'lly`→`felly`, `'chos`→`achos`, ac ati
- **Lluosogion tafodieithol**: `-a` (Gogledd) a `-e` (De) → `-au` safonol (e.e. `petha`/`pethe`→`pethau`)
- **Berfau tafodieithol**: `dechre`→`dechrau`, `gweitho`→`gweithio`, `clwad`→`clywed`
- **Llafariaid mewnol**: `gwbod`→`gwybod`, `me'wl`→`meddwl`, `amsar`→`amser`
- **Sillafu**: `rwbeth`→`rhywbeth`, `isio`→`eisiau`, `pobol`→`pobl`
- **Petruster**: Safoni `yy`/`yrm`/`ymm`→`yym`, neu eu dileu'n gyfan gwbl
- **Dechreuadau ffals**: Dileu geiriau sy'n cael eu torri cyn eu gorffen (e.e. `m-`, `o-`)
- **Ymadroddion aml-air**: `o's gynnoch`→`oes gynnoch`, `dan dred`→`dan draed`
- **Anodiadau `{llafar|ysgrifenedig}`**: Cadw'r ffurf ysgrifenedig, e.e. `{saith|7}`→`7`, `{dau ddeg pump|25}`→`25`

#### Ar gyfer cyfrifo WER yn unig (dinistriol — ddim yn addas ar gyfer isdeitlau na chynnyrch terfynol)

Mae'r opsiynau canlynol i gyd i ffwrdd yn ddiofyn. Maent yn trawsnewid y testun mewn ffyrdd sy'n dileu gwybodaeth (priflythrennau, atalnodi, fformat rhifau, cysylltnodau) er mwyn i gymhariaeth WER ganolbwyntio ar y geiriau eu hunain. Peidiwch â'u defnyddio wrth greu isdeitlau na thrawsgrifiadau terfynol.

- **Normaleiddio rhifau**: Trosi geiriau rhifau Cymraeg i ddigidau (e.e. `tri deg pump`→`35`, `pymtheg ar hugain`→`35`). Yn cefnogi'r system ddegol a'r system ugeinfedol, trefnolion, ac arian
- **Uno cyfansoddeiriau cysylltnodol**: Uno geiriau fel `gwasg-y-fferm`→`gwasg y fferm` yn un tocyn. Yn cefnogi cysylltnod ASCII, lled-doriad (–) a thoriad hir (—). Dim ond cysylltnodau rhwng llythrennau sy'n cael eu dileu; mae cysylltnodau ar ddechrau/diwedd geiriau a dechreuadau ffals (`ww-`) yn aros fel y maent
- **Llythrennau bach**: Trosi'r allbwn i lythrennau bach
- **Dileu atalnodi**: Dileu atalnodi a symbolau

### Fflagio Achosion Ansicr

Mae'r normaleiddiwr yn fflagio achosion lle mae'r normaleiddio cywir yn amwys.
Er enghraifft, mae `'di` heb ragenw o'i flaen yn cael ei fflagio i'w adolygu
â llaw, yn hytrach na'i drawsnewid yn anghywir.

### Defnydd

```python
from techiaith.speech_normalizer import WelshNormalizer

# Creu gyda'r gosodiadau rhagosodedig (y rhan fwyaf o normaleiddiadau ymlaen).
# Mae tagiau di-leferydd a sêr yn cael eu cadw oni bai eich bod yn gofyn am eu dileu:
normalizer = WelshNormalizer(remove_tags=True, remove_asterisks=True)

# Normaleiddio testun — galwadwy fel normaleiddiwr Whisper
result = normalizer("bo' nw'n gwbod <anadlu> petha")
# → "bod nhw'n gwybod pethau"

# Neu defnyddio'r dull .normalize() yn uniongyrchol
result = normalizer.normalize("ma' nw 'di ca'l")
# → "mae nhw wedi cael"

# Normaleiddio gyda fflagiau ansicr
result, flags = normalizer.normalize_with_flags("be' 'di hwnna")
# flags yn rhestru unrhyw achosion amwys

# Normaleiddio ffeil SRT (isdeitlau)
normalizer.normalize_srt_file("input.srt", "output.srt")
```

#### Ar gyfer cyfrifo WER (Cyfradd Gwall Geiriau)

Wrth gymharu allbwn adnabod lleferydd â thrawsgrifiad cyfeirio, mae
priflythrennau ac atalnodi yn sŵn amherthnasol. Mae'r togl `lowercase` a
`strip_punctuation` yn dileu'r sŵn hwn fel bod y gymhariaeth yn canolbwyntio
ar y geiriau eu hunain — yn union fel y mae normaleiddiwr Whisper (OpenAI) yn
ei wneud ar gyfer Saesneg.

```python
# Normaleiddio ar gyfer cyfrifo WER
normalizer = WelshNormalizer(
    normalize_numbers=True,
    join_hyphenated_compounds=True,
    lowercase=True,
    strip_punctuation=True,
)
result = normalizer("Mae tri deg pump o bobl yma")
# → "mae 35 o bobl yma"
```

Mae `normalize_numbers` yn cefnogi:
- **System ddegol**: `tri deg pump` → `35`
- **System ugeinfedol**: `pymtheg ar hugain` → `35`
- **Trefnolion**: `trydydd` → `3ydd`, `cyntaf` → `1af`
- **Arian**: `pum punt a deg ceiniog` → `£5.10`
- **Lluosyddion**: `mil naw cant pedwar deg tri` → `1943`

#### Llinell orchymyn

```bash
# Normaleiddio testun
techiaith-speech-normalize --text "bo' nw'n gwbod"

# Normaleiddio ffeil SRT
techiaith-speech-normalize --srt input.srt --output output.srt

# Cadw'r testun gwreiddiol uwchben y testun normalaidd yn yr allbwn
techiaith-speech-normalize --srt input.srt --output output.srt --include-original

# Dangos y cyfluniad presennol
techiaith-speech-normalize --text "test" --show-config
```

### Strwythur Ffeiliau

| Ffeil | Disgrifiad |
|-------|------------|
| `welsh_normalizer.py` | Y prif ddosbarth `WelshNormalizer` — rheolwr normaleiddio cyfluniadwy |
| `welsh_number_normalizer.py` | `WelshNumberNormalizer` — trosi geiriau rhifau i ddigidau (degol, ugeiniol, trefnolion, arian) |
| `welsh_data.py` | Yr holl dablau chwilio ieithyddol: rhagenwau, byrfoddau, lluosogion, sillafu, ayyb |
| `tokenization.py` | Tocyneiddio sy'n cadw atalnodi a bylchau |

---

## English

### Overview

This module normalizes Welsh verbatim speech transcriptions into more readable
written equivalents. When speech recognition models (such as Whisper) transcribe
spoken Welsh, they often produce dialectal forms, contractions, and
non-standard spellings. The normalizer converts these into standard written
Welsh while preserving the original meaning.

### Examples

The examples below use `WelshNormalizer(remove_tags=True, remove_asterisks=True)`.

| Verbatim (input) | Normalized (output) | Explanation |
|-------------------|---------------------|-------------|
| `bo' nw'n gwbod` | `bod nhw'n gwybod` | Expand verb and pronoun contractions, restore internal vowels |
| `ma' nw 'di ca'l` | `mae nhw wedi cael` | Normalize `ma'`→`mae`, `'di`→`wedi` (contextual), `ca'l`→`cael` |
| `petha <anadlu> dechre` | `pethau dechrau` | Standardize dialectal plurals, remove non-speech tags |
| `rwbeth *actually* gwbod` | `rhywbeth actually gwybod` | Fix spelling, remove asterisks from English words |
| `yy dwi'm isio` | `yym dw i ddim eisiau` | Standardize hesitation, expand negation, fix spelling |

### Normalization Categories

The normalizer handles the following categories, each of which can be
independently enabled or disabled:

#### Transcription normalization (improves text for subtitles / final output)

- **Non-speech tags**: Remove markers like `<anadlu>` (breathing), `<chwerthin>` (laughter), `<aneglur>` (unclear) (off by default; enable with `remove_tags=True`)
- **Asterisks (code-switching)**: Remove `*...*` around English words (off by default; enable with `remove_asterisks=True`)
- **Pronouns**: `nw`→`nhw` (they), `'u`→`eu` (their), `'ych`→`eich` (your)
- **Verb contractions**: `ca'l`→`cael` (get), `bo'`→`bod` (be/that), `neud`→`gwneud` (do), `nath`→`gwnaeth` (did)
- **`mae` contractions**: `ma'`→`mae` (is) with contextual follower normalization
- **Contextual `'di`**: `'di`→`wedi` (have/has) only when preceded by a pronoun (e.g. `dwi 'di`→`dwi wedi`)
- **Other contractions**: `'na`→`yna` (there), `'ma`→`yma` (here), `'lly`→`felly` (so), `'chos`→`achos` (because), etc.
- **Dialectal plurals**: `-a` (North) and `-e` (South) → standard `-au` (e.g. `petha`/`pethe`→`pethau`, things)
- **Dialectal verbs**: `dechre`→`dechrau` (start), `gweitho`→`gweithio` (work), `clwad`→`clywed` (hear)
- **Internal vowels**: `gwbod`→`gwybod` (know), `me'wl`→`meddwl` (think), `amsar`→`amser` (time)
- **Spelling**: `rwbeth`→`rhywbeth` (something), `isio`→`eisiau` (want), `pobol`→`pobl` (people)
- **Hesitations**: Standardize `yy`/`yrm`/`ymm`→`yym`, or remove entirely
- **False starts**: Remove truncated words (e.g. `m-`, `o-`)
- **Multi-word phrases**: `o's gynnoch`→`oes gynnoch` (do you have), `dan dred`→`dan draed` (underfoot)
- **`{spoken|written}` annotations**: Keep the written form, e.g. `{saith|7}`→`7`, `{dau ddeg pump|25}`→`25`

#### For WER calculation only (destructive — not suitable for subtitles or final output)

The following options are all off by default. They transform text in ways that discard information (case, punctuation, number format, hyphens) so that WER comparison focuses on the words themselves. Do not use them when producing subtitles or finished transcriptions.

- **Number normalization**: Convert Welsh number words to digits (e.g. `tri deg pump`→`35`, `pymtheg ar hugain`→`35`). Supports decimal and vigesimal systems, ordinals, and currency
- **Join hyphenated compounds**: Join compounds like `gwasg-y-fferm`→`gwasg y fferm` into single tokens. Supports ASCII hyphens, en dashes (–) and em dashes (—). Only hyphens between word characters are removed; leading/trailing hyphens and false starts (`ww-`) are left alone
- **Lowercase**: Convert output to lowercase
- **Strip punctuation**: Remove punctuation and symbols

### Flagging Uncertain Cases

The normalizer flags cases where the correct normalization is ambiguous.
For example, `'di` without a preceding pronoun is flagged for manual review
rather than being incorrectly transformed. This is based on analysis of
21,259 verbatim Welsh speech transcriptions.

### Usage

```python
from techiaith.speech_normalizer import WelshNormalizer

# Create with the default settings (most normalizations enabled).
# Non-speech tags and asterisks are kept unless you ask for them to be removed:
normalizer = WelshNormalizer(remove_tags=True, remove_asterisks=True)

# Normalize text — callable like Whisper's normalizer
result = normalizer("bo' nw'n gwbod <anadlu> petha")
# → "bod nhw'n gwybod pethau"

# Or use the .normalize() method directly
result = normalizer.normalize("ma' nw 'di ca'l")
# → "mae nhw wedi cael"

# Normalize with uncertainty flags
result, flags = normalizer.normalize_with_flags("be' 'di hwnna")
# flags lists any ambiguous cases

# Normalize an SRT subtitle file
normalizer.normalize_srt_file("input.srt", "output.srt")
```

#### For WER (Word Error Rate) calculation

When comparing speech recognition output against a reference transcription,
uppercase and punctuation are irrelevant noise. The `lowercase` and
`strip_punctuation` toggles remove this noise so the comparison focuses on
the words themselves — exactly as OpenAI's Whisper normalizer does for English.

```python
# Normalize for WER calculation
normalizer = WelshNormalizer(
    normalize_numbers=True,
    lowercase=True,
    strip_punctuation=True,
)
result = normalizer("Mae tri deg pump o bobl yma")
# → "mae 35 o bobl yma"
```

`normalize_numbers` supports:
- **Decimal system**: `tri deg pump` → `35`
- **Vigesimal system**: `pymtheg ar hugain` → `35`
- **Ordinals**: `trydydd` → `3ydd`, `cyntaf` → `1af`
- **Currency**: `pum punt a deg ceiniog` → `£5.10`
- **Multipliers**: `mil naw cant pedwar deg tri` → `1943`

#### Command line

```bash
# Normalize text
techiaith-speech-normalize --text "bo' nw'n gwbod"

# Normalize an SRT file
techiaith-speech-normalize --srt input.srt --output output.srt

# Keep original text above normalized text in output
techiaith-speech-normalize --srt input.srt --output output.srt --include-original

# Show current configuration
techiaith-speech-normalize --text "test" --show-config
```

### Configuration

All normalization categories can be toggled individually:

```python
normalizer = WelshNormalizer(
    remove_tags=True,              # Remove <anadlu> etc. (default: False)
    remove_asterisks=True,         # Remove *English* markers (default: False)
    expand_pronouns=True,          # nw → nhw
    expand_verb_contractions=True,  # ca'l → cael
    expand_mae_contractions=True,   # ma' → mae
    normalize_ma_with_followers=True,  # ma' nw → mae nhw
    expand_di_contextual=True,      # dwi 'di → dwi wedi
    standardize_plurals=True,       # petha → pethau
    standardize_verbs=True,         # dechre → dechrau
    standardize_internal=True,      # gwbod → gwybod
    standardize_spelling=True,      # rwbeth → rhywbeth
    remove_hesitations=False,       # Keep hesitations (default)
    standardize_hesitations=True,   # yym → ym
    remove_false_starts=True,       # Remove m-, o- etc.
    expand_annotations=True,        # {saith|7} → 7
    flag_uncertain=True,            # Flag ambiguous cases
    custom_corrections={"myword": "replacement"},  # Add your own

    # WER-only flags (destructive — not for subtitles/final output)
    normalize_numbers=False,        # Number words → digits
    join_hyphenated_compounds=False, # gwasg-y-fferm → gwasg y fferm
    lowercase=False,                # Lowercase output
    strip_punctuation=False,        # Strip punctuation
)
```

### File Structure

| File | Description |
|------|-------------|
| `welsh_normalizer.py` | Main `WelshNormalizer` class — configurable normalization engine |
| `welsh_number_normalizer.py` | `WelshNumberNormalizer` — converts number words to digits (decimal, vigesimal, ordinals, currency) |
| `welsh_data.py` | All linguistic lookup tables: pronouns, contractions, plurals, spelling, etc. |
| `tokenization.py` | Punctuation- and whitespace-preserving tokenizer |

---

## Datblygu / Development

```bash
git clone https://github.com/techiaith/techiaith-speech-normalizer.git
cd techiaith-speech-normalizer
pip install -e . pytest
pytest
```

Neu gydag [uv](https://docs.astral.sh/uv/) / Or with uv: `uv run pytest`

Gweler [CONTRIBUTING.md](CONTRIBUTING.md) am sut i gyfrannu a rhyddhau fersiynau newydd. /
See [CONTRIBUTING.md](CONTRIBUTING.md) for how to contribute and how new versions are released.

## Trwydded / License

[MIT](LICENSE) © Uned Technolegau Iaith, Prifysgol Bangor / Language Technologies Unit, Bangor University
