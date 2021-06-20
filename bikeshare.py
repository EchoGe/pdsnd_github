import time
import pandas as pd
import numpy as np
import 

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city=input('insert the city. \n').lower()
    while city not in CITY_DATA:
        city=input('This is an invalid input.\n').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month=input('insert the month. \n').lower()
    months=['january', 'february', 'march', 'april', 'may', 'june', 'july','august', 'september', 'october', 'november', 'december',    'all'] 
    while month not in months:
        month=input('This is an invalid input. \n').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('insert the day. \n').lower()
    days=['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']
    while day not in days:
        day=input('This is an invalid input.\n').lower()

    print('-'*40)
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
    df=pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months=['january', 'february', 'march', 'april', 'may', 'june', 'july','august', 'september', 'october', 'november', 'december','all']
        month=months.index(month)+1
        df=df[df['month']==month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    top_m=df['month'].mode()[0]
    print(f'The most common month is: {top_m}')

    # TO DO: display the most common day of week
    top_d=df['day_of_week'].mode()[0]
    print(f'the most common day of week is: {top_d}')

    # TO DO: display the most common start hour
    top_h=df['hour'].mode()[0]
    print(f'the most common start hour is: {top_h}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    com_sta=df['Start Station'].mode()[0]
    print(f'most commonly used start station is: {com_sta}')


    # TO DO: display most commonly used end station
    com_sta_end=df['End Station'].mode()[0]
    print(f'most commonly used end station is: {com_sta_end}')

    # TO DO: display most frequent combination of start station and end station trip
    comb= df['Start Station'] + ' --> ' +df['End Station'] 
    top_comb=comb.mode()[0]
    print('The most frequent combination of start station and end station trip is: {top_comb}' )
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time=df['Trip Duration'].sum()
    print(f'total travel time is: {total_time}sec')

    # TO DO: display mean travel time
    mean_time=df['Trip Duration'].mean()
    print(f'mean travel time is: {mean_time}sec')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type=df['User Type'].value_counts()
    print(f'counts of the user types: \n {user_type}')

    # TO DO: Display counts of gender
    if city != 'washington':
        count_ge=df['Gender'].value_counts()
        print(f'counts of the user gender: \n {count_ge}')
    else:
        print('\n This dataset does not contain gender.')
        
    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        ealiest = df['Birth Year'].min()
        recent_most = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print((f'earliest, most recent, and most common year of birth are : {earliest} , {recent_most} , {most_common_year}')
    else:
        print('\n This dataset does not contain user information.')
        


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def choice(msg, choices=('y', 'n')):
    """Return a valid input from the user given an array of possible answers.
    """

    while True:
        choice = input(msg).lower().strip()
        # terminate the program if the input is end
        if choice == 'end':
            raise SystemExit
        # triggers if the input has only one name
        elif ',' not in choice:
            if choice in choices:
                break
        # triggers if the input has more than one name
        elif ',' in choice:
            choice = [i.strip().lower() for i in choice.split(',')]
            if list(filter(lambda x: x in choices, choice)) == choice:
                break

        msg = ("\nSomething is not right. Please mind the formatting and "
                  "be sure to enter a valid option:\n>")

    return choice

def raw_data(df, point):
    """Display 5 line of sorted raw data each time."""
    print("\nYou opted to view raw data.")
    # this variable holds where the user last stopped
    if point > 0:
        last_point = choice("\n Would you like to continue from where you stopped last time? \n [y] Yes\n [n] No\n\n>")
        if last_point == 'n':
            point = 0
            
    # sort data by column
    if point == 0:
        show_df = choice( "\n What would you like to see first \n Hit Enter to view All.\n \n [st] Start Time\n [et] End Time\n[td] Trip Duration\n [ss] Start Station\n [es] End Station\n\n>", ('st', 'et', 'td', 'ss', 'es', '')) 
        if show_df == 'st':
            df = df.sort_values(['Start Time'])
        elif show_df == 'et':
            df = df.sort_values(['End Time'])
        elif show_df == 'td':
            df = df.sort_values(['Trip Duration'])
        elif show_df == 'ss':
            df = df.sort_values(['Start Station'])
        elif show_df == 'es':
            df = df.sort_values(['End Station'])
        elif show_df == '':
            pass
    # each loop displays 5 lines of raw data
    while True:
        for i in range(point, len(df.index)):
            print(df.iloc[point:point+5].to_string()+"\n")
            point += 5

            if choice("Do you want to keep printing raw data?"
                      "\n\n[y]Yes\n[n]No\n\n>") == 'y':
                continue
            else:
                break
        break
    return point

              
              
              
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
