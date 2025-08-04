import os
import subprocess
import time
from rich.console import Console
from rich.prompt import Prompt
import sys

console = Console()

BANNER = """
⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣴⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣷⣤⡀⠀
⠀⠀⢀⣾⡟⡍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡙⣿⡄
⠀⠀⣸⣿⠃⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⣹⣿
⠀⠀⣿⣿⡆⢚⢄⣀⣠⠤⠒⠈⠁⠀⠀⠈⠉⠐⠢⢄⡀⣀⢞⠀⣾⣿
⠀⠀⠸⣿⣿⣅⠄⠙⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠑⣄⣽⣿⡟
⠀⠀⠀⠘⢿⣿⣟⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⣾⣿⣿⠏⠀
⠀⠀⠀⠀⣸⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡉⢻⠀⠀
⠀⠀⠀⠀⢿⠀⢃⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠁⢸⠀⠀
⠀⠀⠀⠀⢸⢰⡿⢘⣦⣤⣀⠑⢦⡀⠀⣠⠖⣁⣤⣴⡊⢸⡇⡼⠀⠀
⠀⠀⠀⠀⠀⠾⡅⣿⣿⣿⣿⣿⠌⠁⠀⠁⢺⣿⣿⣿⣿⠆⣇⠃⠀⠀
⠀⠀⠀⠀⠀⢀⠂⠘⢿⣿⣿⡿⠀⣰⣦⠀⠸⣿⣿⡿⠋⠈⢀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⢠⣿⢻⣆⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠓⠶⣶⣦⠤⠀⠘⠋⠘⠋⠀⠠⣴⣶⡶⠞⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⢹⣷⠦⢀⠤⡤⡆⡤⣶⣿⢸⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⡀⠘⢯⣳⢶⠦⣧⢷⢗⣫⠇⠀⡸⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠑⢤⡀⠈⠋⠛⠛⠋⠉⢀⡠⠒⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⢦⠀⢀⣀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

SOCIAL = """
[bold cyan]Follow Sigma-Ghost Hacking Profiles:[/bold cyan]
[bold magenta]Twitter:[/bold magenta] https://twitter.com/safderkhan0800_
[bold magenta]Instagram:[/bold magenta] https://www.instagram.com/safderkhan0800_/
[bold magenta]YouTube:[/bold magenta] https://www.youtube.com/@sigma_ghost_hacking
[bold magenta]Telegram:[/bold magenta] https://t.me/Sigma_Cyber_Ghost
"""

def glitch_effect(text, delay=0.05):
    for char in text:
        console.print(f"[bold green]{char}[/bold green]", end="", style="blink")
        time.sleep(delay)
    print()

def check_command_exists(command):
    return subprocess.call(f"type {command}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

def extract_exif_raw(image_path):
    if not check_command_exists("exiftool"):
        console.print("[red]Error: 'exiftool' is not installed.[/red]")
        return
    console.print(f"[yellow]Dumping Full EXIF Metadata from:[/yellow] {image_path}")
    subprocess.run(["exiftool", image_path])

def shred_metadata(image_path, output_path):
    console.print("[yellow]Sanitizing Metadata...[/yellow]")
    if image_path == output_path:
        subprocess.run(["exiftool", "-overwrite_original", "-all=", image_path])
        console.print(f"[green]Metadata wiped from original file: {image_path}[/green]")
    else:
        result = subprocess.run(["exiftool", "-all=", image_path, "-o", output_path], capture_output=True, text=True)
        if result.returncode == 0:
            console.print(f"[green]Clean Image Saved:[/green] {output_path}")
        else:
            console.print(f"[red]Error: {result.stderr}[/red]")

def extreme_purge(image_path):
    console.print("[red bold]Extreme Mode: Sector Overwrite Initiated...[/red bold]")
    purge_cmd = f"dd if=/dev/zero of='{image_path}' bs=1M count=10 conv=notrunc status=none"
    os.system(purge_cmd)
    console.print("[bold red]Image Sector Wipe Complete. Recovery Impossible.[/bold red]")

def stego_scan(image_path):
    if not check_command_exists("steghide"):
        console.print("[red]Error: 'steghide' is not installed.[/red]")
        return
    console.print("[magenta]Scanning for Hidden Data (Stego Mode)...[/magenta]")
    result = subprocess.run(["steghide", "extract", "-sf", image_path, "-p", ""], capture_output=True, text=True)
    if "wrote extracted data" in result.stdout:
        console.print(f"[green]Hidden data extracted successfully.[/green]")
    else:
        console.print(f"[red]No hidden data found or file is clean.[/red]")

def stego_hide(image_path, secret_file):
    if not check_command_exists("steghide"):
        console.print("[red]Error: 'steghide' is not installed.[/red]")
        return
    console.print("[blue]Embedding secret message inside the image...[/blue]")
    result = subprocess.run(["steghide", "embed", "-cf", image_path, "-ef", secret_file, "-p", ""], capture_output=True, text=True)
    if "embedding" in result.stdout or result.returncode == 0:
        console.print(f"[green]Message successfully hidden inside {image_path}[/green]")
    else:
        console.print(f"[red]Failed to hide message: {result.stderr}[/red]")

def main_menu():
    console.print(f"[bold magenta]{BANNER}[/bold magenta]")
    glitch_effect("SIGMA-GHOST-HACKING", 0.08)
    console.print(SOCIAL)

    while True:
        console.print("\n[bold cyan]1.[/bold cyan] Extract Image Metadata")
        console.print("[bold cyan]2.[/bold cyan] Remove Metadata")
        console.print("[bold cyan]3.[/bold cyan] Blast Image")
        console.print("[bold cyan]4.[/bold cyan] Stego-Scanner (Extract Hidden Data)")
        console.print("[bold cyan]5.[/bold cyan] Stego-Hide (Embed Message into Image)")
        console.print("[bold cyan]6.[/bold cyan] Exit")

        choice = Prompt.ask("[bold green]Select Option[/bold green]")

        if choice == "1":
            img = Prompt.ask("Enter Image Path").strip().strip("'\"")
            if not os.path.isfile(img):
                console.print(f"[red]File not found: {img}[/red]")
                continue
            extract_exif_raw(img)

        elif choice == "2":
            img = Prompt.ask("Enter Image Path").strip().strip("'\"")
            if not os.path.isfile(img):
                console.print(f"[red]File not found: {img}[/red]")
                continue
            out = Prompt.ask("Output Clean Image As (or press Enter to overwrite original)").strip().strip("'\"")
            if out == "":
                out = img
            shred_metadata(img, out)

        elif choice == "3":
            img = Prompt.ask("Enter Image Path").strip().strip("'\"")
            if not os.path.isfile(img):
                console.print(f"[red]File not found: {img}[/red]")
                continue
            confirm = Prompt.ask("[red]This will DESTROY the file. Type 'YES' to confirm[/red]")
            if confirm == "YES":
                extreme_purge(img)

        elif choice == "4":
            img = Prompt.ask("Enter Image Path").strip().strip("'\"")
            if not os.path.isfile(img):
                console.print(f"[red]File not found: {img}[/red]")
                continue
            stego_scan(img)

        elif choice == "5":
            img = Prompt.ask("Enter Cover Image Path").strip().strip("'\"")
            if not os.path.isfile(img):
                console.print(f"[red]File not found: {img}[/red]")
                continue
            secret = Prompt.ask("Enter Secret File Path to Hide").strip().strip("'\"")
            if not os.path.isfile(secret):
                console.print(f"[red]Secret file not found: {secret}[/red]")
                continue
            stego_hide(img, secret)

        elif choice == "6":
            console.print("[bold yellow]Exiting... Stay Ghost.[/bold yellow]")
            break
        else:
            console.print("[red]Invalid Option.[/red]")

if __name__ == "__main__":
    if os.geteuid() != 0:
        console.print("[bold red]Run as Root![/bold red]")
        sys.exit(1)
    main_menu()
