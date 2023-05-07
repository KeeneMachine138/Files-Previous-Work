# Q1 (1.5 pts) write the following credit card data to a CSV file:
import csv
credit_card_data = [
["CLIENTNUM","Attrition_Flag","Customer_Age","Gender","Dependent_count","Education_Level","Marital_Status","Income_Category","Card_Category","Months_on_book","Total_Relationship_Count","Months_Inactive_12_mon","Contacts_Count_12_mon","Credit_Limit","Total_Revolving_Bal","Avg_Open_To_Buy","Total_Amt_Chng_Q4_Q1","Total_Trans_Amt","Total_Trans_Ct","Total_Ct_Chng_Q4_Q1","Avg_Utilization_Ratio"],
["768805383","Existing Customer","45","M","3","High School","Married","$60K - $80K","Blue","39","5","1","3","12691","777","11914","1.335","1144","42","1.625","0.061"],
["818770008","Existing Customer","49","F","5","Graduate","Single","Less than $40K","Blue","44","6","1","2","8256","864","7392","1.541","1291","33","3.714","0.105"],
["713982108","Existing Customer","51","M","3","Graduate","Married","$80K - $120K","Blue","36","4","1","0","3418","0","3418","2.594","1887","20","2.333","0"],
["769911858","Existing Customer","40","F","4","High School","Unknown","Less than $40K","Blue","34","3","4","1","3313","2517","796","1.405","1171","20","2.333","0.76"],
["709106358","Existing Customer","40","M","3","Uneducated","Married","$60K - $80K","Blue","21","5","1","0","4716","0","4716","2.175","816","28","2.5","0"],
["713061558","Existing Customer","44","M","2","Graduate","Married","$40K - $60K","Blue","36","3","1","2","4010","1247","2763","1.376","1088","24","0.846","0.311"],
["810347208","Existing Customer","51","M","4","Unknown","Married","$120K +","Gold","46","6","1","3","34516","2264","32252","1.975","1330","31","0.722","0.066"],
["818906208","Existing Customer","32","M","0","High School","Unknown","$60K - $80K","Silver","27","2","2","2","29081","1396","27685","2.204","1538","36","0.714","0.048"]
]

with open("credit_card_data.csv", "w", newline="") as csvfile:
    cc_total = csv.writer(csvfile)
    for row in credit_card_data:
        cc_total.writerow(row)

    cc_total.writerow(credit_card_data)

# Q2 (2.25 pts) find the average utilization rate of the credit card customers
# write the average to a .txt file
count = 0
sum_credit_util = 0

for d in credit_card_data:
    if count != 0:
        sum_credit_util += float(d[-1])
    count += 1

average = sum_credit_util / count

statistics = open('cc_data_average.txt', 'w')
statistics.write('Average: ' +  str(average))
print("Great Succes! Your Credit Card Data has been written into the txt file: cc_data_average")
statistics.close()
