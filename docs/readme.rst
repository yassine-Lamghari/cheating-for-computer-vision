cheating-for-computer-vision
=============================

🕵️‍♂️ Système de Détection de Triche par Vision par Ordinateur
-------------------------------------------------------------

**Détecte les comportements suspects dans les examens avec l'IA (YOLOv5/v8)**

.. image:: assets/demo.gif
   :alt: Démo

Fonctionnalités
---------------

- Détection de triche en temps réel :
  - Téléphone
  - Notes
  - Comportements suspects
- Alerte sonore 🔊
- Export JSON/CSV des détections
- Interface web avec Flask

Technologies utilisées
----------------------

- Roboflow (entrainement des modèles)
- YOLOv5 / YOLOv8
- OpenCV
- Flask (Python)

Installation
------------

Clonez le dépôt :

.. code-block:: bash

   git clone https://github.com/yassine-Lamghari/cheating-for-computer-vision.git
   cd cheating-for-computer-vision

Installez les dépendances :

.. code-block:: bash

   pip install -r requirements.txt

Lancez l'application :

.. code-block:: bash

   python app.py

Utilisation
-----------

- Accédez à l'interface web via http://localhost:5000
- Lancez la détection en temps réel depuis l'interface
- Consultez les alertes et exportez les résultats

Contribuer
----------

Les contributions sont les bienvenues !  
Veuillez ouvrir une issue ou soumettre une pull request.

Licence
-------

Ce projet est sous licence MIT.

---

*Développé par Yassine Lamghari*
