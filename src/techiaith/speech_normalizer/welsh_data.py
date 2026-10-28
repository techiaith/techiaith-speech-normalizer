#!/usr/bin/env python3
"""
Welsh Language Data - Shared normalization patterns

This module contains all the linguistic data used by Welsh normalizers.
All normalization rules and lookup tables are centralized here to ensure
consistency across different normalizer implementations.
"""

# ============================================================================
# PRONOUN NORMALIZATIONS
# ============================================================================
PRONOUN_CORRECTIONS = {
    "nw": "nhw",
    "n'w": "nhw",
    "nw'n": "nhw'n",
    "nw'm": "nhw'm",
    "nw'r": "nhw'r",
    "nhwn": "nhw'n",
    "'u": "eu",
    "'ych": "eich",
    "'yng": "ein",
    "'ym": "ein",
    "wnna": "hwnna",        
    "wnna'n": "hwnna'n",
}

# ============================================================================
# VERB CONTRACTIONS
# ============================================================================
VERB_CONTRACTIONS = {
    "ca'l": "cael",
    "ca'": "cael",
    "ga'l": "gael",
    "ga'": "ga",
    "cha'l": "chael",
    "bo'": "bod",
    "fo'": "fod",
    "gor'o'": "gorfod",
    "gor'o": "gorfod",
    "gorfo": "gorfod",
    "goro": "gorfod",
    "goffod": "gorfod",
    "goso'": "gosod",
    "'neud": "wneud",
    "neud": "wneud",
    "neu'": "neud",
    "gneu": "gwneud",
    "g'neud": "gwneud",
    "gneud": "gwneud",
    "nath": "wnaeth",
    "natha": "wnaeth",
    "nathon": "wnaethon",
    "nathoch": "wnaethoch",
    "nethon": "wnaethon",
    "netho": "wnaethon",
    "neith": "wnaiff",
    "nei": "wnei",
    "neshi": "wnes i",
    "nesh": "wnes",
    "'nes": "wnes",
    "newch": "wnewch",
    "newn": "wnawn",
    "by'": "bydd",
    "fy'": "fydd",
    "gewn": "gawn",
    "gesh": "ges",
    "gathon": "gaethon",
    "gethon": "gaethon",
    "'di": "ydy",
    "'dy": "ydy",
    "wt": "wyt",
    "wi": "dw i",
    "dwi": "dw i",
    "ydan": "ydym",
    "ydach": "ydych",
    "dach": "dych",
    "odd": "oedd",
    "o'dd": "oedd",
    "o'd'd": "oedd",
    "do'dd": "doedd",
    "do'": "doedd",
    "oddan": "oedden",
    "oddwn": "oeddwn",
    "odden": "oedden",
    "oddyn": "oedden",
    "oeddan": "oedden",
    "o'dden": "oedden",
    "oddach": "oeddech",
    "oddat": "oeddet",
    "odda": "roedd",
    "'swn": "baswn",
    "'sa": "basai",
    "swn": "baswn",
    "sa": "basai",
    "sa'n": "basai'n",
    "dyla": "dylai",
    "dylia": "dylai",
    "'ddan": "oedden",
    "'sych": "bysych",
    "'tai": "petai",
}

# ============================================================================
# MAE CONTRACTIONS
# ============================================================================
MAE_CONTRACTIONS = {
    "ma'": "mae",
    "ma'r": "mae'r",
    "ma'n": "mae'n",
    "m'e": "mae",
}

