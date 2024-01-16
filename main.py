exercies

url= "https://github.com/codedthinking/tender-home-bias/releases/download/v1.0/ted-sample.csv"

#use indexing , slicing to fill in the following output
#no copy paste
file_name= url[-14:]
print(file_name) # 'ted-sample.csv'

protocol=url[0:5]
print(protocol) # 'https'

host_name=url[8:19]
print(host_name) # 'github.com'

#use string composition to construct 