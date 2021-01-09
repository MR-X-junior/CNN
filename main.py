#coding=utf-8
from os.path import basename as program
from os import system
from urllib.parse import quote as parse
from sys import *
from datetime import datetime
from time import sleep
from json import *
from urllib.request import urlopen as buka

"""
API : https://github.com/rizki4106/cnnindonesia-news-api
SCRIPT DI TULIS OLEH : RAHMAT ADHA ( Programmer Noob :))
"""

def command():
	try:
		if argv[-1] == 'nasional':
			nasional()
		elif argv[-1] == 'internasional':
			internasional()
		elif argv[-1] == 'ekonomi':
			ekonomi()
		elif argv[-1] == 'olahraga':
			olahraga()
		elif argv[-1] == 'teknologi':
			teknologi()
		elif argv[-1] == 'hiburan':
			hiburan()
		elif argv[-1] == 'gaya_hidup':
			gaya_hidup()
		elif argv[-1] == 'cari':
			Cari()
		else:
			print (f'\033[97mNo command {argv[-1]} found')
	except Exception as err:
		print (f'\033[93m[!] {err}')

#CEK KONEKSI INTERNET
def koneksi():
	try:
		buka('http://216.58.192.142', timeout = 3)
		return True
	except:
		exit ('\033[91mTIDAK ADA \033[4mKONEKSI\033[0m')

satu = """\033[94m****     **** *******     **     **\n/**/**   **/**/**////**   //**   ** \n/**//** ** /**/**   /**    //** **  \n/** //***  /**/*******      //***   \n/**  //*   /**/**///**       **/**  \n/**   /    /**/**  //**     ** //** \n/**        /**/**   //**   **   //**\n//         // //     //   //     // """
dua = """\033[91m                                 \n@@@@@@@@@@   @@@@@@@      @@@  @@@  \n@@@@@@@@@@@  @@@@@@@@     @@@  @@@  \n@@! @@! @@!  @@!  @@@     @@!  !@@  \n!@! !@! !@!  !@!  @!@     !@!  @!!  \n@!! !!@ @!@  @!@!!@!       !@@!@!   \n!@!   ! !@!  !!@!@!         @!!!    \n!!:     !!:  !!: :!!       !: :!!   \n:!:     :!:  :!:  !:!     :!:  !:!  \n:::     ::   ::   :::      ::  :::  \n:      :     :   : :      :   ::                                  """

def tabel_waktu(a):
	versi = version[0] + version[1] + version[2] + version[3] + version [4]
	print (a)
	
	sekarang = datetime.now()

	hari = sekarang.day
	
	bulan = sekarang.month
	
	tahun = sekarang.year
	
	jam = sekarang.hour
	
	menit = sekarang.minute
	
	detik = sekarang.second
	
	tahun = sekarang.year
	
	print ("\033[91m╔═════════════════════════════════════╗\n║\033[91m[\033[93m•\033[91m] \033[92mAuthor : \033[93mMR-X JUNIOR             ║\n║\033[91m[\033[93m•\033[91m] \033[92mGitHub : \033[94mgithub.com/MR-X-Junior  ║\n║\033[91m[\033[93m•\033[91m] \033[92mWA.    : \033[95m+6285754629509          ║\n║\033[91m[\033[93m•\033[91m] \033[92mUPDATE : \033[96m9-1-2021 11:09       ║")
	print ("\033[92m║\033[91m[\033[93m•\033[91m] \033[92mDATE   : \033[93m{}-\033[94m{}-\033[95m{} \033[96m{}:\033[96m{}:\033[96m{}     |\n|\033[91m[\033[93m•\033[91m] \033[92mOS     : \033[96m\033[91m{}      \033[95m             |\n║\033[91m[\033[93m•\033[91m] \033[92mSCRIPT : \033[93m{}                 ║\n║\033[91m[\033[93m•\033[91m] \033[92mPYTHON : \033[93m{}                   ║\n|\033[91m[\033[93m•\033[91m] \033[92mVERSI  : \033[96m\033[92m1.0       \033[95m              |\n\033[97m╚═════════════════════════════════════╝".format(hari, bulan, tahun, jam, menit, detik, platform,program(argv[0]),versi))
	
