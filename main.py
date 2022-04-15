class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return self.name + ' ' + self.calc_employee_netto_salary() + ' ' + str(self.calc_employer_amount()) + ' ' + \
               self.calc_total_employer_amount()

    def calc_employer_amount(self):
        pensionable_pay = round(self.salary * 0.0976, 2)

        # social pension contribution
        spc = round(self.salary * 0.065, 2)

        # accident insurance contribution
        aic = round(self.salary * 0.0193, 2)

        # contribution for Fundusz Pracy
        cfp = round(self.salary * 0.0245, 2)

        # contribution for Fundusz Gwarantowanych Świadczeń Pracowniczych
        cfgsp = round(self.salary * 0.001, 2)

        return round(pensionable_pay + spc + aic + cfp + cfgsp, 2)

    def calc_total_employer_amount(self):
        employer_additional_cost = self.calc_employer_amount()

        employer_total_amount = self.salary + employer_additional_cost

        return f"{employer_total_amount:.2f}"

    def calc_employee_netto_salary(self):
        emp_salary = self.salary
        pensionable_pay = round(emp_salary * 0.0976, 2)

        # social pension contribution
        spc = round(emp_salary * 0.015, 2)
        sickness_pay = round(emp_salary * 0.0245, 2)

        health_contribution = round(pensionable_pay + spc + sickness_pay, 2)

        health_basic = round(emp_salary - health_contribution, 2)

        health_pay = round(health_basic * 0.09, 2)
        health_tax = round(health_basic * 0.0775, 2)

        work_cost = 111.25

        tax_basic = round(emp_salary - work_cost - health_contribution, 0)

        const_pay = 46.33

        work_tax = round((tax_basic * 0.18) - const_pay, 2)

        tax_advance = round(work_tax - health_tax, 0)

        employee_netto_salary = emp_salary - health_contribution - health_pay - tax_advance

        return f"{employee_netto_salary:.2f}"


i = input()
total_cost = 0
for j in range(int(i)):
    temp_input = input()
    name, salary = temp_input.split(' ')
    temp_emp = Employee(name=name, salary=int(salary))
    total_cost += float(temp_emp.calc_total_employer_amount())
    print(temp_emp)
print(total_cost)
