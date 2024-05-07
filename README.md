# Projet Hébergement Mutualisé de Sites Web

## Description
Ce projet implémente une solution d'hébergement mutualisé pour plusieurs sites web sur un serveur Apache, similaire à des solutions comme OVH. L'objectif est de permettre à plusieurs groupes de gérer leurs propres sites tout en partageant les ressources du serveur de manière sécurisée.

## Fonctionnalités
- **Hébergement Mutualisé:** Plusieurs sites web hébergés sur un seul serveur Apache.
- **Sécurité Renforcée:** Configuration sécurisée du serveur web, FTP, et des bases de données.
- **Automatisation:** Scripts pour automatiser le déploiement et la gestion des sites web.

## Outils et Technologies Utilisés
- **Apache:** Serveur web pour l'hébergement des sites.
- **MySQL:** Gestion des bases de données pour les sites.
- **PHP:** Support pour les scripts côté serveur.
- **Python:** Scripts d'automatisation pour la gestion des sites.

## Installation

### Prérequis
- Apache
- MySQL
- Python 3.x

### Librairies Python à installer
```bash
pip install flask
pip install sqlalchemy
pip install mysql.connector
