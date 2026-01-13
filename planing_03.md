## Subgoal Overview and Teaching Plan

| Subgoal | Learning Goal | Start (min) | End (min) | Material Needed (Teacher) |
|--------|---------------|-------------|-----------|----------------------------|
| 1. Further Hands-on Exercise | Students can extend their workflow with additional nodes and error handling | 0 | 20 | slides, n8n instance | 
| 1.1 Discussion with students | Students can reflect on their learning experience and discuss challenges faced | 20 | 30 | Discussion prompts |
| 2. Errors | Students can identify and resolve common errors in n8n workflows | 30 | 35 | Example error scenarios |
| 2.1 Parameters for Webhooks | Students understand how to configure parameters for webhooks in n8n | 35 | 40 | slides |
| 2.2 Validation of Inputs | Students can implement input validation in their workflows | 40 | 45 | Example validation scenarios |
| 2.3 Webhook Returns | Students can configure webhook returns in n8n | 45 | 55 | slides, n8n instance |
| 3. API + Credentials | Students can integrate external APIs using credentials in n8n | 55 | 65 | API documentation, n8n instance, credentials, slides |
| 3.1 Hands-on Exercise | Students can create a workflow that interacts with an external API using credentials | 65 | 90 | n8n instance, API access | 

## Hands on Beispiel

- nutze Data tables um Daten persistent zwischen Workflows zu halten
- task
    - data table
        - erstelle eine Data table mit passenden Spalten
        - firstname, surname, birthday, profession, matrnr, email
    - work flow 1
        - Formular um Daten abzufragen (z.B. Name, Alter, Beruf, Matrnr, email etc.)
        - Achten Sie auf Datentypen, Beruf soll Drop Down Feld sein
    - work flow 2
        - Trägt Daten in Data table ein (eventuell update)
        - webhook
        - sollte daten checken (nutze `data` in json)
    - work flow 3
        - soll einmal am tag eine Liste aller emails mit (namen) auslesen
        - und in eine datei abspeichern (z.B. CSV) (nutze Read/Write Files from Disk und Convert to File)
        - falls das fehlschlägt hochladen auf Cloud Storage (https://dlptest.com/ftp-test/)
            - FTP URL: ftp.dlptest.com
            - FTP User: dlpuser
            - Password: rNrKYTX9g7z3RgJRmxWuGHbeu
            - eventuell Timeout hochsetzen
        - Schedule node trigger (Kann manuell getriggert werden um zu testen)
    
    - publish workflows
        - setzt einen error workflow (trigger error node)
        - benachrichtigt via email (nutze Email node) oder nutzt Read/Write Files from Disk um eine log datei zu schreiben
        - auf FTP speichern

- Subworkflows
    - nutze subworkflows um wiederverwendbare teile zu erstellen
    - z.B. daten validierung, email versand etc.
    - Contracts nutzen um inputs/outputs zu definieren

    
# plan

- 20 min Aufgabe vom letzten mal
- 10 min Besprechen
- 10 min data tables erklären + nodes
- 5 min publish und error workflows
- data table aufgabe siehe oben für ca. 30 min
- 15 min subworkflows + contracts erklären
