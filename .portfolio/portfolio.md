---
title: "Scanner de Ports - Outil de Reconnaissance Réseau"
description: "Scanner de ports réseau avec interface graphique moderne. Implémente des scans TCP/UDP avec détection de services."
date: "2025-11-02T01:14:22Z"
tags: ["security", "python", "network", "cybersecurity"]
lang: "fr"
featured: true
category: "security"

# Configuration techStack
techStack:
  - name: "Python 3"
    category: "language"
    icon: "🐍"
  - name: "Socket"
    category: "tool"
    icon: "🔌"
  - name: "Threading"
    category: "tool"
    icon: "⚡"
  - name: "CustomTkinter"
    category: "framework"
    icon: "🎨"
  - name: "Matplotlib"
    category: "tool"
    icon: "📊"
  - name: "lxml"
    category: "tool"
    icon: "📄"
  - name: "CTkTable"
    category: "framework"
    icon: "📋"

# Architecture du projet
architecture:
  overview: "Scanner de ports réseau avec interface graphique moderne développé en Python. Implémente des scans TCP/UDP avec détection de services via banner grabbing. Interface CustomTkinter avec visualisation des résultats et export des données."
  components:
    - "Interface Graphique (CustomTkinter) : Saisie IP/URL, sélection ports, contrôles scan"
    - "Moteur de Scan : Thread principal, gestion timeouts, file d'attente résultats"
    - "Module TCP Scanner : Connexion complète, banner grabbing, détection services"
    - "Module UDP Scanner : Envoi datagrammes, détection timeout-based"
    - "Visualisation : Tableau CTkTable, graphiques Matplotlib, indicateurs visuels"
    - "Export : Format JSON structuré, CSV, sauvegarde résultats"

# Diagrammes d'architecture
diagrams:
  - path: "/diagrams/github/scanner-port-architecture.svg"
    title: "Architecture globale du scanner"
    description: "Vue d'ensemble de l'architecture avec composants et flux de données"

# URLs et liens
demo_url: ""
demo_label: ""
github_repo: "Tyno14/Scanner-port"
github_url: "https://github.com/Tyno14/Scanner-port"
github_stars: 0
github_language: "Python"
---

## 🎯 Contexte et Objectifs

<div class="overview-hero dark:bg-gradient-to-br dark:from-red-900/10 dark:to-orange-900/10 bg-gradient-to-br from-red-50 to-orange-50 border dark:border-red-500/30 border-red-200 rounded-2xl p-8 my-8 shadow-lg">
  <p class="text-lg dark:text-white/90 text-slate-700 leading-relaxed mb-6">
    Projet personnel réalisé dans le cadre de ma formation en <strong class="dark:text-red-400 text-red-600">cybersécurité</strong> pour comprendre en profondeur le fonctionnement des scanners de ports et les mécanismes de reconnaissance réseau.
  </p>
  
  <div class="text-sm dark:text-white/70 text-slate-600">
    <strong>Problématique :</strong> En tant qu'étudiant en cybersécurité, il est essentiel de comprendre comment fonctionnent les outils de reconnaissance réseau. Ce projet permet d'apprendre par la pratique les mécanismes sous-jacents des scanners de ports professionnels comme Nmap.
  </div>
</div>

### Objectifs pédagogiques

