class View:
    # A view for a agenda DB
    def start(self):
        print('********************')
        print('*      AGENDA      *')
        print('********************')

    def end(self):
        print('******************')
        print('* Hasta la vista *')
        print('******************')

    def menu(self):
        print('****************')
        print('*     MENU     *')
        print('****************')
        print('1. Agenda')
        print('2. Citas')
        print('3. Salir')

    def option(self, last):
        print('Seleccione una opción (1-'+last+'): ', end = '')
    
    def not_void_option(self):
        print('¡Opción no valida\nIntente de nuevo¡')

    def ask(self, output):
        print(output, end = '')
    
    def msg(self, output):
        print(output)

    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+ ¡'+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))

    def error(self, err):
        print(' ¡ERROR! '.center(len(err)+4, '-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))

    #--------------------------Vista de Agenda------------------------#
    def agenda_menu(self):
        print('************************')
        print('* -- Submenu Agenda -- *')
        print('************************')
        print('1. Agregar contacto.')
        print('2. Mostrar un contacto.')
        print('3. Mostrar todos los contactos.')
        print('4. Buscar contacto por nombre.')
        print('5. Actualizar contacto.')
        print('6. Borrar contacto.')
        print('7. Regresar.')

    def show_a_contact(self, record):
        print('ID: ', record[0])
        print('Nombre: ', record[1])
        print('Apellido paterno: ', record[2])
        print('Apellido materno: : ', record[3])
        print('Correo: ', record[4])
        print('Calle: ', record[5])
        print('Numero: ', record[6])
        print('Colonia: ', record[7])
        print('Telefono: ', record[8])

    def show_a_contact_brief(self, record):
        print('ID: ', record[0])
        print('Nombre: ', record[1] + ' ' + record[2] + ' ' + record[3])
        print('Telefono: ', record[8])
        print('Dirección: ', record[5] + ' ' + record[6] + ' ' + record[7])

    def show_contact_header(self, header):
        print(header.center(53, '*'))
        print('-'*53)

    def show_contact_midder(self):
        print('-'*53)

    def show_contact_footer(self):
        print('*'*53)



    #--------------------------Vista de Agenda------------------------#
    def cita_menu(self):
        print('************************')
        print('* -- Submenu Citas -- *')
        print('************************')
        print('1. Agregar Cita.')
        print('2. Mostrar una cita.')
        print('3. Mostrar todas las citas.')
        print('4. Buscar cita por contacto.')
        print('5. Buscar cita por fecha.')
        print('6. Actualizar cita.')
        print('7. Borrar cita.')
        print('8. Regresar.')


    def show_a_appoitment(self, record):
        print('ID de la cita: ', record[0])
        print('Fecha: ', record[1])
        print('Hora: ', record[2])
        print('Asunto: : ', record[3])
        print('ID del contacto: ', record[4])
    
    def show_appoiment_header(self, header):
        print(header.center(53, '*'))
        print('-'*53)

    def show_appoiment_midder(self):
        print('-'*53)

    def show_appoiment_footer(self):
        print('*'*53)
