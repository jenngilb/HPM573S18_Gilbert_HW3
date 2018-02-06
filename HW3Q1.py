class patient:
    #base class
    def __init__(self, name):
        self.name = name

    def discharge(self):
        """
        :returns #error message """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

class emergencypatient(patient):
      def __init__(self,name):
          patient.__init__(self,name)
          self.cost=1000 #cost of emergency patient

      def discharge(self):
          """

          :return: #cost of patient discharge post-emergency care without being admitted
          """
          print(self.name, 'EmergencyPatient')

class hospitalizedpatient(patient):
      def __init__(self,name):
          patient.__init__(self,name)
          self.cost=2000 #cost of hospitalized patient

      def discharge(self):
          """

          :return: #cost of patient discharge post-hospitalization
          """
          print(self.name, 'HospitalizedPatient')

class hospital:
    #master class
    def __init__(self):
        self.patients = []
        self.cost = 0

    def admit(self,patients):
        self.patients.append(patients) #add additional patients

    def discharge_all(self):
        for patients in self.patients:
            patients.discharge() #apply discharge function
            self.cost += patients.cost

    def get_total_cost(self): #return hospital's total costs
        return self.cost

P1 = hospitalizedpatient('P1')
P2 = hospitalizedpatient('P2')
P3 = emergencypatient('P3')
P4 = emergencypatient('P4')
P5 = emergencypatient('P5')

H1 = hospital()
H1.admit(P1)
H1.admit(P2)
H1.admit(P3)
H1.admit(P4)
H1.admit(P5)
H1.discharge_all()

print(H1.get_total_cost())
