# Rapport d'Audit de Sécurité Synthétique (OWASP Top 10)

## 1. Contexte & Périmètre de l'Évaluation
* **Cibles analysées** : 
  * Application Web UI : `https://formy-project.herokuapp.com`
  * API REST Backend : `https://reqres.in/api`
* **Méthodologie** : Analyse des vulnérabilités basée sur le référentiel **OWASP Top 10 (2021)** et audits d'en-têtes HTTP / mécanismes d'authentification.

---

## 2. Matrice d'Analyse des Vulnérabilités (OWASP Top 10)

| Catégorie OWASP | Niveau de Risque | Description & Impact potentiel | Statut & Recommandation |
| :--- | :---: | :--- | :--- |
| **A01:2021 - Broken Access Control** | **Moyen** | Absence de contrôle de jeton OAuth2/JWT strict sur certains endpoints publics. | Implémenter un contrôle RBAC (Role-Based Access Control) sur l'API. |
| **A02:2021 - Cryptographic Failures** | **Faible** | Le protocole HTTPS/TLS 1.2+ est activé. Toutefois, manque de directive HSTS explicite. | Ajouter l'en-tête `Strict-Transport-Security` avec `max-age=31536000`. |
| **A03:2021 - Injection (XSS / SQLi)** | **Moyen** | Champs de saisie du formulaire UI sans assainissement strict côté client (*Sanitization*). | Appliquer une validation stricte des entrées et un échappement HTML des caractères spéciaux. |
| **A04:2021 - Insecure Design** | **Faible** | Absence de mécanisme de Captcha sur les formulaires de soumission rapide. | Intégrer un système reCAPTCHA v3 pour éviter le spam automatisé. |
| **A05:2021 - Security Misconfiguration** | **Élevé** | En-têtes de sécurité HTTP clés manquants (`X-Frame-Options`, `Content-Security-Policy`). | Injecter les en-têtes HTTP de sécurité recommandés au niveau du serveur Web / Reverse Proxy. |

---

## 3. Analyse détaillée des En-têtes HTTP de Sécurité

Les audits d'en-têtes de sécurité sur `formy-project.herokuapp.com` révèlent l'absence des directives suivantes :

1. **Content-Security-Policy (CSP)** :
   * *Risque* : Exposition accrue aux attaques XSS et à l'injection de scripts malveillants.
   * *Correction* : Configurer une politique CSP restrictive autorisant uniquement les sources de confiance.
2. **X-Frame-Options** :
   * *Risque* : Vulnérabilité potentielle au *Clickjacking* via l'intégration de la page dans une `<iframe>`.
   * *Correction* : Ajouter la directive `X-Frame-Options: DENY` ou `SAMEORIGIN`.
3. **X-Content-Type-Options** :
   * *Risque* : Attaques par *MIME-sniffing*.
   * *Correction* : Ajouter la directive `X-Content-Type-Options: nosniff`.

---

## 4. Conclusion & Plan d'Action
L'évaluation démontre une base fonctionnelle stable mais souligne la nécessité d'endurcir la couche de sécurité HTTP (*Security Hardening*) et de renforcer la protection contre l'injection de données avant tout déploiement en production.