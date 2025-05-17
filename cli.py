import argparse
import json
from colorama import init, Fore
from network.discover import discover_network
from network.scanner import scan_ip, print_scan_results

# Initialisation de Colorama
init(autoreset=True)

# ASCII art affiché au lancement du programme
ASCII_ART = r"""
             ('-.         .-') _  _ .-') _             .-')                                 (`-.      ('-.  _  .-')   
            ( OO ).-.    ( OO ) )( (  OO) )           ( OO ).                             _(OO  )_  _(  OO)( \( -O )  
 ,--.       / . --. /,--./ ,--,'  \     .'_   ,-.-') (_)---\_)   .-----.  .-'),-----. ,--(_/   ,. \(,------.,------.  
 |  |.-')   | \-.  \ |   \ |  |\  ,`'--..._)  |  |OO)/    _ |   '  .--./ ( OO'  .-.  '\   \   /(__/ |  .---'|   /`. ' 
 |  | OO ).-'-'  |  ||    \|  | ) |  |  \  '  |  |  \\  :` `.   |  |('-. /   |  | |  | \   \ /   /  |  |    |  /  | | 
 |  |`-' | \| |_.'  ||  .     |/  |  |   ' |  |  |(_/ '..`''.) /_) |OO  )\_) |  |\|  |  \   '   /, (|  '--. |  |_.' | 
(|  '---.'  |  .-.  ||  |\    |   |  |   / : ,|  |_.'.-._)   \ ||  |`-'|   \ |  | |  |   \     /__) |  .--' |  .  '.' 
 |      |   |  | |  ||  | \   |   |  '--'  /(_|  |   \       /(_'  '--'\    `'  '-'  '    \   /     |  `---.|  |\  \  
 `------'   `--' `--'`--'  `--'   `-------'   `--'    `-----'    `-----'      `-----'      `-'      `------'`--' '--' 
"""

def main():
    # Configuration du parser pour accepter les arguments -n, -s et -o
    parser = argparse.ArgumentParser(description="Scanner réseau modulaire")
    parser.add_argument(
        "-n", "--network", help="Plage réseau CIDR (ex: 192.168.1.0/24)"  # Pour la découverte réseau
    )
    parser.add_argument("-s", "--scan", help="IP à scanner avec Nmap")  # Pour scanner une IP précise
    parser.add_argument("-o", "--output", help="Fichier de sortie JSON")  # Pour exporter les résultats en JSON

    # Analyse des arguments passés au script
    args = parser.parse_args()

    # Si l'utilisateur a demandé une découverte réseau
    if args.network:
        print(Fore.CYAN + f"Découverte ARP sur {args.network}...")  # Message informatif en bleu
        devices = discover_network(args.network)  # Appel de la fonction qui fait la découverte ARP
        if devices:
            print(Fore.GREEN + f"\n{len(devices)} appareils trouvés :")  # En vert, nombre d'appareils détectés
            # Affichage des IP et MAC de chaque appareil trouvé
            for dev in devices:
                print(f"  - IP: {dev['ip']}\tMAC: {dev['mac']}")
        else:
            print(Fore.RED + "Aucun appareil trouvé.")  # En rouge si rien n'a été détecté

        # Export des résultats dans un fichier JSON si demandé
        if args.output:
            with open(args.output, "w") as f:
                json.dump({"devices": devices}, f, indent=4)
            print(Fore.CYAN + f"Résultats exportés dans {args.output}")

    # Si l'utilisateur a demandé un scan Nmap sur une IP spécifique
    elif args.scan:
        print(Fore.CYAN + f"Scan Nmap sur {args.scan}...")  # Message informatif en bleu
        results = scan_ip(args.scan)  # Appel du scan Nmap
        if results:
            print_scan_results(results)  # Affichage formaté des résultats du scan
        else:
            print(Fore.RED + "Aucun résultat ou échec du scan.")  # Message d'erreur en rouge

        # Export des résultats dans un fichier JSON si demandé
        if args.output:
            with open(args.output, "w") as f:
                json.dump({"scan": results}, f, indent=4)
            print(Fore.CYAN + f"Résultats exportés dans {args.output}")
    else:
        # Message jaune pour indiquer qu'il faut utiliser un argument valide
        print(Fore.YELLOW + "Utilise -n pour découvrir ou -s pour scanner une IP.")


# Point d'entrée du programme
if __name__ == "__main__":
    # Affichage de l'ASCII art en violet au démarrage
    print(Fore.CYAN + ASCII_ART)
    main()
