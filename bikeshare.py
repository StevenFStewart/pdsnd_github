import calendar
import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "All" to apply no month filter
        (str) day - name of the day of week to filter by, or "All" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    valid_input = False
    while not valid_input:
        city = input(
            '\nWhich city?  Enter Chicago, New York City or Washington?\n').lower()
        if city in ('chicago', 'new york city', 'washington'):
            valid_input = True
        else:
            print('\nOops! Your city selection was invalid.  Please retry.')

    # get user input for month (all, january, february, ... , june)
    valid_input = False
    while not valid_input:
        month = input('\nWhich month - Enter Jan, Feb, Mar, Apr, May, Jun or All.\n').title()
        if month in ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'All'):
            valid_input = True
        else:
            print('\nOops! Your month selection was invalid.  Please retry.')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    valid_input = False
    while not valid_input:
        day = input("\nWhich day - Enter Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All.\n").title()
        if day in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All'):
            valid_input = True
        else:
            print("\nOops! Your day selection was invalid.  Please retry.")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "All" to apply no month filter
        (str) day - name of the day of week to filter by, or "All" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA.get(city))

    # convert the Start Time and End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month, day of week and start hour from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day_Of_Week'] = df['Start Time'].dt.weekday_name
    df['Start_Hour'] = df['Start Time'].dt.hour

    # extract duration from Start Time and End Time to create new column
    df['Duration'] = df['End Time'] - df['Start Time']

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['Month'] == month]

    # filter by day of week if applicable
    if day != 'All':

        # filter by day of week to create the new dataframe
        df = df[df['Day_Of_Week'] == day]

    return df


def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.

    Args:
        (Panda Dataframe) df - Containing city data filtered by month and day
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month and its count
    common_month = df['Month'].mode()[0]
    common_month_name = calendar.month_name[common_month]
    common_month_count = df['Month'].value_counts()[common_month]
    print('\nMost common month is', common_month_name, 'with a count of', common_month_count)

    # display the most common day of week and its count
    common_day = df['Day_Of_Week'].mode()[0]
    common_day_count = df['Day_Of_Week'].value_counts()[common_day]
    print('\nMost common day of week is', common_day, 'with a count of', common_day_count)

    # display the most common start hour and its count
    common_hour = df['Start_Hour'].mode()[0]
    common_hour_count = df['Start_Hour'].value_counts()[common_hour]
    print('\nMost common start hour is', common_hour, 'with a count of', common_hour_count)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.

    Args:
        (Panda Dataframe) df - Containing city data filtered by month and day
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station and count
    common_start_station = df['Start Station'].mode()[0]
    common_start_station_count = df['Start Station'].value_counts()[common_start_station]
    print('\nMost common start station is', common_start_station, 'with a count of', common_start_station_count)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    common_end_station_count = df['End Station'].value_counts()[common_end_station]
    print('\nMost common end station is', common_end_station, 'with a count of', common_end_station_count)

    # display most frequent combination of start station and end station trip
    common_trip = (df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    common_trip_count = (df['Start Station'] + ' to ' + df['End Station']).value_counts()[common_trip]
    print('\nMost common trip is', common_trip, 'with a count of', common_trip_count)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def split_timedelta_parts(time_delta_value):
    """
    Splits a timedelta parts into days, hours, minutes and seconds.
    Theory behind this function was based upon selected answer in Stack Overflow article:
    https://stackoverflow.com/questions/2119472/convert-a-timedelta-to-days-hours-and-minutes
    Answered on Jan 22, 2010 at 18:26 by Alex Martelli

    Args:
        (timedelta) time_delta_value - the timedelta value to split
    Returns:
        calculated_days - The number of days determined for the given timedelta value
        calculated_hours - The number of hours determined for the given timedelta value
        calculated_minutes - The number of minutes determined for the given timedelta value
        calculated_seconds - The number of seconds determined for the given timedelta value
    """

    calculated_days = time_delta_value.days
    calculated_hours = time_delta_value.seconds//3600
    calculated_minutes = (time_delta_value.seconds//60)%60
    calculated_seconds = time_delta_value.seconds - (calculated_hours * 3600) - (calculated_minutes * 60)

    return calculated_days, calculated_hours, calculated_minutes, calculated_seconds


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.

    Args:
        (Panda Dataframe) df - Containing city data filtered by month and day
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time (to seconds excluding microseconds)
    travel_days, travel_hours, travel_minutes, travel_seconds = split_timedelta_parts(df['Duration'].sum())
    print('\nTotal trip duration is', travel_days, 'days,', travel_hours, 'hours,', travel_minutes, 'minutes and', travel_seconds, 'seconds')

    # display mean travel time
    travel_days, travel_hours, travel_minutes, travel_seconds = split_timedelta_parts(df['Duration'].mean())
    print('\nTotal mean travel time is', travel_days, 'days,', travel_hours, 'hours,', travel_minutes, 'minutes and', travel_seconds, 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """
    Displays statistics on bikeshare users including type, gender and birth year metrics.

    Args:
        (Panda Dataframe) df - Containing city data filtered by month and day
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('\nDisplaying user type counts appropriate to your chosen filter.\n')
    print(df['User Type'].value_counts())

    # Display counts of gender
    # Checks for gender column in data frame as not applicable to Washington
    print('\nDisplaying gender counts appropriate to your chosen filter.\n')
    if 'Gender' in df:
        print(df['Gender'].value_counts())
    else:
        print('Your filter selection included no data for Gender.')

    # Display earliest, most recent, and most common year of birth
    # Checks for gender column in data frame as not applicable to Washington
    print('\nDisplaying birth year statistics appropriate to your chosen filter.\n')
    if 'Birth Year' in df:
        print('Earliest birth year is', int(df['Birth Year'].min()))
        print('\nLatest birth year is', int(df['Birth Year'].max()))
        print('\nMost common birth year is', int(df['Birth Year'].mode()[0]))
    else:
        print('Your filter selection included no data for Birth Year.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def get_sample_raw_data_rows(df):
    """
    Yields raw data from passed in dataframe in 5 row chunks.

    Args:
        (Panda Dataframe) df - Containing city data filtered by month and day

    Yields:
        (Panda Dataframe) df - Subset of original dataset covering 5 rows of data
    """

    # Loops through data frame and yields 5 rows at a time
    for i in range(0, len(df), 5):
        yield df[i:i + 5]


def show_raw_data(df):
    """
    Displays the underlying raw data in the filtered dataframe in 5 row chunks until user says to stop.

    Args:
        (Panda Dataframe) df - Containing city data filtered by month and day
    """

    # Display raw data in 5 row blocks while user confirms
    show_data = input('\nWould you like to see raw data rows? Enter yes or no.\n')
    if show_data.lower() == 'yes':
        print('\nDisplaying sample rows from underlying data set appropriate to your chosen filter.\n')
        for somesamplerows in get_sample_raw_data_rows(df):
            print(somesamplerows)
            show_more = input('\nWould you like to see more rows? Enter yes or no.\n')
            if show_more.lower() != 'yes':
                break

    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
