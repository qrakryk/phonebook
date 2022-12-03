import pandas as pd
import random

#function that generates random phone book where n is quantity of records
def phone_book_gen(n):
  #load list of names and urnames
  names = pd.read_csv('/names.txt')
  surnames = pd.read_csv('/surnames.txt')
  
  #create empty dataframe to put records there 
  phone_book = pd.DataFrame(columns=['SURNAME','NAME','PHONE NUMBER']) 
  
  for i in range(0,n):
    #get random phone number
    phone_number=random.randint(100000000,999999999)
    
    #get and scrap random name
    name = names.sample()
    name = name.iloc[0]['NAMES']
    
    #get and scrap random surname
    surname = surnames.sample()
    surname = surname.iloc[0]['SURNAMES']
    
    #add random records to data frame
    phone_book = phone_book.append({'SURNAME':surname,'NAME':name,'PHONE NUMBER':phone_number}, ignore_index=True)

  #sort and return phonebook
  phone_book.sort_values('SURNAME',inplace=True,ignore_index=True)
  return phone_book

#generate phone_book and export it to csv
phone_book = phone_book_gen(10000)
phone_book.to_csv('phoneBook.csv')