# ============================================================================
# OTHER CONTRACTIONS
# ============================================================================
OTHER_CONTRACTIONS = {
    "ne'": "neu",
    "'na": "yna",
    "'ne": "yna",
    "'ma": "yma",
    "fama": "fan yma",
    "fyma": "fan yma",
    "fana": "fan yna",
    "fan'na": "fan yna",
    "fyna": "fan yna",
    "fan'cw": "fan acw",
    "'lly": "felly",
    "'elly": "felly",
    "lly": "felly",
    "'llu": "felly",
    "'fo": "efo",
    "'da": "gyda",
    "timod": "ti'n gwybod",
    "t'mod": "ti'n gwybod",
    "t'bo'": "ti'n gwybod",
    "t'mo": "ti'n gwybod",
    "'wan": "rŵan",
    "rwan": "rŵan",
    "ŵan": "rŵan",
    "'w'rach": "hwyrach",
    "'chos": "achos",
    "'c'os": "achos",
    "chos": "achos",
    "'im": "dim",
    "im": "dim",
    "'nol": "yn ôl",
    "'fyd": "hefyd",
    "'to": "eto",
    "'stafell": "ystafell",
    "'sgubor": "ysgubor",
    "'mlan": "ymlaen",
    "'mlaen": "ymlaen",
    "bla'n": "blaen",
    "'run": "yr un",
    "run": "yr un",
    "'biti": "piti",
    "'wna": "hwnna",
    "'ddo": "iddo",
    "'chydig": "ychydig",
    "'lla": "efallai",
#    "'yn": "fy",
    "'i'n": "hi'n",
    "o'no": "ohono",
    "'ta'": "yntau",
    "'am": "yna ddim",
    "'ndoes": "onid oes",
    "'thrawon": "athrawon",
    "oe'": "oed",
}

# ============================================================================
# VOWEL REDUCTIONS - PLURALS
# ============================================================================
PLURAL_REDUCTIONS = {
    # North forms (-a)
    "petha": "pethau",
    "betha": "bethau",
    "pwysa": "pwysau",
    "bwysa'": "bwysau",
    "lleisia": "lleisiau",
    "lleisia'": "lleisiau",
    "lleisa": "lleisiau",
    "profiada": "profiadau",
    "brofiada": "brofiadau",
    "sgilia": "sgiliau",
    "sgilia'": "sgiliau",
    "hawlia'": "hawliau",
    "ffinia'": "ffiniau",
    "llunia'": "lluniau",
    "norma'": "normau",
    "cama'": "camau",
    "cyfrynga'": "cyfryngau",
    "emosiyna": "emosiynau",
    "hemosiyna": "hemosiynau",
    "dyddia'": "dyddiau",
    "dyddia": "dyddiau",
    "sesiyna": "sesiynau",
    "problema": "problemau",
    "gema": "gemau",
    "gema'": "gemau",
    "gweithgaredda": "gweithgareddau",
    "anawstera": "anawsterau",
    "grwpia'": "grwpiau",
    "heria'": "heriau",
    "radda": "raddau",
    "gwasanaetha'": "gwasanaethau",
    "wasanaetha'": "wasanaethau",
    "bywyda": "bywydau",
    "asiantaetha": "asiantaethau",
    "sgyrsia'": "sgyrsiau",
    "syniada": "syniadau",
    "newidiada": "newidiadau",
    "ffrindia": "ffrindiau",
    "elfenna'": "elfennau",
    "elfenna": "elfennau",
    "dyheada": "dyheadau",
    "pyncia'": "pynciau",
    "penderfyniada": "penderfyniadau",
    "mudiada": "mudiadau",
    "gyfnoda": "gyfnodau",
    "sylwada'": "sylwadau",
    "patryma": "patrymau",
    "ddatblygiada": "ddatblygiadau",
    "cyrsia": "cyrsiau",
    "terma": "termau",
    "clwbia": "clybiau",
    "systema": "systemau",
    "diwyllianna": "diwylliannau",
    "geiria'": "geiriau",
    "apia": "apiau",
    "agwedda'": "agweddau",
    "sefydliada": "sefydliadau",
    "cymuneda": "cymunedau",
    "gwefanna": "gwefannau",
    "anwyldera": "anhwylderau",
    "tegana": "teganau",
    "brojecta": "brojectau",
    "anabledda": "anableddau",
    "cyfrifoldeba": "cyfrifoldebau",
    "perthnasa'": "perthnasau",
    "adolygiada": "adolygiadau",
    "awdurdoda'": "awdurdodau",
    "polisia": "polisïau",
    "darpariaetha": "darpariaethau",
    "effeithia'": "effeithiau",
    "cyffuria": "cyffuriau",
    "delwedda'": "delweddau",
    "amgylchiada": "amgylchiadau",
    "ffactora'": "ffactorau",
    "oria": "oriau",
    "cwestiyna'": "cwestiynau",
    "adroddiada": "adroddiadau",
    "trefniada": "trefniadau",
    "bwyntia'": "bwyntiau",
    "saithdega": "saithdegau",
    "chwedega": "chwedegau",
    "harddega": "harddegau",
    "disgwyliada": "disgwyliadau",
    "weithia": "weithiau",
    "weithia'": "weithiau",
    "sylwada": "sylwadau",

    # South forms (-e)
    "pethe": "pethau",
    "bethe": "bethau",
    "gore": "gorau",
    "coese": "coesau",
    "enwe": "enwau",
    "pwyse": "pwysau",
    "geirie": "geiriau",
    "ffrindie": "ffrindiau",
    "cymeriade": "cymeriadau",
    "effeithie": "effeithiau",
    "canlyniade": "canlyniadau",
    "potie": "potiau",
    "orie": "oriau",
    "delwedde": "delweddau",
    "astudiaethe": "astudiaethau",
    "risge": "risgiau",
    "anabledde": "anableddau",
    "trafodaethe": "trafodaethau",
    "terme": "termau",
    "elfenne": "elfennau",
    "cymwystere": "cymwysterau",
    "syniade": "syniadau",
    "asiantaethe": "asiantaethau",
    "gwasanaethe": "gwasanaethau",
    "radde": "raddau",
    "cyfrynge": "cyfryngau",
    "hawlie": "hawliau",
    "profiade": "profiadau",
    "brofiade": "brofiadau",
    "weithie": "weithiau",
    "resyme": "resymau",
    "idiome": "idiomau",
}