#MENU UTAMA
def main():
	system('clear')
	try:
		tabel_waktu(satu) ; koneksi() ; print ('\033[95mCNN \033[91mINDO\033[97mNESIA') ; print (20* '\033[96m=')
		a = int(input('\033[94m[\033[91m1\033[94m] \033[92mNASIONAL\n\033[94m[\033[91m2\033[94m] \033[93mINTERNASIONAL\n\033[94m[\033[91m3\033[94m] \033[94mEKONOMI\n\033[94m[\033[91m4\033[94m] \033[95mOLAHRAGA\n\033[94m[\033[91m5\033[94m] \033[96mTEKNOLOGI\n\033[94m[\033[91m6\033[94m] \033[97mHIBURAN\n\033[94m[\033[91m7\033[94m] \033[92mGAYA HIDUP\n\033[94m[\033[91m8\033[94m] \033[93mPENCARIAN BERITA\n\033[94m[\033[91m0\033[94m] \033[91mKELUAR\n\033[92m>>> \033[93m'))
		if a == 1:
			nasional()
		elif a == 2:
			internasional()
		elif a == 3:
			ekonomi()
		elif a == 4:
			olahraga()
		elif a == 5:
			teknologi()
		elif a == 6:
			hiburan()
		elif a == 7:
			gaya_hidup()
		elif a == 8:
			Cari()
		else:
			print ('\033[93m[!] PILIHAN TIDAK TERSEDIA') ; sleep(3) ; main()
	except KeyboardInterrupt:
		exit()
	except ValueError as ab:
		print (f'\033[93m[!] {ab}') ; sleep(3) ; main()
	except Exception as err:
		print (f'\033[93m[!] {err}')

def nasional():
	total = 0
	Nasional = "https://www.news.developeridn.com/nasional"
	system ('clear')
	try:
		tabel_waktu(dua) ; print ('\033[97mNASIONAL') ; print (20* '\033[93m=')
		a = buka(Nasional)
		b = loads(a.read())
		for c in b['data']:
			print (f"\033[92m[✓] JUDUL : \033[93m{c['judul']}")
			print (f"\033[92m[✓] LINK : \033[94m{c['link']}")
			print (f"\033[92m[✓] TIPE : \033[95m{c['tipe']}")
			print (f"\033[92m[✓] WAKTU : \033[96m{c['waktu']}\n\n")
			total += 1
		print ('\033[93mTotal : \033[95m',total)
	except KeyboardInterrupt:
		exit()
	except Exception as err:
		print (f'\033[93m[!] {err}')

def internasional():
	total = 0
	Internasional = "https://www.news.developeridn.com/internasional"
	system('clear')
	try:
		tabel_waktu(dua) ; print ('\033[97mINTERNASIONAL') ; print (20* '\033[93m=')
		a = buka(Internasional)
		b = loads(a.read())
		for c in b['data']:
			print (f"\033[92m[✓] JUDUL : \033[93m{c['judul']}")
			print (f"\033[92m[✓] LINK : \033[94m{c['link']}")
			print (f"\033[92m[✓] TIPE : \033[95m{c['tipe']}")
			print (f"\033[92m[✓] WAKTU : \033[96m{c['waktu']}\n\n")
			total += 1
		print ('\033[93mTotal : \033[95m',total)
	except KeyboardInterrupt:
		exit()
	except Exception as err:
		print (f'\033[93m[!] {err}')
		
def ekonomi():
	Ekonomi = "https://www.news.developeridn.com/ekonomi"
	system('clear')
	total = 0
	try:
		tabel_waktu(dua) ; print ('\033[97mEKONOMI') ; print (20* '\033[93m=')
		a = buka(Ekonomi)
		b = loads(a.read())
		for c in b['data']:
			print (f"\033[92m[✓] JUDUL : \033[93m{c['judul']}")
			print (f"\033[92m[✓] LINK : \033[94m{c['link']}")
			print (f"\033[92m[✓] TIPE : \033[95m{c['tipe']}")
			print (f"\033[92m[✓] WAKTU : \033[96m{c['waktu']}\n\n")
			total += 1
		print ('\033[93mTotal : \033[95m',total)
	except KeyboardInterrupt:
		exit()
	except Exception as err:
		print (f'\033[93m[!] {err}')
		
def olahraga():
	total = 0
	Olahraga = "https://www.news.developeridn.com/olahraga"
	system('clear')
	try:
		tabel_waktu(dua) ; print ('\033[97mOLAHRAGA') ; print (20* '\033[93m=')
		a = buka(Olahraga)
		b = loads(a.read())
		for c in b['data']:
			print (f"\033[92m[✓] JUDUL : \033[93m{c['judul']}")
			print (f"\033[92m[✓] LINK : \033[94m{c['link']}")
			print (f"\033[92m[✓] TIPE : \033[95m{c['tipe']}")
			print (f"\033[92m[✓] WAKTU : \033[96m{c['waktu']}\n\n")
			total += 1
		print ('\033[93mTotal : \033[95m',total)
	except KeyboardInterrupt:
		exit()
	except Exception as err:
		print (f'\033[93m[!] {err}')
		
