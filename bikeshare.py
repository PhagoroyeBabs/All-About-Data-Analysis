## Import the following modules to allow the smooth running of the code 🏍✈✈
import time
import pandas as pd
import numpy as np
from scipy import stats

#Load the Data into the functions by placing them using a dictionary
##Date of Creation: 6th December 2021
### Modified 20th December 2021

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_LIST = ['all','january','february','march','april','may','june']

DAYS_LIST = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    try:
        city = input("Enter the city here. It should be any of chicago, new york city, washington").casefold()
        while city not in CITY_DATA:
            print('The information given is not allowed.\n Enter a new one')
            city = input("Enter the city here. It should be any of chicago, new york city, washington").casefold()
        print('You entered:', city)

    # TO DO: get user input for month (all, january, february, ... , june)
        months = ['all','january','february','march','april','may','june']
        month = input('please enter month. should be within January - June').casefold()
        while month not in months:
            print("You entered a wrong month check")
            month = input('please enter month. should be within January - June').casefold()
        print('You entered the month:', month)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        week_days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        day = input('please enter day. should be within monday - sunday').casefold()
        while day not in week_days:
            print("You entered a wrong day check")
            day = input('please enter month. should be within January - June').casefold()
        print('You entered day:',day)
        
    except Exception as e:
        print('There is an error in your input: {}'.format(e))
    print('-'*40) 
    city,month,day = city.lower(), month.lower(), day.lower()
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    try:
        df = pd.read_csv(CITY_DATA[city])
     
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['End Time'] = pd.to_datetime(df['End Time'])
        df['month'] = df['Start Time'].dt.month
        df['week_days'] = df['Start Time'].dt.day_name() 
        #df['week_days'] = df['day_of_week'].replace({0:'monday', 1: 'tuesday', 2:'wednesday', 3: 'thursday', 4:'friday',5:'friday',6:'saturday',7:'sunday'})
        df['hour'] = df['Start Time'].dt.hour

        # filter by month if applicable
        if month != 'all':
        # use the index of the months list to get the corresponding int
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            monthz = months.index(month) + 1 
    
            # filter by month to create the new dataframe
            df = df[df['month'] == monthz ]

    # filter by day of week if applicable
        if day != 'all':
            # filter by day of week to create the new dataframe
           DAYS_LIST = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
           df = df[df['week_days'] == day.title()] 
        return df
    except Exception as e:
        print('Can\'t load this file, Error Noticed: {}'.format(e))


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #df['Start Time'] = pd.to_datetime(df['Start Time'])
    #df['End Time'] = pd.to_datetime(df['End Time'])
    #df['month'] = df['Start Time'].dt.month
    #df['week_days'] = df['Start Time'].dt.day_name() 
        #df['week_days'] = df['day_of_week'].replace({0:'monday', 1: 'tuesday', 2:'wednesday', 3: 'thursday', 4:'friday',5:'friday',6:'saturday',7:'sunday'})
    #df['hour'] = df['Start Time'].dt.hour

    # TO DO: display the most common month
    try:
        popular_month_no = df['Start Time'].dt.month.mode()[0] #It is better to use mode() attribute insead of the max() attribute as it helps to get the month with the highest occurrence. 
        popular_month = MONTH_LIST[popular_month_no-1].title() #This looks at the list from the 
        print('The most popular month is:', popular_month)
    except Exception as e:
        print('Can\'t calculate the most common month, Error Noticed: {}'.format(e))

    # TO DO: display the most common day of week
    try:
        popular_day_of_week = df['week_days'].mode()[0]
        print('The most popular weekday', 'is:',popular_day_of_week)
    except Exception as e:
        print('Can\'t calculate the most common day of week, Error Noticed: {}'.format(e))

    # TO DO: display the most common start hour
    try:
        popular_start_hour = df['hour'].mode()[0]
        print('The most popular starting hour', 'is:',popular_start_hour)
    except Exception as e:
        print('Can\'t calculate the most common start hour, Error Noticed: {}'.format(e))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    try:
        popular_start_station= df['Start Station'].value_counts().index[0]
        print('The most popular start station is:',popular_start_station)
    except Exception as e:
        print('Can\'t calculate the most used start station, Error Noticed: {}'.format(e))

    # TO DO: display most commonly used end station
    try:
        popular_end_station= df['End Station'].value_counts().index[0]
        print('The most popular end station is:',popular_end_station)
    except Exception as e:
        print('Can\'t calculate the most used end station, Error Noticed: {}'.format(e))
    # TO DO: display most frequent combination of start station and end station trip
    try:
        most_frequent_trip = df.loc[:, 'Start Station':'End Station'].mode()[0:] #df['End Station'].value_counts().index[0]
        print('the most popular trip is:', most_frequent_trip)
    except Exception as e:
        print('Can\'t calculate the most frequent combination of start station and end station, Error Noticed: {}'.format(e))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    #df['Start Time'] = pd.to_datetime(df['Start Time'])
    #df['End Time'] = pd.to_datetime(df['End Time'])
    #df['month'] = df['Start Time'].dt.month
    #df['week_days'] = df['Start Time'].dt.day_name() 
        #df['week_days'] = df['day_of_week'].replace({0:'monday', 1: 'tuesday', 2:'wednesday', 3: 'thursday', 4:'friday',5:'friday',6:'saturday',7:'sunday'})
    #df['hour'] = df['Start Time'].dt.hour

    # TO DO: display total travel time
    df['Time Diff'] = df['End Time'] - df['Start Time']
    total_travel_time = df['Time Diff'].sum()
    print('the total travel time was:', total_travel_time)
    
    # TO DO: display mean travel time
    Mean_travel_time = df['Time Diff'].mean()
    print('the mean travel time was about:', Mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        print('The amount and type of users are as followed:\n', df['User Type'].value_counts())
    except Exception as e:
        print('Couldn\'t calculate the type of users, as an Error occurred: {}'.format(e))
    # Display counts of gender
    if 'Gender' in df:
        print('The amount and gender of users in are as followed:\n',df['Gender'].value_counts())
    else:
        print('Couldn\'t calculate the amount and gender of users, as an Error occurred')
    
    if 'Birth Year' in df:
        earliest_birthyear = df['Birth Year'].min()
        most_recent_birthyear = df['Birth Year'].max()
        most_common_birthyear = df['Birth Year'].mode()
        
        print('The age structure of our customers in is:\n' 'oldest customer was born in:', int(earliest_birthyear),'\n' 'youngest customer: was born in:', int(most_recent_birthyear),'\n' 'most of our customer are born in:', int(most_common_birthyear))
    else:
        print('Couldn\'t calculate the age structure of our customers, as an Error occurred')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    """Displays raw bikeshare data."""
    row_len = df.shape[0]

    # iterate from 0 to the number of rows in steps of 5
    for i in range(0, row_len, 5):
        
        usertrip = input('\nWould you like to examine the particular user trip data? Type \'yes\' or \'no\'\n> ')
        if usertrip.lower() != 'yes':
            break
         
        row_data = df.iloc[i: i + 5]
        print(row_data)
#         for a in row_data:
#             print(a)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            


if __name__ == "__main__":
	main()
