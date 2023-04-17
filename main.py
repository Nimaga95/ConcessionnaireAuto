import pymysql
import flask
from flask import Flask, request, render_template, flash, redirect, session, url_for
#import pycountry

# pip install  pymy
# pip install  pycountry
# pip install  flask
# pip installe

app = flask.Flask(__name__)

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="lennyplante5@Sql.com",  # à remplacer par le password de votre ordinateur pour les tests
    db="glo_2005_Projet_ConcessionnaireNouvelleAuto",
    autocommit=True,
)

cursor = mydb.cursor()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    # Vérifier si l'utilisateur est connecté
    user_id = session.get('user_id')
    print(user_id)
    if 'user_id' not in session:
        flash('Vous devez être connecté pour accéder à cette page.', category='error')
        return redirect(url_for('login'))  # Rediriger l'utilisateur vers la page de connexion

    if flask.request.method == 'POST':
        # Récupérer la requête de l'utilisateur
        query = flask.request.form['query']
        print(query)

        # Requête SQL pour sélectionner les données dans la table "articles"
        cursor = mydb.cursor()
        sql = "SELECT idPiece, nomPiece, categorie, poidsPiece, prixPiece, datePiece " \
              "FROM glo_2005_projet_concessionnairenouvelleauto.pieces " \
              "WHERE idPiece LIKE %s " \
              "OR nomPiece LIKE %s " \
              "OR categorie LIKE %s " \
              "OR poidsPiece LIKE %s " \
              "OR prixPiece LIKE %s " \
              "OR datePiece LIKE %s"
        cursor.execute(sql, ('%' + query + '%', '%' + query + '%', '%' + query + '%',
                             '%' + query + '%', '%' + query + '%', '%' + query + '%'))
        results = cursor.fetchall()

        return flask.render_template('searchPiece.html', results=results, query=query)

    return render_template('barre_recherche_Pieces.html')


@app.route('/search-auto', methods=['GET', 'POST'])
def searchAuto():
    # Vérifier si l'utilisateur est connecté
    user_id = session.get('user_id')
    if 'user_id' not in session:
        flash('Vous devez être connecté pour accéder à cette page.', category='error')
        return redirect(url_for('login'))  # Rediriger l'utilisateur vers la page de connexion

    if flask.request.method == 'POST':
        # Récupérer la requête de l'utilisateur
        queryAuto = flask.request.form['queryAuto']
        print(queryAuto)

        # Requête SQL pour sélectionner les données dans la table "articles"
        cursor = mydb.cursor()
        sql = "SELECT * FROM glo_2005_projet_concessionnairenouvelleauto.Automobile " \
              "WHERE niv LIKE %s " \
              "OR marque LIKE %s " \
              "OR modele LIKE %s " \
              "OR annee LIKE %s " \
              "OR couleur LIKE %s " \
              "OR odometre LIKE %s " \
              "OR nbPlaces LIKE %s " \
              "OR prixAuto LIKE %s " \
              "OR locationVente LIKE %s " \
              "OR sousCategorie LIKE %s " \
              "OR poidsAuto LIKE %s " \
              "OR dateAuto LIKE %s " \
              "ORDER BY prixAuto"
        cursor.execute(sql, ('%' + queryAuto + '%', '%' + queryAuto + '%', '%' + queryAuto + '%',
                             '%' + queryAuto + '%', '%' + queryAuto + '%', '%' + queryAuto + '%',
                             '%' + queryAuto + '%', '%' + queryAuto + '%', '%' + queryAuto + '%',
                             '%' + queryAuto + '%', '%' + queryAuto + '%', '%' + queryAuto + '%'))
        resultsAuto = cursor.fetchall()

        return flask.render_template('searchAuto.html', results=resultsAuto, query=queryAuto)

    return render_template('barre_recherche_Auto.html')


@app.route('/search-employe', methods=['GET', 'POST'])
def searchEmploye():
    # Vérifier si l'utilisateur est connecté
    user_id = session.get('user_id')
    if 'user_id' not in session:
        flash('Vous devez être connecté pour accéder à cette page.', category='error')
        return redirect(url_for('login'))  # Rediriger l'utilisateur vers la page de connexion

    if flask.request.method == 'POST':
        # Récupérer la requête de l'utilisateur
        queryEmploye = flask.request.form['queryEmploye']
        # print(queryAuto)

        # Requête SQL pour sélectionner les données dans la table "articles"
        cursor = mydb.cursor()
        sql = "SELECT * FROM glo_2005_projet_concessionnairenouvelleauto.employe " \
              "WHERE prenomEmploye LIKE %s " \
              "OR nomEmploye LIKE %s " \
              "OR ageEmploye LIKE %s " \
              "OR numCellEmploye LIKE %s " \
              "OR numPoste LIKE %s " \
              "OR titreEmploi LIKE %s " \
              "OR salaireAnnuel LIKE %s " \
              "OR anciennete LIKE %s " \
              "ORDER BY anciennete"
        cursor.execute(sql, ('%' + queryEmploye + '%', '%' + queryEmploye + '%', '%' + queryEmploye + '%',
                             '%' + queryEmploye + '%', '%' + queryEmploye + '%', '%' + queryEmploye + '%',
                             '%' + queryEmploye + '%', '%' + queryEmploye + '%'))
        resultsEmploye = cursor.fetchall()

        return flask.render_template('searchemploye.html', results=resultsEmploye, query=queryEmploye)

    return render_template('barre_recherche_Employes.html')


