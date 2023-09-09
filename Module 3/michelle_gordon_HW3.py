"""
Module 3 HW 
BMI 6018 Fall 2022
Completed by Michelle Gordon
"""

#    Question 1--------------------------------------------------------------
one_a = [x for x in range(10)]
new_fifth_element = one_a[5] + 3
temp_list = one_a
temp_list[5] = new_fifth_element
one_b = temp_list
one_c = [float(x) for x in one_b]
one_d = set(one_c)
one_e = one_d
one_e.add(10)
one_f = one_d.pop()
one_g = len(one_d)
one_h = (len(one_d) == len(one_a))
one_i = (list(one_d) + one_a)
one_j = set(one_i)
one_k = len(one_j)


#    Question 2--------------------------------------------------------------
two_a = {
    "two_patient_dictionary_kinoko" : {"name" : "Kinoko",   "year" : 2021 },
    "two_patient_dictionary_dango" :   {"name" : "Dango",   "year" : 2019 },
    "two_patient_dictionary_mochi" :   {"name" : "Mochi",   "year" : 2020 }
}
two_b = two_a["two_patient_dictionary_dango"]["name"]
#2.c is below:
two_a["two_patient_dictionary_mochi"]["year"] = 2018
# two_d = {"n":"y" for patient in two_a for n,y in (patient["name"],patient["year"])}
two_d = {
    two_a["two_patient_dictionary_kinoko"]["name"] : two_a["two_patient_dictionary_kinoko"]["year"],
    two_a["two_patient_dictionary_dango"]["name"] : two_a["two_patient_dictionary_dango"]["year"],
    two_a["two_patient_dictionary_mochi"]["name"] : 2019
}
two_e = list(two_d.keys())
two_f = list(two_d.values())
two_g = dict(zip(two_e, two_f))


#    Question 3--------------------------------------------------------------
setA = {1,2,3,4,5}
setB = {2,3,4,5,6}
setC = {3,5,7,9}
setD = {2,4,6,8}
setE = {1,2,3,4}

three_a = (setE.issubset(setA))
# alternate syntax for 3.a: setE <= setA
three_b = (setE.issubset(setA)) & (setE != setA)
# alternate syntax for 3.b: setE < setA
three_c = setA.intersection(setB)
# alternate syntax for 3.c: setA & setB
three_d = setC | setD | setE
#3.e below:
three_d.add(9)
three_f = (three_d == one_a)
three_g = "they are not the same because one_a's list includes 0, which three_d does not have.  I would have to use .add() to add 0 to the set"


#    Question 4--------------------------------------------------------------
four_a = 8
four_b = []
four_c = four_b.append(type(four_a))
four_d = four_b.append(0.39)
four_e = four_b.append(type(0.39))
four_f = four_b.append(0.39**-10)
four_g = four_b.append(type(0.39**-10))


#    Question 5--------------------------------------------------------------
keys = [index for index in range(len(four_b))]
five_a = dict(zip(keys, four_b))
five_b = four_b.append(str(300))
five_c = four_b.append(type(four_b[5]))
five_d = four_b[5][0:2]
five_e = four_b.append(type(five_d))
five_f = [int(num) for num in four_b if (type(num) == type(1.1)) | (type(num) == type("string"))]
five_g = four_b.append(type(5))
five_h = four_b.append(type(setA))
