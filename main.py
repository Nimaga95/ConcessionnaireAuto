import flask
from flask import Flask, request, render_template,flash
import pymysql

app = flask.Flask(__name__)

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="teddybear",  # à remplacer par le password de votre ordinateur pour les tests
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

    return render_template('barre_recherche.html')



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

    return render_template('barre_recherche.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/sign-up', methods=['GET', 'POST'])
def sign_upt():
    if request.method == 'POST':
        email = request.form['email']
        firstName = request.form['firstName']
        password1 = request.form['password1']
        password2 = request.form['password2']

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
    app.run(debug=True)
