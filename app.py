import pandas as pd
import streamlit as st
import joblib
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches

model = joblib.load(r"./default_model.sav")

df_final = pd.read_csv('dataset.csv')

def main():

    st.set_page_config(
        page_title = 'Alura Ca$h - Client Default Prediction',
        page_icon = '✅',
        layout = 'wide')

    st.sidebar.title('Client Default Prediction')

    image = Image.open('alura_cash.png')

    st.image(image)


    person_age = st.sidebar.number_input('Client age: ', min_value = 18, max_value = 120, value = 18)


    person_home_ownership = st.sidebar.selectbox('Type of home ownership: ', ('Mortgage', 'Rent', 'Own', 'Other'))


    person_income = st.sidebar.number_input('Client annual income: ', min_value = 0.0, max_value = 1000000000.0, value = 0.0, step = 0.1)


    person_emp_length = st.sidebar.slider('Employment length (years): ', min_value = 0, max_value = 50, value = 0)


    loan_intent = st.sidebar.radio('Loan intent: ', ('Homeimprovement', 'Venture', 'Personal', 'Medical', 'Education', 'Debtconsolidation'))


    loan_amnt = st.sidebar.number_input('Loan amount: ', min_value = 0.0, max_value = 1000000000.0, value = 0.0, step = 0.1)


    loan_int_rate = st.sidebar.number_input('Loan interest rate: ', min_value = 0.00, max_value = 40.00, value = 0.00, step = 0.01)


    loan_percent_income = st.sidebar.number_input('Loan percentage of income: ', min_value = 0.00, max_value = 1.00, value = 0.00, step = 0.01)


    person_default_on_file = st.sidebar.selectbox('Historical default: ', ('Yes', 'No'))

    if person_default_on_file == 'Yes':
        cb_person_default_on_file = 1
    else:
        cb_person_default_on_file = 0


    loan_grade = st.sidebar.radio('Loan grade: ', ('A', 'B', 'C', 'D', 'E', 'F', 'G'))

    if person_home_ownership == 'Mortgage':
        person_home_ownership_Mortgage = 1
        person_home_ownership_Other = 0
        person_home_ownership_Own = 0
        person_home_ownership_Rent = 0

    if person_home_ownership == 'Other':
        person_home_ownership_Mortgage = 0
        person_home_ownership_Other = 1
        person_home_ownership_Own = 0
        person_home_ownership_Rent = 0

    if person_home_ownership == 'Own':
        person_home_ownership_Mortgage = 0
        person_home_ownership_Other = 0
        person_home_ownership_Own = 1
        person_home_ownership_Rent = 0

    if person_home_ownership == 'Rent':
        person_home_ownership_Mortgage = 0
        person_home_ownership_Other = 0
        person_home_ownership_Own = 0
        person_home_ownership_Rent = 1

    if loan_intent == 'Homeimprovement':
        loan_intent_Homeimprovement = 1
        loan_intent_Venture = 0
        loan_intent_Personal = 0
        loan_intent_Medical = 0
        loan_intent_Education = 0
        loan_intent_Debtconsolidation = 0

    if loan_intent == 'Venture':
        loan_intent_Homeimprovement = 0
        loan_intent_Venture = 1
        loan_intent_Personal = 0
        loan_intent_Medical = 0
        loan_intent_Education = 0
        loan_intent_Debtconsolidation = 0

    if loan_intent == 'Personal':
        loan_intent_Homeimprovement = 0
        loan_intent_Venture = 0
        loan_intent_Personal = 1
        loan_intent_Medical = 0
        loan_intent_Education = 0
        loan_intent_Debtconsolidation = 0

    if loan_intent == 'Medical':
        loan_intent_Homeimprovement = 0
        loan_intent_Venture = 0
        loan_intent_Personal = 0
        loan_intent_Medical = 1
        loan_intent_Education = 0
        loan_intent_Debtconsolidation = 0

    if loan_intent == 'Education':
        loan_intent_Homeimprovement = 0
        loan_intent_Venture = 0
        loan_intent_Personal = 0
        loan_intent_Medical = 0
        loan_intent_Education = 1
        loan_intent_Debtconsolidation = 0

    if loan_intent == 'Debtconsolidation':
        loan_intent_Homeimprovement = 0
        loan_intent_Venture = 0
        loan_intent_Personal = 0
        loan_intent_Medical = 0
        loan_intent_Education = 0
        loan_intent_Debtconsolidation = 1

    if loan_grade == 'A':
        loan_grade_A = 1
        loan_grade_B = 0
        loan_grade_C = 0
        loan_grade_D = 0
        loan_grade_E = 0
        loan_grade_F = 0
        loan_grade_G = 0

    if loan_grade == 'B':
        loan_grade_A = 0
        loan_grade_B = 1
        loan_grade_C = 0
        loan_grade_D = 0
        loan_grade_E = 0
        loan_grade_F = 0
        loan_grade_G = 0

    if loan_grade == 'C':
        loan_grade_A = 0
        loan_grade_B = 0
        loan_grade_C = 1
        loan_grade_D = 0
        loan_grade_E = 0
        loan_grade_F = 0
        loan_grade_G = 0

    if loan_grade == 'D':
        loan_grade_A = 0
        loan_grade_B = 0
        loan_grade_C = 0
        loan_grade_D = 1
        loan_grade_E = 0
        loan_grade_F = 0
        loan_grade_G = 0

    if loan_grade == 'E':
        loan_grade_A = 0
        loan_grade_B = 0
        loan_grade_C = 0
        loan_grade_D = 0
        loan_grade_E = 1
        loan_grade_F = 0
        loan_grade_G = 0

    if loan_grade == 'F':
        loan_grade_A = 0
        loan_grade_B = 0
        loan_grade_C = 0
        loan_grade_D = 0
        loan_grade_E = 0
        loan_grade_F = 1
        loan_grade_G = 0

    if loan_grade == 'G':
        loan_grade_A = 0
        loan_grade_B = 0
        loan_grade_C = 0
        loan_grade_D = 0
        loan_grade_E = 0
        loan_grade_F = 0
        loan_grade_G = 1


    predict_button = st.sidebar.button('Predict')

    st.sidebar.markdown("""&copy; Fabiano Manetti - 2022""", unsafe_allow_html=True)

    if predict_button:

        X = [{'person_age': person_age, 'person_income': person_income,
              'person_emp_length': person_emp_length,
              'loan_amnt': loan_amnt, 'loan_int_rate': loan_int_rate,
              'loan_percent_income': loan_percent_income,
              'cb_person_default_on_file': cb_person_default_on_file,
              'person_home_ownership_Mortgage': person_home_ownership_Mortgage,
              'person_home_ownership_Other': person_home_ownership_Other,
              'person_home_ownership_Own': person_home_ownership_Own,
              'person_home_ownership_Rent': person_home_ownership_Rent,
              'loan_intent_Debtconsolidation': loan_intent_Debtconsolidation,
              'loan_intent_Education': loan_intent_Education,
              'loan_intent_Homeimprovement': loan_intent_Homeimprovement,
              'loan_intent_Medical': loan_intent_Medical, 'loan_intent_Personal': loan_intent_Personal,
              'loan_intent_Venture': loan_intent_Venture, 'loan_grade_A': loan_grade_A,
              'loan_grade_B': loan_grade_B, 'loan_grade_C': loan_grade_C, 'loan_grade_D': loan_grade_D,
              'loan_grade_E': loan_grade_E, 'loan_grade_F': loan_grade_F, 'loan_grade_G': loan_grade_G}]

        X_df = pd.DataFrame(X)

        prediction = model.predict(X_df)