@app.route('/profil-employe/<int:id>')
def profilEmploye(id):
    employe = getEmployeById(id)
    # print(employe)
    if employe:
        return render_template('profil_Employes.html', employe=employe)
    else:
        return 'Employé non trouvé'


def getEmployeById(id):
    # Requête SQL pour sélectionner les données dans la table "employes"
    cursor = mydb.cursor()
    sql = "SELECT * FROM glo_2005_projet_concessionnairenouvelleauto.employe WHERE idEmploye =%s"
    cursor.execute(sql, (id,))
    resultsEmploye = cursor.fetchone()

    # print(resultsEmploye)

    return resultsEmploye


@app.route('/add-fournisseur-auto', methods=['GET', 'POST'])
def addFournisseurAuto():
    # Vérifier si l'utilisateur est connecté
    user_id = session.get('user_id')
    print(user_id)
    if 'user_id' not in session:
        flash('Vous devez être connecté pour accéder à cette page.', category='error')
        return redirect(url_for('login'))  # Rediriger l'utilisateur vers la page de connexion

    if flask.request.method == 'POST':
        name = request.form['name']
        adress = request.form['adress']
        tel = request.form['tel']
        email = request.form['email']
        city = request.form['city']
        state = request.form['state']
        country = request.form['country']

        # print(name, firstName, password1, password2)

        if len(name) < 2:
            flash('Nom invalide', category='error')
        if len(tel) < 10:
            flash('Téléphone invalide', category='error')
        if len(email) < 4:
            flash('E-Mail invalide.', category='error')
        if len(city) < 2:
            flash('Ville invalide', category='error')
        if len(state) < 2:
            flash('État / Province invalide', category='error')
        if len(country) < 2:
            flash('Pays invalide', category='error')
        if len(name) > 2:
            flash('Fournisseur ajouté', category='success')

        # Récupérer la requête de l'utilisateur
        queryAddFournAuto = flask.request.form['queryEmploye']

        # cursor = mydb.cursor()
        # sql = f"""INSERT INTO todo (text) VALUE ("{text}")"""

        # cursor = mydb.cursor()
        # commande = "INSERT INTO users VALUES (NULL, '{}', '{}', '{}');".format\
        #     (name, firstName, password1)
        #
        # cursor.execute(commande)

    return render_template('ajouterFournisseursAuto.html')


@app.route('/search-fournisseur-auto', methods=['GET', 'POST'])
def searchFournisseurAuto():
    # Vérifier si l'utilisateur est connecté
    user_id = session.get('user_id')
    print(user_id)
    if 'user_id' not in session:
        flash('Vous devez être connecté pour accéder à cette page.', category='error')
        return redirect(url_for('login'))  # Rediriger l'utilisateur vers la page de connexion
    if flask.request.method == 'POST':
        # Récupérer la requête de l'utilisateur
        queryAuto = flask.request.form['queryAuto']
        print(queryAuto)

        # Requête SQL pour sélectionner les données dans la table "articles"
        cursor = mydb.cursor()
        sql = "SELECT * FROM glo_2005_Projet_ConcessionnaireNouvelleAuto.FournisseursAutomobiles " \
              "WHERE idFournisseursVehicules LIKE %s " \
              "OR nomFournisseursVehicules LIKE %s " \
              "OR adresseFournisseursVehicules LIKE %s " \
              "OR numTelephoneFournisseursVehicules LIKE %s " \
              "OR adresseCourrielFournisseursVehicules LIKE %s " \
              "OR villeFournisseursVehicules LIKE %s " \
              "OR provinceEtatFournisseursVehicules LIKE %s " \
              "OR paysFournisseursVehicules LIKE %s " \
              "ORDER BY idFournisseursVehicules"
        cursor.execute(sql, ('%' + queryAuto + '%', '%' + queryAuto + '%', '%' + queryAuto + '%',
                             '%' + queryAuto + '%', '%' + queryAuto + '%', '%' + queryAuto + '%',
                             '%' + queryAuto + '%', '%' + queryAuto + '%'))
        resultsAuto = cursor.fetchall()

        return flask.render_template('searchFournisseurAuto.html', results=resultsAuto, query=queryAuto)

    return render_template('trouverFournisseursAuto.html')