<div class="objectives-grid grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 my-8">
  <div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 hover:scale-105 transition-all duration-300 hover:shadow-xl">
    <div class="icon-wrapper text-4xl mb-4 flex items-center justify-center w-16 h-16 rounded-full dark:bg-blue-500/10 bg-blue-100 mx-auto">
      🔌
    </div>
    <h3 class="text-lg font-bold mb-3 dark:text-white text-slate-900 text-center">Protocoles TCP/UDP</h3>
    <p class="dark:text-white/70 text-slate-600 text-sm text-center">Comprendre les protocoles au niveau applicatif</p>
  </div>
  
  <div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 hover:scale-105 transition-all duration-300 hover:shadow-xl">
    <div class="icon-wrapper text-4xl mb-4 flex items-center justify-center w-16 h-16 rounded-full dark:bg-green-500/10 bg-green-100 mx-auto">
      🐍
    </div>
    <h3 class="text-lg font-bold mb-3 dark:text-white text-slate-900 text-center">Programmation Réseau</h3>
    <p class="dark:text-white/70 text-slate-600 text-sm text-center">Maîtriser la programmation réseau avec Python</p>
  </div>
  
  <div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 hover:scale-105 transition-all duration-300 hover:shadow-xl">
    <div class="icon-wrapper text-4xl mb-4 flex items-center justify-center w-16 h-16 rounded-full dark:bg-purple-500/10 bg-purple-100 mx-auto">
      🔍
    </div>
    <h3 class="text-lg font-bold mb-3 dark:text-white text-slate-900 text-center">Détection de Services</h3>
    <p class="dark:text-white/70 text-slate-600 text-sm text-center">Apprendre les techniques de banner grabbing</p>
  </div>
  
  <div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 hover:scale-105 transition-all duration-300 hover:shadow-xl">
    <div class="icon-wrapper text-4xl mb-4 flex items-center justify-center w-16 h-16 rounded-full dark:bg-pink-500/10 bg-pink-100 mx-auto">
      🎨
    </div>
    <h3 class="text-lg font-bold mb-3 dark:text-white text-slate-900 text-center">Interface Graphique</h3>
    <p class="dark:text-white/70 text-slate-600 text-sm text-center">Développer une interface professionnelle</p>
  </div>
  
  <div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 hover:scale-105 transition-all duration-300 hover:shadow-xl">
    <div class="icon-wrapper text-4xl mb-4 flex items-center justify-center w-16 h-16 rounded-full dark:bg-red-500/10 bg-red-100 mx-auto">
      ⚖️
    </div>
    <h3 class="text-lg font-bold mb-3 dark:text-white text-slate-900 text-center">Éthique</h3>
    <p class="dark:text-white/70 text-slate-600 text-sm text-center">S'initier aux bonnes pratiques d'éthique en cybersécurité</p>
  </div>
</div>

## ⚙️ Fonctionnalités Principales

