import PatientClass as pc
import ProcedureClass as pro

def main():
    patient = create_patient()
    procs = enter_procedures()
    display_bill(patient, procs)

def create_patient():
    #Initialize patient attributes
    patient_id = 1
    patient_name = 'Matt Jones'
    address =  '123 Main st, Waco TX 76706'
    phone = '254-555-7415'
    vet_status = True
    
    #create patient
    patient = pc.Patient(patient_id, patient_name, address, phone, vet_status)
    return patient


def enter_procedures():
    #initialize
    cont = 'y'
    procedures = []

    #loop for entering new procedures
    while cont.lower() == 'y':
        print('***New Procedure***')
        proc_name = input('Enter procedure name: ')
        proc_date = input('Enter procedure date: ')
        practitioner = input('Enter practitioner: ')
        charge = int(input('Enter charge: '))
        patient_id = int(input('Enter patient ID: '))
        
        procedure = pro.Procedure(proc_name, proc_date, practitioner, charge, patient_id)
        procedures.append(procedure)

        cont = input('\nDo you want to add a new procedure? y/n ')
        print()
    return procedures


def display_bill(patient, procedures):
    #variable
    vet_discount = 0.4

    #Display Patient Info
    print('\n*** Patient Bill ***')
    print('Name:', pc.Patient.get_name(patient).title())
    print('Address:', pc.Patient.get_address(patient))
    print('Phone:', pc.Patient.get_phone(patient))

    #Display Patient's procedures
    i = 0
    total = 0.0
    for row in procedures:
        if pro.Procedure.get_patient_id(procedures[i]) == pc.Patient.get_ID(patient):
            procedure = pro.Procedure.get_name(procedures[i])
            date = pro.Procedure.get_date(procedures[i])
            prac = pro.Procedure.get_practitioner(procedures[i])
            charge = pro.Procedure.get_charges(procedures[i])
            print()
            print('Procedure:', procedure)
            print('Date:', date)
            print('Practitioner:', prac.title())
            print('Charge: $', format(charge, '<5,.2f'), sep = '')
            print()
            total += charge
            i += 1
    #Check for veteran discount
    if pc.Patient.get_veteran_status(patient) == True:
        total *= (1 - vet_discount)

    #Display Total Charges    
    print('Total Charges: $', format(total, '<5,.2f'), sep = '')


main() 