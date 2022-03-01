import PatientClass as pc
import ProcedureClass as pro

def main():
    patient = create_patient()
    procedures = enter_procedures()
    display_bill(patient, procedures)

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
    #Initialize Procedures
    procedure1 = pro.Procedure('Physical Exam', '2/15/2022', 'Dr. Irvine', 250, 1)
    procedure2 = pro.Procedure('MRI', '2/15/2022', 'Dr. Hamilton', 1500, 1)
    procedure3 = pro.Procedure('CT Scan', '2/17/2022', 'Dr. Drey', 1200, 2)
    procedures = [procedure1, procedure2, procedure3]

    return procedures


def display_bill(patient, procedures):
    #variable
    VET_DISCOUNT = 0.4
    #Display Patient Info
    print('\n*** Patient Bill ***')
    print('Name:', pc.Patient.get_name(patient).title())
    print('Address:', pc.Patient.get_address(patient))
    print('Phone:', pc.Patient.get_phone(patient))

    #Display Patient's procedures
    i = 0
    total = 0.0
    for row in procedures:
        if procedures[i].get_patient_id() == patient.get_ID():
            procedure = procedures[i].get_name()
            date = procedures[i].get_date()
            prac = procedures[i].get_practitioner()
            charge = procedures[i].get_charges()
            print()
            print('Procedure:', procedure)
            print('Date:', date)
            print('Practitioner:', prac.title())
            print('Charge: $', format(charge, '<5,.2f'), sep = '')
            print()
            total += charge
            i += 1

    #Check for veteran discount
    if patient.get_veteran_status() == True:
        total *= (1 - VET_DISCOUNT)

    #Display Total Charges    
    print('Total Charges: $', format(total, '<5,.2f'), sep = '')


main() 