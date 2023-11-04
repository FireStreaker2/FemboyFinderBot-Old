![FemboyFinderBot](https://socialify.git.ci/FireStreaker2/FemboyFinderBot/image?description=1&forks=1&issues=1&logo=https%3A%2F%2Fi.pinimg.com%2F736x%2F50%2F77%2F1f%2F50771f45b1c015cfbb8b0853ba7b8521.jpg&name=1&owner=1&pulls=1&stargazers=1&theme=Dark)

# History
This is the repository for the old version of [FemboyFinderBot](http://github.com/FireStreaker2/FemboyFinderBot). It will still be maintained, but new updates will be primarily for the newer version.

# About
FemboyFinderBot-Old is a Discord bot written in Python. It utilizes the <a href="https://github.com/FireStreaker2/FemboyFinder#api">FemboyFinder API</a> to bring FemboyFinder to Discord!

# Usage
FemboyFinderBot can be invited to servers <a href="https://discord.com/oauth2/authorize?&client_id=1132490986736582736&scope=bot&permissions=274877908992">here</a>

The default prefix is ``.``, which can be changed if you are selfhosting the bot.

## Commands
| Command        | Description             |
| ---------------|-------------------------|
| .find [query]  | Find a femboy!          |
| .about         | Sends an about message. |
| .stats         | Sends the bot's stats.  |
| .help          | Sends a help message.   |

> Please note that if you are using the ``.find`` command, the channel you are currently in **must** be either marked as NSFW or be a DM channel before you can run the command.

# Selfhosting
If you would like to selfhost this, you may.
```bash
$ git clone https://github.com/FireStreaker2/FemboyFinderBot.git
$ cd FemboyFinderBot
$ pip install -r requirements.txt
$ cp .env.example .env
# put bot token into .env file 
$ python main.py
```

# Configuration
If you are selfhosting this bot, you can easily configure it to your needs. The configuration options below can be found in ``main.py``, lines 11-14.
```py
config = {
    "Prefix": ".", # bot prefix
    "Status": "Femboys", # what the bot is "watching" 
}
```

Also be sure to enable the ``Message Content Intent`` in your developer panel so the bot will work.

# Support
For support regarding FemboyFinderBot, you can join our Discord server:
[![Support Server](https://invidget.switchblade.xyz/bruQhB8Eg5?theme=dark)](https://discord.gg/bruQhB8Eg5)

# License
<a href="https://github.com/FireStreaker2/FemboyFinderBot/blob/main/LICENSE">MIT</a>