# ============================================================================
# VERB REDUCTIONS
# ============================================================================
VERB_REDUCTIONS = {
    "dechre": "dechrau",
    "dechra": "dechrau",
    "dechra'": "dechrau",
    "ddechre": "ddechrau",
    "gweitho": "gweithio",
    "gwithio": "gweithio",
    "withio": "weithio",
    "gwitho": "gweithio",
    "disgwl": "disgwyl",
    "gobitho": "gobeithio",
    "grando": "gwrando",
    "gwryndo": "gwrando",
    "gadal": "gadael",
    "gadel": "gadael",
    "gada'l": "gadael",
    "gade'l": "gadael",
    "adal": "adael",
    "cyrradd": "cyrraedd",
    "gyrradd": "gyrraedd",
    "diodde": "dioddef",
    "gyfadde": "gyfaddef",
    "gyfadda": "gyfaddef",
    "cwmpo": "cwympo",
    "lico": "licio",
    "timlo": "teimlo",
    "chwara": "chwarae",
    "chware": "chwarae",
    "clwad": "clywed",
    "clywad": "clywed",
    "glywad": "glywed",
    "glwad": "glywed",
    "cl'wad": "clywed",
    "deu": "dweud",
    "deud": "dweud",
    "deu'": "dweud",
    "ddeu": "ddweud",
    "weud": "ddweud",
    "deutha": "dweud wrth",
    "daetho": "dweud wrth",
    "ymatab": "ymateb",
    "myn'": "mynd",
    "arfar": "arfer",
    "ymarfar": "ymarfer",
    "bita": "bwyta",
    "dadla": "dadlau",
    "ffindio": "ffeindio",
    "ffeithio": "effeithio",
    "cerddad": "cerdded",
    "iste": "eistedd",
    "cyfadda": "cyfaddef",
    "gorffan": "gorffen",
    "darllan": "darllen",
    "edrach": "edrych",
    "angan": "angen",
    "hangan": "hangen",
    "gweud": "dweud",
    "roid": "roi",
    "rhoid": "rhoi",
    "styried": "ystyried",
    "ystyriad": "ystyried",
    "atab": "ateb",
    "wela'": "welaf",
    "gwel'": "gweld",
    "ath": "aeth",
    "dath": "daeth",
    "ddath": "ddaeth",
    "ddoth": "ddaeth",
    "'wharae": "chwarae",
    "'drycha": "edrycha",
    "'drychwch": "edrychwch",
    "ty'd": "tyrd",
    "'nabod": "adnabod",
    "gwbod": "gwybod",
    "gwbo": "gwybod",
    "gwy'": "gwybod",
    "gw'bo'": "gwybod",
    "wbod": "wybod",
    "w'bod": "wybod",
    "me'wl": "meddwl",
    "mewl": "meddwl",
    "me'l": "meddwl",
    "m'wl": "meddwl",
    "meddw'": "meddwl",
    "cymyd": "cymryd",
    "cymud": "cymryd",
    "dalld": "deall",
    "diall": "deall",
    "deallt": "deall",
    "camtrin": "cam-trin",
    "cyffwr": "cyffwrdd",
    "sicrau": "sicrhau",
    "cydnabot": "cydnabod",
    "sy": "sydd",
    "su'": "sydd",
    "sy'": "sydd",
    "isie": "eisiau",
    "isia": "eisiau",
    "isio": "eisiau",
    "isio'i": "eisiau ei",
    "isio'u": "eisiau eu",
    "eisia": "eisiau",
    "gafal": "gafael",
    "angofio": "anghofio",
}

