## Choosing the dataset

I wanted a recommender where the evaluation could be done properly
over time, so I picked the Video Games category of Amazon Reviews 2023
(McAuley Lab). From the benchmark files I use the 5-core
"rating_only" version instead of the raw reviews, which carry text I
do not need: 814,586 interactions from 94,762 users on 25,612 items,
and every user and item has at least 5 interactions.

The dataset has no formal license. Its authors say it is released
mainly for research use, so I do not commit the data. A script
(download_data.py) downloads it from Hugging Face into data/raw/,
which is in .gitignore.

Known limitations: the data is very sparse (density of 0.03%, and the
median user has only 6 interactions). 64% of the ratings are 5 stars,
so I treat every interaction as a positive (implicit feedback) and do
not try to predict the rating. The 5-core filter was computed on the
whole period, so it uses a little information from the future.

## Loading the data and splitting by time

I explored the file first with a throwaway script (explore.py, kept
out of the repository through .gitignore). load_interactions() in
data.py reads the CSV, converts the timestamps (in milliseconds) to
dates and sorts the rows by time.

My first idea was to split by time quantiles, 80% train, 10%
validation and 10% test. I measured how much of each part a model
trained only on the past could actually recommend: in the test part
only 52.9% of the interactions came from known users and 31.8% were
on known items, so only 17.3% had both. A model based on user and
item identifiers cannot recommend items it has never seen, so that
split would have mostly measured new-item noise.

I then measured the same thing for 6-month test windows at different
cut-off dates, and the share of evaluable interactions went up to
between 47% and 69%, with 17,000 to 44,000 test interactions per
window. The final split is by date:

- Train: everything before July 2021.
- Validation: July to December 2021.
- Test: January to June 2022.

To choose models I train on the train part and evaluate on
validation (65.5% of its interactions are evaluable). For the final
result I retrain on train and validation together and evaluate on
test (69.0% evaluable), so the test part is not touched before that.
Later windows are kept to study how the quality decays over time.
warm_only() keeps the interactions whose user and item are known, and
I will always report the percentage left out next to each result.

One thing I have not investigated: the window starting in July 2022
has a much lower share of known items (60.4%).