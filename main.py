import pandas as pd
import matplotlib.pyplot as plt


def load_and_process_data(file_path):
    data = pd.read_excel(file_path)

    data['Дата (період) данних'] = pd.to_datetime(data['Дата (період) данних'], format='%d.%m.%Y', errors='coerce')

    return data


def filter_and_plot_vaccinations(data):
    september_pfizer_vaccinations = data[(data['Дата (період) данних'].dt.month == 9) & data['Назва території'].notna()]

    plt.figure(figsize=(12, 6))
    plt.bar(september_pfizer_vaccinations['Назва території'], september_pfizer_vaccinations['Pfizer-BioNTech, осіб'])
    plt.xlabel('Область')
    plt.ylabel('Кількість вакциованих Pfizer-BioNTech у вересні')
    plt.title('Вакцинація Pfizer-BioNTech у вересні за областями')
    plt.xticks(rotation=90)
    plt.tight_layout()

    plt.savefig('vacination_plot.png', bbox_inches='tight')

    plt.show()


if __name__ == "__main__":
    file_path = 'vaccination_process_2021_regions.xlsx'
    vaccination_data = load_and_process_data(file_path)
    filter_and_plot_vaccinations(vaccination_data)