@app.route('/add-fournisseur-pieces', methods=['GET', 'POST'])
def addFournisseurPieces():
    # Vérifier si l'utilisateur est connecté
    user_id = session.get('user_id')
    print(user_id)
    if 'user_id' not in session:
        flash('Vous devez être connecté pour accéder à cette page.', category='error')
        return redirect(url_for('login'))  # Rediriger l'utilisateur vers la page de connexion

    # if flask.request.method == 'POST':
    #     # Récupérer la requête de l'utilisateur
    #     queryAddFournPieces = flask.request.form['queryAddFournPieces']
    #     print(queryAddFournPieces)
    #
    #     # Requête SQL pour sélectionner les données dans la table "articles"
    #     cursor = mydb.cursor()
    #     # sql = "INSERT INTO glo_2005_Projet_ConcessionnaireNouvelleAuto.FournisseursAutomobiles (" \
    #     #       "idFournisseursVehicules, nomFournisseursVehicules, adresseFournisseursVehicules, " \
    #     #       "numTelephoneFournisseursVehicules, adresseCourrielFournisseursVehicules, villeFournisseursVehicules, " \
    #     #       "provinceEtatFournisseursVehicules, paysFournisseursVehicules) " \
    #     #       "VALUE ("{}")"
    #     cursor.execute(sql, (
    #         '%' + queryAddFournPieces + '%', '%' + queryAddFournPieces + '%', '%' + queryAddFournPieces + '%',
    #         '%' + queryAddFournPieces + '%', '%' + queryAddFournPieces + '%', '%' + queryAddFournPieces + '%',
    #         '%' + queryAddFournPieces + '%', '%' + queryAddFournPieces + '%', '%' + queryAddFournPieces + '%',
    #         '%' + queryAddFournPieces + '%', '%' + queryAddFournPieces + '%', '%' + queryAddFournPieces + '%'))
    #     resultsAddFournPieces = cursor.fetchall()
    #
    #     return flask.render_template('fournisseurs.html', results=resultsAddFournPieces, query=queryAddFournPieces)

    return render_template('ajouterFournisseursPieces.html')


