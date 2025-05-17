from scapy.all import ARP, Ether, srp, get_if_addr, conf
from colorama import Fore


def discover_network(network_cidr, timeout=3):
    """
    Découverte ARP sur le réseau spécifié.

    Args:
        network_cidr (str): La plage réseau à scanner au format CIDR (ex: '192.168.1.0/24').
        timeout (int): Temps d'attente pour les réponses ARP (en secondes).

    Returns:
        list of dict: Liste des appareils détectés, chaque élément contenant 'ip' et 'mac'.
    """
    try:
        # Création d'une requête ARP destinée à l'ensemble du réseau ciblé (pdst).
        # psrc est l'adresse IP source (IP locale de l'interface réseau utilisée).
        arp = ARP(pdst=network_cidr, psrc=get_if_addr(conf.iface))

        # Création d'une trame Ethernet de broadcast (ff:ff:ff:ff:ff:ff)
        # pour que tous les appareils du réseau reçoivent la requête ARP.
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")

        # Combinaison des deux paquets pour créer une requête ARP encapsulée dans une trame Ethernet.
        packet = ether / arp

        # Envoi de la requête et réception des réponses avec srp (send/receive at layer 2).
        # `verbose=0` évite les impressions inutiles.
        result = srp(packet, timeout=timeout, verbose=0)[0]

        devices = []  # Liste des appareils détectés

        for _, received in result:
            mac = received.hwsrc  # Adresse MAC source de la réponse

            # On ignore les réponses avec une adresse MAC vide ou multicast
            if mac != "00:00:00:00:00:00" and not mac.startswith("01:00:5e"):
                devices.append(
                    {
                        "ip": received.psrc,  # Adresse IP source de la réponse ARP
                        "mac": mac,
                    }
                )

        return devices  # Retourne la liste des appareils détectés (IP + MAC)

    except Exception as e:
        # En cas d'erreur lors de la découverte (ex: interface réseau non trouvée)
        print(Fore.RED + f"Erreur découverte réseau : {e}")
        return []  # Retourne une liste vide si une erreur survient
