from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kb1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Al-Fatihah", callback_data="fa"),
        InlineKeyboardButton(text="Al-Baqarah", callback_data="ba")
    ],
    [
        InlineKeyboardButton(text="Aali Imran", callback_data="im"),
        InlineKeyboardButton(text="An-Nisa’", callback_data="ni")
    ],
    [
        InlineKeyboardButton(text="Al-Ma’idah", callback_data="ma"),
        InlineKeyboardButton(text="Al-An’am", callback_data="ana")
    ],
    [
        InlineKeyboardButton(text="Al-A’raf", callback_data="ara"),
        InlineKeyboardButton(text="Al-Anfal", callback_data="anf")
    ],
    [
        InlineKeyboardButton(text="At-Taubah", callback_data="ta"),
        InlineKeyboardButton(text="Yunus", callback_data="yun")
    ],
    [
        InlineKeyboardButton(text="Hud", callback_data="hu"),
        InlineKeyboardButton(text="Yusuf", callback_data="yu")
    ],
    [
        InlineKeyboardButton(text="Ar-Ra’d", callback_data="rad"),
        InlineKeyboardButton(text="Ibrahim", callback_data="ib")
    ],
    [
        InlineKeyboardButton(text="Al-Hijr", callback_data="hi"),
        InlineKeyboardButton(text="An-Nahl", callback_data="nah")
    ],
    [
        InlineKeyboardButton(text="Al-Isra’", callback_data="is"),
        InlineKeyboardButton(text="Al-Kahf", callback_data="kaf")
    ],
    [
        InlineKeyboardButton(text="Maryam", callback_data="mar"),
        InlineKeyboardButton(text="Ta-Ha", callback_data="taha")
    ],
    [
        InlineKeyboardButton(text="Next", callback_data="nex1")
    ]
])

kb2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Al-Anbiya’", callback_data="anb"),
        InlineKeyboardButton(text="Al-Haj", callback_data="haj")
    ],
    [
        InlineKeyboardButton(text="Al-Mu’minun", callback_data="mum"),
        InlineKeyboardButton(text="An-Nur", callback_data="nur")
    ],
    [
        InlineKeyboardButton(text="Al-Furqan", callback_data="fur"),
        InlineKeyboardButton(text="Ash-Shu’ara’", callback_data="shu")
    ],
    [
        InlineKeyboardButton(text="An-Naml", callback_data="nam"),
        InlineKeyboardButton(text="Al-Qasas", callback_data="qa")
    ],
    [
        InlineKeyboardButton(text="Al-Ankabut", callback_data="ank"),
        InlineKeyboardButton(text="Ar-Rum", callback_data="rum")
    ],
    [
        InlineKeyboardButton(text="Luqman", callback_data="luq"),
        InlineKeyboardButton(text="As-Sajdah", callback_data="saj")
    ],
    [
        InlineKeyboardButton(text="Al-Ahzab", callback_data="ah"),
        InlineKeyboardButton(text="Saba’", callback_data="saba")
    ],
    [
        InlineKeyboardButton(text="Al-Fat’h", callback_data="fath"),
        InlineKeyboardButton(text='Yaseen',callback_data='yas'),
        InlineKeyboardButton(text="Al-Hujurat", callback_data="huj")
    ],
    [
        InlineKeyboardButton(text="Qaf", callback_data="qaf"),
        InlineKeyboardButton(text="Adz-Dzariyah", callback_data="zar")
    ],
    [
        InlineKeyboardButton(text="At-Tur", callback_data="tur"),
        InlineKeyboardButton(text="An-Najm", callback_data="naj")
    ],
    [
        InlineKeyboardButton(text="Al-Qamar", callback_data="qam"),
        InlineKeyboardButton(text="Ar-Rahman", callback_data="rah")
    ],
    [
        InlineKeyboardButton(text="Al-Waqi’ah", callback_data="waq"),
        InlineKeyboardButton(text="Al-Hadid", callback_data="had")
    ],
    [
        InlineKeyboardButton(text="Al-Mujadilah", callback_data="muj"),
        InlineKeyboardButton(text="Al-Hashr", callback_data="hash")
    ],
    [
        InlineKeyboardButton(text="Al-Mumtahanah", callback_data="mumt"),
        InlineKeyboardButton(text="Back", callback_data="bk1")
    ],
    [
        InlineKeyboardButton(text="Next", callback_data="nex2")
    ]
])