def teknologi():
	total = 0
	Teknologi = "https://www.news.developeridn.com/teknologi"
	system('clear')
	try:
		tabel_waktu(dua) ; print ('\033[97mTEKNOLOGI') ; print (20* '\033[93m=')
		a = buka(Teknologi)
		b = loads(a.read())
		for c in b['data']:
			print (f"\033[92m[✓] JUDUL : \033[93m{c['judul']}")
			print (f"\033[92m[✓] LINK : \033[94m{c['link']}")
			print (f"\033[92m[✓] TIPE : \033[95m{c['tipe']}")
			print (f"\033[92m[✓] WAKTU : \033[96m{c['waktu']}\n\n")
			total += 1
		print ('\033[93mTotal : \033[95m',total)
	except KeyboardInterrupt:
		exit()
	except Exception as err:
		print (f'\033[93m[!] {err}')
		
def hiburan():
	total = 0
	system('clear')
	Hiburan = "https://www.news.developeridn.com/hiburan"
	try:
		tabel_waktu(dua) ; print ('\033[97mHIBURAN') ; print (20* '\033[93m=')
		a = buka(Hiburan)
		b = loads (a.read())
		for c in b['data']:
			print (f"\033[92m[✓] JUDUL : \033[93m{c['judul']}")
			print (f"\033[92m[✓] LINK : \033[94m{c['link']}")
			print (f"\033[92m[✓] TIPE : \033[95m{c['tipe']}")
			print (f"\033[92m[✓] WAKTU : \033[96m{c['waktu']}\n\n")
			total += 1
		print ('\033[93mTotal : \033[95m',total)
	except KeyboardInterrupt:
		exit()
	except Exception as err:
		print (f'\033[93m[!] {err}')
		
def gaya_hidup():
	system ('clear')
	total = 0
	Gaya_hidup = "https://www.news.developeridn.com/gaya-hidup"
	try:
		tabel_waktu(dua) ; print ('\033[97mGAYA HIDUP') ; print (20* '\033[93m=')
		a = buka(Gaya_hidup)
		b = loads(a.read())
		for c in b['data']:
			print (f"\033[92m[✓] JUDUL : \033[93m{c['judul']}")
			print (f"\033[92m[✓] LINK : \033[94m{c['link']}")
			print (f"\033[92m[✓] TIPE : \033[95m{c['tipe']}")
			print (f"\033[92m[✓] WAKTU : \033[96m{c['waktu']}\n\n")
			total += 1
		print ('\033[93mTotal : \033[95m',total)
	except KeyboardInterrupt:
		exit()
	except Exception as err:
		print (f'\033[93m[!] {err}')

def Cari():
	system('clear')
	total = 0
	try:
		tabel_waktu(dua) ; print ('\033[97mPENCARIAN BERITA') ; print (20* '\033[93m=')
		cari = input('\033[92m[?] KATA KUNCI : \033[96m')
		if len(cari) < 4:
			print ('\033[91m[!] MINIMAL \033[93m"4" \033[91mKARAKTER') ; sleep(3) ; Cari()
		else:
			print ('\033[93m[!] MOHON TUNGGU')
			Shifa = parse(cari)
			pencarian = f"https://www.news.developeridn.com/search/?q={Shifa}"
			print ('\033[93m[!] MEMBUKA : \033[95m',pencarian) ; sleep(1)
			a = buka(pencarian)
			b = loads(a.read())
			print ('\n')
			for c in b['data']:
				print (f"\033[92m[✓] JUDUL : \033[93m{c['judul']}")
				print (f"\033[92m[✓] LINK : \033[94m{c['link']}")
				print (f"\033[92m[✓] TIPE : \033[95m{c['tipe']}")
				print (f"\033[92m[✓] WAKTU : \033[96m{c['waktu']}\n\n")
				total += 1
		if total == 0:
			exit(f'\033[91m[!] BERITA \033[93m"{cari}" \033[91mTIDAK DI TEMUKAN')
		else:
			print ('\033[93mTotal : \033[95m',total)
	except KeyboardInterrupt:
		exit('\033[91m[!] Keluar')
	except Exception as err:
		print (f'\033[93m[!] {err}')
		

if __name__=="__main__":
	if len(argv) == 2:
		command()
	elif len(argv) > 2:
		system('clear')
		print ('\033[95m')
		raise TypeError('\033[93mCOMMAND TIDAK DI KENALI')
	else:
		main()