@app.route('/search-fournisseur-pieces', methods=['GET', 'POST'])
def searchFournisseurPieces():
    # Vérifier si l'utilisateur est connecté
    user_id = session.get('user_id')
    #print(user_id)
    if 'user_id' not in session:
        flash('Vous devez être connecté pour accéder à cette page.', category='error')
        return redirect(url_for('login'))  # Rediriger l'utilisateur vers la page de connexion

    if flask.request.method == 'POST':
        # Récupérer la requête de l'utilisateur
        querySearchFournPieces = flask.request.form['querySearchFournPieces']
        print(querySearchFournPieces)

        # Requête SQL pour sélectionner les données dans la table "articles"
        cursor = mydb.cursor()
        sql = "SELECT * FROM glo_2005_Projet_ConcessionnaireNouvelleAuto.Fournisseurspieces " \
              "WHERE idFournisseursPieces LIKE %s " \
              "OR nomFournisseursPieces LIKE %s " \
              "OR adresseFournisseursPieces LIKE %s " \
              "OR numTelephoneFournisseursPieces LIKE %s " \
              "OR adresseCourrielFournisseursPieces LIKE %s " \
              "OR villeFournisseursPieces LIKE %s " \
              "OR provinceEtatFournisseursPieces LIKE %s " \
              "OR paysFournisseursPieces LIKE %s " \
              "ORDER BY idFournisseursPieces"
        cursor.execute(sql, (
            '%' + querySearchFournPieces + '%', '%' + querySearchFournPieces + '%', '%' + querySearchFournPieces + '%',
            '%' + querySearchFournPieces + '%', '%' + querySearchFournPieces + '%', '%' + querySearchFournPieces + '%',
            '%' + querySearchFournPieces + '%', '%' + querySearchFournPieces + '%'))
        resultsSearchFournPieces = cursor.fetchall()

        return flask.render_template('searchFournisseurPieces.html', results=resultsSearchFournPieces,
                                     query=querySearchFournPieces)

    return render_template('trouverFournisseursPieces.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    user_id = session.get('user_id')
    #print(user_id)
    if 'user_id' in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # print(password)

        cursor = mydb.cursor()
        sql = "SELECT passe,email from users WHERE email = %s"
        cursor.execute(sql, (email,))
        resultat = cursor.fetchone()

        if resultat is None:
            flash("Identifiants incorrects. Veuillez réessayer.", category='error')
            return redirect(url_for('login'))

        else:
            row = resultat[0].strip()
            if row == password:

                session['user_id'] = email  # ajout du code de la session

                # flash('Connexion reussie', category='success')
                return redirect(url_for('utilisateur'))
            else:
                flash("Identifiants incorrects. Veuillez réessayer.", category='error')

    return render_template('login.html')


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    session.pop('user_id', None)

    return render_template('home.html')


@app.route('/page_utilisateur', methods=['POST', 'GET'])
def utilisateur():
    return render_template('page_utilisateur.html')


@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    user_id = session.get('user_id')
    #print(user_id)
    if 'user_id' in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        email = request.form['email']
        firstName = request.form['firstName']
        Name = request.form['lastName']
        sex = request.form['gender']
        Date = request.form['birthdate']
        country = request.form['country']
        phone = request.form['phone']
        password1 = request.form['password1']
        password2 = request.form['password2']

        # print(email, firstName, Name, sex, country,password2,password2)
        # print(email, firstName, password1, password2)

        if len(email) < 4:
            flash('Email invalide', category='error')
        if len(firstName) < 2:
            flash('Le nom doit être plus grand qu\'un caractère', category='error')
        elif password1 != password2:
            flash('Les mot de passe ne correspondent pas', category='error')
        elif len(password1) < 8:
            flash('Le mot de passe doit faire au moins 8 caracteres.', category='error')
        elif not country:
            flash('Veuillez sélectionner votre pays.', category='error')
        elif not sex:
            flash('Veuillez sélectionner votre pays.', category='error')
        else:
            cursor = mydb.cursor()

            sql = "SELECT * FROM users WHERE email = %s"
            cursor.execute(sql, (email,))
            result = cursor.fetchone()
            if result:
                # L'adresse e-mail existe déjà, renvoyer un message d'erreur
                # Triger ici?
                flash('Ce compte existe déjà. Veuillez vous connecter ou choisir un autre email.')
                return redirect(url_for('login'))
            else:
                sql = "INSERT INTO users (email, passe, first_name, last_name,  gender, birthdate, region, phone ) VALUES(%s, %s, %s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, (email, password1, firstName, Name, sex, Date, country, phone))
                mydb.commit()
                flash('Compte crée avec succées', category='success')
                return redirect(url_for('login'))

    return render_template("sign-up.html")


@app.route('/appropos', methods=['GET', 'POST'])
def appropos():
    return render_template("a_propos.html")


# for country in pycountry.countries:
#  print(country.name)

@app.route('/test', methods=['GET', 'POST'])
def test():
    # Vérifier si l'utilisateur est connecté
    user_id = session.get('user_id')
    print(user_id)
    if 'user_id' not in session:
        flash('Vous devez être connecté pour accéder à cette page.', category='error')
        return redirect(url_for('login'))  # Rediriger l'utilisateur vers la page de connexion

    if flask.request.method == 'POST':
        query = flask.request.form['query']
        print(query)
        # Récupérer la requête de l'utilisateur
        id = 0
        nom = 0
        prix = 0
        category = 0
        poid = 0
        compteur = 0
        piece = request.form.getlist('piece')
        if "ID" in piece:
            id = 1
            print("id = 1")
        if "NOM" in piece:
            nom = 1
            print("nom = 1")
        if "PRIX" in piece:
            prix = 1
            print("prix = 1")
        if "CATEGORY" in piece:
            category = 1
            print("category = 1")
        if "POID" in piece:
            poid = 1
            print("poid = 1")

        time = request.form.getlist('time')
        if "last_week" in time:
            cursor = mydb.cursor()
            sql = "call statisticsPieces('semaine', 1, 1, 0, 1, 1, 1, 1);"
        if "last_month" in time:
            cursor = mydb.cursor()
            sql = "call statisticsPieces('mois', 1, 1, 0, 1, 1, 1, 1);"
        if "last_year" in time:
            cursor = mydb.cursor()
            sql = "call statisticsPieces('year', 1, 1, 0, 1, 1, 1, 1);"
        if "all_date" in time:
            cursor = mydb.cursor()
            sql = "call statisticsPieces('all', 1, 1, 0, 1, 1, 1, 1);"

        #sql = "call statisticsPieces('mois', %s, %s, 0, %s, %s, %s, 1);"

        #cursor.execute(sql, (id, nom, prix, category, poid,))
        cursor.execute(sql)
        results = cursor.fetchall()

        return flask.render_template('test.html', results=results, query=query)

    return render_template('barre_test.html')

if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'hjshjhdjahhhhhhhhhhhhhhhkjshkjdhjs'  # ne pas enléver important

    app.run(debug=True)