<div class="features-section my-12">
  <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
    <div class="feature-card p-6 rounded-xl dark:bg-gradient-to-br dark:from-blue-900/20 dark:to-cyan-900/20 bg-gradient-to-br from-blue-50 to-cyan-50 border dark:border-blue-500/30 border-blue-200">
      <div class="flex items-start gap-4">
        <div class="icon-box w-12 h-12 rounded-lg dark:bg-blue-500/20 bg-blue-200 flex items-center justify-center flex-shrink-0 text-2xl">
          ✅
        </div>
        <div>
          <h3 class="text-xl font-bold mb-2 dark:text-white text-slate-900">Scan TCP</h3>
          <p class="dark:text-white/70 text-slate-600 text-sm mb-2">Connexion complète pour détecter les ports ouverts</p>
          <ul class="text-sm dark:text-white/60 text-slate-500 space-y-1">
            <li>• Three-way handshake</li>
            <li>• Banner grabbing</li>
            <li>• Détection services (HTTP, SSH, FTP, etc.)</li>
          </ul>
        </div>
      </div>
    </div>
    
    <div class="feature-card p-6 rounded-xl dark:bg-gradient-to-br dark:from-green-900/20 dark:to-teal-900/20 bg-gradient-to-br from-green-50 to-teal-50 border dark:border-green-500/30 border-green-200">
      <div class="flex items-start gap-4">
        <div class="icon-box w-12 h-12 rounded-lg dark:bg-green-500/20 bg-green-200 flex items-center justify-center flex-shrink-0 text-2xl">
          📡
        </div>
        <div>
          <h3 class="text-xl font-bold mb-2 dark:text-white text-slate-900">Scan UDP</h3>
          <p class="dark:text-white/70 text-slate-600 text-sm mb-2">Détection de services UDP</p>
          <ul class="text-sm dark:text-white/60 text-slate-500 space-y-1">
            <li>• Envoi de datagrammes</li>
            <li>• Détection timeout-based</li>
            <li>• Identification ports ouverts/filtrés</li>
          </ul>
        </div>
      </div>
    </div>
    
    <div class="feature-card p-6 rounded-xl dark:bg-gradient-to-br dark:from-purple-900/20 dark:to-pink-900/20 bg-gradient-to-br from-purple-50 to-pink-50 border dark:border-purple-500/30 border-purple-200">
      <div class="flex items-start gap-4">
        <div class="icon-box w-12 h-12 rounded-lg dark:bg-purple-500/20 bg-purple-200 flex items-center justify-center flex-shrink-0 text-2xl">
          🎯
        </div>
        <div>
          <h3 class="text-xl font-bold mb-2 dark:text-white text-slate-900">Plage Personnalisable</h3>
          <p class="dark:text-white/70 text-slate-600 text-sm mb-2">Scannez de 1 à 65535 ports</p>
          <ul class="text-sm dark:text-white/60 text-slate-500 space-y-1">
            <li>• Ports spécifiques</li>
            <li>• Plages multiples</li>
            <li>• Scan ciblé</li>
          </ul>
        </div>
      </div>
    </div>
    
    <div class="feature-card p-6 rounded-xl dark:bg-gradient-to-br dark:from-orange-900/20 dark:to-red-900/20 bg-gradient-to-br from-orange-50 to-red-50 border dark:border-orange-500/30 border-orange-200">
      <div class="flex items-start gap-4">
        <div class="icon-box w-12 h-12 rounded-lg dark:bg-orange-500/20 bg-orange-200 flex items-center justify-center flex-shrink-0 text-2xl">
          📊
        </div>
        <div>
          <h3 class="text-xl font-bold mb-2 dark:text-white text-slate-900">Visualisation</h3>
          <p class="dark:text-white/70 text-slate-600 text-sm mb-2">Résultats clairs et détaillés</p>
          <ul class="text-sm dark:text-white/60 text-slate-500 space-y-1">
            <li>• Tableau interactif</li>
            <li>• Graphiques Matplotlib</li>
            <li>• Export JSON/CSV</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>

## 📦 Installation et Utilisation

### Prérequis

- Python 3.x (3.7 ou supérieur recommandé)
- Pip pour l'installation des dépendances
- Système : Linux, macOS, Windows

### Installation

```bash
# Cloner le dépôt
git clone https://github.com/Tyno14/Scanner-port.git
cd Scanner-port

# Installer les dépendances
pip install -r requirements.txt

# Ou installer manuellement
pip install customtkinter matplotlib lxml CTkTable
```

### Lancement

```bash
# Lancer l'interface graphique
python scanner.py

# Ou avec Python 3 explicitement
python3 scanner.py
```

### Utilisation de l'Interface

1. **Saisir la cible** : Entrez une adresse IP ou un nom de domaine
   - Exemple : `192.168.1.1` ou `example.com`

2. **Définir la plage** : Choisissez les ports à scanner
   - Ports courants : `1-1024`
   - Tous les ports : `1-65535`
   - Ports spécifiques : `80,443,8080`

3. **Sélectionner le type** : TCP, UDP ou les deux

4. **Lancer le scan** : Cliquez sur "Start Scan"

5. **Visualiser les résultats** :
   - Tableau interactif avec détails
   - Graphiques statistiques
   - Ports ouverts mis en évidence

6. **Exporter** : Sauvegardez en JSON ou CSV

## 🔬 Caractéristiques Techniques

