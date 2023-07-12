# ByeBye-Bitcoin-Remaster

ByeBye-Bitcoin-Remaster is a Python script that checks random Bitcoin Private Keys for non-zero balances and logs the results.

## Features

- Retrieves random Bitcoin private keys from bitcoinlist.io
- Checks the balance of each wallet
- Logs wallets with non-zero balances to a file (`hits.txt`)
- Displays wallet information in the console
- Uses requests, BeautifulSoup, and logging libraries

## Requirements

- Python 3.7 or above
- Install the required packages using the command: `pip install -r requirements.txt`

## Usage

1. Clone the repository:

   ```shell
   git clone https://github.com/lopekinz/ByeBye-Bitcoin-Remaster.git
   ```

2. Change to the project directory:

   ```shell
   cd ByeBye-Bitcoin-Remaster
   ```

3. Install the required packages:

   ```shell
   pip install -r requirements.txt
   ```

4. Run the script:

   ```shell
   python byebye_bitcoin.py
   ```

5. The script will continuously check random Bitcoin wallets and display the results in the console. Wallets with non-zero balances will be logged in the `hits.txt` file.

## Configuration

You can customize the script by modifying the following variables:

- `url`: The URL of the website that provides random Bitcoin wallets.
- `headers`: Custom headers for the HTTP requests (User-Agent).
- `time.sleep()`: The delay between wallet checks (in seconds).

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

- This script is for educational purposes only. Use it responsibly and at your own risk.
- Be cautious when interacting with websites or APIs that provide random wallets. Verify the source and legality before using any wallet information.

