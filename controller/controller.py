from model.model import Model
from view.view import View
from datetime import date

class Controller:
    # A controller for agenda DB
    def __init__(self):
        self.model = Model()
        self.view = View()

    def start(self):
        self.view.start()
        self.main_menu()

    #------------------------Controlador general----------------------#
    def main_menu(self):
        o = '0'
        while o != '3':
            self.view.menu()
            self.view.option('3')

            o = input()
            if o == '1':
                self.agenda_menu()
            elif o == '2':
                self.cita_menu()
            elif o == '3':
                return
            else:
                self.view.not_void_option()
        return

    def update_list(self, fs, vs):
        fields = []
        vals = []

        for f,v in zip(fs, vs):
            if v != ' ':
                fields.append(f + ' = %s')
                vals.append(v)
        
        return fields, vals
    
    #----------------------Controlador de contactos---------------------#
    def agenda_menu(self):
        o = '0'
        while o != '7':
            self.view.agenda_menu()
            self.view.option('7')

            o = input()
            if o == '1':
                self.create_contact()
            elif  o == '2':
                self.read_a_contact()
            elif o == '3':
                self.read_all_contacts()
            elif o == '4':
                self.read_contact_name()
            elif o == '5':
                self.update_contact()
            elif o == '6':
                self.delete_contact()
            elif o == '7':
                self.main_menu()
            else:
                self.view.not_void_option()
        return

    def ask_contact(self):
        self.view.ask('Nombre: ')
        name = input()
        self.view.ask('Apellido paterno: ')
        sname1 = input()
        self.view.ask('Apellido materno: ')
        sname2 = input()
        self.view.ask('Correo: ')
        email = input()
        self.view.ask('Calle: ')
        street = input()
        self.view.ask('Numero: ')
        num = input()
        self.view.ask('Colonia: ')
        col = input()
        self.view.ask('Telefono: : ')
        phone = input()
        return [name, sname1, sname2, email, street, num, col, phone]

    def create_contact(self):
        name, sname1, sname2, email, street, num, col, phone = self.ask_contact()
        
        out = self.model.create_contact(name, sname1, sname2, email, street, num, col, phone)
        if out == True:
            self.view.ok(name+' '+sname1+' ', 'agregado')
        else:
            self.view.error('No se pudo agregar el contacto')
        return

    def read_a_contact(self):
        self.view.ask('ID contacto: ')
        id_contact = input()

        contact = self.model.read_a_contact(id_contact)
        if type(contact) == tuple:
            self.view.show_contact_header('Datos del contacto ' +  id_contact + ' ')
            self.view.show_a_contact(contact)
            self.view.show_contact_midder()
            self.view.show_contact_footer()
        else:
            if contact == None:
                self.view.error('El contacto no existe')
            else:
                self.view.error('Problema al leer contacto')
        return

    def read_all_contacts(self):
        contacts = self.model.read_all_contacts()
        if type(contacts) == list:
            self.view.show_contact_header('Todos los contactos')
            
            for contact in contacts:
                self.view.show_a_contact(contact)
                self.view.show_contact_midder()
            self.view.show_contact_footer()
        else:
            self.view.error('Problema al leer los contactos')

    def read_contact_name(self):
        self.view.ask('Nombre: ')
        name = input()

        contacts  = self.model.read_contact_name(name)
        if type(contacts) == list:
            self.view.show_contact_header('Contactos con el nombre: ' + name + ' ')
            
            for contact in contacts:
                self.view.show_a_contact(contact)
                self.view.show_contact_midder()
            self.view.show_contact_footer()
        else:
            self.view.error('Problema al leer los contactos')
        return

    def update_contact(self):
        self.view.ask('ID contacto a modificar: ')
        id_contact = input()

        contact = self.model.read_a_contact(id_contact)
        if type(contact) == tuple:
            self.view.show_contact_header('Datos del contacto ' + id_contact + ' ')
            self.view.show_a_contact(contact)
            self.view.show_contact_midder()
            self.view.show_contact_footer()
        else: 
            if contact == None:
                self.view.error('El contacto no existe')
            else:
                self.view.error('Problema al leer los contactos')
            return

        self.view.msg('Ingresa los valores a modificar (vacio para omitir el campo): ')
        whole_vals = self.ask_contact()
        fields, vals = self.update_list(['nombre', 'a_paterno', 'a_materno', 'correo', 'calle', 'numero', 'colonia', 'telefono'], whole_vals)
        vals.append(id_contact)
        vals = tuple(vals)

        out = self.model.update_contact(fields, vals)
        if out == True:
            self.view.ok(id_contact, ' Actualizado')
        else:
            self.view.error('No se pudo actulizar el contacto')
        return 

    def delete_contact(self):
        self.view.ask('ID contacto a borrar: ')
        id_contac = input()

        count = self.model.delete_contact(id_contac)
        if count != 0:
            self.view.ok(id_contac, ' se borro')
        else:
            if count == 0:
                self.view.error('El contacto no existe')
            else:
                self.view.error('Problema al borrar el contacto')

    #----------------------Controlador de citas---------------------#
    def cita_menu(self):
        o = '0'
        while o != '8':
            self.view.cita_menu()
            self.view.option('8')

            o = input()
            if o == '1':
                self.create_appoiment()
            elif  o == '2':
                self.read_a_appointment()
            elif o == '3':
                self.read_all_appoitments()
            elif o == '4':
                self.read_appointmet_contact()
            elif o == '5':
                self.read_appointmet_date()
            elif o == '6':
                self.update_appointment()
            elif o == '7':
                self.delete_appointment()
            elif o == '8':
                return self.main_menu()
            else: 
                self.view.not_void_option()
        return
    
    def ask_cita(self):
        self.view.ask('ID cliente asosiado:')
        id_contacto = input()
        self.view.ask('Fecha de la cita: (yy-mm-dd): ')
        fecha = input()
        self.view.ask('Asunto:')
        affair = input()
        self.view.ask('Hora:')
        hour = input()
        return [fecha, hour, affair, id_contacto]

    def create_appoiment(self):
        fecha , hora, asunto, id_contact = self.ask_cita()

        out = self.model.create_appointment(fecha, hora, asunto, id_contact)
        print(out)
        if out == True:
            self.view.ok(fecha + ' ' + asunto + ' ', 'agregado')
        else:
            self.view.error('No')
        return

    def read_a_appointment(self):
        self.view.ask('ID de la cita: ')
        id_cita = input()

        appoitment = self.model.read_a_appointment(id_cita)
        if type(appoitment) == tuple:
            self.view.show_appoiment_header('Datos de la cita ' +  id_cita  + ' ')
            self.view.show_a_appoitment(appoitment)
            self.view.show_appoiment_midder()
            self.view.show_appoiment_footer()
        else:
            if appoitment == None:
                self.view.error('La cita no existe')
            else:
                self.view.error('Problema al leer la cita')
        return

    def read_all_appoitments(self):
        appoitments = self.model.read_all_appointments()
        if type(appoitments) == list:
            self.view.show_appoiment_header('Todas las citas')
            
            for appoitment in appoitments:
                self.view.show_a_appoitment(appoitment)
                self.view.show_appoiment_midder()
            self.view.show_appoiment_footer()
        else:
            self.view.error('Problema al leer las citas')

    def read_appointmet_contact(self):
        self.view.ask('Id del contaco asosiado: ')
        id = input()
        appoitments  = self.model.read_appointmet_contact(id)
        if type(appoitments) == list:
            self.view.show_appoiment_header('Citas con el id: ' +  id  + ' ')
            
            for appoitment in appoitments:
                self.view.show_a_appoitment(appoitment)
                self.view.show_appoiment_midder()
            self.view.show_appoiment_footer()
            
        else:
            self.view.error('Problema al leer las citas')
        return
        

    def read_appointmet_date(self):
        self.view.ask('Id del contaco asosiado: ')
        id_contact = input()
        self.view.ask('Fecha de la cita: ')
        date = input()
        appoitments  = self.model.read_appointmet_date(date, id_contact)
        if type(appoitments) == list:
            self.view.show_appoiment_header('Citas con el id: ' +  id_contact  + ' y la fecha '+ date)
            
            for appoitment in appoitments:
                self.view.show_a_appoitment(appoitment)
                self.view.show_appoiment_midder()
            self.view.show_appoiment_footer()
            
        else:
            self.view.error('Problema al leer las citas')
        return


    def update_appointment(self):
        self.view.ask('ID cita a modificar: ')
        id_cita = input()

        cita = self.model.read_a_appointment(id_cita)
        if type(cita) == tuple:
            self.view.show_appoiment_header('Datos de la cita ' + id_cita + ' ')
            self.view.show_a_appoitment(cita)
            self.view.show_appoiment_midder()
            self.view.show_appoiment_footer()
        else:
            if cita == None:
                self.view.error('La cita no existe')
            else:
                self.view.error('Problema al leer la cita')
            return
        
        self.view.msg('Ingresa valores')
        whole_vals = self.ask_cita()
        fields, vals = self.update_list(['fecha', 'hora', 'asunto', 'id_contacto'], whole_vals)
        vals.append(id_cita)
        vals =tuple(vals)

        out = self.model.update_appointment(fields, vals)
        print(out)
        if out == True:
            self.view.ok(id_cita, 'Actualizada')
        else:
            self.view.error('No se pudo actualizar la cita')
        return 

    def delete_appointment(self):
        self.view.ask('ID cita a borrar: ')
        id_cita = input()

        count = self.model.delete_appointment(id_cita)
        if count != 0:
            self.view.ok(id_cita, ' se borro')
        else:
            if count == 0:
                self.view.error('La cita no existe')
            else:
                self.view.error('Problema al borrar la cita')
