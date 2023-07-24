
https://github.com/Nimaga95/Site_Internet_ConcessionnaireAuto/assets/117949986/f622082b-8e44-4ecb-804c-2029ac24b00e


# ConcessionnaireNouvelleAuto

In this project we decided to create an intranet for a car dealership. In this site the dealer
will be able to consult information on employees, check if the stocks of parts, look at the cars in stock.
He can also search for information on suppliers and the products they offer. He will be able to add/search for information on a supplier. Add data on a part, a car or an employee.

facilitate the management of a Car Dealership.

### Requirements

##### 1. MySQL 8.0

- The project is made on **MySQL 8.0** as the database. Install MySQL from [this page](https://dev.mysql.com/downloads/installer/).

- In the database, console1, main files replace the info below:

  ```
    host="localhost",
    user="root",
    password="your_password", # to be replaced by the password of your computer for the tests
    db="glo_2005_NewAuto_Dealership_Project",
    autocommit=True,

  ```

##### 2. Install the project libraries by entering this command in the terminal of your Python application:

```
 pip install -r requirements.txt
```

#### 3. Use

1. First make sure you are using a recent Python interpreter.
2. Start by executing the SQL code in the file: creationDeRequete.sql
3. Connect your database and put the Schema on 'glo_2005_Projet_ConcessionnaireNouvelleAuto.
4. Then run the database file to load the data into your database
5. Once the data is created and the data entered, simply run the main or z file in the terminal:

   ```
   $ pyton main.py
   ```

6. Go [here](http://localhost:5000/home) to access the site!

### Bonus: create an account or simply enter your info
    
        
   ```
   Email: janedoe@gmail.com
   Password: 123456
   ```
