"""
    1. Пользователь вводит данные о количестве предприятий,
    их наименования и прибыль за 4 квартала для каждого предприятия.
    Программа должна определить среднюю прибыль (за год для всех предприятий)
    и вывести наименования предприятий, чья прибыль выше среднего и отдельно
    вывести наименования предприятий, чья прибыль ниже среднего.
    Примечание: 4 квартала - это 4 разных прибыли ;-)
"""
import sys

companies = []
company_count = 1

start_input_data = input(f'Do you want to start enter info about companies(y/n)?')

if start_input_data == 'y' or start_input_data == 'Y':
    while True:
        name = input('Please enter company name: ')
        if name == 'q' or name == 'Q':
            break
        income1 = input("Please enter the company's profit in the 1-st quarter: ")
        if income1 == 'q' or income1 == 'Q':
            break
        income2 = input("Please enter the company's profit in the 2-nd quarter: ")
        if income2 == 'q' or income2 == 'Q':
            break
        income3 = input("Please enter the company's profit in the 3-rd quarter: ")
        if income3 == 'q' or income3 == 'Q':
            break
        income4 = input("Please enter the company's profit in the 4-th quarter: ")
        if income4 == 'q' or income4 == 'Q':
            break

        def company_creator(name, income1, income2, income3, income4, company_count):
            name_key = 'key' + str(company_count)
            income1_key = name_key + '_income1'
            income2_key = name_key + '_income2'
            income3_key = name_key + '_income3'
            income4_key = name_key + '_income4'
            company[name_key] = name
            company[income1_key] = income1
            company[income2_key] = income2
            company[income3_key] = income3
            company[income4_key] = income4
            return company

        company = {}
        company_creator(name, income1, income2, income3, income4, company_count)
        companies.append(company)
        company_count += 1
        for company in companies:
            print(company)
        end_input_data = input(f'Do you want to add another company for calculations(y/n)?')
        if end_input_data == 'n' or end_input_data == 'N':
            break
        else:
            continue
    number_of_companies = len(companies)

    comp_counter = 1
    while comp_counter < int(number_of_companies) + 1:
        company_fin = []
        for company in companies:
            def fin_inf_creator(company):
                key_name = 'key' + str(comp_counter)
                total_income = int(company[key_name + '_income1']) + \
                               int(company[key_name + '_income2']) + \
                               int(company[key_name + '_income3']) + \
                               int(company[key_name + '_income4'])
                company_f[key_name] = company[key_name]
                company_f['total_income'] = total_income
                return company_f

            company_f = {}
            fin_inf_creator(company)
            company_fin.append(company_f)
            comp_counter += 1

        number_of_companies_f = len(company_fin)

    total_income_all = 0
    for company_f in company_fin:
        total_income_all += company_f['total_income']

    total_income_all_avr = total_income_all / number_of_companies
    print(f'\nAverage income for all companies is: {total_income_all_avr}')


    max_min_income = []
    for company_f in company_fin:

        max_min_income.append(company_f['total_income'])


    max_income = max(max_min_income)
    min_income = min(max_min_income)

    comp_f_counter = 1
    for company_f in company_fin:
        key_name = 'key' + str(comp_f_counter)
        if company_f['total_income'] == max_income:
            print(f'{company_f[key_name]} has income = {company_f["total_income"]} which more than average in the market.')
            comp_f_counter += 1
        elif company_f['total_income'] == min_income:
            print(f'{company_f[key_name]} has income = {company_f["total_income"]} which less than average in the market.')
            comp_f_counter += 1
        else:
            comp_f_counter += 1
            continue
else:
    sys.exit()