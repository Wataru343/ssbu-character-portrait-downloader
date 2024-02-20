import os
import urllib.request

base_url="https://www.smashbros.com/assets_v2/img/fighter"
character_list = [
    "mario",
    "donkey_kong",
    "link",
    "samus",
    "dark_samus",
    "yoshi",
    "kirby",
    "fox",
    "pikachu",
    "luigi",
    "ness",
    "captain_falcon",
    "jigglypuff",
    "peach",
    "daisy",
    "bowser",
    "ice_climbers",
    "sheik",
    "zelda",
    "dr_mario",
    "pichu",
    "falco",
    "marth",
    "lucina",
    "young_link",
    "ganondorf",
    "mewtwo",
    "roy",
    "chrom",
    "mr_game_and_watch",
    "meta_knight",
    "pit",
    "dark_pit",
    "zero_suit_samus",
    "wario",
    "snake",
    "ike",
    "pokemon_trainer",
    "diddy_kong",
    "lucas",
    "sonic",
    "king_dedede",
    "olimar",
    "lucario",
    "robot",
    "toon_link",
    "wolf",
    "villager",
    "mega_man",
    "wii_fit_trainer",
    "rosalina_and_luma",
    "little_mac",
    "greninja",
    "mii_brawler",
    "mii_swordfighter",
    "mii_gunner",
    "palutena",
    "pac_man",
    "robin",
    "shulk",
    "bowser_jr",
    "duck_hunt",
    "ryu",
    "ken",
    "cloud",
    "corrin",
    "bayonetta",
    "inkling",
    "ridley",
    "simon",
    "richter",
    "king_k_rool",
    "isabelle",
    "incineroar",
    "piranha_plant",
    "joker",
    "dq_hero",
    "banjo_and_kazooie",
    "terry",
    "byleth",
    "minmin",
    "steve",
    "sephiroth",
    "pyra",
    "kazuya",
    "sora"
    ]


for i, character in enumerate(character_list, start=1):
    os.makedirs(f"{os.path.curdir}/{str(i).zfill(2)}.{character}", exist_ok=True)

    if i <= 53 or i >= 57:
        for j in range(1, 9):
            if j == 1:
                url = f"{base_url}/{character}/main.png"
            else:
                url = f"{base_url}/{character}/main{j}.png"
            save_name=f"{os.path.curdir}/{str(i).zfill(2)}.{character}/{j}.png"

            print(f"Downloading {url} to {save_name}")
            urllib.request.urlretrieve(url, save_name)
    elif i == 54:
        urllib.request.urlretrieve("https://www.ssbwiki.com/images/archive/e/e4/20180703015005%21Mii_Brawler_SSBU.png", f"{os.path.curdir}/{str(i).zfill(2)}.{character}/1.png")
    elif i == 55:
        urllib.request.urlretrieve("https://www.ssbwiki.com/images/archive/f/fa/20180703015048%21Mii_Swordfighter_SSBU.png", f"{os.path.curdir}/{str(i).zfill(2)}.{character}/1.png")
    elif i == 56:
        urllib.request.urlretrieve("https://www.ssbwiki.com/images/archive/e/e5/20180703015051%21Mii_Gunner_SSBU.png", f"{os.path.curdir}/{str(i).zfill(2)}.{character}/1.png")
