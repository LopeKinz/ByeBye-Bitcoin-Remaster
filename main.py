import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
import time
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

checked = 0


def get_wallet_info(wallet):
    getwallet = str(wallet.getText()).strip()
    privkey, uncompaddy, compaddy, balance = map(str.strip, getwallet.split()[:4])
    return privkey, uncompaddy, compaddy, balance


def process_wallet(wallet):
    global checked
    privkey, uncompaddy, compaddy, balance = get_wallet_info(wallet)
    if "Private Key" in getwallet:
        return

    checked += 1
    try:
        balance = float(balance)
        if balance > 0:
            with open('hits.txt', 'a+') as hits_file:
                hits_file.write(f"{balance} BTC found in Address: {compaddy} // Private Key: {privkey}\n")

        os.system("cls")
        os.system(f"title Bye Bye Bitcoin // Checked Wallets: {checked} // by clout")
        logging.info(f"""
        .-.____________________.-.
 ___ _.' .-----.    _____________|======+-----------------------+
/_._/   (      |   /_____________|       |   Bye Bye Bitcoin    |
  /      `  _ ____/                      |      by clout        |
 |_      .\( \\                          |_Remaster by Lopekinz_|
.'  `-._/__`_//
.'       |'           Private Key: {privkey}
/        /             Uncompressed Address: {uncompaddy}
/        |              Compressed Address: {compaddy}
|        '              Balance: {balance}
|        |
`-._____.-'""")
    except ValueError:
        # Failed to convert balance to float
        return


while True:
    os.system(f"title Bye Bye Bitcoin // Checked Wallets: {checked} // by clout")
    url = "https://www.bitcoinlist.io/random"
    headers = CaseInsensitiveDict()
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
    try:
        with requests.Session() as session:
            req = session.get(url, headers=headers)
            req.raise_for_status()
            soup = BeautifulSoup(req.content, 'html.parser')
            wallets = soup.find_all("tr")
            for wallet in wallets:
                process_wallet(wallet)
    except requests.RequestException as e:
        logging.error(f"Request failed: {e}")

    time.sleep(0.5)
