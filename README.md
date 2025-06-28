# Scanner port

![Python Version](https://img.shields.io/badge/python-3.x-brightgreen.svg)
![GUI Framework](https://img.shields.io/badge/GUI-CustomTkinter-blue.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

Un outil de scan de ports doté d'une interface graphique. Ce projet permet aux utilisateurs de scanner des adresses IP et des plages de ports pour identifier les ports ouverts et applicaations lié de manière efficace.

## Fonctionnalités

*   **Scan de Ports TCP :** Capacité à détecter les ports TCP ouverts sur une adresse IP cible.
*   **Scan de Plage de Ports :** Permet de spécifier une plage de ports à scanner pour une analyse plus approfondie.
*   **Affichage Clair des Résultats :** Présentation lisible des ports ouverts, dès application lié et de leur état.

## Structure du Projet

```
.
├── main.py           # Point d'entrée de l'application
├── app_ui.py         # Interface graphique utilisateur
├── scanner.py        # Logique de scan des ports
└── requirements.txt  # Liste des dépendances Python
```

## Installation

Suivez ces étapes pour configurer et exécuter le projet sur votre machine locale.

1.  **Clonez le dépôt :**
    ```bash
    git clone https://github.com/Tyno14/Scanner-port.git
    cd port-scanner-gui
    ```

2.  **Créez un environnement virtuel (recommandé) :**
    ```bash
    python3 -m venv venv
    ```

3.  **Activez l'environnement virtuel :**
    *   **Sur Linux/macOS :**
        ```bash
        source venv/bin/activate
        ```
    *   **Sur Windows :**
        ```bash
        .\venv\Scripts\activate
        ```

4.  **Installez les dépendances :**
    ```bash
    pip install -r requirements.txt
    ```

## Utilisation

Une fois l'installation terminée, vous pouvez lancer l'application :

```bash
python main.py
```

L'interface graphique s'ouvrira, vous permettant d'entrer l'adresse IP cible et la plage de ports à scanner.

## Contribuer

Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet, veuillez suivre les étapes ci-dessous :

1.  Forkez le dépôt.
2.  Créez une nouvelle branche pour votre fonctionnalité (`git checkout -b feature/ma-nouvelle-fonctionnalite`).
3.  Commitez vos modifications (`git commit -m 'Ajout d'une nouvelle fonctionnalité'`).
4.  Poussez votre branche (`git push origin feature/ma-nouvelle-fonctionnalite`).
5.  Ouvrez une Pull Request.

## Licence

Ce projet est distribué sous la licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
