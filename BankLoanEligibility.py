def loan_eligibility(salary, age, credit_score):
    min_salary = 30000
    min_age = 21
    min_credit_score = 650
    if salary < min_salary:
        return f"Loan Rejected: Salary minimum required is {min_salary}."
    if age < min_age:
        return f"Loan Rejected: Age minimum required is {min_age}."
    if credit_score < min_credit_score:
        return f"Loan Rejected: Credit score is below minimum requirement{min_credit_score}."

    return "Loan Approved"

salary = float(input("Enter your salary: "))
age = int(input("Enter your age: "))
credit_score = int(input("Enter your credit score: "))

ans= loan_eligibility(salary, age, credit_score)
print(ans)