# ============================================================================
# ADJECTIVE REDUCTIONS - AF
# ============================================================================
ADJECTIVE_REDUCTIONS = {
    "nesa": "nesaf",
    "nesa'": "nesaf",
    "ola": "olaf",
    "ola'": "olaf",
    "gora": "gorau",
    "gora'": "gorau",
    "ora'": "orau",
    "cynta": "cyntaf",
    "cynta'": "cyntaf",
    "gynta'": "gyntaf",
    "gynta": "gyntaf",
    "cynhara": "cynharaf",
    "eitha": "eithaf",
    "eitha'": "eithaf",
    "itha": "eithaf",
    "mwya": "mwyaf",
    "mwya'": "mwyaf",
    "fwya'": "fwyaf",
    "fwya": "fwyaf",
    "isa": "isaf",
    "gry": "gryf",
    "ifan'": "ifanc",
    "gra": "gryf",
    "gre": "gref",
    "uchal": "uchel",
}

# ============================================================================
# VOWEL REDUCTIONS - INTERNAL
# ============================================================================
INTERNAL_REDUCTIONS = {
    "m'wn": "mewn",
    "mew'": "mewn",
    "meddwlgarwch": "meddylgarwch",
    "sicir": "sicr",
    "amsar": "amser",
    "mowr": "mawr",
    "amal": "aml",
    "wthnos": "wythnos",
    "wsos": "wythnos",
    "ymlan": "ymlaen",
    "hunen": "hunain",
    "angenion": "anghenion",
    "hannar": "hanner",
    "hwna": "hwnna",
    "ynny": "hynny",
    "hynna'": "hynnaf",
    "'ynny": "hynny",
    "'ny": "hynny",
    "yne": "hynny",
    "chydig": "ychydig",
    "chdig": "ychydig",
    "rei": "rhai",
    "rhei": "rhai",
    "eryll": "eraill",
    "hunianiaeth": "hunaniaeth",
    "hunanieth": "hunaniaeth",
    "ymwybyddieth": "ymwybyddiaeth",
    "trw": "trwy",
    "trw'r": "trwy'r",
    "drw": "drwy",
    "drw": "drwy",
    "drost": "dros",
    "wth": "wrth",
    "llawar": "llawer",
    "elle": "efallai",
    "ella": "efallai",
    "e'lla": "efallai",
    "gwanol": "gwahanol",
    "gwahaniath": "gwahaniaeth",
    "gwahanieth": "gwahaniaeth",
    "wahanieth": "wahaniaeth",
    "hydnod": "hyd yn oed",
    "hanas": "hanes",
    "cyfla": "cyfle",
    "enghraiff": "enghraifft",
    "enhraifft": "enghraifft",
    "pentre": "pentref",
    "pentra": "pentref",
    "cartra": "cartref",
    "cartre": "cartref",
    "traffath": "trafferth",
    "negas": "neges",
    "blesar": "bleser",
    "plesar": "pleser",
    "gynhenydd": "gynhenid",
    "ersdalwm": "ers dalwm",
    "problam": "problem",
    "broblam": "broblem",
    "cwbwl": "cwbl",
    "gwbwl": "gwbl",
    "dat": "dad",
    "amrywieth": "amrywiaeth",
    "ystol": "ystod",
    "pŵar": "pŵer",
    "cwricilwm": "cwricwlwm",
    "darpariath": "darpariaeth",
    "cymddeithasol": "cymdeithasol",
    "trosglwyddiadwy": "trosglwyddadwy",
    "ugian": "ugain",
    "ugen": "ugain",
    "bymthag": "bymtheg",
    "ddeugen": "ddeugain",
    "Portsmuth": "Portsmouth",
    "mown": "mewn",
    "withia": "weithiau",
    "withia'": "weithiau",
}

