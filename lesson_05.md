<!--

author: Volker G. Göhler

email:  volker.goehler@informatik.tu-freiberg.de

version: 0.0.1

language: de

narrator: Deutsch Male

edit: true
date: 2026
icon: img/TUBAF_Logo_EN_blau.png

logo: 
attribute: 

comment: Distributed Software

import: https://raw.githubusercontent.com/liaScript/mermaid_template/master/README.md

link: ./styles.css

title: N8N Workflows REST 05

tags: Lehre, TUBAF

-->
[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://raw.githubusercontent.com/vgoehler/introduction-to-n8n/refs/heads/main/lesson_05.md)

# n8n Workflows: REST APIs nutzen und MCP integrieren

Volker Göhler, TU Bergakademie Freiberg

------------------------------

![Welcome](https://n8n.io/brandguidelines/logo-dark.svg "n8n Logo [n8n.io](https://n8n.io/)")<!-- style="width:500px;" -->

> "Code" auf https://github.com/vgoehler/introduction-to-n8n als Open Educational Ressource.

----------------------------------------

## Rückblick

**Nachtrag vom letzten mal**<!-- class="head" -->

Was haben wir letztes Mal gemacht?

    {{1}}
- cron jobs
- error workflows
- files
- subworkflows
- REST

### REST mit n8n nutzen

<!-- class="head" -->
Hands-on: n8n Workflow

<section class="flex-container">
<div class="flex-child">
Studierende bauen einen Workflow, der:

- eine Episode-ID entgegennimmt
- alle Charaktere dieser Episode abruft
- mit Name, Species und Status auflöst
- strukturierte Daten zurückgibt

Beispiel-Ausgabe:

```json
{
  "episode": "Pilot",
  "characters": [
    {
        "name": "Rick Sanchez",
        "species": "Human", 
        "status": "Alive" },
    { 
        "name": "Morty Smith", 
        "species": "Human", 
        "status": "Alive" }
  ]
}
```

</div>
<div class="flex-child">
![](https://upload.wikimedia.org/wikipedia/commons/0/00/Zaden_van_een_Gele_lis_%28Iris_pseudacorus%29._06-03-2024._%28d.j.b.%29.jpg "Dominicus Johannes Bergsma, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons")<!-- style="min-width: 300px; width:400px; margin-top:20px;" -->
</div>
</section>

https://ifiweb.informatik.tu-freiberg.de/public/lehre/vs/api.php?action=fetch-model&model_id=1

## REST APIs für KI nutzbar machen

**Zwischenfrage: Was braucht eine KI dafür?**<!-- class="head" -->

<div class="colorbox colorbox--steps">
<div class="colorbox__title">
Ein LLM kann:
</div>

- Text verstehen (Input)
- Entscheidungen treffen (Output)
- Wissen abrufen (Training)

</div>

<!-- class="head" -->
Aber: 

- LLMs sind wahrscheinlichkeitsbasierte Textgeneratoren
- sie haben **keine** eingebauten Fähigkeiten, um Aktionen durchzuführen.

<div class="colorbox colorbox--hints">
<div class="colorbox__title">
Ein LLM kann **nicht**:
</div>

- selbst REST APIs aufrufen
- Fehler sauber behandeln
- Daten persistent speichern
- sich an vorherige Aktionen erinnern

</div>

<!-- class="lia-callout--note" -->
> ➡️ Es braucht **Werkzeuge**.

---

### Was braucht ein LLM, um REST zu nutzen?

<div class="colorbox colorbox--steps">
<div class="colorbox__title">
Notwendig sind:
</div>
- beschreibbare Funktionen
- klare Inputs
- klare Outputs
- stabile Schnittstellen
</div>

<!-- class="lia-callout--note" -->
> ➡️ Genau hier kommt **MCP** ins Spiel.


---

### Was ist MCP?

MCP = **Model Context Protocol**

Es beschreibt:

- welche Tools existieren
- wie sie aufgerufen werden
- welche Daten sie erwarten
- was sie zurückgeben

<!-- class="lia-callout--note arrow-list" -->
> - MCP verbindet **KI** mit **Systemen**.
> - [github.com/SebastianZug/MCP_tutorial](https://github.com/SebastianZug/MCP_tutorial/blob/main/mcp-kompakt.md)

---

### Verbindung: n8n ↔ MCP


<div class="colorbox colorbox--but">
<div class="colorbox__title">
In unserem Setup:
</div>
- n8n-Workflows *sind* Tools
- MCP beschreibt diese Tools
- n8n stellt die Schnittstelle bereit
- KI nutzt MCP, um n8n zu steuern
- n8n nimmt strukturierte Daten entgegen
- n8n liefert strukturierte Daten zurück
</div>

<!-- class="lia-callout--note" -->
> **LLM:**<!-- class="subhead" -->
>
> entscheidet *wann* welches Tool benutzt wird.

### 🗣️ Diskussion: Den n8n-Workflow "MCP-ready" machen

Wir wollen einen Workflow bauen, den eine KI (via MCP) selbstständig steuern kann. 
**Was sind die harten Anforderungen?**

1. **Der Startschuss**

   <!-- class="question" -->
   Wie erfährt der Workflow präzise, was er tun soll?

   {{1}} 
    <!-- class="solution" -->
   Klarer, validierter **Input** (JSON-Schema).

2. **Das Ergebnis**

   <!-- class="question" -->
   Was braucht die KI als Rückmeldung, um den nächsten Schritt zu planen?

   {{2}}
   <!-- class="solution" -->
   Strukturierter **Output** (JSONS).

3. **Wenn es knallt**
   
   <!-- class="question" -->
   Was passiert bei fehlerhafter Eingabe, einem API-Timeout oder einem 404-Fehler?
   
   {{3}}
   <!-- class="solution" -->
   Definierte **Fehlerpfade** ([JSON RPC Errors](https://www.mcpevals.io/blog/mcp-error-codes)).

4. **User Interaktion?**
   
   <!-- class="question" -->
   Kann der Prozess ohne menschliche Interaktion überleben?

   {{4}}
   <!-- class="solution" -->
   Null **UI-Abhängigkeit** (Workflow als Service, nicht als Klickstrecke).

---

{{5}}
<!-- class="lia-callout--note" -->
> 💡 **Zusammenfassung:**
> Ein MCP-Workflow ist eine **autonome Funktion**.
> Er muss **klar definierte Schnittstellen** haben, um von einer KI sicher genutzt zu werden.

### Beispiel: MCP in n8n nutzen

<div class="colorbox colorbox--but">
<div class="colorbox__title">
Beispiel MCP Workflow:
</div>

- [MCP in the Docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger/#how-the-mcp-server-trigger-node-works)
- MCP Server Node
- Call n8n Worflow Tool
</div>

<!-- class="head" -->
**Zwei Möglichkeiten für Tools:**

<!-- class="arrow-list" -->
- subworkflow als Tool im MCP-Workflow aufrufen
- subworkflow im MCP-Workflow aufrufen

<!-- class="lia-callout--note" -->
> Parameterdefinition und Output-Schema müssen klar definiert sein.


### Aufgabe: MCP für den REST-Workflow

<section class="flex-container">
<div class="flex-child">

basierend auf der vorherigen Aufgabe sollen Studierende:

<div class="colorbox colorbox--steps">

- einen **Subworkflow** bauen der

   - eine Episoden-ID entgegennimmt
   - Charakternamen mit Status und Species dieser Episode zurückgibt

- einen **MCP-Workflow** bauen, der

   - den Subworkflow als Tool nutzt
   - die Eingabe in der Trigger Node definieren
   - die Ausgabe des Subworkflows festlegen
   - Episoden-ID als KI-Input erlaubt

</div>

<div class="colorbox colorbox--hints">
<div class="colorbox__title">
Bonus Tools:
</div>

1. Anstelle der Id den Episodentitle als Input nutzen
2. Eine Blacklist für Charakternamen implementieren
3. Für den Charakternamen alle Episodentitle zurückgeben wo dieser vorkommt.

</div>
</div>

<div class="flex-child">
![](https://upload.wikimedia.org/wikipedia/commons/6/68/Orchards_in_snow%2C_Sangla%2C_Himachal_Pradesh%2C_India.jpg "UnpetitproleX, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons")<!-- style="min-width: 300px; width:400px; margin-top:20px;" -->
</div>
</section>

---

### Reflexion

Diskussionsfragen:

- Was passiert bei falschen Parametern?
- Welche Fehler kann die KI nicht erkennen?
- Wo braucht es menschliche Kontrolle?

---

### Takeaways

- KI halluziniert ohne Informationen
- KI braucht Werkzeuge für Aktionen
- MCP verbindet KI mit realer Funktionalität
- n8n Workflows können als MCP-Tools dienen
- Klare Inputs/Outputs sind essenziell

---

![Claude Monet Gemälde Soleil Levant](https://upload.wikimedia.org/wikipedia/commons/5/54/Claude_Monet%2C_Impression%2C_soleil_levant.jpg "Claude Monet, Public domain, via Wikimedia Commons")<!-- style="width:500px;" -->

> "Impression, soleil levant" von Claude Monet (1872) gilt als das Gemälde, das der Impressionismus-Bewegung ihren Namen gab.

## Vorbereitung für die Blockaufgabe

- REST API aus Übung 8
- an n8n anschließen
- MCP dafür nutzen
- LLM Zugang für n8n


### Paläo REST API

- In Übung 8 haben Sie eine REST API geschrieben.
- starten Sie diese lokal oder auf einem Server (nutzen Sie z.B. `uvicorn`)
- Lösungscode: [Übung 8 REST API](https://ificloud.xsitepool.tu-freiberg.de/index.php/s/ZtZo32PsDLdGioR)

<div class="colorbox colorbox--but">
<div class="colorbox__title">
Nutzen Sie die API in einem n8n Workflow
</div>

- crawlen Sie die Päleontologische Sammlung der TUBAF um Daten abzurufen und zu speichern
- [Digitale Päleontologische Sammlung der TUBAF](https://ifiweb.informatik.tu-freiberg.de/public/paleoweb/index.html)
- Endpoint: https://ifiweb.informatik.tu-freiberg.de/public/lehre/vs/api.php?action=fetch-model&model_id=<ID_NR>
- Achtung: Die ID_NR ist eine positive Zahl, die nicht notwendigerweise kontinuierlich ist.
</div>

<div class="colorbox colorbox--hints">
<div class="colorbox__title">
Hinweise:
</div>
- Was macht der Endpoint im Fehlerfall?
- Können wir Daten persistent speichern?
- Überwachung der bereits gelesenen Fosilien?
</div>

---

### 🤖 Strategien für den LLM-Zugang

<!-- class="head" -->
🌐 Option A: Cloud-API (Maximale Leistung)

- Globale Marktführer: Integration von OpenAI (GPT), Anthropic (Claude) oder Google (Gemini).
- 🇪🇺 Fokus Europa: Nutzung von Mistral AI (aus Frankreich) – exzellente Performance bei hoher Datenschutz-Konformität.
- HuggingFace Endpoints: 

    - Schnittstelle für tausende Open-Source-Modelle.
    - Achtung: Free Credits sind minimal (~10 Cent) 🐼.

- 📍 Lokal-Spezifisch: Für Göttingen (Chat-AI) kann ich bei Bedarf API-Keys bereitstellen.

<!-- class="head" -->
🏠 Option B: Lokales Self-Hosting (Maximale Kontrolle)

Die datenschutzfreundliche Lösung via Ollama direkt auf der eigenen Hardware.

- **Setup:** 📥 Runterladen (https://ollama.com/) → ⌨️ Terminal: `ollama run mistral` oder `ollama pull llama3.3`.
- **n8n-Integration:** Nahtlose Anbindung über den dedizierten Ollama-Node 🔗.
- **Hardware-Check:** 

   - ⚡ Bedarf an GPU (VRAM), RAM und CPU prüfen.
   - 💡 Tipp: Bei weniger Leistung auf hocheffiziente kleine Modelle setzen (z.B. `Mistral-7B-v0.3` oder `Llama3.2-3B`).

<!-- class="lia-callout--note" -->
> **⚠️ Wichtige Praxis-Hinweise**
>
> 📡 : Modell-Downloads sind riesig (GB-Bereich). Bitte niemals über Eduroam herunterladen!

