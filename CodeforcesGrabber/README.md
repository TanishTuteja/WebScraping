# Codeforces Grabber

This project consists of 3 python scripts which use Selenium to scrape Codeforces website and fetch contests/problems from it.

For each problem fetched, the scripts take a screenshot of the problem statement (with the sample testcases) as well as store input and output of each sample testcase in separate text files. The files are named problem.png, and input*i*.txt and output*i*.txt respectively, for each testcase _i_.

The details of the scripts are as follows:

## 1. fetch_round

This script fetches a specific contest, given the contest id.

### Running the script:

In this (CodeforcesGrabber) directory, run the following:

```
python fetch_round.py <contest_num>
```

Here,

`contest_num: ID of the contest to be fetched`

### Output:

Running the script will create a new directory with `contest_num` name, and within it create separate sub-directories for each problem.

## 2. past_contests

Given an `X`, the script will fetch the past `X` contests.

### Running the script:

In this (CodeforcesGrabber) directory, run the following:

```
python past_contests.py <num_of_contests>
```

Here,

`num_of_contests: Number of past contests to be fetched`

### Output:

Running the script will create a new directory `past` which will have separate sub-directories for each past contest, the structure of which will be the same as that created by `fetch_round` script.

## 3. diff_range

Given a difficulty range and a number `num`, the script will fetch `num` number of problems lying within the specified range.

### Running the script:

In this (CodeforcesGrabber) directory, run the following:

```
python diff_range.py [min_diff] [max_diff] [num]
```

Here,

`min_diff: Minimum difficulty of the problems (Inclusive) or 'd' to use default value (0)`

`max_diff: Maximum difficulty of the problems (Inclusive) or 'd' to use default value (infinite)`

`num: Number of problems to be fetched, or 'd' to use default value (10)`

_Note: Arguments not provided will automatically take the default value._

### Output:

Running the script will create a new directory with the name `(<min_diff>-<max_diff>)` which will consist of sub-directories for each problem fetched.
