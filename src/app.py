import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def load_data(path_data):
    data_input = pd.read_csv(path_data)
    return data_input

def comparative_chart(data_2020, data_2021, data_2022, cause, state='BRASIL'):

    if state == 'BRASIL':
        #total_deaths_2019 = data_2019.groupby(['tipo_doenca']).sum()
        total_deaths_2020 = data_2020.groupby(['tipo_doenca']).sum()
        total_deaths_2021 = data_2021.groupby(['tipo_doenca']).sum()
        total_deaths_2022 = data_2022.groupby(['tipo_doenca']).sum()
        list_cause = [int(total_deaths_2019.loc[cause]), int(total_deaths_2020.loc[cause]), int(total_deaths_2021.loc[cause]), int(total_deaths_2022.loc[cause])]
        data_list = pd.DataFrame({'Total': list_cause,
                                'Year': [2019, 2020, 2021, 2022]})

    else:

        #total_deaths_2019 = data_2019.groupby(['uf', 'tipo_doenca']).sum()
        total_deaths_2020 = data_2020.groupby(['uf', 'tipo_doenca']).sum()
        total_deaths_2021 = data_2021.groupby(['uf', 'tipo_doenca']).sum()
        total_deaths_2022 = data_2022.groupby(['uf', 'tipo_doenca']).sum()
        list_cause = [int(total_deaths_2020.loc[state, cause]), int(total_deaths_2021.loc[state, cause]), int(total_deaths_2022.loc[state, cause])]
        data_list = pd.DataFrame({'Total': list_cause,
                                'Year': [2020, 2021, 2022]})

    
    fig, ax = plt.subplots()
    ax = sns.barplot(x = 'Year', y = 'Total', data = data_list)
    ax.set_title(f"Deaths by {cause} at {state}")

    return fig

def main():
    #data_2019 = load_data('data\obitos-2019.csv')
    data_2020 = load_data('data\obitos-2020.csv')
    data_2021 = load_data('data\obitos-2021.csv')
    data_2022 = load_data('data\obitos-2022.csv')
    
    diseases = data_2020['tipo_doenca'].unique()
    state = np.append(data_2020['uf'].unique(), 'BRASIL')

    st.title('Analysis of respiratory diseases in Brazil from 2019 to 2022')
    st.markdown('This work is for didatical purposes only')
    
    desease = st.sidebar.selectbox('Select the desease',
                  diseases)
    state = st.sidebar.selectbox('Select the state',
                  state)

    chart = comparative_chart(data_2020, 
    data_2021, data_2022, desease, state)

    st.pyplot(chart)
    #st.dataframe(data_2019)


if __name__ == '__main__':
    main()