<div class="tech-features grid grid-cols-1 md:grid-cols-2 gap-6 my-8">
  <div class="tech-card p-6 rounded-xl dark:bg-blue-500/10 bg-blue-50 border dark:border-blue-500/20 border-blue-200">
    <div class="flex items-center gap-3 mb-4">
      <span class="text-3xl">⚡</span>
      <h3 class="text-lg font-bold dark:text-white text-slate-900">TCP Connect Scan</h3>
    </div>
    <p class="dark:text-white/70 text-slate-600 text-sm mb-2">Connexion complète (SYN → SYN/ACK → ACK)</p>
    <div class="code-box p-3 rounded dark:bg-black/20 bg-white/50 font-mono text-xs dark:text-white/80 text-slate-700">
      socket.connect((target, port))
    </div>
  </div>
  
  <div class="tech-card p-6 rounded-xl dark:bg-green-500/10 bg-green-50 border dark:border-green-500/20 border-green-200">
    <div class="flex items-center gap-3 mb-4">
      <span class="text-3xl">📡</span>
      <h3 class="text-lg font-bold dark:text-white text-slate-900">UDP Scan</h3>
    </div>
    <p class="dark:text-white/70 text-slate-600 text-sm mb-2">Envoi de datagrammes avec détection timeout</p>
    <div class="code-box p-3 rounded dark:bg-black/20 bg-white/50 font-mono text-xs dark:text-white/80 text-slate-700">
      sock.sendto(packet, (target, port))
    </div>
  </div>
  
  <div class="tech-card p-6 rounded-xl dark:bg-purple-500/10 bg-purple-50 border dark:border-purple-500/20 border-purple-200">
    <div class="flex items-center gap-3 mb-4">
      <span class="text-3xl">🔍</span>
      <h3 class="text-lg font-bold dark:text-white text-slate-900">Banner Grabbing</h3>
    </div>
    <p class="dark:text-white/70 text-slate-600 text-sm mb-2">Récupération des 1024 premiers octets</p>
    <div class="code-box p-3 rounded dark:bg-black/20 bg-white/50 font-mono text-xs dark:text-white/80 text-slate-700">
      banner = sock.recv(1024)
    </div>
  </div>
  
  <div class="tech-card p-6 rounded-xl dark:bg-orange-500/10 bg-orange-50 border dark:border-orange-500/20 border-orange-200">
    <div class="flex items-center gap-3 mb-4">
      <span class="text-3xl">⏱️</span>
      <h3 class="text-lg font-bold dark:text-white text-slate-900">Timeouts</h3>
    </div>
    <p class="dark:text-white/70 text-slate-600 text-sm mb-2">2 secondes par défaut (configurable)</p>
    <div class="code-box p-3 rounded dark:bg-black/20 bg-white/50 font-mono text-xs dark:text-white/80 text-slate-700">
      sock.settimeout(2.0)
    </div>
  </div>
</div>

## ⚠️ Sécurité et Éthique

<div class="warning-box p-6 rounded-xl dark:bg-red-900/20 bg-red-50 border-2 dark:border-red-500/50 border-red-300 my-8">
  <div class="flex items-start gap-4">
    <div class="text-4xl">⚠️</div>
    <div>
      <h3 class="text-xl font-bold mb-3 dark:text-red-400 text-red-700">Avertissements Légaux</h3>
      <p class="dark:text-white/90 text-slate-700 mb-4 font-semibold">IMPORTANT - À LIRE AVANT UTILISATION :</p>
      
      <div class="space-y-3 dark:text-white/80 text-slate-600">
        <div>
          <strong class="dark:text-white text-slate-900">1. Utilisation légale uniquement</strong>
          <p class="text-sm mt-1">N'utilisez cet outil que sur :</p>
          <ul class="text-sm ml-4 mt-1 space-y-1">
            <li>• Vos propres systèmes et réseaux</li>
            <li>• Des systèmes pour lesquels vous avez une autorisation écrite explicite</li>
            <li>• Des environnements de test/lab personnels</li>
          </ul>
        </div>
        
        <div>
          <strong class="dark:text-white text-slate-900">2. Illégalité</strong>
          <p class="text-sm mt-1">Le scan de ports non autorisé est :</p>
          <ul class="text-sm ml-4 mt-1 space-y-1">
            <li>• Illégal dans de nombreux pays (France, USA, UK, etc.)</li>
            <li>• Considéré comme une intrusion informatique</li>
            <li>• Passible de poursuites pénales et d'amendes</li>
          </ul>
        </div>
        
        <div>
          <strong class="dark:text-white text-slate-900">3. Usage éducatif recommandé</strong>
          <p class="text-sm mt-1">Utilisez dans :</p>
          <ul class="text-sm ml-4 mt-1 space-y-1">
            <li>• Labs personnels : VMs, containers Docker</li>
            <li>• Plateformes légales : HackTheBox, TryHackMe, PentesterLab</li>
            <li>• Cours/certifications : CEH, OSCP, eJPT</li>
            <li>• Réseaux de test : GNS3, Packet Tracer</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>

