# Projet d'Automatisation des Tests & Assurance Qualité (QA)

Ce dépôt contient la suite complète de tests automatisés (UI, API REST, Performance et Sécurité) développée dans le cadre du module **Automatisation des Tests et Qualité Logicielle**.

**Auteur :** Yassine Chabab  
**Application évaluée :** Formy Web UI & Reqres REST API  
**Dépôt GitHub :** [https://github.com/yassine-chabab/projet-qualite-et-automatisation](https://github.com/yassine-chabab/projet-qualite-et-automatisation)

---

## 🛠️ Arborescence du Projet

```text
projet-qualite-et-automatisation/
├── .github/
│   └── workflows/
│       └── test-automation.yml    # Pipeline CI/CD GitHub Actions
├── ui-tests/                       # Tests Automatisés UI (Selenium + Pytest)
│   ├── pages/                     # Design Pattern Page Object Model (POM)
│   ├── tests/                     # Scripts d'exécution Pytest
│   └── requirements.txt           # Dépendances Python
├── api-tests/                      # Tests Automatisés API (Postman + Newman)
│   ├── Reqres_API_Tests.postman_collection.json
│   └── api-report.html            # Rapport d'exécution Newman HTML
├── performance-tests/              # Tests de Charge (Apache JMeter)
│   └── JMeter_Performance_Test.jmx
├── security-tests/                 # Audit de Sécurité (OWASP Top 10)
│   └── security-audit-notes.md
└── README.md                       # Documentation du projet