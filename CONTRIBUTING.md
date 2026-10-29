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

1. Mewn cais tynnu, diweddarwch `version` yn `pyproject.toml`, diweddarwch
   `version` a `date-released` yn `CITATION.cff`, a symudwch y nodiadau yn
   `CHANGELOG.md` o "Unreleased" i bennawd y fersiwn newydd, gyda'r dyddiad.
2. Ar ôl ei uno, tagiwch y commit newydd ar `main` a gwthiwch y tag:

   ```bash
   git switch main && git pull
   git tag -a v0.3.0 -m v0.3.0
   git push origin v0.3.0
   ```

3. Mae'r llif gwaith `.github/workflows/publish.yml` yn gwirio bod y tag ar
   `main` a'i fod yn cyfateb i'r fersiwn yn `pyproject.toml`, `CITATION.cff` a
   `CHANGELOG.md`, ac yna'n adeiladu'r pecyn. Mae cyhoeddi ar PyPI yn aros am
   gymeradwyaeth yn yr amgylchedd `pypi` (y botwm "Review deployments" yn
   rhediad y llif gwaith). Wedyn mae'r llif gwaith yn creu'r datganiad (release)
   ar GitHub, gyda'r ffeiliau a'r nodiadau o `CHANGELOG.md`.

Dim ond gweinyddwyr yr ystorfa sy'n gallu gwthio tagiau `v*`. Ni ellir newid
datganiad ar ôl ei gyhoeddi, ar PyPI nac ar GitHub: rhaid rhyddhau fersiwn
newydd i gywiro camgymeriad.

Mae'r offer sy'n adeiladu'r pecyn wedi'u pinio gyda hashes yn
`.github/build-requirements.txt`, ac mae Dependabot yn cynnig diweddariadau
iddynt ac i'r GitHub Actions. I'w newid â llaw, golygwch
`.github/build-requirements.in` a rhedwch:

```bash
uvx --python 3.12 --from pip-tools pip-compile --generate-hashes --strip-extras --output-file .github/build-requirements.txt .github/build-requirements.in
```

Mae cyhoeddi ar PyPI yn defnyddio
[cyhoeddi dibynadwy (trusted publishing)](https://docs.pypi.org/trusted-publishers/),
felly nid oes tocyn API yn cael ei gadw yn unman. Mae'r cyhoeddwr dibynadwy ar
PyPI wedi'i osod i berchennog `techiaith`, ystorfa `techiaith-speech-normalizer`,
llif gwaith `publish.yml` ac amgylchedd `pypi`; os caiff ffeil y llif gwaith
neu'r amgylchedd eu hailenwi, bydd cyhoeddi'n methu nes eu diweddaru yno hefyd.

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

1. In a pull request, update `version` in `pyproject.toml`, update `version`
   and `date-released` in `CITATION.cff`, and move the notes in `CHANGELOG.md`
   from "Unreleased" to a heading for the new version, with the date.
2. Once it is merged, tag the new commit on `main` and push the tag:

   ```bash
   git switch main && git pull
   git tag -a v0.3.0 -m v0.3.0
   git push origin v0.3.0
   ```

3. The `.github/workflows/publish.yml` workflow checks that the tag is on
   `main` and matches the versions in `pyproject.toml`, `CITATION.cff` and
   `CHANGELOG.md`, then builds the package. Publishing to PyPI waits for
   approval in the `pypi` environment (the "Review deployments" button on the
   workflow run). The workflow then creates the GitHub release, with the files
   and the notes from `CHANGELOG.md`.

Only repository admins can push `v*` tags. A release cannot be changed once it
is published, on PyPI or on GitHub: fix a mistake by releasing a new version.

The tools that build the package are pinned with hashes in
`.github/build-requirements.txt`, and Dependabot proposes updates to them and
to the GitHub Actions. To change them by hand, edit
`.github/build-requirements.in` and run:

```bash
uvx --python 3.12 --from pip-tools pip-compile --generate-hashes --strip-extras --output-file .github/build-requirements.txt .github/build-requirements.in
```

PyPI publishing uses
[trusted publishing](https://docs.pypi.org/trusted-publishers/), so no API
token is stored anywhere. The trusted publisher on PyPI is set to owner
`techiaith`, repository `techiaith-speech-normalizer`, workflow `publish.yml`
and environment `pypi`; renaming the workflow file or the environment breaks
publishing until it is updated there too.