### ✅ Bonnes Pratiques Éthiques

<div class="grid grid-cols-1 md:grid-cols-2 gap-4 my-6">
  <div class="p-4 rounded-lg dark:bg-green-900/20 bg-green-50 border dark:border-green-500/30 border-green-200">
    <h4 class="font-bold mb-2 dark:text-green-400 text-green-700 flex items-center gap-2">
      <span>✅</span> À FAIRE
    </h4>
    <ul class="text-sm dark:text-white/70 text-slate-600 space-y-1">
      <li>• Obtenir une autorisation écrite avant tout scan</li>
      <li>• Utiliser dans un environnement lab/sandbox</li>
      <li>• Documenter vos tests de sécurité</li>
      <li>• Respecter les règles d'engagement</li>
    </ul>
  </div>
  
  <div class="p-4 rounded-lg dark:bg-red-900/20 bg-red-50 border dark:border-red-500/30 border-red-200">
    <h4 class="font-bold mb-2 dark:text-red-400 text-red-700 flex items-center gap-2">
      <span>❌</span> À NE PAS FAIRE
    </h4>
    <ul class="text-sm dark:text-white/70 text-slate-600 space-y-1">
      <li>• Scanner des systèmes publics sans autorisation</li>
      <li>• Utiliser pour du hacking malveillant</li>
      <li>• Ignorer les avertissements légaux</li>
      <li>• Tester sur des infrastructures critiques</li>
    </ul>
  </div>
</div>

## 📚 Apprentissages et Compétences Acquises

<div class="learning-section my-12">
  <h3 class="text-2xl font-bold mb-6 dark:text-white text-slate-900 flex items-center gap-3">
    <span class="text-3xl">🎓</span>
    Compétences Techniques
  </h3>
  
  <div class="space-y-4">
    <div class="skill-item p-4 rounded-lg dark:bg-white/5 bg-white border dark:border-white/10 border-slate-200">
      <h4 class="font-bold mb-2 dark:text-white text-slate-900">Programmation Réseau</h4>
      <p class="text-sm dark:text-white/70 text-slate-600">Manipulation bas niveau des sockets TCP/UDP, gestion des connexions, timeouts et erreurs réseau</p>
    </div>
    
    <div class="skill-item p-4 rounded-lg dark:bg-white/5 bg-white border dark:border-white/10 border-slate-200">
      <h4 class="font-bold mb-2 dark:text-white text-slate-900">Protocoles Réseau</h4>
      <p class="text-sm dark:text-white/70 text-slate-600">Compréhension approfondie de TCP (SYN/ACK), UDP, et des différences entre les deux protocoles</p>
    </div>
    
    <div class="skill-item p-4 rounded-lg dark:bg-white/5 bg-white border dark:border-white/10 border-slate-200">
      <h4 class="font-bold mb-2 dark:text-white text-slate-900">Threading et Concurrence</h4>
      <p class="text-sm dark:text-white/70 text-slate-600">Gestion de threads multiples pour scanner plusieurs ports simultanément sans bloquer l'interface</p>
    </div>
    
    <div class="skill-item p-4 rounded-lg dark:bg-white/5 bg-white border dark:border-white/10 border-slate-200">
      <h4 class="font-bold mb-2 dark:text-white text-slate-900">Développement GUI</h4>
      <p class="text-sm dark:text-white/70 text-slate-600">Création d'interfaces graphiques modernes avec CustomTkinter et intégration de visualisations</p>
    </div>
  </div>
</div>

## 🚀 Évolutions Possibles

