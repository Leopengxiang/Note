my_dic = {"lover":"zhangcheng", "sister":"liaoyang"};
print(my_dic);
my_dic["grand_mother"] = "zengsonghua";
print(my_dic);

my_col = {1, 3, 4, 5, 3, 5};
print(my_col);
sorted(my_col);
print(my_col);
print("lover" in my_dic);

sorted_by_key = sorted(my_dic.items(), key=lambda x : x[0]);
sorted_by_num = sorted(my_dic.items(), key=lambda x : x[1]);
print(sorted_by_key);
print(sorted_by_num);



def find_product_price(products, product_id):
    for id, price in products:
        if id == product_id:
            return price
    return None 
     
products = [
    (143121312, 100), 
    (432314553, 30),
    (32421912367, 150) 
]

print('The price of product 432314553 is {}'.format(find_product_price(products, 432314553)))


products = {
    143121312 : 100,
    432314553 : 30,
    32421912367 : 150
}

print('The price of product 32421912367 is {}'.format(products[32421912367]));


# list version
def find_unique_price_using_list(products):
    unique_price_list = []
    for _, price in products: # A
        if price not in unique_price_list: #B
            unique_price_list.append(price)
    return len(unique_price_list)

products = [
    (143121312, 100), 
    (432314553, 30),
    (32421912367, 150),
    (937153201, 30)
]
print('number of unique price is: {}'.format(find_unique_price_using_list(products)))


# set version
def find_unique_price_using_set(products):
    unique_price_set = set()
    for _, price in products:
        unique_price_set.add(price)
    return len(unique_price_set)        

products = [
    (143121312, 100), 
    (432314553, 30),
    (32421912367, 150),
    (937153201, 30)
]
print('number of unique price is: {}'.format(find_unique_price_using_set(products)))



import time
id = [x for x in range(0, 100000)]
price = [x for x in range(200000, 300000)]
products = list(zip(id, price))

# 计算列表版本的时间
start_using_list = time.perf_counter()
find_unique_price_using_list(products)
end_using_list = time.perf_counter()
print("time elapse using list: {}".format(end_using_list - start_using_list))


# 计算集合版本的时间
start_using_set = time.perf_counter()
find_unique_price_using_set(products)
end_using_set = time.perf_counter()
print("time elapse using set: {}".format(end_using_set - start_using_set))


