# Cyfrannu / Contributing

## Cymraeg

Croeso i gyfraniadau: adroddiadau am wallau, geiriau ac ymadroddion newydd ar
gyfer y tablau yn `welsh_data.py`, a gwelliannau i'r cod.

### Gosod ar gyfer datblygu

```bash
git clone https://github.com/techiaith/techiaith-speech-normalizer.git
cd techiaith-speech-normalizer
pip install -e . pytest
pytest
```

Neu gydag [uv](https://docs.astral.sh/uv/): `uv run pytest`.

### Ychwanegu geiriau neu reolau newydd

Mae'r holl dablau ieithyddol yn `src/techiaith/speech_normalizer/welsh_data.py`.
Ar ôl eu newid:

1. Ychwanegwch brawf yn `tests/` ar gyfer y ffurf newydd.
2. Rhedwch `pytest` a sicrhewch fod pob prawf yn pasio.

### Ceisiadau tynnu (pull requests)

- Agorwch issue yn gyntaf ar gyfer newidiadau mawr.
- Cadwch bob cais yn fach ac yn canolbwyntio ar un peth.
- Ychwanegwch nodyn o dan "Unreleased" yn `CHANGELOG.md`.

### Rhyddhau fersiwn newydd (cynhalwyr)

1. Diweddarwch `version` yn `pyproject.toml` a symudwch y nodiadau yn
   `CHANGELOG.md` o "Unreleased" i bennawd y fersiwn newydd, gyda'r dyddiad.
2. Gwnewch commit a gwthiwch i `main`.
3. Crëwch dag a datganiad (release) ar GitHub, e.e. `v0.3.0`. Mae'r llif gwaith
   `.github/workflows/publish.yml` yn adeiladu'r pecyn, yn ei gyhoeddi ar PyPI
   ac yn atodi'r ffeiliau i'r datganiad yn awtomatig.

## English

Contributions are welcome: bug reports, new words and phrases for the tables in
`welsh_data.py`, and improvements to the code.

### Development setup

```bash
git clone https://github.com/techiaith/techiaith-speech-normalizer.git
cd techiaith-speech-normalizer
pip install -e . pytest
pytest
```

Or with [uv](https://docs.astral.sh/uv/): `uv run pytest`.

### Adding words or rules

All the linguistic tables live in `src/techiaith/speech_normalizer/welsh_data.py`.
After changing them:

1. Add a test in `tests/` for the new form.
2. Run `pytest` and make sure everything passes.

### Pull requests

- Open an issue first for larger changes.
- Keep each pull request small and focused on one thing.
- Add a note under "Unreleased" in `CHANGELOG.md`.

### Releasing a new version (maintainers)

1. Update `version` in `pyproject.toml` and move the notes in `CHANGELOG.md`
   from "Unreleased" to a heading for the new version, with the date.
2. Commit and push to `main`.
3. Create a tag and a GitHub release, e.g. `v0.3.0`. The
   `.github/workflows/publish.yml` workflow builds the package, publishes it to
   PyPI and attaches the files to the release automatically. The release tag
   must match the version in `pyproject.toml`, or the workflow fails before
   publishing anything.

One-time setup for PyPI publishing: the workflow uses
[trusted publishing](https://docs.pypi.org/trusted-publishers/), so no API
token is stored in the repository. On PyPI, add a trusted publisher for the
project `techiaith-speech-normalizer` with owner `techiaith`, repository
`techiaith-speech-normalizer`, workflow `publish.yml` and environment `pypi`.
The first release can be registered as a "pending publisher" before the project
exists on PyPI.
