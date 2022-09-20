# Alura Challenge 2
 
## Week 01

<center><img src="alura_cash.png" width="1000" height="1000"></center><br>

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


