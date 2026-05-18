#!/data/data/com.termux/files/usr/bin/python
# ULTIMATE SKY TOOL v3.0 - Mega Terminal Customizer

import os
import sys
import json
import time
import webbrowser
from datetime import datetime
from pathlib import Path

CONFIG_DIR = Path.home() / ".sky_tool"
CONFIG_FILE = CONFIG_DIR / "config.json"
BASHRC_FILE = Path.home() / ".bashrc"

# Colors
R = '\033[0m'
G = '\033[92m'
Y = '\033[93m'
C = '\033[96m'
M = '\033[95m'
B = '\033[94m'
W = '\033[97m'
RED = '\033[91m'

def open_youtube_auto():
    """Auto open YouTube subscribe link for @skybsprobs"""
    url = "https://youtube.com/@skybsprobs?sub_confirmation=1"
    print(f"\n{Y}📺 Opening YouTube channel @skybsprobs...{R}")
    time.sleep(1)
    webbrowser.open(url)
    print(f"{G}✅ Channel opened! Please subscribe{R}\n")
    time.sleep(2)

def mega_banner():
    os.system('clear')
    mega_text = f"""
{R}╔══════════════════════════════════════════════════════════════════════╗
║{C}███████╗██╗  ██╗██╗   ██╗     ████████╗ ██████╗  ██████╗ ██╗         ║
║{C}██╔════╝██║ ██╔╝╚██╗ ██╔╝     ╚══██╔══╝██╔═══██╗██╔═══██╗██║         ║
║{C}███████╗█████╔╝  ╚████╔╝         ██║   ██║   ██║██║   ██║██║         ║
║{C}╚════██║██╔═██╗   ╚██╔╝          ██║   ██║   ██║██║   ██║██║         ║
║{C}███████║██║  ██╗   ██║           ██║   ╚██████╔╝╚██████╔╝███████╗    ║
║{C}╚══════╝╚═╝  ╚═╝   ╚═╝           ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝    ║
║{G}                      MEGA TERMINAL CUSTOMIZER v3.0                    ║
╚══════════════════════════════════════════════════════════════════════════╝
    """
    print(mega_text)

def get_mega_size():
    """Return mega size ANSI codes"""
    sizes = {
        "1": {"name": "HALF SCREEN (MEGA)", "code": "\033[1m\033[7m\033[3m", "lines": 8},
        "2": {"name": "FULL SCREEN (ULTRA)", "code": "\033[1m\033[7m\033[3m\033[4m", "lines": 12},
        "3": {"name": "NORMAL", "code": "\033[1m", "lines": 3}
    }
    return sizes

def color_options():
    colors = {
        "1": {"name": "🔥 RED", "code": "31"},
        "2": {"name": "💚 GREEN", "code": "32"},
        "3": {"name": "⭐ YELLOW", "code": "33"},
        "4": {"name": "💙 BLUE", "code": "34"},
        "5": {"name": "💜 MAGENTA", "code": "35"},
        "6": {"name": "💎 CYAN", "code": "36"},
        "7": {"name": "⚪ WHITE", "code": "37"}
    }
    print(f"\n{Y}🎨 SELECT TEXT COLOR:{R}")
    for k, v in colors.items():
        print(f"  {M}{k}. {v['name']}{R}")
    choice = input(f"\n{C}👉 Enter (1-7): {R}")
    return colors.get(choice, colors["6"])

def style_options():
    styles = {
        "1": {"name": "NORMAL", "code": "0"},
        "2": {"name": "BOLD", "code": "1"},
        "3": {"name": "UNDERLINE", "code": "4"},
        "4": {"name": "BLINK", "code": "5"}
    }
    print(f"\n{Y}✍️ SELECT TEXT STYLE:{R}")
    for k, v in styles.items():
        print(f"  {M}{k}. {v['name']}{R}")
    choice = input(f"\n{C}👉 Enter (1-4): {R}")
    return styles.get(choice, styles["2"])