########################################################################################################################
        st.subheader('Default Status Prediction:')

        if prediction[0] == 0:
            st.success('Client will probably NOT DEFAULT on its debt')
        else:
            st.warning('Client will probably DEFAULT on its debt')


########################################################################################################################
        st.subheader('Client Statistics')


        plt.figure(figsize = (20,8))

        sns.set(style='darkgrid')

        ax1 = plt.subplot(121)
        ax1 = sns.histplot(x=df_final['loan_amnt'], color='royalblue', kde=False, bins=20)

        ax1.set_title('Loan amount histogram', fontsize=18, color='black')
        ax1.set_ylabel('Count', color='black', fontsize=13)
        ax1.set_xlabel('loan amount - clients database', color='black', fontsize=13, labelpad=15)
        ax1.axvline(X[0]['loan_amnt'], color='red')

        ax1.annotate('loan amount taken by the client',
                     horizontalalignment='center',
                     verticalalignment='center',
                     xytext=(29700, 3000),
                     xy=(X[0]['loan_amnt'], 4000),
                     arrowprops=dict(facecolor='red', shrink=0.03),
                     bbox=dict(facecolor='none', edgecolor='black', boxstyle='round,pad=1'))

        sns.set(style='darkgrid')

        ax2 = plt.subplot(122)
        ax2 = sns.boxplot(data = df_final['loan_amnt'], orient = 'h', color = 'royalblue')

        ax2.set_title('Loan amount boxplot', fontsize=18, color='black')
        ax2.set_xlabel('loan amount - clients database', color='black', fontsize=13, labelpad=15)
        ax2.axvline(X[0]['loan_amnt'], color='red')

        ax2.annotate('loan amount taken by the client',
                    horizontalalignment='center',
                    verticalalignment='center',
                    xytext=(29700, -0.3),
                    xy=(X[0]['loan_amnt'], -0.2),
                    arrowprops=dict(facecolor='red', shrink=0.03),
                    bbox=dict(facecolor='none', edgecolor='black', boxstyle='round,pad=1'))

        st.pyplot(plt)

