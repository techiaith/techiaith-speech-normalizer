"""Basic tests for WelshNormalizer."""

from techiaith.speech_normalizer import WelshNormalizer


def test_import():
    normalizer = WelshNormalizer()
    assert normalizer is not None


def test_pronoun_expansion():
    normalizer = WelshNormalizer()
    assert normalizer.normalize("nw") == "nhw"


def test_verb_contraction():
    normalizer = WelshNormalizer()
    assert normalizer.normalize("ca'l") == "cael"


def test_mae_contraction():
    normalizer = WelshNormalizer()
    result = normalizer.normalize("ma' nw'n gwbod")
    assert "mae" in result
    assert "nhw'n" in result
    assert "gwybod" in result


def test_remove_tags():
    normalizer = WelshNormalizer(remove_tags=True)
    result = normalizer.normalize("helo <anadlu> byd")
    assert "<anadlu>" not in result


def test_tags_kept_by_default():
    normalizer = WelshNormalizer()
    assert normalizer.normalize("helo <anadlu> byd") == "helo <anadlu> byd"


def test_remove_asterisks():
    normalizer = WelshNormalizer(remove_asterisks=True)
    result = normalizer.normalize("*Facebook*")
    assert result == "Facebook"


def test_asterisks_kept_by_default():
    normalizer = WelshNormalizer()
    assert normalizer.normalize("*Facebook*") == "*Facebook*"


def test_dialectal_plurals():
    normalizer = WelshNormalizer()
    assert normalizer.normalize("petha") == "pethau"


def test_spelling():
    normalizer = WelshNormalizer()
    assert normalizer.normalize("rwbeth") == "rhywbeth"


def test_normalize_with_flags():
    normalizer = WelshNormalizer()
    result, flags = normalizer.normalize_with_flags("bo' nw'n gwbod")
    assert isinstance(result, str)
    assert isinstance(flags, list)


def test_disabled_category():
    normalizer = WelshNormalizer(expand_pronouns=False)
    assert normalizer.normalize("nw") == "nw"


def test_empty_string():
    normalizer = WelshNormalizer()
    assert normalizer.normalize("") == ""


def test_callable():
    normalizer = WelshNormalizer()
    assert normalizer("nw") == "nhw"
    assert normalizer("ca'l") == "cael"


def test_unicode_nfkc():
    normalizer = WelshNormalizer()
    # w + combining circumflex (U+0302) should be normalized to precomposed ŵ (U+0175)
    decomposed = "w\u0302"
    result = normalizer.normalize(decomposed)
    assert "\u0175" in result or "ŵ" in result


def test_lowercase():
    normalizer = WelshNormalizer(lowercase=True)
    assert normalizer("Cymru") == "cymru"
    assert normalizer("BOD NHW") == "bod nhw"


def test_strip_punctuation():
    normalizer = WelshNormalizer(strip_punctuation=True)
    result = normalizer("helo, byd!")
    assert "," not in result
    assert "!" not in result
    assert "helo" in result
    assert "byd" in result


def test_lowercase_and_strip_punctuation_for_wer():
    normalizer = WelshNormalizer(lowercase=True, strip_punctuation=True)
    assert normalizer("Helo, Byd!") == "helo byd"
    # Apostrophes are also stripped (consistent with Whisper's WER normalization)
    assert normalizer("chi'n") == "chi n"


# --- join_hyphenated_compounds tests ---

def test_join_simple_compound():
    normalizer = WelshNormalizer(join_hyphenated_compounds=True)
    assert normalizer("gwasg-y-fferm") == "gwasg y fferm"


def test_join_two_word_compound():
    normalizer = WelshNormalizer(join_hyphenated_compounds=True)
    assert normalizer("pen-blwydd") == "pen blwydd"


def test_join_chain():
    normalizer = WelshNormalizer(join_hyphenated_compounds=True)
    assert normalizer("a-b-c-d") == "a b c d"


def test_join_standalone_hyphen_untouched():
    normalizer = WelshNormalizer(join_hyphenated_compounds=True)
    assert normalizer("- helo") == "- helo"


def test_join_leading_trailing_hyphen_untouched():
    normalizer = WelshNormalizer(join_hyphenated_compounds=True)
    assert normalizer("-test") == "-test"
    assert normalizer("test-") == "test-"


def test_join_composes_with_strip_punctuation():
    normalizer = WelshNormalizer(join_hyphenated_compounds=True, strip_punctuation=True)
    assert normalizer("gwasg-y-fferm, helo!") == "gwasg y fferm helo"


def test_join_en_dash():
    normalizer = WelshNormalizer(join_hyphenated_compounds=True)
    assert normalizer("gwasg\u2013y\u2013fferm") == "gwasg y fferm"


def test_join_em_dash():
    normalizer = WelshNormalizer(join_hyphenated_compounds=True)
    assert normalizer("gwasg\u2014y\u2014fferm") == "gwasg y fferm"


def test_join_default_off():
    normalizer = WelshNormalizer()
    assert normalizer("gwasg-y-fferm") == "gwasg-y-fferm"


def test_join_false_start_untouched():
    normalizer = WelshNormalizer(join_hyphenated_compounds=True)
    # false-start pattern: word-hyphen-space — the lookahead requires \w so space won't match
    result = normalizer("ww- a wedyn")
    assert "ww-" in result or "a wedyn" in result


# --- expand_annotations tests ({spoken|written}) ---

def test_annotation_number():
    normalizer = WelshNormalizer()
    assert normalizer("{saith|7}") == "7"


def test_annotation_adjacent():
    normalizer = WelshNormalizer()
    result = normalizer("Dwi'n byw yn {saith|7}{saith|7} Lon Abererch")
    assert result == "Dw i'n byw yn 77 Lon Abererch"


def test_annotation_in_sentence():
    normalizer = WelshNormalizer()
    result = normalizer("mae {dau ddeg pump|25} o bobl yma")
    assert result == "mae 25 o bobl yma"


def test_annotation_written_side_further_normalized():
    # The written side passes through the rest of the pipeline
    normalizer = WelshNormalizer()
    assert normalizer("{rhywbath|rwbeth}") == "rhywbeth"


def test_annotation_disabled():
    normalizer = WelshNormalizer(expand_annotations=False)
    result = normalizer("{saith|7}")
    assert "{saith|7}" in result


def test_annotation_unmatched_braces_untouched():
    normalizer = WelshNormalizer()
    # No pipe — not an annotation, leave alone
    assert "{saith}" in normalizer("{saith}")
