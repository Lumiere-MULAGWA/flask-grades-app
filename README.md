# Application Flask de Gestion des Notes

`Flask Grades App` est une application Flask qui permet de gérer les étudiants, les cours et les notes. Elle consomme le service `flask-student-app` pour récupérer les informations des étudiants et fournit des fonctionnalités pour attribuer des notes aux étudiants pour des cours spécifiques.

---

## Structure du Projet

```
flask-grades-app
├── app.py                      # Code principal de l'application Flask
├── templates                   # Dossier contenant les fichiers HTML
│   ├── index.html              # Page d'accueil
│   ├── grades_list.html        # Page pour afficher les notes des étudiants
│   ├── courses_list.html       # Page pour afficher les cours et les étudiants inscrits
│   └── add_student_to_course.html # Page pour ajouter un étudiant à un cours
├── static                      # Dossier contenant les fichiers statiques (CSS, JS)
│   ├── css
│   │   └── styles.css          # Fichiers CSS pour le style de l'application
│   └── js
│       └── scripts.js          # Fichiers JavaScript pour les interactions (si nécessaire)
└── README.md                   # Documentation du projet
```

---

## Fonctionnalités

- **Intégration avec `flask-student-app` :**
  - Consomme le service des étudiants pour récupérer leurs données via une API REST.
  
- **Gestion des Cours :**
  - Affiche la liste des cours disponibles.
  - Permet d'ajouter des étudiants à des cours spécifiques.

- **Gestion des Notes :**
  - Permet d'attribuer des notes aux étudiants pour des cours spécifiques.
  - Affiche les notes des étudiants par cours.

- **API REST pour les Notes :**
  - Expose des endpoints pour récupérer les notes par cours ou toutes les notes.

---

## Instructions d'Installation

1. **Cloner le dépôt :**
   ```bash
   git clone <repository-url>
   cd flask-grades-app
   ```

2. **Créer un environnement virtuel :**
   Il est recommandé d'utiliser un environnement virtuel pour isoler les dépendances.
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows utilisez `venv\Scripts\activate`
   ```

3. **Installer les dépendances nécessaires :**
   Installez Flask et `requests` :
   ```bash
   pip install Flask requests
   ```

4. **Lancer l'application :**
   ```bash
   python app.py
   ```
   L'application sera disponible sur `http://127.0.0.1:5001/`.

5. **Assurez-vous que `flask-student-app` est en cours d'exécution :**
   L'application dépend du service `flask-student-app` pour récupérer les données des étudiants. Assurez-vous qu'il est en cours d'exécution sur `http://127.0.0.1:5000/`.

---

## Utilisation

### Interface Web

- **Page d'Accueil :**
  - Accédez à `http://127.0.0.1:5001/` pour voir la page d'accueil.

- **Voir les Notes :**
  - Accédez à `http://127.0.0.1:5001/grades` pour voir les notes de tous les étudiants.

- **Voir les Cours :**
  - Accédez à `http://127.0.0.1:5001/courses` pour voir les cours et les étudiants inscrits à chaque cours.

- **Ajouter un Étudiant à un Cours :**
  - Utilisez le lien "Add Student" sous chaque cours pour inscrire un étudiant à ce cours avec une note.

### API REST

- **Récupérer les Notes par Cours :**
  ```
  GET /api/courses/<course_name>/grades
  ```
  Exemple :
  ```bash
  curl http://127.0.0.1:5001/api/courses/Mathematics/grades
  ```

- **Récupérer Toutes les Notes :**
  ```
  GET /api/grades
  ```
  Exemple :
  ```bash
  curl http://127.0.0.1:5001/api/grades
  ```

---

## Données d'Exemple

- **Cours :**
  - Mathematics
  - Physics
  - Computer Science

- **Notes :**
  - Les notes sont attribuées dynamiquement aux étudiants via l'interface web.

---

## Fonctionnement Technique

1. **Intégration avec `flask-student-app` :**
   - Les données des étudiants sont récupérées via l'API REST exposée par `flask-student-app`.

2. **Gestion des Cours et des Notes :**
   - Les cours et les notes sont stockés dans une structure Python (`grades_by_course`) et gérés dynamiquement.

3. **API REST :**
   - Les notes sont exposées via des endpoints REST pour être consommées par d'autres services ou applications.

---

## Licence

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, de le modifier et de le distribuer.