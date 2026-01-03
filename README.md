# 🛡️ Nexus Cleaner Pro - Simulation de Malware (Silent Execution)

> **⚠️ AVERTISSEMENT / DISCLAIMER** > Ce projet a été réalisé dans un cadre strictement **pédagogique** pour le module de Sécurité Informatique.  
> Il s'agit d'une démonstration de concept (PoC) visant à comprendre les mécanismes d'attaque pour mieux s'en défendre.  
> **L'auteur décline toute responsabilité en cas d'utilisation malveillante de ce code.**

## 📋 Description du Projet

Ce projet s'inscrit dans la catégorie **"Silent Execution"** (Exécution Silencieuse). 

L'objectif est de démontrer comment un programme malveillant peut se dissimuler derrière une application légitime en utilisant des techniques d'**Ingénierie Sociale** et de **Multi-threading**.

L'application se présente comme un "Optimiseur de Système" moderne (GUI), mais exécute une chaîne d'attaque complète (Kill Chain) en arrière-plan sans alerter l'utilisateur.

## 🚀 Fonctionnalités Techniques

Le script `nexus_cleaner.py` combine deux comportements parallèles :

1.  **Façade Légitime (Main Thread) :**
    * Interface graphique moderne avec `tkinter` (Thème Dark).
    * Barre de progression simulant un nettoyage système.
    * Messages rassurants pour l'utilisateur.

2.  **Payload Malveillant (Background Thread) :**
    * **Persistance :** Auto-réplication dans le dossier `%APPDATA%` pour survivre au redémarrage.
    * **Reconnaissance & Exfiltration :** Scan récursif du dossier `Documents` (ciblage des `.pdf`, `.docx`, `.txt`) et copie locale des fichiers.
    * **Ransomware (Simulation) :** Génération d'une note de rançon (`URGENT_README.txt`) et journalisation des actions (`system_audit.log`).

## 🛠️ Installation et Exécution

### Prérequis
* Python 3.x installé.
* Aucune bibliothèque externe n'est requise (utilise uniquement les libs standards : `os`, `shutil`, `threading`, `tkinter`).

### Démarrage
1.  Cloner le dépôt :
    ```bash
    git clone [https://github.com/VOTRE-USERNAME/Nom-du-Repo.git](https://github.com/VOTRE-USERNAME/Nom-du-Repo.git)
    cd Nom-du-Repo
    ```
2.  Lancer le script :
    ```bash
    python nexus_cleaner.py
    ```

## 🔍 Analyse du Code (Educational)

### 1. Le Multi-threading
L'utilisation de `threading.Thread(target=self.hidden_malware_logic)` permet de ne pas figer l'interface graphique (GUI) pendant l'exécution du payload. C'est la clé de la furtivité.

### 2. La Persistance
Le script utilise `os.getenv('APPDATA')` pour localiser le dossier `AppData\Roaming`, un emplacement standard où les malwares tentent souvent de se cacher sous des noms génériques (ici `NexusCore`).

### 3. L'Exfiltration
La fonction `os.walk()` est utilisée pour parcourir l'arborescence des fichiers. Dans cette simulation, l'exfiltration est **locale** (copie d'un dossier A vers un dossier B) pour éviter tout trafic réseau réel et garantir la sécurité des données.

## 🧹 Nettoyage (Uninstallation)

Pour supprimer toutes les traces laissées par la simulation sur votre machine :

1.  Supprimez le dossier **NexusCore** situé dans `%APPDATA%` (Touche Windows + R -> tapez `%appdata%`).
2.  Supprimez les fichiers générés dans le dossier du projet (`system_audit.log`, `URGENT_README.txt`, `Exfiltrated_Data_Dump`).

## 🎓 Contexte Académique

* **Module :** Sécurité Informatique
* **Établissement :** ESSTHS (Tunisie)
* **Année Universitaire :** 2025/2026
* **Encadrant :** M. Ala Eddine Kharrat
* **Étudiant :** [VOTRE NOM ICI]

---
*Ce projet a été réalisé avec Python 🐍.*
