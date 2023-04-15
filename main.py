import hashlib

import flask
from flask import Flask, request, render_template, flash, redirect, session, url_for
from passlib.hash import bcrypt_sha256

import pymysql


# install pip pymy

app = flask.Flask(__name__)


mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="Ni4157120162022",  # à remplacer par le password de votre ordinateur pour les tests
    db="glo_2005_Projet_ConcessionnaireNouvelleAuto",
    autocommit=True,
)

cursor = mydb.cursor()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
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
    if flask.request.method == 'POST':
        # Récupérer la requête de l'utilisateur
        queryAuto = flask.request.form['queryAuto']
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
        cursor.execute(sql, ('%' + queryAuto + '%', '%' + queryAuto + '%', '%' + queryAuto + '%',
                             '%' + queryAuto + '%', '%' + queryAuto + '%', '%' + queryAuto + '%',
                             '%' + queryAuto + '%', '%' + queryAuto + '%'))
        resultsEmploye = cursor.fetchall()

        return flask.render_template('searchemploye.html', results=resultsEmploye, query=queryAuto)

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
    if flask.request.method == 'POST':
        # Récupérer la requête de l'utilisateur
        queryAddFournAuto = flask.request.form['queryAddFournAuto']
        print(queryAddFournAuto)

        # Requête SQL pour sélectionner les données dans la table "articles"
        cursor = mydb.cursor()
        # sql = "INSERT INTO glo_2005_Projet_ConcessionnaireNouvelleAuto.FournisseursAutomobiles (" \
        #       "idFournisseursVehicules, nomFournisseursVehicules, adresseFournisseursVehicules, " \
        #       "numTelephoneFournisseursVehicules, adresseCourrielFournisseursVehicules, villeFournisseursVehicules, " \
        #       "provinceEtatFournisseursVehicules, paysFournisseursVehicules) " \
        #       "VALUE ("{}")"
        cursor.execute(sql,
                       ('%' + queryAddFournAuto + '%', '%' + queryAddFournAuto + '%', '%' + queryAddFournAuto + '%',
                        '%' + queryAddFournAuto + '%', '%' + queryAddFournAuto + '%', '%' + queryAddFournAuto + '%',
                        '%' + queryAddFournAuto + '%', '%' + queryAddFournAuto + '%', '%' + queryAddFournAuto + '%',
                        '%' + queryAddFournAuto + '%', '%' + queryAddFournAuto + '%', '%' + queryAddFournAuto + '%'))
        resultsAddFournAuto = cursor.fetchall()

        return flask.render_template('fournisseurs.html', results=resultsAddFournAuto, query=queryAddFournAuto)

    return render_template('ajouterFournisseursAuto.html')


@app.route('/search-fournisseur-auto', methods=['GET', 'POST'])
def searchFournisseurAuto():
    if flask.request.method == 'POST':
        # Récupérer la requête de l'utilisateur
        querySearchFournAuto = flask.request.form['querySearchFournAuto']
        print(querySearchFournAuto)

        # Requête SQL pour sélectionner les données dans la table "articles"
        cursor = mydb.cursor()
        # sql = "INSERT INTO glo_2005_Projet_ConcessionnaireNouvelleAuto.FournisseursAutomobiles (" \
        #       "idFournisseursVehicules, nomFournisseursVehicules, adresseFournisseursVehicules, " \
        #       "numTelephoneFournisseursVehicules, adresseCourrielFournisseursVehicules, villeFournisseursVehicules, " \
        #       "provinceEtatFournisseursVehicules, paysFournisseursVehicules) " \
        #       "VALUE ("{}")"
        cursor.execute(sql, (
            '%' + querySearchFournAuto + '%', '%' + querySearchFournAuto + '%', '%' + querySearchFournAuto + '%',
            '%' + querySearchFournAuto + '%', '%' + querySearchFournAuto + '%', '%' + querySearchFournAuto + '%',
            '%' + querySearchFournAuto + '%', '%' + querySearchFournAuto + '%', '%' + querySearchFournAuto + '%',
            '%' + querySearchFournAuto + '%', '%' + querySearchFournAuto + '%', '%' + querySearchFournAuto + '%'))
        resultsSearchFournAuto = cursor.fetchall()

        return flask.render_template('fournisseurs.html', results=resultsSearchFournAuto, query=querySearchFournAuto)

    return render_template('trouverFournisseursAuto.html')


