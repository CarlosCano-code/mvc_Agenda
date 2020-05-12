from mysql import connector

class Model:
    # A data model to MySQL for an agenda DB
    def __init__(self, config_db_file = 'config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connector_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d

    def connector_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()

    def close_db(self):
        self.cnx.close()

    #----------------------- Metodos contactos ---------------------------#
    def create_contact(self, name, last1, last2, email, street, num, col, phone):
        try:
            sql = 'INSERT INTO contact(`nombre`, `a_paterno`, `a_materno`, `correo`, `calle`, `numero`, `colonia`, `telefono`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
            vals = ( name, last1, last2, email, street, num, col, phone)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err 

    def read_a_contact(self, id_contact):
        try:
            sql = 'SELECT * FROM contact WHERE id_contacto = %s'
            vals = (id_contact,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record

        except connector.Error as err:
            return err 

    def read_all_contacts(self):
        try:
            sql = 'SELECT * FROM contact'
            self.cursor.execute(sql)

            # Recuperar el resultado despues de la consulta
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err 

    def read_contact_name(self, name):
        try:
            sql = 'SELECT * FROM contact WHERE nombre = %s'
            vals = (name,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err 

    def update_contact(self, fields, vals):
        try:
            sql = 'UPDATE contact SET '+','.join(fields)+' WHERE id_contacto = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
            
        except connector.Error as err:
            self.cnx.rollback()
            return err  

    def delete_contact(self, id_contact):
        try:
            sql = 'DELETE FROM contact WHERE id_contacto = %s'
            vals = (id_contact,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #-------------------------- Metodos cita -----------------------------#
    def create_appointment(self , date, hour, affair, id_contacto):
        try:
            sql = 'INSERT INTO appointment(`fecha`, `hora`, `asunto`, `id_contacto`) VALUES(%s, %s, %s, %s)'
            vals = (date, hour, affair, id_contacto)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_a_appointment(self, id_cita):
        try:
            sql = 'SELECT * FROM appointment WHERE id_cita = %s'
            vals = (id_cita,)
            self.cursor.execute(sql, vals)

            # Recuperar el resultado despues de la consulta
            record = self.cursor.fetchone()
            return record

        except connector.Error as err:
            return err 

    def read_all_appointments(self):
        try:
            sql = 'SELECT * FROM appointment'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err 

    def read_appointmet_contact(self, id_contact):
        try:
            sql = 'SELECT * FROM appointment WHERE id_contacto = %s'
            vals = (id_contact,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err 

    def read_appointmet_date(self, date, id_contact):
        try:
            sql = 'SELECT * FROM appointment WHERE fecha = %s and id_contacto = %s'
            vals = (date, id_contact,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err 

    def update_appointment(self, fields, vals):
        try:
            sql = 'UPDATE appointment SET ' + ','.join(fields)+ ' WHERE id_cita = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err 

    def delete_appointment(self, id_cita):
        try:
            sql = 'DELETE FROM appointment WHERE id_cita = %s'
            vals = tuple(id_cita,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err