########################################################################################################################
        kpi1, kpi2 = st.columns(2)

        kpi1.metric(label = 'Client age', value = X[0]['person_age'],
                    delta = str(round(100 * (X[0]['person_age'] - df_final['person_age'].mean()) / df_final['person_age'].mean(), 2 )) + ' % average client age')

        kpi2.metric(label = 'Employment length (years)', value  = X[0]['person_emp_length'],
                    delta = str(round(100 * (X[0]['person_emp_length'] - df_final['person_emp_length'].mean()) / df_final['person_emp_length'].mean(), 2 )) + ' % average client employment length')

########################################################################################################################
        plt.figure(figsize=(20, 8))

        sns.set(style='darkgrid')

        ax1 = plt.subplot(121)
        ax1 = sns.histplot(x=df_final['loan_int_rate'], color='royalblue', kde=False, bins=20)

        ax1.set_title('Loan interest rate histogram', fontsize=18, color='black')
        ax1.set_ylabel('Count', color='black', fontsize=13)
        ax1.set_xlabel('loan interest - clients database', color='black', fontsize=13, labelpad=15)
        ax1.axvline(X[0]['loan_int_rate'], color='red')

        ax1.annotate('loan interest rate of the client',
                     horizontalalignment='center',
                     verticalalignment='center',
                     xytext=(20.5, 2500),
                     xy=(X[0]['loan_int_rate'], 3000),
                     arrowprops=dict(facecolor='red', shrink=0.03),
                     bbox=dict(facecolor='none', edgecolor='black', boxstyle='round,pad=1'))


        sns.set(style='darkgrid')

        ax2 = plt.subplot(122)
        ax2 = sns.boxplot(data=df_final['loan_int_rate'], orient='h', color='royalblue')

        ax2.set_title('Loan interest rate boxplot', fontsize=18, color='black')
        ax2.set_xlabel('loan interest - clients database', color='black', fontsize=13, labelpad=15)
        ax2.axvline(X[0]['loan_int_rate'], color='red')

        ax2.annotate('loan interest rate of the client',
                     horizontalalignment='center',
                     verticalalignment='center',
                     xytext=(20.6, -0.3),
                     xy=(X[0]['loan_int_rate'], -0.2),
                     arrowprops=dict(facecolor='red', shrink=0.03),
                     bbox=dict(facecolor='none', edgecolor='black', boxstyle='round,pad=1'))

        st.pyplot(plt)

########################################################################################################################

        if X[0]['cb_person_default_on_file'] == 1:

            historic_default = 'Yes'

        else:

            historic_default = 'No'

        if X[0]['loan_intent_Homeimprovement'] == 1:

            client_intent = 'Home improvement'

        elif X[0]['loan_intent_Venture'] == 1:

            client_intent = 'Venture'

        elif X[0]['loan_intent_Personal'] == 1:

            client_intent = 'Personal'

        elif X[0]['loan_intent_Medical'] == 1:

            client_intent = 'Medical'

        elif X[0]['loan_intent_Education'] == 1:

            client_intent = 'Education'

        elif X[0]['loan_intent_Debtconsolidation'] == 1:

            client_intent = 'Debt consolidation'

        kpi1, kpi2 = st.columns(2)

        kpi1.metric(label='Client historical default', value=historic_default)

        kpi2.metric(label='Loan intent', value=client_intent)