@app.route('/add-fournisseur-pieces', methods=['GET', 'POST'])
def addFournisseurPieces():
    if flask.request.method == 'POST':
        # Récupérer la requête de l'utilisateur
        queryAddFournPieces = flask.request.form['queryAddFournPieces']
        print(queryAddFournPieces)

        # Requête SQL pour sélectionner les données dans la table "articles"
        cursor = mydb.cursor()
        # sql = "INSERT INTO glo_2005_Projet_ConcessionnaireNouvelleAuto.FournisseursAutomobiles (" \
        #       "idFournisseursVehicules, nomFournisseursVehicules, adresseFournisseursVehicules, " \
        #       "numTelephoneFournisseursVehicules, adresseCourrielFournisseursVehicules, villeFournisseursVehicules, " \
        #       "provinceEtatFournisseursVehicules, paysFournisseursVehicules) " \
        #       "VALUE ("{}")"
        cursor.execute(sql, (
            '%' + queryAddFournPieces + '%', '%' + queryAddFournPieces + '%', '%' + queryAddFournPieces + '%',
            '%' + queryAddFournPieces + '%', '%' + queryAddFournPieces + '%', '%' + queryAddFournPieces + '%',
            '%' + queryAddFournPieces + '%', '%' + queryAddFournPieces + '%', '%' + queryAddFournPieces + '%',
            '%' + queryAddFournPieces + '%', '%' + queryAddFournPieces + '%', '%' + queryAddFournPieces + '%'))
        resultsAddFournPieces = cursor.fetchall()

        return flask.render_template('fournisseurs.html', results=resultsAddFournPieces, query=queryAddFournPieces)

    return render_template('ajouterFournisseursPieces.html')


@app.route('/search-fournisseur-pieces', methods=['GET', 'POST'])
def searchFournisseurPieces():
    if flask.request.method == 'POST':
        # Récupérer la requête de l'utilisateur
        querySearchFournPieces = flask.request.form['querySearchFournPieces']
        print(querySearchFournPieces)

        # Requête SQL pour sélectionner les données dans la table "articles"
        cursor = mydb.cursor()
        # sql = "INSERT INTO glo_2005_Projet_ConcessionnaireNouvelleAuto.FournisseursAutomobiles (" \
        #       "idFournisseursVehicules, nomFournisseursVehicules, adresseFournisseursVehicules, " \
        #       "numTelephoneFournisseursVehicules, adresseCourrielFournisseursVehicules, villeFournisseursVehicules, " \
        #       "provinceEtatFournisseursVehicules, paysFournisseursVehicules) " \
        #       "VALUE ("{}")"
        cursor.execute(sql, (
            '%' + querySearchFournPieces + '%', '%' + querySearchFournPieces + '%', '%' + querySearchFournPieces + '%',
            '%' + querySearchFournPieces + '%', '%' + querySearchFournPieces + '%', '%' + querySearchFournPieces + '%',
            '%' + querySearchFournPieces + '%', '%' + querySearchFournPieces + '%', '%' + querySearchFournPieces + '%',
            '%' + querySearchFournPieces + '%', '%' + querySearchFournPieces + '%', '%' + querySearchFournPieces + '%'))
        resultsSearchFournPieces = cursor.fetchall()

        return flask.render_template('fournisseurs.html', results=resultsSearchFournPieces,
                                     query=querySearchFournPieces)

    return render_template('trouverFournisseursPieces.html')


@app.route('/login', methods=['POST', 'GET'])
def login():

    if request.method == 'POST':
        email = request.form['email']
        password = request.form ['password']
        #print(password)

        cursor = mydb.cursor()
        sql = "SELECT passe from users WHERE email = %s"
        cursor.execute(sql, (email,))
        resultat = cursor.fetchone()

        if resultat is None :
            flash('Identifiants incorrects. Veuillez réessayer.')
        else:
            row = resultat[0].strip()
            if row == password :
            #session['user_id'] = user.id
                flash('Connexion reussie', category='success')
                return render_template('page_utilisateur.html')
            else:
                flash("Identifiants incorrects. Veuillez réessayer.", category='error')

    return render_template('login.html')


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    return render_template('logout.html')


@app.route('/page_utilisateur', methods=['POST', 'GET'])
def utilisateur():
    return render_template('page_utilisateur.html')


@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form['email']
        firstName = request.form['firstName']
        password1 = request.form['password1']
        password2 = request.form['password2']
        print(email, firstName, password1, password2)
        cursor = mydb.cursor()
        sql = "INSERT INTO users VALUES (NULL, '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}')",
        cursor.execute(sql, (email,))

        if len(email) < 4:
            flash('Email not valid.', category='error')
        if len(firstName) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 8 characters.', category='error')
        else:
            flash('Account created.', category='success')

    return render_template("sign-up.html")




if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'hjshjhdjahhhhhhhhhhhhhhhkjshkjdhjs'

    app.run(debug=True)
