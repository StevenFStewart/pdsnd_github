24th April 2022

### Bikeshare Project by Steven Stewart

### Description
Created for the Udacity Programming for Data Science in Python course.

The project allows the user to calculate selected statistical analysis
on bike share data from three U.S. cities, Chicago, New York and
Washington.

### Data Sets
For this project, data was provided by [Motivate](https://www.motivateco.com/), a bike share system provider for many major cities in the United States.  However, to avoid the upload of large data files to Git Hub, the data files required by this python programme are **not** included in this project.

Data was randomly selected for the first six months of 2017 for all three cities. All three of the data files contained the same core six (6) columns:

- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)

The Chicago and New York City files also had the following two columns:
- Gender
- Birth Year

You can access the full data sets for [Chicago](https://www.divvybikes.com/system-data), [New York City](https://www.citibikenyc.com/system-data) and [Washington](https://www.capitalbikeshare.com/system-data).  However, please note that these files have more columns and they differ in format in many cases. Some data wrangling was performed by Udacity to condense these files to the above core six columns.

### Stats Computed
1. Popular times of travel (i.e., occurs most often in the start time)
   - most common month
   - most common day of week
   - most common hour of day


2. Popular stations and trip
   - most common start station
   - most common end station
   - most common trip from start to end (i.e., most frequent combination of start station and end station)


3. Trip duration
   - total travel time
   - average travel time


4. User info
   - counts of each user type
   - counts of each gender (only available for NYC and Chicago)
   - earliest, most recent, most common year of birth (only available for NYC and Chicago)

### Files used
The following files are included in this project:
- bikeshare.py
- README.md

### Credits
Thanks to [Udacity](https://www.udacity.com) for offering a wonderful course.

In addition, I'd like to specifically credit this [convert a timedelta to days hours and minutes StackFlow article](https://stackoverflow.com/questions/2119472/convert-a-timedelta-to-days-hours-and-minutes) which I referenced when writing the code for the project.