- 🔄 **SYN Scan** : Implémentation de scans furtifs (nécessite droits root)
- 🌐 **Scan de sous-réseaux** : Support CIDR (192.168.1.0/24)
- 📊 **Dashboard temps réel** : Graphiques animés pendant le scan
- 💾 **Base de données** : Historique et comparaison de scans
- 🔔 **Alertes** : Notifications pour ports critiques ouverts
- 🎯 **Presets** : Profils de scan pré-configurés (Quick, Deep, Stealth)
- 🔐 **Authentification** : Test de connexion aux services détectés

## � Ressources & Documentation

<div class="documentation-grid grid grid-cols-1 md:grid-cols-2 gap-6 my-8">
  
  <div class="doc-card dark:bg-gradient-to-br dark:from-slate-900/50 dark:to-slate-800/50 bg-gradient-to-br from-slate-50 to-slate-100 border dark:border-white/10 border-slate-300 rounded-2xl p-6 hover:scale-[1.02] transition-all duration-300 cursor-pointer" data-doc-type="details">
    <div class="flex items-center gap-3 mb-4">
      <span class="text-3xl">📖</span>
      <h3 class="text-lg font-bold dark:text-white text-slate-900">Documentation complète</h3>
    </div>
    <ul class="space-y-3">
      <li class="flex items-start gap-2">
        <span class="text-blue-500">▸</span>
        <span class="dark:text-white/70 text-slate-600">Guide d'installation détaillé</span>
      </li>
      <li class="flex items-start gap-2">
        <span class="text-blue-500">▸</span>
        <span class="dark:text-white/70 text-slate-600">Utilisation pas à pas de l'interface</span>
      </li>
      <li class="flex items-start gap-2">
        <span class="text-blue-500">▸</span>
        <span class="dark:text-white/70 text-slate-600">Exemples de scan et cas d'usage</span>
      </li>
      <li class="flex items-start gap-2">
        <span class="text-blue-500">▸</span>
        <span class="dark:text-white/70 text-slate-600">Guide d'éthique et bonnes pratiques</span>
      </li>
    </ul>
    <div class="mt-4 text-center">
      <span class="text-sm dark:text-blue-400 text-blue-600 font-semibold">→ Voir les détails techniques</span>
    </div>
  </div>

  <div class="doc-card dark:bg-gradient-to-br dark:from-purple-900/30 dark:to-indigo-900/30 bg-gradient-to-br from-purple-50 to-indigo-50 border dark:border-purple-500/30 border-purple-300 rounded-2xl p-6 hover:scale-[1.02] transition-all duration-300 cursor-pointer" data-doc-type="architecture">
    <div class="flex items-center gap-3 mb-4">
      <span class="text-3xl">🗺️</span>
      <h3 class="text-lg font-bold dark:text-white text-slate-900">Diagramme interactif</h3>
    </div>
    <p class="dark:text-white/70 text-slate-600 mb-4">Visualisation complète de l'architecture avec détails pour chaque composant du scanner.</p>
    <div class="flex flex-wrap gap-2 mb-4">
      <span class="px-3 py-1 dark:bg-blue-500/20 bg-blue-200 dark:text-blue-300 text-blue-700 rounded-full text-xs">Interface</span>
      <span class="px-3 py-1 dark:bg-purple-500/20 bg-purple-200 dark:text-purple-300 text-purple-700 rounded-full text-xs">Moteur</span>
      <span class="px-3 py-1 dark:bg-green-500/20 bg-green-200 dark:text-green-300 text-green-700 rounded-full text-xs">TCP/UDP</span>
      <span class="px-3 py-1 dark:bg-orange-500/20 bg-orange-200 dark:text-orange-300 text-orange-700 rounded-full text-xs">Visualisation</span>
    </div>
    <div class="text-center">
      <span class="text-sm dark:text-purple-400 text-purple-600 font-semibold">→ Voir l'architecture</span>
    </div>
  </div>

</div>

### 📚 Ressources Externes

