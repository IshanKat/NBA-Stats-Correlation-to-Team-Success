# NBA-Stats-Correlation-to-Team-Success

[Published Paper](https://www.curieuxacademicjournal.com/_files/ugd/99711c_d14b57dd234d424baf2399e4b10c7c57.pdf#page=405)

## Running the Project (works for any NBA statistic)
1. Run cramer.py using "python3 cramer.py"
2. Enter the season year you are testing.
3. Scrape the [NBA Advanced Statistics Website](https://www.nba.com/stats/teams/advanced) or any other stat page for your desired stat and order the teams from best to worst.
4. Paste the list of teams as input into the program. You will get a Cramer's V value from 0 to 1. Lower value = lower correlation to team success, higher value = higher correlation.
