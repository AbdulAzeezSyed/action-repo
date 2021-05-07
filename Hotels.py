import pandas as pd
from HotelsMangaer.Hotel_Manager import Choosing




if __name__ == '__main__':
    df = pd.read_csv('hotels.csv')
    flag = True
    while flag:
        try:
            state = input('What is the state (karnataka/tamilnadu/maharashtra/india): ').capitalize()
            cost = input("Cost or Rating: cost/ratings: ").capitalize()
            operation = input('Operation: cheapest/highest/average: ').capitalize()

            choose = Choosing(df, state, cost, operation)
            hotelcode, cost_rate, hotelstate = choose.chose()

            if cost == 'Cost':
                print(f"Hotel with {operation} price in {hotelstate} is {hotelcode} with price {cost_rate}")
            else:
                print(f"Hotel with {operation} rating in {hotelstate} is {hotelcode} with rating {cost_rate}")
            flag = False
        except Exception as e:
            print("Error in input data! ", e)
            flag = True
