# 💡 Hue Lampen Interface

Ein minimalistisches Webinterface zur Anzeige und Verwaltung von Philips Hue Lampen über die lokale Hue-API.  
Ideal für Smart-Home-Fans, die ein übersichtliches Dashboard zur Steuerung ihrer Leuchtmittel suchen.

---

## 🚀 Features

- 🔍 Anzeige aller Hue-Lampen mit Gerätenamen, Produkttyp und ID
- 🎨 Übersichtliche Darstellung im Grid-Layout mit TailwindCSS
- ⚙️ REST-Schnittstelle über FastAPI zum Abrufen von Lampenstatus und zur Steuerung
- 💾 Konfigurierbare Bridge-IP und API-Key über `.env`-Datei
- 🔒 Keine Daten werden extern gespeichert – lokale Steuerung

---

## 📦 Technologien

| Bereich        | Technologie        |
|----------------|-------------------|
| Frontend       | HTML, TailwindCSS, JavaScript |
| Backend        | Python, FastAPI    |
| API            | Philips Hue (v2, lokal) |
| Sicherheit     | `.env` für vertrauliche Daten |
| Sonstiges      | CORS aktiviert, REST-API-Struktur |

---

## ⚙️ Installation

1. **Projekt klonen**
   ```bash
   git clone https://github.com/Racermarco20/PhillipsHueControll.git
   cd PhillipsHueControll
   ```

2. **Python-Abhängigkeiten installieren**
   ```bash
   pip install -r requirements.txt
   ```

3. **`.env` Datei erstellen**

> ℹ️ Den Hue Application Key musst du dir manuell über die Philips Hue Developer API generieren. 
> Eine Anleitung findest du auf der offiziellen Seite: [developers.meethue.com – Getting Started](https://developers.meethue.com/develop/hue-api-v2/getting-started/)


   Erstelle im Projektverzeichnis eine `.env` mit folgendem Inhalt:

   ```env
   BRIDGE_IP=192.168.1.100
   HUE_APP_KEY=dein-hue-api-schlüssel
   ```

4. **Backend starten**
   ```bash
   uvicorn main:app --reload
   ```

5. **Frontend öffnen**

   Öffne die HTML-Datei (`index.html`) direkt im Browser.  
   Das Webinterface lädt automatisch die verfügbaren Lampen über den lokalen FastAPI-Server.

---

## 📂 Projektstruktur

```
├── .env                # Deine Hue-Bridge-Konfiguration
├── main.py             # Backend mit FastAPI
├── index.html          # Webinterface zur Anzeige der Lampen
├── requirements.txt    # Python-Abhängigkeiten
```

---

## 🔐 Hinweise

- Stelle sicher, dass deine Hue Bridge im selben Netzwerk wie dein PC läuft.
- Die Verbindung zur Hue-Bridge erfolgt über HTTPS mit einem lokalen Application Key.
- Die IP-Adresse kann sich ändern – nutze DHCP-Reservierung oder prüfe regelmäßig.

---

## 📃 Lizenz

MIT – frei verwendbar, gerne mit Attribution 😊

---

## 🙋‍♂️ Autor

**Marco Braun** – HTL Hollabrunn, Abteilung IT  
📧 [Marco.Braun@it.htl-hl.ac.at](mailto:Marco.Braun@it.htl-hl.ac.at)
