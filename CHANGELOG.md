# Changelog

All notable changes to this project are documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and the project follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.2.0] - 2026-10-28

First public release, on GitHub and PyPI. Changes since 0.1.0:

### Added
- `WelshNumberNormalizer`: converts Welsh number words to digits (decimal and
  vigesimal systems, ordinals, currency, mutated forms). Enabled in
  `WelshNormalizer` with `normalize_numbers=True`.
- WER-only toggles, all off by default: `lowercase`, `strip_punctuation`,
  `join_hyphenated_compounds`.
- Unicode NFKC normalisation as the first step of the pipeline, and a callable
  `__call__` interface matching OpenAI Whisper's normalizers.
- Expansion of `{llafar|ysgrifenedig}` annotations, e.g. `{saith|7}` → `7`.
- `standardize_adjectives` and the `ADJECTIVE_REDUCTIONS` table, plus many new
  vocabulary entries including possessive forms.
- Contractions `timod`/`t'mod`/`t'bo'`, `fan'na`, `'na beth yw`, `fel na` and
  `ma' na`; fixes for `dwi'n`/`dwi'm`, `ma' 'na` → `mae yna`, and tokens with a
  leading apostrophe (`'di`, `'na`).
- `COMPARISON.md`, comparing this normaliser with OpenAI Whisper's text
  normalisers.
- GitHub Actions workflows for tests and for publishing to PyPI, plus
  `CONTRIBUTING.md` and `CITATION.cff`.

### Changed
- Package renamed to the `techiaith.speech_normalizer` namespace.
- The README now states that `remove_tags` and `remove_asterisks` are off by
  default (as the code has always behaved), and its examples reflect the
  current hesitation standardisation (`yy`/`yrm`/`ymm` → `yym`).
- The tests for tag and asterisk removal now enable those options explicitly,
  and new tests check that both are kept by default.

## [0.1.0] - 2026-05-19

### Added
- Initial release: configurable `WelshNormalizer` for Welsh verbatim speech
  transcriptions, SRT subtitle file support, uncertainty flagging and the
  `techiaith-speech-normalize` command-line tool.
