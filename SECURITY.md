# Diogelwch / Security

## Cymraeg

### Adrodd am wendid

Peidiwch ag agor issue cyhoeddus am wendid diogelwch. Yn lle hynny, adroddwch
amdano'n breifat drwy'r botwm "Report a vulnerability" ar dab
[Security](https://github.com/techiaith/techiaith-speech-normalizer/security)
yr ystorfa. Byddwn yn ymateb cyn gynted ag y gallwn.

Dim ond y datganiad diweddaraf sy'n cael cywiriadau diogelwch.

### Gwirio pecyn

Mae pob datganiad yn cael ei adeiladu a'i gyhoeddi gan y llif gwaith
`.github/workflows/publish.yml`. Mae gan y ffeiliau ar PyPI ardystiadau
(attestations) PEP 740, sydd i'w gweld ar dudalen y prosiect ar PyPI, a gallwch
wirio ffeil o PyPI neu o ddatganiad ar GitHub gyda'r
[GitHub CLI](https://cli.github.com/):

```bash
gh attestation verify techiaith_speech_normalizer-0.2.0-py3-none-any.whl \
  --repo techiaith/techiaith-speech-normalizer
```

## English

### Reporting a vulnerability

Please don't open a public issue for a security vulnerability. Instead, report
it privately with the "Report a vulnerability" button on the repository's
[Security](https://github.com/techiaith/techiaith-speech-normalizer/security)
tab. We will respond as soon as we can.

Only the latest release receives security fixes.

### Verifying a package

Every release is built and published by the `.github/workflows/publish.yml`
workflow. The files on PyPI carry PEP 740 attestations, shown on the project's
PyPI page, and you can verify a file from PyPI or from a GitHub release with
the [GitHub CLI](https://cli.github.com/):

```bash
gh attestation verify techiaith_speech_normalizer-0.2.0-py3-none-any.whl \
  --repo techiaith/techiaith-speech-normalizer
```
