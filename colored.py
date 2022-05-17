#*******
#colored
class color:
	BlackLIGHT = '\u001b[30m;1'
	RedLIGHT = '\u001b[31m;1'
	GreenLIGHT = '\u001b[32;1m'
	YellowLIGHT = '\u001b[33;1m'
	BlueLIGHT = '\u001b[34;1m'
	MagentaLIGHT = '\u001b[35;1m'
	CyanLIGHT = '\u001b[36;1m'
	WhiteLIGHT = '\u001b[37;1m'
	
	Black = '\u001b[30m'
	Red = '\u001b[31m'
	Green = '\u001b[32m'
	Yellow = '\u001b[33m'
	Blue = '\u001b[34m'
	Magenta = '\u001b[35m'
	Cyan = '\u001b[36m'
	White = '\u001b[37m'

class background:
	Reset = '\u001b[0m'
	Black = '\u001b[40m'
	Red = '\u001b[41m'
	Green = '\u001b[42m'
	Yellow = '\u001b[43m'
	Blue = '\u001b[44m'
	Magenta = '\u001b[45m'
	Cyan = '\u001b[46m'
	White = '\u001b[47m'
	
class style:
	Reset = '\u001b[0m'
	Bold = '\033[1m'
	Underline = '\033[4m'
print(f'{color.BlueLIGHT}{background.Red}Warning{style.Reset}')