kb3 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Fusilat", callback_data="fus"),
        InlineKeyboardButton(text="Ash-Shura", callback_data="shur")
    ],
    [
        InlineKeyboardButton(text="Az-Zukhruf", callback_data="zuk"),
        InlineKeyboardButton(text="Ad-Dukhan", callback_data="duk")
    ],
    [
        InlineKeyboardButton(text="Al-Jathiyah", callback_data="jat"),
        InlineKeyboardButton(text="Al-Ahqaf", callback_data="ahq")
    ],
    [
        InlineKeyboardButton(text="Muhammad", callback_data="mum"),
        InlineKeyboardButton(text="Al-Fat’h", callback_data="fath")
    ],
    [
        InlineKeyboardButton(text="Al-Hujurat", callback_data="huj"),
        InlineKeyboardButton(text="Qaf", callback_data="qaf")
    ],
    [
        InlineKeyboardButton(text="Adz-Dzariyah", callback_data="zar"),
        InlineKeyboardButton(text="At-Tur", callback_data="tur")
    ],
    [
        InlineKeyboardButton(text="An-Najm", callback_data="naj"),
        InlineKeyboardButton(text="Al-Qamar", callback_data="qam")
    ],
    [
        InlineKeyboardButton(text="Ar-Rahman", callback_data="rah"),
        InlineKeyboardButton(text="Al-Waqi’ah", callback_data="waq")
    ],
    [
        InlineKeyboardButton(text="Al-Hadid", callback_data="had"),
        InlineKeyboardButton(text="Al-Mujadilah", callback_data="muj")
    ],
    [
        InlineKeyboardButton(text="Al-Hashr", callback_data="hash"),
        InlineKeyboardButton(text="Al-Mumtahanah", callback_data="mumt")
    ],
    [
        InlineKeyboardButton(text="Back", callback_data="bk2"),
        InlineKeyboardButton(text="Next", callback_data="nex3")
    ]
])

kb4 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="As-Saf", callback_data="saf"),
        InlineKeyboardButton(text="Al-Jum’ah", callback_data="juma")
    ],
    [
        InlineKeyboardButton(text="Al-Munafiqun", callback_data="muna"),
        InlineKeyboardButton(text="At-Taghabun", callback_data="taga")
    ],
    [
        InlineKeyboardButton(text="At-Talaq", callback_data="tala"),
        InlineKeyboardButton(text="At-Tahrim", callback_data="tahr")
    ],
    [
        InlineKeyboardButton(text="Al-Mulk", callback_data="mul"),
        InlineKeyboardButton(text="Al-Qalam", callback_data="qal")
    ],
    [
        InlineKeyboardButton(text="Al-Haqqah", callback_data="haq"),
        InlineKeyboardButton(text="Al-Ma’arij", callback_data="maar")
    ],
    [
        InlineKeyboardButton(text="Nuh", callback_data="nuh"),
        InlineKeyboardButton(text="Al-Jinn", callback_data="jin")
    ],
    [
        InlineKeyboardButton(text="Al-Muzammil", callback_data="muzam"),
        InlineKeyboardButton(text="Al-Mudaththir", callback_data="muda")
    ],
    [
        InlineKeyboardButton(text="Al-Qiyamah", callback_data="qi"),
        InlineKeyboardButton(text="Al-Insan", callback_data="ins")
    ],
    [
        InlineKeyboardButton(text="Al-Mursalat", callback_data="murs"),
        InlineKeyboardButton(text="An-Naba'", callback_data="nab")
    ],
    [
        InlineKeyboardButton(text="An-Nazi’at", callback_data="nazi"),
        InlineKeyboardButton(text="Abasa", callback_data="aba")
    ],
    [
        InlineKeyboardButton(text="Back", callback_data="bk3"),
        InlineKeyboardButton(text="Next", callback_data="nex4")
    ]
])

