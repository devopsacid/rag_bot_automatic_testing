# Inštrukcia k testovaniu

Tento dokument podrobne opisuje postup testovania projektu, ktorý zahŕňa manuálne aj automatizované testovanie. Nasledujúce kroky, vrátane názvov sekcií, obsahujú všetky potrebné informácie:

---

## 1) Manuálne testovanie

- **Postup:**  
  Najprv vykonávame manuálne testovanie. Zaznamenávame všetko, čo je zjavne nesprávne alebo sa nám nepáči v stĺpci **Todo**.

- **Kontrola duplicity:**  
  Pred vytvorením novej issue je nutné skontrolovať, či podobná issue už neexistuje.

- **Prioritizácia:**  
  Každej issue sa priraďuje priorita podľa závažnosti:
  - **P0:** Najdôležitejšia (kritická).
  - **P1:** Stredne dôležitá.
  - **P2:** Menej dôležitá.

---

## 2) Ak problém pretrváva

- **Postup:**  
  Ak sa chyba alebo problém opakuje z verzie na verziu, pridáme automatických testerov do **assignments** pre danú issue v stĺpci **Todo**.

---

## 3) Postup manuálnych testerov

- **Testované oblasti:**  
  Manuálni testeri testujú všetko, čo sa nachádza v stĺpcoch **Todo** a **Final Testing**.

- **Rozdelenie práce:**  
  - Ak sú manuálni testeri dvaja a problémov je veľa, môže jeden testovať položky v **Todo** a druhý položky v **Final Testing**.
  - Ak je issue len málo, obaja testeri testujú všetko.

- **Iniciatíva:**  
  Manuálni testeri sa vždy snažia hľadať nové problémy a pridávajú ich do stĺpca **Todo**.

---

## 4) Postup automatických testerov

- **Vývoj testov:**  
  Automatickí testeri píšu automatické testy.

- **Priradenie a rozdelenie:**  
  Pozrú sa, ku ktorým issue boli priradení, rozdelia si úlohy medzi sebou a presunú issue do stĺpca **In Progress**, pričom odstránia druhého testera zo **assignments**.

- **Postup po realizácii:**  
  Po implementácii automatických testov presunú issue do stĺpca **Final Testing** alebo do **Done** (v závislosti od toho, či je potrebné manuálne testovanie).

---

## 5) Finálne manuálne testovanie

- **Testovanie:**  
  Manuálni testeri otestujú všetko, čo sa nachádza v stĺpci **Final Testing**.

- **Presun issue:**  
  - Ak všetko funguje korektne, issue presunú do stĺpca **Done**.
  - Ak je niečo v poriadku, issue presunú do stĺpca **Final Testing Failed**.

---

## 6) Opätovné testovanie automatickými testerami

- **Postup:**  
  Automatickí testeri skontrolujú issue v stĺpci **Final Testing Failed** a presunú ich opäť do **Final Testing** pre ďalšie testovanie.

---

## 7) Dodatočné pridávanie automatických testov

- **Možnosť pridania:**  
  Automatickí testeri môžu vytvárať a pridávať vlastné testy, ak ich považujú za potrebné, aj keď nie sú pôvodne prítomné v stĺpci **Todo**.

- **Postup pridania:**  
  Takéto testy je potrebné pridať do stĺpca **Todo** alebo **In Progress**, po ktorom prejdú štandardnými krokmi testovania.

---

## -------------- PRE AUTOMATICKÝCH TESTEROV ------------------

Na svoju prácu budete potrebovať základné znalosti GIT-u. Stiahnite si ho do svojho počítača, ak ho ešte nemáte: [https://git-scm.com/downloads](https://git-scm.com/downloads)

Musíte sa naučiť (a pochopiť, prečo je to dôležité):

1. Ako vytvárať vetvy lokálne;
2. Ako do nich pridávať svoje zmeny;
3. Ako tieto vetvy pridať na Github a synchronizovať ich s lokálnymi;
4. Ako vytvárať PR (Pull Requests).

Stiahnite si [projekt](https://github.com/OlegQm/rag_bot_automatic_testing) a [Python 3.10](https://www.python.org/downloads/release/python-31016/)** lokálne, vytvorte si novú vetvu (z vetvy master) a pridajte do nej akékoľvek zmeny. Potom sa uistite, že vaše vetvy s lokálnymi zmenami sú prítomné aj na GitHube v našom repozitári. Následne vytvorte PR z vašej vetvy do **master**.

Vo **master** sa bude zhromažďovať naša spoločná práca. **PR** sú potrebné na to, aby sa "váš príspevok dostal do spoločnej základne" a aby si ostatní účastníci mohli pozrieť, čo ste zmenili.

- **Nastavenie OpenAI API:**
  - Zaregistrujte sa na [https://openai.com/](https://openai.com/).
  - Vytvorte OpenAI API kľúč na [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys).
  - Nabite účet OpenAI na **5 dolárov** (podrobnosti: [OpenAI Billing Overview](https://platform.openai.com/settings/organization/billing/overview)), aby kľúč fungoval správne.

- **Šetrenie OpenAI tokenov:**  
  Pri automatickom testovaní je potrebné šetriť OpenAI tokeny (tých 5 dolárov). Preto najprv spustite testy, ktoré tokeny nevyžadujú, a ak prebehnú úspešne, spustite testy, ktoré ich vyžadujú (využite závislosti v pytest).

---

## -------------- PRE MANULANÝCH TESTEROV ------------------

- **Prístup pre manuálne testovanie:**
  Pre vykonanie manuálneho testovania je potrebný účet pre prístup na stránku [https://prod.agentkovac.sk/](https://prod.agentkovac.sk/).

- **Discord:**
  Môžete testovať aj na Discorde v našom kanáli botov @AgentKovac (stabilná verzia bota) a @DEVAgentKovac (verzia bota s novými funkciami).

---

## --------------DODATOČNÉ INFORMÁCIE----------------

- **Používame [Python 3.10](https://www.python.org/downloads/release/python-31016/)**

- **Backlog (zoznam všetkých issue):**
  [https://github.com/users/OlegQm/projects/3/views/1](https://github.com/users/OlegQm/projects/3/views/1)