# ============================================================================
# SPELLING STANDARDIZATIONS
# ============================================================================
SPELLING_CORRECTIONS = {
    "gyment": "gymaint",
    "cyment": "cymaint",
    "rwbeth": "rhywbeth",
    "rwbath": "rhywbeth",
    "r'wbath": "rhywbeth",
    "wbath": "rhywbeth",
    "rhwbath": "rhywbeth",
    "rywbath": "rhywbeth",
    "rhwbeth": "rhywbeth",
    "rwle": "rywle",
    "gellu": "gallu",
    "efyd": "hefyd",
    "gwrnado": "gwrando",
    "cymra'g": "cymraeg",
    "gymra'g": "gymraeg",
    "gymraig": "gymraeg",
    "lloeger": "lloegr",
    "ytrach": "hytrach",
    "sicirhau": "sicrhau",
    "jys": "jyst",
    "sud": "sut",
    "be'": "beth",
    "be": "beth",
    "rhyfadd": "rhyfedd",
    "cymru": "Cymru",
    "gymru": "Gymru",
    "cymraeg": "Cymraeg",
    "gymraeg": "Gymraeg",
    "ewrop": "Ewrop",
    "sgandenafia": "Sgandinafia",
    "bobol": "bobl",
    "pobol": "pobl",
    "cwpwl": "cwpl",
    "powb": "pawb",
    "rywyn": "rywun",
    "rwun": "rywun",
    "unryw": "unrhyw",
    "ffor": "ffordd",
    "ginnon": "gennym",
    "ganddon": "gennym",
    "ginon": "gennym",
    "gennyn": "gennym",
    "genddyn": "ganddyn",
    "gannyn": "ganddyn",
    "sgynnoch": "oes gynnoch",
    "sgennych": "oes gennych",
    "dwytha": "diwetha",
    "dwetha": "diwetha",
    "'nde": "ynde",
    "nacdi": "nac ydi",
    "on'": "ond",
    "ont": "ond",
    "on'd": "onid",
    "ne'n": "neu'n",
    "ynnyn": "ynddyn",
    "ch'mod": "chi'n gwybod",
    "chi'mod": "chi'n gwybod",
    "ch'mo'": "chi'n gwybod",
    "ch'mo": "chi'n gwybod",
    "ch'mbo'": "chi'n gwybod",
    "d'chmod": "dach chi'n gwybod",
    "d'ch'mod": "dach chi'n gwybod",
    "d'ch'od": "dach chi'n gwybod",
    "dach'mod": "dach chi'n gwybod",
    "dach'bo'": "dach chi'n gwybod",
    "ch'bo'": "chi'n gwybod",
    "ch'od": "chi'n gwybod",
    "ch'bod": "chi'n gwybod",
    "dych'bo'": "dach chi'n gwybod",
    "dych'mod": "dach chi'n gwybod",
    "t'o'": "ti'n gwybod",
    "t'mo'": "ti'n gwybod",
    "t'bo'": "ti'n gwybod",
    "t'w'o'": "ti'n gwybod",
    "t'wo'": "ti'n gwybod",
    "t'wod": "ti'n gwybod",
    "t'": "ti'n gwybod",
    "ti'o'": "ti'n gwybod",
    "sti": "wyddost ti",
    "d'chi'n": "rydych chi'n",
    "sbio": "sbïo",
    "ano": "arno",
    "ry": "rhy",
    "dou": "dau",
    "ddou": "ddau",
    "flan": "ymlaen",
    "dy'": "dydd",
    "camra": "camera",
    "barbiciw": "barbeciw",
    "capal": "capel",
    "nyrfys": "nerfus",
    "coedan": "coeden",
    "ogyn": "hogyn",
    "wedig": "enwedig",
    "fforyma": "fforymau",
    "cynor": "cyngor",
    "pethan": "petha'n",
    "osa": "oes yna",
    "jiom": "dydi o ddim",
    "diom": "dydi o ddim",
    "rhai'": "rhaid",
    "rai'": "raid",
    "mlynadd": "mlynedd",
    "blynadd": "blynedd",
    "flynadd": "flynedd",
    "adag": "adeg",
    "ama": "amau",
    "hy'": "hyd",
    "y'": "yn",
    "teuluodd": "teuluoedd",
    "deuluodd": "deuluoedd",
    "blynyddodd": "blynyddoedd",
}