kb5 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="At-Takwir", callback_data="tawk"),
        InlineKeyboardButton(text="Al-Infitar", callback_data="inf")
    ],
    [
        InlineKeyboardButton(text="Al-Mutaffifin", callback_data="muta"),
        InlineKeyboardButton(text="Al-Inshiqaq", callback_data="inshi")
    ],
    [
        InlineKeyboardButton(text="Al-Buruj", callback_data="bur"),
        InlineKeyboardButton(text="At-Tariq", callback_data="tari")
    ],
    [
        InlineKeyboardButton(text="Al-A’la", callback_data="ala"),
        InlineKeyboardButton(text="Al-Ghashiyah", callback_data="gash")
    ],
    [
        InlineKeyboardButton(text="Al-Fajr", callback_data="faj"),
        InlineKeyboardButton(text="Al-Balad", callback_data="bala")
    ],
    [
        InlineKeyboardButton(text="Ash-Shams", callback_data="sham"),
        InlineKeyboardButton(text="Al-Layl", callback_data="layl")
    ],
    [
        InlineKeyboardButton(text="Adh-Dhuha", callback_data="duha"),
        InlineKeyboardButton(text="Al-Inshirah", callback_data="inshir")
    ],
    [
        InlineKeyboardButton(text="At-Tin", callback_data="tin"),
        InlineKeyboardButton(text="Al-‘Alaq", callback_data="alaq")
    ],
    [
        InlineKeyboardButton(text="Al-Qadar", callback_data="qad"),
        InlineKeyboardButton(text="Al-Bayinah", callback_data="bayi")
    ],
    [
        InlineKeyboardButton(text="Az-Zalzalah", callback_data="zal"),
        InlineKeyboardButton(text="Al-‘Adiyah", callback_data="adi")
    ],
    [
        InlineKeyboardButton(text="Back", callback_data="bk4"),
        InlineKeyboardButton(text="Next", callback_data="nex5")
    ]
])

kb6 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Al-Qari’ah", callback_data="qari"),
        InlineKeyboardButton(text="At-Takathur", callback_data="taka")
    ],
    [
        InlineKeyboardButton(text="Al-‘Asr", callback_data="asr"),
        InlineKeyboardButton(text="Al-Humazah", callback_data="huma")
    ],
    [
        InlineKeyboardButton(text="Al-Fil", callback_data="fil"),
        InlineKeyboardButton(text="Quraish", callback_data="qur")
    ],
    [
        InlineKeyboardButton(text="Al-Ma’un", callback_data="mau"),
        InlineKeyboardButton(text="Al-Kauthar", callback_data="kau")
    ],
    [
        InlineKeyboardButton(text="Al-Kafirun", callback_data="kafi"),
        InlineKeyboardButton(text="An-Nasr", callback_data="nasr")
    ],
    [
        InlineKeyboardButton(text="Al-Masad", callback_data="masad"),
        InlineKeyboardButton(text="Al-Ikhlas", callback_data="ikhlas")
    ],
    [
        InlineKeyboardButton(text="Al-Falaq", callback_data="flaq"),
        InlineKeyboardButton(text="An-Nas", callback_data="nas")
    ],
    [
        InlineKeyboardButton(text="Back", callback_data="bk5"),
        InlineKeyboardButton(text="Main Menu ✅", callback_data="main_menu")
    ]
])

pages = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Page 1 ▶️", callback_data="pg1"),
        InlineKeyboardButton(text="Page 2 ▶️", callback_data="pg2")
    ],
    [
        InlineKeyboardButton(text="Page 3 ▶️", callback_data="pg3"),
        InlineKeyboardButton(text="Page 4 ▶️", callback_data="pg4"),
    ],
    [
        InlineKeyboardButton(text="Page 5 ▶️", callback_data="pg5"),
        InlineKeyboardButton(text="Page 6 ▶️", callback_data="pg6")
    ]

])