def get_first_text():
    print(f"\n{Y}📝 ENTER YOUR MAIN TITLE (BIG - WILL COVER HALF SCREEN):{R}")
    print(f"{C}   Example: WELCOME TO SKY TOOL or ALEX{R}")
    return input(f"\n{M}✍️  Text: {R}")

def get_right_text():
    print(f"\n{Y}📝 ENTER YOUR PROMPT TEXT (small, before command):{R}")
    print(f"{C}   Example: [ALEX] or [SKY] or [➜]{R}")
    return input(f"\n{M}✍️  Text: {R}")

def generate_mega_banner(config):
    """Generate half-screen mega banner"""
    color_code = f"\033[{config['style_code']};{config['color_code']}m"
    size_info = get_mega_size()[config['size_choice']]
    size_code = size_info['code']
    lines_count = size_info['lines']
    
    text = config['first_text'].upper()
    
    banner_lines = ["clear", "echo ''"]
    
    # Top fancy border
    banner_lines.append(f"echo '{color_code}{'═' * 60}{R}'")
    
    # Mega size text (half screen)
    for i in range(lines_count):
        if i == lines_count // 2:
            # Center text with padding
            padding = (60 - len(text)) // 2
            banner_lines.append(f"echo '{color_code}{size_code}{' ' * padding}{text}{' ' * (60 - len(text) - padding)}{R}'")
        else:
            # Fill rest with style lines
            banner_lines.append(f"echo '{color_code}{size_code}{'█' * 60}{R}'")
    
    # Bottom border
    banner_lines.append(f"echo '{color_code}{'═' * 60}{R}'")
    banner_lines.append("echo ''")
    
    # PS1 with time
    ps1 = f"PS1='{color_code}{config['second_text']} ⏰ \\[\\033[36m\\]\\t\\[\\033[0m\\] \\$ '"
    banner_lines.append(ps1)
    
    return "\n".join(banner_lines)

def save_config(data):
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_config():
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return None

def add_to_bashrc(content):
    # Remove old entries
    if BASHRC_FILE.exists():
        with open(BASHRC_FILE, "r") as f:
            lines = f.readlines()
        
        new_lines = []
        skip = False
        for line in lines:
            if "# SKY TOOL Setup" in line:
                skip = True
            if skip and ("PS1=" in line or "echo '" in line) and "SKY" not in line:
                continue
            if skip and line.strip() == "":
                skip = False
                continue
            if not skip:
                new_lines.append(line)
        
        with open(BASHRC_FILE, "w") as f:
            f.writelines(new_lines)
    
    # Add new
    with open(BASHRC_FILE, "a") as f:
        f.write("\n# SKY TOOL Setup\n")
        f.write(content + "\n")

def preview_mega():
    config = load_config()
    if not config:
        print(f"{RED}⚠️ No setup found! Run full setup first.{R}")
        return
    
    os.system('clear')
    color_code = f"\033[{config['style_code']};{config['color_code']}m"
    size_info = get_mega_size()[config['size_choice']]
    size_code = size_info['code']
    
    text = config['first_text'].upper()
    lines_count = size_info['lines']
    
    print(f"{color_code}{'═' * 60}{R}")
    for i in range(lines_count):
        if i == lines_count // 2:
            padding = (60 - len(text)) // 2
            print(f"{color_code}{size_code}{' ' * padding}{text}{' ' * (60 - len(text) - padding)}{R}")
        else:
            print(f"{color_code}{size_code}{'█' * 60}{R}")
    print(f"{color_code}{'═' * 60}{R}")
    print(f"\n{color_code}{config['second_text']} ⏰ {C}{datetime.now().strftime('%H:%M:%S')}{R}")
    print(f"\n{G}✅ MEGA PREVIEW - Text covers {lines_count} lines!{R}")

