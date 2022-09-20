# Alura Challenge 2
 
## Week 01

<center><img src="alura_cash.png"></center><br>

The international digital bank **Alura Cash** is facing challenges in its loan sector, where the clients' default is recurrently increasing. This way, it's important to comprehend the main features that affect most the default. The company also requires a prediction model in order to classify the currently client loan and the new ones by the risk of default.


It was provided by the company a dataset containing the historical information of the loans along with personal data of the clients. The dataset is hosted in a Relational Database accesed by MySQL DBMS and summarized as follows:


<table style="width:100%">
<thead>
<tr>
<th style="text-align:justify; font-weight: bold; font-size:14px">Feature Name</th>
<th style="text-align:justify; font-weight: bold; font-size:14px">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:justify"><b>person_age</b></td>
<td style="text-align:justify">Client age</td>
</tr>
<tr>
<td style="text-align:justify"><b>person_income</b></td>
<td style="text-align:justify">Annual income</td>
</tr>
<tr>
<td style="text-align:justify"><b>person_home_ownership</b></td>
<td style="text-align:justify">Type of home ownership</td>
</tr>
<tr>
<td style="text-align:justify"><b>person_emp_length</b></td>
<td style="text-align:justify">Employment length (in years)</td>
</tr>
<tr>
<td style="text-align:justify"><b>loan_intent</b></td>
<td style="text-align:justify">Loan intent</td>
</tr>
<tr>
<td style="text-align:justify"><b>loan_grade</b></td>
<td style="text-align:justify">Loan grade</td>
</tr>
<tr>
<td style="text-align:justify"><b>loan_amnt</b></td>
<td style="text-align:justify">Loan amount</td>
</tr>
<tr>
<td style="text-align:justify"><b>loan_int_rate</b></td>
<td style="text-align:justify">Loan interest rate</td>
</tr>
<tr>
<td style="text-align:justify"><b>loan_status</b></td>
<td style="text-align:justify">Loan status (0 is non default, 1 is default)</td>
</tr>
<tr>
<td style="text-align:justify"><b>loan_percent_income</b></td>
<td style="text-align:justify">Loan percent income</td>
</tr>
<tr>
<td style="text-align:justify"><b>cb_person_default_on_file</b></td>
<td style="text-align:justify">Historical default</td>
</tr>
<tr>
<td style="text-align:justify"><b>cb_person_cred_hist_length</b></td>
<td style="text-align:justify">Credit history length</td>
</tr>
</tbody>
</table>

---

💸**Objectives**
* Explore the Dataset
* Analyse the type of data
* Look for inconsistencies
* Correct the inconsistencies
* Join the tables on their ID
* Export Dataframe to a .csv file

### Exploring the content of the Database

* It was created a connection to the MySQL DBMS and a cursor that allowed the access to the data
* Through **SQL** commands, it was identified 4 different tables with consistent type of data

### Checking for inconsistencies

* It was identified **4 null values** for `person_id` that wasn't identified by the Pandas method .info. Besides, the numbers of null values for `person_emp_length` didn't match too. Later, those inconsistencies were identified as being **missing values** that represented only **0.01%* of the final dataframe
* Some inconsistencies were found onn both `person_age` (max_age = 144 years) and `person_emp_length` (max_emp_length = 123 years) columns
* There were no **apparent** duplicate data

### Joining tables and exporting the final dataframe

* It was used the `INNER JOIN` command to join all the columns, using `IDS` table as auxiliary
* The missing values before identified were solved
* The final dataframe was then export as a .csv file

## Week 02

🏦**Objectives**
* Remove missing values
* Identify and treat outliers
* Explore the data
* Transform categorical features
* Calculate feature correlation
* Normalize and balance data
* Create predictive models
* Evaluate the models
* Optimize models
* Export best model

### Removing missing values

* Following company's **orientation**, the missing values were removed

### Identifying and treating Outliers

* It was visually identify some **outliers** in the plots. They were basically located on the right of boxplots and also cause a distortion in the respective histograms
* The outliers werer removed from the dataset
* Although the other columns seemed to have discrepant values, we could not affirm with certainty they represent outliers as they might be possible to be observed in this context

### Exploratory Analysis

* Most of the clients live currently in either **rent or mortgage homes**
* The reasons why a client borrow money from Alura Cash are diversified, being **education** as the main purpose
* A great part of the loan granted can be classified as being of **good grade** (A or B) 
* The proportion between the status of clients' default is **imbalanced** and will need to be treated further 
* Most of the clients **don't have a history of default**
* There is no **clear difference** in the loan status in terms of **client age**
* Clients with **rent houses** tend to present **default** loans
* The **bigger** the **person income**, the **less** probable is the **default**
* Regarding the **loan intention**, debt consolidation, medical and home improvement are the reasons with **biggest** percentage of **default**
* **Biggest loan amount** are related to **default** clients
* Almost all the clients with **G grade** have **default loan**. The percentage of loan decreases as the grade get higher
* **Default** clients are paying **higher loan interest rates**
* **Only 37.8 %** of the clients with history of default have currently **negative** status
* It seems to have **no difference** in the loan status considering the **credit history length** of the clients
* Clients with **higher employment's period of time** are the ones with **higher default rate**

### Creating predictive models

* First, it was checked the **correlation** and choosed the **best** features for the models
* For **normalization, balancing and training**, it was used the **Pipeline** function, since it helps to avoid the **data leakage**

### Evaluating the models

* The worst results in the validation data for **undersampling** indicated that this technique was **not suitable** for the dataset. For this reason, we focused on the **oversampling** models only
* For our the objective to **classify the risk of default** among the clients, it was **more important** that the number of **False Negatives** to be **as low as possible** in order to avoid future loss of credit. On the other hand, although also important, the number of False Positives would only prevent the company to concede loan to certain clients
* We were then more focused on the **Recall** metric rather than the Precision. From the models evaluated, Decision Tree , Random Forest, Gradient Boosting and XGBoost are the ones with the higher score
* Two more diagnostic tools used to help us decide for the best model were the **ROC** and **Precision-Recall** plot, being the latter preferred since it is appropriate for imbalanced datasets. The **AUC** is the area under the curves and can be used as the metric
* The Decision Tree Classifier presented the best recall metric, however it didn't fit well for the validation dataset according to the plots. Also, there's no great difference between Random Forest and Gradient Boosting, being the first faster. This way, we choosed **Random Forest Classifier** and **XGBoost Classifier** for then and followed through with tuning

### Model tuning and model exportation

* For tuning the models, it was used **GridSearchCV** function
* Comparing the model results, we choosed **XGBoost Classifier** because it performed better on both the training set (recall metric) and the validation set (AUC metric)
* In order to explort the model to be further deployed, we used **Joblib** library

## Week 03

💻**Objetives**
* Deploy the trained model to a web app
* Create a dashboard with client statistics

### Deploying the model

* For this project, we used **Streamlit** framework to deploy our trained model. Along with the final prediction, the user will have access to interesting plots comparing the client situation to those from Alura Cash database.

Link for the web  app: https://fabianomanetti-alurachallenge-2-app-2fn8rn.streamlitapp.com/?embedded=true
