# LanDiscover

```
             ('-.         .-') _  _ .-') _             .-')                                 (`-.      ('-.  _  .-')   
            ( OO ).-.    ( OO ) )( (  OO) )           ( OO ).                             _(OO  )_  _(  OO)( \( -O )  
 ,--.       / . --. /,--./ ,--,'  \     .'_   ,-.-') (_)---\_)   .-----.  .-'),-----. ,--(_/   ,. \(,------.,------.  
 |  |.-')   | \-.  \ |   \ |  |\  ,`'--..._)  |  |OO)/    _ |   '  .--./ ( OO'  .-.  '\   \   /(__/ |  .---'|   /`. ' 
 |  | OO ).-'-'  |  ||    \|  | ) |  |  \  '  |  |  \\  :` `.   |  |('-. /   |  | |  | \   \ /   /  |  |    |  /  | | 
 |  |`-' | \| |_.'  ||  .     |/  |  |   ' |  |  |(_/ '..`''.) /_) |OO  )\_) |  |\|  |  \   '   /, (|  '--. |  |_.' | 
(|  '---.'  |  .-.  ||  |\    |   |  |   / : ,|  |_.'.-._)   \ ||  |`-'|   \ |  | |  |   \     /__) |  .--' |  .  '.' 
 |      |   |  | |  ||  | \   |   |  '--'  /(_|  |   \       /(_'  '--'\    `'  '-'  '    \   /     |  `---.|  |\  \  
 `------'   `--' `--'`--'  `--'   `-------'   `--'    `-----'    `-----'      `-----'      `-'      `------'`--' '--' 
```

## Description

LanDiscover est un outil Python pour découvrir les appareils sur un réseau local et scanner des IP spécifiques avec Nmap. Il permet aussi d’exporter les résultats en JSON.

## Utilisation

Lance le script avec les options suivantes :

```bash
python lan_discover.py [-n <réseau CIDR>] [-s <IP à scanner>] [-o <fichier JSON>]
```

### Options :

* `-n`, `--network` : Découvrir les appareils d’un réseau (ex: `192.168.1.0/24`)
* `-s`, `--scan` : Scanner une IP précise avec Nmap
* `-o`, `--output` : Exporter les résultats dans un fichier JSON

## Exemples

* Découverte réseau :

  ```bash
  python lan_discover.py -n 192.168.1.0/24
  ```

* Scan d’une IP :

  ```bash
  python lan_discover.py -s 192.168.1.10
  ```

* Découverte avec export :

  ```bash
  python lan_discover.py -n 192.168.1.0/24 -o resultat.json
  ```