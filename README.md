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

LanDiscover est un outil Python permettant de :

* Découvrir les appareils connectés sur un réseau local via une plage CIDR.
* Scanner une IP spécifique avec Nmap.
* Exporter les résultats au format JSON.

## Structure du projet

```
lan-discover/
├── cli.py
├── network/
│   ├── discover.py
│   ├── scanner.py
│   ├── __init__.py
│   └── __pycache__/
│       ├── discover.cpython-313.pyc
│       ├── scanner.cpython-313.pyc
│       └── __init__.cpython-313.pyc
├── README.md
└── requirements.txt
```

## Utilisation

Il est recommandé d’exécuter le script avec les privilèges `sudo` pour accéder aux fonctionnalités réseau.

**Important :** Pense à utiliser le chemin absolu vers l’interpréteur Python dans ton environnement virtuel `.venv`. Par exemple :

```bash
sudo /chemin/absolu/vers/.venv/bin/python cli.py [options]
```

### Options disponibles

* `-n`, `--network` : plage réseau au format CIDR pour la découverte (ex: `192.168.1.0/24`)
* `-s`, `--scan` : scanner une IP spécifique avec Nmap
* `-o`, `--output` : exporter les résultats dans un fichier JSON

## Exemples

* Découvrir les appareils sur un réseau local :

  ```bash
  sudo /chemin/absolu/vers/.venv/bin/python cli.py -n 192.168.1.0/24
  ```

* Scanner une IP précise :

  ```bash
  sudo /chemin/absolu/vers/.venv/bin/python cli.py -s 192.168.1.10
  ```

* Découvrir un réseau et exporter les résultats :

  ```bash
  sudo /chemin/absolu/vers/.venv/bin/python cli.py -n 192.168.1.0/24 -o resultat.json
  ```