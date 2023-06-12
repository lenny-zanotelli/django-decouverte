# Journal personnel

Journal de bord test technique continué à la maison pour mon continuer ma découverte de Django.

- Samedi 10/06
  - Configuration de l'environnement de travail avec la création de mon environnement virtuel sur ma VM avec python3.8
  - installation de python3-venv non présent sur ma VM : `sudo apt-get install python3-venv`
  - Création l'environnement virtuel : `python3.8 -m venv env`
  - Installation de django4.2.2
  - Je recommence le tutorial de la doc de Django
  
  > Concernant la partie `startproject` et `startapp` qui me semblait très flou sur le moment.
  > En relisant la >documentation officiel, les dev précisent que "project" est une collection de paramètres et d'applications pour >un siteweb particulier.
  >Un projet peut contenir plusieurs applications. Cependant, une application peut être dans de multiple projets. > Alors qu'une appl est application web qui "fait quelquechose", par exemple, un blog, une todo list etc.

  - Je reçois une erreur après avoir fait une migration pour la création de mon models Article, mon ficher `models.py` de `MyApp`, une erreur de syntaxe s'était glissé sur mon `models.Model`. Suite à la correction, mon model Article a bien été créé.
  - Les 3 étapes pour confirmer le changement d'un Model est la suivante :
    - Effectuer un changement dans `models.py`
    - Lancer la commande `python manage.py makmigrations` afin de créer les migrations pour les changements
    - Lancer la commande `python manage.py migrate` afin d'appliquer les changements à la BDD

  - Création du dossier template pour les fichiers html, j'ai créé deux vues : une page d'accueil et une page article.
    - J'ai eu un soucis avec la page d'accueil pour son affichage avec l'error `TypeError: context must be a dict rather than WSGIRequest`. L'erreur a été corrigé en passant un dictionnaire vide en context dans mon fichier `views.py` dans le return de fin.
  - Après la mise en place, la création et la modification de mes fichiers pour django. Je me suis attaqué à Bootstrap4 sans utiliser le CDN. J'ai installé le code compilé JS et CSS directement dans un fichier static présent dans MyApp.
  - Afin de prendre en compte bootstrap, j'ai connecté mes vues aux versions minifiés CSS et JS de Bootstrap.
  - Concernant Django et afin que les fichiers static soit pris en compte j'ai modifié mon fichier `settings.py` en ajoutant les lignes suivantes :

  ``` python
  STATIC_URL = 'static/'
  STATIC_ROOT = os.path.join(BASE_DIR, 'static')
  ```

  Ces deux lignes définissent l'URL debase et le chemin pour mes fichiers statiques, ce qui me permettre de les servir correctement lors d'un déploiement en prod.
  - J'ai beaucoup parcouru la doc Bootstrap pour partie Responsive Design et manipuler les composants de Bootstrap.

- Lundi 12/06
  - Aujourd'hui, je vais configurer Webpack dans ce projet et ensuite, je continuerai la page form et je commencerai la feature du carousel.
  -PLAN : 
    - install node + npm + webpack
    - webpack basic config