########################################################################################################################

        df_final['loan_status'] = df_final['loan_status'].map({0: 'Non Default', 1: 'Default'})

        plt.figure(figsize=(12, 8))

        sns.set(style='darkgrid')

        ax1 = plt.subplot(121)
        ax1= sns.boxplot(data=df_final, x='loan_status', y='person_income', orient='v', width=0.5,
                          color='royalblue')
        ax1.set_title('Distribution per income per person and loan status', fontsize=15, color='black', y=1.02)

        plt.ylim([0, df_final['person_income'].median() * 4])

        circle = plt.Circle((prediction, X[0]['person_income']), radius = 0.25, color = 'red')

        ax1.add_patch(circle)

        ax1.annotate('Client',
                     horizontalalignment='center',
                     verticalalignment='center',
                     xytext=(0.5, 125000),
                     xy=(prediction, X[0]['person_income']),
                     arrowprops=dict(facecolor='red', shrink=0.03),
                     bbox=dict(facecolor='none', edgecolor='black', boxstyle='round,pad=1'))

        df_filter = df_final[['loan_grade', 'loan_status']]

        df_filter_default = df_filter[df_filter['loan_status'] == 'Default']
        df_filter_default = df_filter_default.rename(columns={'loan_status': 'Default'})
        df_filter_default = df_filter_default.groupby('loan_grade').agg(func='count')

        df_filter_nondefault = df_filter[df_filter['loan_status'] == 'Non Default']
        df_filter_nondefault = df_filter_nondefault.rename(columns={'loan_status': 'Non-Default'})
        df_filter_nondefault = df_filter_nondefault.groupby('loan_grade').agg(func='count')

        df_filter_final = df_filter_default.join(df_filter_nondefault)
        df_filter_final['Total'] = df_filter_final['Default'] + df_filter_final['Non-Default']
        df_filter_final['Default (%)'] = round(100 * df_filter_final['Default'] / df_filter_final['Total'], 2)
        df_filter_final = df_filter_final.sort_values("Default (%)", ascending=False)

        sns.set(style='darkgrid')

        ax2 = plt.subplot(122)

        sns.set_color_codes('pastel')

        ax2 = sns.barplot(x='Total', y=df_filter_final.index, data=df_filter_final, color='0.9')

        sns.set_color_codes('muted')
        sns.barplot(x='Default (%)', y=df_filter_final.index, data=df_filter_final, color='royalblue')

        ax2.set(xlim=(0, 100), ylabel="", xlabel='%')
        ax2.set_title('Distribution per loan grade and Default status', color='black', fontsize=15, y=1.02)
        ax2.bar_label(ax2.containers[1], fmt='%1.1f%%')

        if loan_grade == 'A':

            y_grade = 6

        elif loan_grade == 'B':

            y_grade = 5

        elif loan_grade == 'C':

            y_grade = 4

        elif loan_grade == 'D':

            y_grade = 3

        elif loan_grade == 'E':

            y_grade = 2

        elif loan_grade == 'F':

            y_grade = 1

        elif loan_grade == 'G':

            y_grade =0

        ax2.annotate('Client',
                     horizontalalignment='center',
                     verticalalignment='center',
                     xytext=(80, 4.5),
                     xy=(0, y_grade),
                     arrowprops=dict(facecolor='red', shrink=0.03), fontsize=12,
                     bbox=dict(facecolor='none', edgecolor='black', boxstyle='round,pad=1'))

        st.pyplot(plt)

########################################################################################################################

        if X[0]['person_home_ownership_Mortgage'] == 1:

            home_ownership = 'Mortgage'

        elif X[0]['person_home_ownership_Other'] == 1:

            home_ownership = 'Other'

        elif X[0]['person_home_ownership_Own'] == 1:

            home_ownership = 'Own'

        elif X[0]['person_home_ownership_Rent'] == 1:

            home_ownership = 'Rent'

        kpi1, kpi2 = st.columns(2)

        kpi1.metric(label='Client type of home', value=home_ownership)

########################################################################################################################
        plt.figure(figsize=(20, 8))

        sns.set(style='darkgrid')

        ax1 = plt.subplot(121)
        ax1 = sns.histplot(x=df_final['loan_percent_income'], color='royalblue', kde=False, bins=20)

        ax1.set_title('Loan percentage of income histogram', fontsize=18, color='black')
        ax1.set_ylabel('Count', color='black', fontsize=13)
        ax1.set_xlabel('loan percentage of income - clients database', color='black', fontsize=13, labelpad=15)
        ax1.axvline(X[0]['loan_percent_income'], color='red')

        ax1.annotate('loan percentage of income of the client',
                     horizontalalignment='center',
                     verticalalignment='center',
                     xytext=(0.66, 4000),
                     xy=(X[0]['loan_percent_income'], 3000),
                     arrowprops=dict(facecolor='red', shrink=0.03),
                     bbox=dict(facecolor='none', edgecolor='black', boxstyle='round,pad=1'))


        sns.set(style='darkgrid')

        ax2 = plt.subplot(122)
        ax2 = sns.boxplot(data=df_final['loan_percent_income'], orient='h', color='royalblue')

        ax2.set_title('Loan percentage of income boxplot', fontsize=18, color='black')
        ax2.set_xlabel('loan percentage of income - clients database', color='black', fontsize=13, labelpad=15)
        ax2.axvline(X[0]['loan_percent_income'], color='red')

        ax2.annotate('loan percentage of income of the client',
                     horizontalalignment='center',
                     verticalalignment='center',
                     xytext=(0.66, -0.3),
                     xy=(X[0]['loan_percent_income'], -0.2),
                     arrowprops=dict(facecolor='red', shrink=0.03),
                     bbox=dict(facecolor='none', edgecolor='black', boxstyle='round,pad=1'))

        st.pyplot(plt)


if __name__ == '__main__':
    main()