<div class="resources-grid grid grid-cols-1 md:grid-cols-2 gap-4 my-6">
  <a href="https://docs.python.org/3/library/socket.html" target="_blank" class="resource-link p-4 rounded-lg dark:bg-white/5 bg-white border dark:border-white/10 border-slate-200 hover:scale-[1.02] transition-all duration-300 hover:shadow-lg">
    <div class="flex items-center gap-3">
      <span class="text-2xl">📘</span>
      <div>
        <h4 class="font-semibold dark:text-white text-slate-900">Python Socket Docs</h4>
        <p class="text-xs dark:text-white/60 text-slate-600">Documentation officielle des sockets</p>
      </div>
    </div>
  </a>
  
  <a href="https://github.com/TomSchimansky/CustomTkinter" target="_blank" class="resource-link p-4 rounded-lg dark:bg-white/5 bg-white border dark:border-white/10 border-slate-200 hover:scale-[1.02] transition-all duration-300 hover:shadow-lg">
    <div class="flex items-center gap-3">
      <span class="text-2xl">🎨</span>
      <div>
        <h4 class="font-semibold dark:text-white text-slate-900">CustomTkinter</h4>
        <p class="text-xs dark:text-white/60 text-slate-600">Framework GUI moderne pour Python</p>
      </div>
    </div>
  </a>
  
  <a href="https://nmap.org/book/man.html" target="_blank" class="resource-link p-4 rounded-lg dark:bg-white/5 bg-white border dark:border-white/10 border-slate-200 hover:scale-[1.02] transition-all duration-300 hover:shadow-lg">
    <div class="flex items-center gap-3">
      <span class="text-2xl">🔍</span>
      <div>
        <h4 class="font-semibold dark:text-white text-slate-900">Nmap Reference</h4>
        <p class="text-xs dark:text-white/60 text-slate-600">Guide de référence du scanner professionnel</p>
      </div>
    </div>
  </a>
  
  <a href="https://www.hackthebox.com/" target="_blank" class="resource-link p-4 rounded-lg dark:bg-white/5 bg-white border dark:border-white/10 border-slate-200 hover:scale-[1.02] transition-all duration-300 hover:shadow-lg">
    <div class="flex items-center gap-3">
      <span class="text-2xl">🎯</span>
      <div>
        <h4 class="font-semibold dark:text-white text-slate-900">HackTheBox</h4>
        <p class="text-xs dark:text-white/60 text-slate-600">Plateforme légale de pentesting</p>
      </div>
    </div>
  </a>
  
  <a href="https://tryhackme.com/" target="_blank" class="resource-link p-4 rounded-lg dark:bg-white/5 bg-white border dark:border-white/10 border-slate-200 hover:scale-[1.02] transition-all duration-300 hover:shadow-lg">
    <div class="flex items-center gap-3">
      <span class="text-2xl">🛡️</span>
      <div>
        <h4 class="font-semibold dark:text-white text-slate-900">TryHackMe</h4>
        <p class="text-xs dark:text-white/60 text-slate-600">Apprentissage cybersécurité interactif</p>
      </div>
    </div>
  </a>
  
  <a href="https://www.pentesterlab.com/" target="_blank" class="resource-link p-4 rounded-lg dark:bg-white/5 bg-white border dark:border-white/10 border-slate-200 hover:scale-[1.02] transition-all duration-300 hover:shadow-lg">
    <div class="flex items-center gap-3">
      <span class="text-2xl">💻</span>
      <div>
        <h4 class="font-semibold dark:text-white text-slate-900">PentesterLab</h4>
        <p class="text-xs dark:text-white/60 text-slate-600">Exercices pratiques de pentest</p>
      </div>
    </div>
  </a>
</div>

<script is:inline>
  document.addEventListener('DOMContentLoaded', function() {
    const docCards = document.querySelectorAll('[data-doc-type]');
    docCards.forEach(card => {
      card.addEventListener('click', function() {
        const type = this.getAttribute('data-doc-type');
        const tabButton = document.querySelector(`[data-tab="${type}"]`);
        if (tabButton) {
          tabButton.click();
        }
      });
    });
  });
</script>

---

**Projet éducatif** | **Formation Cybersécurité 2025** | **⚠️ Utilisation responsable uniquement**
