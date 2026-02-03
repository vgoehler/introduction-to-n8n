# Introduction to n8n

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://raw.githubusercontent.com/vgoehler/introduction-to-n8n/refs/heads/main/lesson_01.md)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![GitHub stars](https://img.shields.io/github/stars/vgoehler/introduction-to-n8n?style=social)](https://github.com/vgoehler/introduction-to-n8n/stargazers)

## Über dieses Projekt / About this Project

Dieses Modul bietet eine Einführung in **n8n**, eine Open-Source-Workflow-Automatisierungsplattform. Die Teilnehmer lernen, wie sie n8n installieren, konfigurieren und nutzen können, um verschiedene Anwendungen und Dienste zu integrieren und automatisierte Workflows zu erstellen.

This module provides an introduction to **n8n**, an open-source workflow automation platform. Participants will learn how to install, configure, and use n8n to integrate various applications and services and create automated workflows.

> **Open Educational Resource** für das Modul "Verteilte Software" an der TU Bergakademie Freiberg

## 📚 Kursübersicht / Course Overview

- [Einführung in N8N](lesson_01.md) - Grundlagen und erste Schritte
- [Weiterführende Konzepte in N8N](lesson_02.md) - Erweiterte Funktionen
- [API-Nutzung und System mit N8N](lesson_03.md) - API-Integration
- [REST API mit N8N](lesson_04.md) - RESTful Services
- [MCP Tools an eine REST API anschließen](lesson_05.md) - Tool-Integration
- [Blockaufgabe -- Päläo REST an eine KI anschließen](lesson_06.md) - Praxisaufgabe

## 🚀 n8n Installation

### Voraussetzungen / Prerequisites

- Docker und Docker Compose (empfohlen / recommended)
- Alternativ: Node.js 18.x oder höher
- Mindestens 4GB RAM
- Webbrowser (Chrome, Firefox, Safari, Edge)

### Installation mit Docker (Empfohlen / Recommended)

Die einfachste Methode ist die Verwendung von Docker Compose. Dieses Repository enthält bereits eine `docker-compose.yaml` Datei.

The easiest method is using Docker Compose. This repository already includes a `docker-compose.yaml` file.

```bash
# Repository klonen / Clone repository
git clone https://github.com/vgoehler/introduction-to-n8n.git
cd introduction-to-n8n

# n8n starten / Start n8n
docker-compose up -d

# n8n ist nun verfügbar unter / n8n is now available at
# http://localhost:5678
```

**n8n stoppen / Stop n8n:**
```bash
docker-compose down
```

**Logs ansehen / View logs:**
```bash
docker-compose logs -f n8n
```

### Alternative Installation mit npm

```bash
# Global installation
npm install n8n -g

# n8n starten / Start n8n
n8n

# n8n ist nun verfügbar unter / n8n is now available at
# http://localhost:5678
```

### Alternative Installation mit npx

```bash
# Ohne Installation direkt ausführen / Run directly without installation
npx n8n
```

### Desktop App

n8n bietet auch eine Desktop-Anwendung für Windows, macOS und Linux:
- Download: https://n8n.io/download

## 📖 LiaScript - Interaktive Kurse

Die Kursmaterialien sind mit **LiaScript** erstellt, einem Markdown-basierten Format für interaktive Online-Kurse.

The course materials are created with **LiaScript**, a Markdown-based format for interactive online courses.

### LiaScript Kurse ansehen / View LiaScript Courses

**Option 1: Online (Empfohlen / Recommended)**

Klicken Sie einfach auf das LiaScript Badge oben oder verwenden Sie diese URL:

Simply click the LiaScript badge above or use this URL:

```
https://liascript.github.io/course/?https://raw.githubusercontent.com/vgoehler/introduction-to-n8n/refs/heads/main/lesson_01.md
```

Für andere Lektionen, ersetzen Sie `lesson_01.md` durch `lesson_02.md`, `lesson_03.md`, etc.

For other lessons, replace `lesson_01.md` with `lesson_02.md`, `lesson_03.md`, etc.

**Option 2: PDF Export**

PDFs können mit dem Makefile generiert werden:

PDFs can be generated using the Makefile:

```bash
# Voraussetzungen installieren / Install prerequisites
npm install -g liascript-exporter

# PDFs generieren / Generate PDFs
make pdf

# Dies erstellt / This creates:
# - n8n_01.pdf, n8n_02.pdf, ... (Lektionen / Lessons)
# - planing_01.pdf, planing_02.pdf, ... (Planungsdokumente / Planning docs)
```

### Was ist LiaScript? / What is LiaScript?

LiaScript ist ein Werkzeug zur Erstellung interaktiver Bildungsinhalte:

LiaScript is a tool for creating interactive educational content:

- ✅ **Markdown-basiert** - Einfache Syntax
- ✅ **Interaktiv** - Quizze, Animationen, Code-Ausführung
- ✅ **Open Source** - Frei verfügbar
- ✅ **Keine Server nötig** - Läuft im Browser
- ✅ **Versionskontrolle** - Über Git/GitHub

Mehr Informationen: https://liascript.github.io

## 🛠️ Entwicklung / Development

### Repository Struktur / Repository Structure

```
.
├── lesson_*.md         # LiaScript Kurs-Lektionen / Course lessons
├── planing_*.md        # Planungsdokumente / Planning documents
├── docker-compose.yaml # n8n Docker Konfiguration / n8n Docker config
├── Makefile           # Build-Automatisierung / Build automation
├── styles.css         # Custom LiaScript Styles
├── img/               # Bilder / Images
└── README.md          # Diese Datei / This file
```

### Kurse bearbeiten / Edit Courses

1. Bearbeiten Sie die `lesson_*.md` Dateien / Edit the `lesson_*.md` files
2. Testen Sie im LiaScript Viewer / Test in LiaScript viewer
3. Committen Sie Ihre Änderungen / Commit your changes

## 📝 Lizenz / License

Dieses Projekt ist lizenziert unter der Creative Commons Attribution-ShareAlike 4.0 International License.

This project is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.

Siehe [LICENSE](LICENSE) für weitere Details / See [LICENSE](LICENSE) for details.

## 👤 Autor / Author

**Volker G. Göhler**
- TU Bergakademie Freiberg
- Email: volker.goehler@informatik.tu-freiberg.de

## 🔗 Nützliche Links / Useful Links

- **n8n Dokumentation / Documentation**: https://docs.n8n.io
- **n8n Community Forum**: https://community.n8n.io
- **LiaScript**: https://liascript.github.io
- **GitHub Repository**: https://github.com/vgoehler/introduction-to-n8n
