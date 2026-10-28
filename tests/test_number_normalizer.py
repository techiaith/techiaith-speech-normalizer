"""Tests for the Welsh number normalizer."""

import pytest
from techiaith.speech_normalizer.welsh_number_normalizer import WelshNumberNormalizer
from techiaith.speech_normalizer import WelshNormalizer


@pytest.fixture
def n():
    return WelshNumberNormalizer()


# ── Decimal system ──────────────────────────────────────────────────────────

class TestDecimal:
    def test_basic_tens(self, n):
        assert n("tri deg pump") == "35"
        assert n("pum deg dau") == "52"
        assert n("saith deg naw") == "79"
        assert n("naw deg naw") == "99"

    def test_tens_without_unit(self, n):
        assert n("tri deg") == "30"
        assert n("pum deg") == "50"

    def test_un_deg(self, n):
        assert n("un deg un") == "11"
        assert n("un deg dau") == "12"


# ── Vigesimal system ───────────────────────────────────────────────────────

class TestVigesimal:
    def test_multiples_of_twenty(self, n):
        assert n("ugain") == "20"
        assert n("deugain") == "40"
        assert n("trigain") == "60"

    def test_teens(self, n):
        assert n("un ar ddeg") == "11"
        assert n("deuddeg") == "12"
        assert n("tri ar ddeg") == "13"
        assert n("pymtheg") == "15"
        assert n("un ar bymtheg") == "16"
        assert n("deunaw") == "18"
        assert n("pedwar ar bymtheg") == "19"

    def test_vigesimal_addition(self, n):
        assert n("pymtheg ar hugain") == "35"
        assert n("un ar hugain") == "21"
        assert n("deunaw ar hugain") == "38"


# ── Units ───────────────────────────────────────────────────────────────────

class TestUnits:
    def test_basic_units(self, n):
        assert n("dim") == "0"
        assert n("sero") == "0"
        assert n("un") == "1"
        assert n("pump") == "5"
        assert n("naw") == "9"

    def test_feminine_forms(self, n):
        assert n("dwy") == "2"
        assert n("tair") == "3"
        assert n("pedair") == "4"


# ── Multipliers ─────────────────────────────────────────────────────────────

class TestMultipliers:
    def test_cant(self, n):
        assert n("cant") == "100"
        assert n("cant tri deg pump") == "135"

    def test_mil(self, n):
        assert n("mil") == "1000"
        assert n("mil naw cant pedwar deg tri") == "1943"
        assert n("dwy fil") != "dwy fil"  # should attempt parse

    def test_dau_gant(self, n):
        assert n("dau gant") == "200"


# ── Ordinals ────────────────────────────────────────────────────────────────

class TestOrdinals:
    def test_basic_ordinals(self, n):
        assert n("cyntaf") == "1af"
        assert n("cynta") == "1af"
        assert n("ail") == "2il"
        assert n("trydydd") == "3ydd"
        assert n("pumed") == "5ed"
        assert n("degfed") == "10fed"

    def test_feminine_ordinals(self, n):
        assert n("trydedd") == "3edd"
        assert n("pedwaredd") == "4edd"

    def test_ordinal_in_sentence(self, n):
        assert n("y trydydd dyn") == "y 3ydd dyn"


# ── Currency ────────────────────────────────────────────────────────────────

class TestCurrency:
    def test_pounds_only(self, n):
        assert n("pum punt") == "£5"
        assert n("tri phunt") == "£3"

    def test_pounds_and_pence(self, n):
        assert n("pum punt a deg ceiniog") == "£5.10"

    def test_currency_in_sentence(self, n):
        result = n("mae'n costio pum punt")
        assert "£5" in result


# ── Mutated forms (treigladau) ──────────────────────────────────────────────

class TestMutations:
    def test_soft_mutation_units(self, n):
        assert n("ddau") == "2"
        assert n("ddwy") == "2"
        assert n("dri") == "3"
        assert n("dair") == "3"
        assert n("bedwar") == "4"
        assert n("bedair") == "4"
        assert n("bum") == "5"
        assert n("nau") == "9"
        assert n("ddeg") == "10"

    def test_aspirate_mutation_units(self, n):
        assert n("thri") == "3"
        assert n("thair") == "3"
        assert n("phum") == "5"
        assert n("phedwar") == "4"

    def test_soft_mutation_teens(self, n):
        assert n("dri ar ddeg") == "13"
        assert n("bedwar ar ddeg") == "14"
        assert n("bymtheg") == "15"
        assert n("ddeunaw") == "18"

    def test_soft_mutation_decimal_tens(self, n):
        assert n("dri deg pump") == "35"
        assert n("bedwar deg dau") == "42"
        assert n("bum deg tri") == "53"

    def test_soft_mutation_vigesimal(self, n):
        assert n("ddeugain") == "40"
        assert n("drigain") == "60"

    def test_soft_mutation_multipliers(self, n):
        assert n("fil") == "1000"
        assert n("dau gant") == "200"
        assert n("dwy fil") == "2000"

    def test_soft_mutation_ordinals(self, n):
        assert n("gyntaf") == "1af"
        assert n("drydydd") == "3ydd"
        assert n("drydedd") == "3edd"
        assert n("bedwerydd") == "4ydd"
        assert n("bumed") == "5ed"

    def test_mutation_in_sentence(self, n):
        assert n("o ddau gant") == "o 200"
        assert n("y gyntaf") == "y 1af"
        assert n("tua thri deg") == "tua 30"


# ── Sentence context ────────────────────────────────────────────────────────

class TestSentenceContext:
    def test_numbers_in_sentence(self, n):
        assert n("mae tri deg pump o bobl yma") == "mae 35 o bobl yma"
        assert n("mae pedwar deg dau o bobl yma") == "mae 42 o bobl yma"

    def test_non_number_text_unchanged(self, n):
        assert n("bore da") == "bore da"
        assert n("") == ""


# ── Integration with WelshNormalizer ────────────────────────────────────────

class TestIntegration:
    def test_normalize_numbers_toggle(self):
        norm = WelshNormalizer(normalize_numbers=True)
        assert "35" in norm("tri deg pump o bobl")

    def test_normalize_numbers_off_by_default(self):
        norm = WelshNormalizer()
        assert "tri deg pump" in norm("tri deg pump")

    def test_full_wer_mode(self):
        norm = WelshNormalizer(
            normalize_numbers=True,
            lowercase=True,
            strip_punctuation=True,
        )
        result = norm("Mae Tri Deg Pump o bobl!")
        assert "35" in result
        assert result.islower() or result.replace("35", "").strip().islower()
