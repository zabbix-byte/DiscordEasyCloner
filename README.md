# DiscordEasyCloner | Build in [**Pypulse**](https://github.com/zabbix-byte/PyPulse)
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fzabbix-byte%2FDiscordEasyCloner%2F&countColor=%23263759)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge&logo=windows&logoColor=white)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.8-blue?style=for-the-badge&logo=windows&logoColor=white)](https://www.python.org/downloads/)
[![Github-sponsors](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=white)](https://github.com/sponsors/zabbix-byte)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
[![](https://img.shields.io/github/downloads/zabbix-byte/DiscordEasyCloner/v1.1/total?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/zabbix-byte/DiscordEasyCloner/releases/download/v1.1/DiscordEasyCloner_portable.zip)

**🌀DiscordEasyCloner**, a straightforward app that simplifies the process of duplicating Discord servers.

![](https://github.com/zabbix-byte/DiscordEasyCloner/blob/main/aplication_preview.png)

## Util Info 💡
- #### Get the Discord server ID https://www.alphr.com/discord-find-server-id/
- #### Get Authentication Token https://gist.github.com/MarvNC/e601f3603df22f36ebd3102c501116c6

## Compile for [Windows OS] 🛠️
**Please Note**: Compatible with Python 3.8 🐍
### 1. Nuitka Installation Instructions 📥
```sh
python -m pip install -U nuitka
```
### 2. Install requirements 🐍
```sh
pip install -r requirements.txt
```
### 3. Running Command (This process may require some time) 🔄

**PowerShell**
```sh
nuitka --mingw64 --standalone --disable-console --plugin-enable=multiprocessing --show-memory --show-progress --output-dir=output --include-module=baseapp --include-data-file=window_logo.ico=. --include-data-file=data.json=. --include-data-dir=templates=templates  --include-data-dir=static=static .\DiscordEasyCloner.py ; xcopy baseapp output\DiscordEasyCloner.dist\baseapp /i /s
```
**CMD**
```sh
nuitka --mingw64 --standalone --disable-console --plugin-enable=multiprocessing --show-memory --show-progress --output-dir=output --include-module=baseapp --include-data-file=window_logo.ico=. --include-data-file=data.json=. --include-data-dir=templates=templates  --include-data-dir=static=static .\DiscordEasyCloner.py && xcopy baseapp output\DiscordEasyCloner.dist\baseapp /i /s
```
**The compiled file can be found in the "output/bin" folder**

## Contributing 🤝
We welcome contributions from the community. If you'd like to contribute to mytool, please follow these guidelines:

- Fork the repository.
- Make your changes.
- Submit a pull request.

## 💌 Contact & [Sponsor](https://github.com/sponsors/zabbix-byte)

If you have any questions, suggestions, or feedback, please don't hesitate to reach out to us at [zabbix@ztrunk.space](mailto:zabbix@ztrunk.space).

We hope PyPulse accelerates your desktop application development and simplifies the integration of web content into your Python projects. Happy coding! 😎🚀


