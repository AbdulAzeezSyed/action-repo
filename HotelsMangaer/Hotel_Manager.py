
class Choosing:

    def __init__(self, df, state, cost, operation):

        self.df = df
        self.state = state
        self.cost = cost
        self.operation = operation
        self.states = list(self.df['State'].unique())
        self.states.append('India')
        self.operations = ['Highest', 'Average', 'Cheapest']
        self.cost_ratings = ['Cost', 'Ratings']

    def chose(self):

        if self.state in self.states:
            self.dataframe = self.get_dataframe()
            HCode, Cost_Rate, HState = self.get_bestvalues()
            return HCode, Cost_Rate, HState

    def get_dataframe(self):  # get Dataframe based on State= Karnataka/Tamilnadu/Maharashtra

        if self.state in self.states:

            if self.state == 'India':
                data = self.df

            else:
                data = (self.df[self.df['State'] == self.state])

        return data

    def get_bestvalues(self):  # get Hotel Code, Cost, Ratings Values, State

        self.dataframe_desc = self.dataframe[self.cost].describe()
        kar_avg = self.dataframe_desc.iloc[5]
        if self.cost in self.cost_ratings:
            self.cost = self.cost

        if self.cost in self.cost_ratings:  # cost = Cost or Ratings

            if self.operation == self.operations[0]:  # operation = Highest
                self.final_dataframe = self.dataframe[['Hotel Code', 'State', 'Cost', 'Ratings']].loc[
                    (self.dataframe[self.cost] >= self.dataframe[self.cost].max())]

            if self.operation == self.operations[1]:  # operation = Average
                self.final_dataframe = self.dataframe[['Hotel Code', 'State', 'Cost', 'Ratings']].loc[
                    (self.dataframe[self.cost] == kar_avg)]

            if self.operation == self.operations[2]:  # operation = Cheapest:
                self.final_dataframe = self.dataframe[['Hotel Code', 'State', 'Cost', 'Ratings']].loc[
                    (self.dataframe[self.cost] <= self.dataframe[self.cost].min())]

            if self.cost == self.cost_ratings[0]:  # cost = Cost
                self.final_values = self.final_dataframe[['Hotel Code', 'Cost', 'State']].loc[
                    (self.final_dataframe['Ratings'] == self.final_dataframe['Ratings'].max())]
                self.final_values_list = self.final_values.to_string(index=False, header=False).split(' ')

                while ('' in self.final_values_list):
                    self.final_values_list.remove('')

                hotelcode = self.final_values_list[0]
                cost_rate = self.final_values_list[1]
                hotelstate = self.final_values_list[2]

            else:  # cost = Ratings
                self.final_values = self.final_dataframe[['Hotel Code', 'Ratings', 'State']].loc[
                    (self.final_dataframe['Cost'] == self.final_dataframe['Cost'].max())]
                self.final_values_list = self.final_values.to_string(index=False, header=False).split(' ')

                while ('' in self.final_values_list):
                    self.final_values_list.remove('')

                hotelcode = self.final_values_list[0]
                cost_rate = self.final_values_list[1]
                hotelstate = self.final_values_list[2]

            return hotelcode, cost_rate, hotelstate