# ============================================================================
# HESITATION STANDARDIZATION
# ============================================================================
HESITATION_STANDARDIZATION = {
    "yy": "yym",
    "yrm": "yym",
    "ymm": "yym",
    "yrr": "yym",
    #"hmm": "yym",
}

# ============================================================================
# CONTEXT RULES FOR MA'
# ============================================================================

# Lookup table for normalizing followers after "ma'"
# ma' ALWAYS becomes mae
# This maps the follower word to what the follower should become
# e.g., "ma' nw" -> "mae nhw" (nw becomes nhw)
#       "ma' nhw" -> "mae nhw" (nhw stays nhw)
#       "ma' wnna" -> "mae hwnna" (wnna becomes hwnna)
#       "ma' 'na" -> "mae 'na" ('na stays 'na)
MA_FOLLOWERS = {
    # Existential/possessive patterns (follower stays same)
    "'na": "yna",           # ma' 'na -> mae yna (there is)
    "na": "yna",            # ma' na -> mae yna
    "'di": "wedi",           # ma' 'di -> mae wedi
#    "'da": "gyda",           # ma' 'da fi -> mae gyda fi (I have)

    # Pronouns (follower normalized to standard form)
    "nw": "nhw",            # ma' nw -> mae nhw
    "n'w": "nhw",           # ma' n'w -> mae nhw
    "nw'": "nhw",           # ma' nw' -> mae nhw
    "nw'n": "nhw'n",        # ma' nw'n -> mae nhw'n
    "nw'm": "nhw'm",        # ma' nw'm -> mae nhw'm
    "fe": "fe",             # ma' fe -> mae fe
    "fe'n": "fe'n",         # ma' fe'n -> mae fe'n
    "o": "o",               # ma' o -> mae o
    "o'n": "o'n",           # ma' o'n -> mae o'n
    "hi": "hi",             # ma' hi -> mae hi
    "hi'n": "hi'n",         # ma' hi'n -> mae hi'n
    "nhw": "nhw",           # ma' nhw -> mae nhw
    "nhw'n": "nhw'n",       # ma' nhw'n -> mae nhw'n

    # Possession markers (follower stays same)
    "gen": "gen",           # ma' gen i -> mae gen i
    "genna": "genna",       # ma' genna i -> mae genna i
    "genno": "genno",       # ma' genno fo -> mae genno fo
    "genni": "genni",       # ma' genni -> mae genni
    "gyda": "gyda",         # ma' gyda fi -> mae gyda fi
    "gynnon": "gynnon",     # ma' gynnon ni -> mae gynnon ni
    "gynno": "gynno",       # ma' gynno fo -> mae gynno fo
    "gynni": "gynni",       # ma' gynni hi -> mae gynni hi
    "gynna": "gynna",       # ma' gynna i -> mae gynna i
    "gynnoch": "gynnoch",   # ma' gynnoch chi -> mae gynnoch chi
    "gennych": "gennych",   # ma' gennych chi -> mae gennych chi
    "gennyn": "gennyn",     # ma' gennyn nhw -> mae gennyn nhw
    "ganddyn": "ganddyn",   # ma' ganddyn nhw -> mae ganddyn nhw
    "ganddo": "ganddo",     # ma' ganddo (ni/fo) -> mae ganddo (ni/fo)


    # Demonstrative patterns (follower stays same or gets normalized)
    "hwnna": "hwnna",       # ma' hwnna -> mae hwnna
    "hwnna'n": "hwnna'n",   # ma' hwnna'n -> mae hwnna'n
    "honna": "honna",       # ma' honna -> mae honna
    "honna'n": "honna'n",   # ma' honna'n -> mae honna'n
    "hynny": "hynny",       # ma' hynny -> mae hynny
    "hynny'n": "hynny'n",   # ma' hynny'n -> mae hynny'n
    "hynna": "hynna",       # ma' hynna -> mae hynna
    "hynna'n": "hynna'n",   # ma' hynna'n -> mae hynna'n
    "hwn": "hwn",           # ma' hwn -> mae hwn
    "hon": "hon",           # ma' hon -> mae hon

    # Modal patterns (follower normalized to standard form)
    "raid": "rhaid",        # ma' raid -> mae rhaid (must)
    "rhaid": "rhaid",       # ma' rhaid -> mae rhaid
    "angen": "angen",       # ma' angen -> mae angen (need)
    "isio": "eisiau",       # ma' isio -> mae eisiau (want)
    "isho": "eisiau",       # ma' isho -> mae eisiau
    "isie": "eisiau",       # ma' isie -> mae eisiau
    "eisiau": "eisiau",     # ma' eisiau -> mae eisiau
    "'sha": "eisiau",       # ma' 'sha -> mae eisiau

    # Repetition (hesitation) (follower normalized to standard form)
    "ma'": "mae",           # ma' ma' -> mae mae
    "ma'r": "mae'r",        # ma' ma'r -> mae mae'r
    "ma'n": "mae'n",        # ma' ma'n -> mae mae'n
}