def setup_interactive():
    # AUTO YOUTUBE - pehle hi khulega
    open_youtube_auto()
    
    mega_banner()
    print(f"{Y}⚡ MEGA SETUP STARTED!{R}\n")
    time.sleep(1)
    
    # Size select
    print(f"{Y}📐 SELECT TEXT SIZE:{R}")
    sizes = get_mega_size()
    for k, v in sizes.items():
        print(f"  {M}{k}. {v['name']} ({v['lines']} lines tall){R}")
    size_choice = input(f"\n{C}👉 Choose (1-3): {R}")
    if size_choice not in ['1', '2', '3']:
        size_choice = '1'
    
    # Color
    color = color_options()
    
    # Style
    style = style_options()
    
    # First text (mega)
    first_text = get_first_text()
    
    # Second text (small prompt)
    second_text = get_right_text()
    
    config = {
        "size_choice": size_choice,
        "color_name": color['name'],
        "color_code": color['code'],
        "style_name": style['name'],
        "style_code": style['code'],
        "first_text": first_text,
        "second_text": second_text
    }
    
    save_config(config)
    banner_code = generate_mega_banner(config)
    add_to_bashrc(banner_code)
    
    os.system('clear')
    print(f"{G}{'█'*60}{R}")
    print(f"{G}✅ MEGA SETUP COMPLETE!{R}")
    print(f"{C}   Size: {get_mega_size()[size_choice]['name']}{R}")
    print(f"{C}   Color: {color['name']}{R}")
    print(f"{C}   Style: {style['name']}{R}")
    print(f"{C}   Main Text: {first_text}{R}")
    print(f"{C}   Prompt: {second_text}{R}")
    print(f"{G}{'█'*60}{R}")
    print(f"\n{Y}👉 RESTART TERMUX to see your MEGA setup!{R}")
    print(f"{M}👉 Text will cover HALF/ FULL screen!{R}\n")

def reset_setup():
    confirm = input(f"{RED}⚠️ DELETE all settings? (y/n): {R}")
    if confirm.lower() == 'y':
        os.system(f"rm -rf {CONFIG_DIR}")
        # Clear bashrc
        if BASHRC_FILE.exists():
            with open(BASHRC_FILE, "r") as f:
                lines = f.readlines()
            with open(BASHRC_FILE, "w") as f:
                for line in lines:
                    if "# SKY TOOL Setup" not in line and "PS1=" not in line:
                        f.write(line)
        print(f"{G}✅ Reset complete. Restart Termux.{R}")
    else:
        print(f"{Y}Cancelled{R}")

def main():
    # AUTO YOUTUBE on every start
    open_youtube_auto()
    
    CONFIG_DIR.mkdir(exist_ok=True)
    
    while True:
        mega_banner()
        print(f"""
{R}╔════════════════════════════════════════════════════════════╗
║{C}                    🚀 SKY TOOL v3.0 MENU                    ║{R}
╠════════════════════════════════════════════════════════════╣
║  {G}1.{R} ⚡ MEGA SETUP (Half/Full Screen Text)                 ║
║  {G}2.{R} 👁️  PREVIEW Current Setup                             ║
║  {G}3.{R} 🔄 RESET Setup                                        ║
║  {G}4.{R} 📺 YouTube (@skybsprobs)                              ║
║  {G}5.{R} ❌ EXIT                                               ║
╚════════════════════════════════════════════════════════════╝
        """)
        
        choice = input(f"{C}👉 Choose {Y}(1-5){C}: {R}")
        
        if choice == "1":
            setup_interactive()
            input(f"\n{Y}Press Enter...{R}")
        elif choice == "2":
            preview_mega()
            input(f"\n{Y}Press Enter...{R}")
        elif choice == "3":
            reset_setup()
            input(f"\n{Y}Press Enter...{R}")
        elif choice == "4":
            open_youtube_auto()
            input(f"\n{Y}Press Enter...{R}")
        elif choice == "5":
            print(f"\n{G}✨ Thanks for using SKY TOOL MEGA!{R}\n")
            break
        else:
            print(f"{RED}❌ Invalid!{R}")
            time.sleep(1)

if __name__ == "__main__":
    main()
