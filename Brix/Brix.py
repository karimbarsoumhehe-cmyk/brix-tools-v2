# Copyright (c) Brix

from Program.Config.Config import *
from Program.Config.Util import *

try:
   import webbrowser
   import re
   import os
except Exception as e:
   ErrorModule(e)

option_01 = "Discord-Token-Nuker"
option_02 = "Discord-Token-Info"
option_03 = "Discord-Token-Joiner"
option_04 = "Discord-Token-Leaver"
option_05 = "Discord-Token-Login"
option_06 = "Discord-Token-Server-Raid"
option_07 = "Discord-Token-Spammer"
option_08 = "Discord-Token-Delete-Friends"
option_09 = "Discord-Token-Block-Friends"
option_10 = "Discord-Webhook-Delete"
option_11 = "Discord-Webhook-Spammer"
option_12 = "Discord-Token-Mass-Dm"
option_13 = "Discord-Token-Delete-Dm"
option_14 = "Discord-Token-Status-Changer"
option_15 = "Discord-Token-Language-Changer"
option_16 = "Discord-Token-Theme-Changer"
option_17 = "Discord-Token-Generator"
option_18 = "Discord-Bot-Server-Nuker"
option_19 = "Discord-Bot-Invite-To-Id"
option_20 = "Discord-Server-Info"
option_21 = "Ip-Pinger"
option_22 = "Ip-Lookup"

option_01_txt = f"{red}[{white}01{red}]{white} " + option_01.ljust(30)[:30].replace("-", " ")
option_02_txt = f"{red}[{white}02{red}]{white} " + option_02.ljust(30)[:30].replace("-", " ")
option_03_txt = f"{red}[{white}03{red}]{white} " + option_03.ljust(30)[:30].replace("-", " ")
option_04_txt = f"{red}[{white}04{red}]{white} " + option_04.ljust(30)[:30].replace("-", " ")
option_05_txt = f"{red}[{white}05{red}]{white} " + option_05.ljust(30)[:30].replace("-", " ")
option_06_txt = f"{red}[{white}06{red}]{white} " + option_06.ljust(30)[:30].replace("-", " ")
option_07_txt = f"{red}[{white}07{red}]{white} " + option_07.ljust(30)[:30].replace("-", " ")
option_08_txt = f"{red}[{white}08{red}]{white} " + option_08.ljust(30)[:30].replace("-", " ")
option_09_txt = f"{red}[{white}09{red}]{white} " + option_09.ljust(30)[:30].replace("-", " ")
option_10_txt = f"{red}[{white}10{red}]{white} " + option_10.ljust(30)[:30].replace("-", " ")
option_11_txt = f"{red}[{white}11{red}]{white} " + option_11.ljust(30)[:30].replace("-", " ")
option_12_txt = f"{red}[{white}12{red}]{white} " + option_12.ljust(30)[:30].replace("-", " ")
option_13_txt = f"{red}[{white}13{red}]{white} " + option_13.ljust(30)[:30].replace("-", " ")
option_14_txt = f"{red}[{white}14{red}]{white} " + option_14.ljust(30)[:30].replace("-", " ")
option_15_txt = f"{red}[{white}15{red}]{white} " + option_15.ljust(30)[:30].replace("-", " ")
option_16_txt = f"{red}[{white}16{red}]{white} " + option_16.ljust(30)[:30].replace("-", " ")
option_17_txt = f"{red}[{white}17{red}]{white} " + option_17.ljust(30)[:30].replace("-", " ")
option_18_txt = f"{red}[{white}18{red}]{white} " + option_18.ljust(30)[:30].replace("-", " ")
option_19_txt = f"{red}[{white}19{red}]{white} " + option_19.ljust(30)[:30].replace("-", " ")
option_20_txt = f"{red}[{white}20{red}]{white} " + option_20.ljust(30)[:30].replace("-", " ")
option_21_txt = f"{red}[{white}21{red}]{white} " + option_21.ljust(30)[:30].replace("-", " ")
option_22_txt = f"{red}[{white}22{red}]{white} " + option_22.ljust(30)[:30].replace("-", " ")

def Menu():
   banner = f"""                                                   
                                    ▀█████████▄     ▄████████  ▄█  ▀████    ▐████▀      
                                     ███    ███   ███    ███ ███    ███▌   ████▀       
                                     ███    ███   ███    ███ ███▌    ███  ▐███         
                                    ▄███▄▄▄██▀   ▄███▄▄▄▄██▀ ███▌    ▀███▄███▀         
                                   ▀▀███▀▀▀██▄  ▀▀███▀▀▀▀▀   ███▌    ████▀██▄          
                                     ███    ██▄ ▀███████████ ███    ▐███  ▀███         
                                     ███    ███   ███    ███ ███   ▄███     ███▄       
                                   ▄█████████▀    ███    ███ █▀   ████       ███▄      
                                                  ███    ███                                                     """
   menu_number = "1"
   return banner, menu_number