# ============================================================================
# CONTEXT RULES FOR 'DI
# ============================================================================

# Pronouns that precede 'di (safe to expand 'di → wedi after these)
DI_WEDI_SAFE_PRECEDERS = {
    "dwi", "dw", "fi", "i", "ti", "ni", "chi", "nhw", "nw", "n'w",
    "sy", "sydd", "oedd", "o'dd", "ma'", "mae", "e", "o"
}

# ============================================================================
# MULTI-WORD REPLACEMENTS
# ============================================================================

# Multi-word phrase replacements
# Format: "phrase in lowercase" : "normalized phrase"
# These are checked BEFORE single-word replacements
MULTI_WORD_REPLACEMENTS = {
    "o's gynnoch": "oes gynnoch",
    "o's gynno": "oes gynno",
    "o's gynni": "oes gynni",
    "o's gynna": "oes gynna",
    "o's gen": "oes gen",
    "o's gyda": "oes gyda",
    "o's 'na": "oes yna",
    "dan dred": "dan draed",
    "dan dra'": "dan draed",
    "neshi dweud": "nes i ddweud",
    "neshi deud": "nes i ddeud",
    "neshi wneud": "nes i wneud",
    "neshi neud": "nes i neud",
    "ti 'bo": "ti'n gwybod",
    "ti bo": "ti'n gwybod",
    "'na beth yw": "dyna beth yw",
    "na beth yw": "dyna beth yw",
    "fel 'na": "fel yna",
    "fel 'a": "fel yna",
    "fel na": "fel yna",
    "dwi'm": "dw i ddim",
    "dwim": "dw i ddim",
    "dwi'n": "dw i'n",
}
