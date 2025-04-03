# Monad Testnet Automation

## Requirements
- Python 3.11 or higher
- Git

## Installation

1. Clone the repository
```bash
git clone https://github.com/0xFAREIAN/FAREIAN-Monad.git
cd FAREIAN-Monad
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Set up your data files:
   - Copy the template files from `data/*.txt.template` to `data/*.txt`
   - Add your data to the following files:
     - `data/private_keys.txt` - One private key per line
     - `data/proxies.txt` - One proxy per line (format: `user:pass@ip:port`)
     - `data/keys_for_faucet.txt` - One private key per line
     - `data/twitter_tokens.txt` - One Twitter auth token per line

4. Configure the bot:
   - Run `python main.py`
   - Choose the edit config option
   - Adjust settings in `config.yaml` as needed

5. Run the bot
```bash
python main.py
```

## Configuration

The bot can be configured through `config.yaml`. Key settings include:
- Transaction amounts
- Wait times
- Task sequences
- API endpoints

## Security Notes

- Never commit your private keys or sensitive data
- The `.gitignore` file is configured to exclude sensitive data
- Always use template files for data configuration

## Support

For support, please refer to:
- Telegram: https://t.me/FAREIANTech
- Chat: https://t.me/FAREIANChat