def Welcome():
   ascii_art = r"""
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝
                                                         
   """
   sys.stdout.write('\033[2J\033[H')
   w = os.get_terminal_size().columns
   h = os.get_terminal_size().lines
   lines = ascii_art.split('\n')
   art_h = len(lines)
   art_w = max(len(l) for l in lines)
   ox = max(0, (w - art_w) // 2)
   oy = max(0, (h - art_h - 3) // 2)
   gray_colors = []
   for i in range(9):
      v = 30 + (200 - 30) * i // 8
      gray_colors.append(v)
   gray_colors += list(reversed(gray_colors[:-1]))
   for r, line in enumerate(lines):
      for c, ch in enumerate(line):
         if ch != ' ':
            idx = (r + c) % len(gray_colors)
            v = gray_colors[idx]
            sys.stdout.write(f'\033[{oy + r + 1};{ox + c + 1}H\033[38;2;{v};{v};{v}m{ch}{reset}')
   bar_w = min(50, w - 4)
   bar_x = max(0, (w - bar_w) // 2)
   bar_y = oy + art_h + 1
   frames = 40
   for f in range(frames + 1):
      pct = f / frames
      filled = int(bar_w * pct)
      empty = bar_w - filled
      bar = "\033[38;2;200;200;200m[\033[0m"
      for i in range(bar_w):
         if i < filled:
            v = 100 + int(100 * (i / bar_w))
            bar += f"\033[38;2;{v};{v};{v}m█\033[0m"
         else:
            bar += " "
      bar += f"\033[38;2;200;200;200m] {int(pct * 100)}%\033[0m"
      sys.stdout.write(f'\033[{bar_y};{bar_x}H{bar}')
      sys.stdout.flush()
      time.sleep(3.0 / frames)
   time.sleep(1)

import sys
if '--no-welcome' not in sys.argv:
   Welcome()
while True:
   try:
      Clear()

      banner, menu_number = Menu()

      Title(f"Menu")
      Slow(MainColor(banner))

      width = os.get_terminal_size().columns
      pad = " " * max(0, (width - 75) // 2)

      print(f"{pad}{red}┌─────────────────────────────────────────────────────────────────────────┐{reset}")
      print(f"{pad}{red}│{reset} {option_01_txt} {option_12_txt} {red}│{reset}")
      print(f"{pad}{red}│{reset} {option_02_txt} {option_13_txt} {red}│{reset}")
      print(f"{pad}{red}│{reset} {option_03_txt} {option_14_txt} {red}│{reset}")
      print(f"{pad}{red}│{reset} {option_04_txt} {option_15_txt} {red}│{reset}")
      print(f"{pad}{red}│{reset} {option_05_txt} {option_16_txt} {red}│{reset}")
      print(f"{pad}{red}│{reset} {option_06_txt} {option_17_txt} {red}│{reset}")
      print(f"{pad}{red}│{reset} {option_07_txt} {option_18_txt} {red}│{reset}")
      print(f"{pad}{red}│{reset} {option_08_txt} {option_19_txt} {red}│{reset}")
      print(f"{pad}{red}│{reset} {option_09_txt} {option_20_txt} {red}│{reset}")
      print(f"{pad}{red}│{reset} {option_10_txt} {option_21_txt} {red}│{reset}")
      print(f"{pad}{red}│{reset} {option_11_txt} {option_22_txt} {red}│{reset}")
      print(f"{pad}{red}└─────────────────────────────────────────────────────────────────────────┘{reset}")
      print()

      choice = input(MainColor(f""" ┌──({white}{username_pc}@Brix)─{red}[{white}~/{os_name}/Menu{red}]
 └─{white}$ {reset}"""))

      if choice in ['I', 'i', 'INFO', 'Info', 'info']:
         StartProgram(f"{option_info}.py")
         continue
      
      options = {
         '01': option_01, '02': option_02, '03': option_03, '04': option_04,
         '05': option_05, '06': option_06, '07': option_07, '08': option_08,
         '09': option_09, '10': option_10, '11': option_11, '12': option_12,
         '13': option_13, '14': option_14, '15': option_15, '16': option_16,
         '17': option_17, '18': option_18, '19': option_19, '20': option_20,
         '21': option_21, '22': option_22
      }

      if choice in options:  
         StartProgram(f"{options[choice]}.py")
      elif '0' + choice in options:
         StartProgram(f"{options['0' + choice]}.py")
      else:
         ErrorChoiceStart()

   except Exception as e:
      Error(e)
