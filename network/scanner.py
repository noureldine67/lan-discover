import nmap
from colorama import Fore


def scan_ip(ip, nmap_args="-sS -O -T4"):
    """
    Scan Nmap d'une IP avec détection OS, services et ports uniquement (sans scripts NSE).

    Args:
        ip (str): L'adresse IP cible à scanner.
        nmap_args (str): Les arguments à passer à Nmap (type de scan, vitesse, etc.).

    Returns:
        dict | None: Un dictionnaire avec les infos scannées (OS, ports),
                     ou None si l'IP n'est pas joignable ou qu'une erreur survient.
    """
    nm = nmap.PortScanner()
    try:
        nm.scan(hosts=ip, arguments=nmap_args)

        if ip not in nm.all_hosts():
            return None

        result = {"ip": ip, "os": [], "ports": []}

        # --- Détection du système d'exploitation ---
        if "osmatch" in nm[ip]:
            result["os"] = [
                {"name": os["name"], "accuracy": os["accuracy"]}
                for os in nm[ip]["osmatch"]
            ]

        # --- Récupération des ports ouverts et services associés ---
        for proto in nm[ip].all_protocols():
            for port, info in nm[ip][proto].items():
                result["ports"].append(
                    {
                        "port": int(port),
                        "state": info["state"],
                        "service": info.get("name", ""),
                        "version": info.get("version", ""),
                    }
                )

        return result

    except Exception as e:
        print(Fore.RED + f"Erreur Nmap : {e}")
        return None


def print_scan_results(result):
    """
    Affiche les résultats du scan (OS + ports), sans les scripts.

    Args:
        result (dict): Les résultats du scan
    """
    print(Fore.CYAN + f"\nRésultats pour {result['ip']} :")

    # --- OS détecté ---
    if result["os"]:
        print(Fore.GREEN + "  Système(s) détecté(s) :")
        for os in result["os"]:
            print(f"    - {os['name']} (précision {os['accuracy']}%)")
    else:
        print("  OS non détecté.")

    # --- Ports/services ---
    if result["ports"]:
        print(Fore.YELLOW + "  Ports ouverts :")
        for port in sorted(result["ports"], key=lambda x: x["port"]):
            print(
                f"    - Port {port['port']} : {port['state']} | {port['service']} {port['version']}"
            )
    else:
        print("  Aucun port ouvert détecté.")
