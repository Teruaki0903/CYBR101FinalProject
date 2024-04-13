Submit data 2023/12/06


Bitcoin Alarm







Teruaki Murakami
Shingo Kitamura
Prajna Das
1.	Role and Responsibilities
Murakami Teruaki: Main coder
Shingo Kitamura: Dataset analyst
Prajna Das: Presentation and documentation
2.	Statement of the problem
Purpose:
make ai model, dataset and software that checks bitcoin tweets and alert in some way.
Background:
The price of the bitcoin is change so fast and far.  Sometimes big companies introduce bitcoin bill or government try to regulate bitcoin. The decision affects bitcoin price. Many people lose money or gain big profits. Bitcoin is not dice. If People think bitcoin has value the price of the bitcoin will be higher, and vice versa. As you know people decide value of bitcoin by information. The information is very important for all investigation. Unfortunately, the individual investigator does not have information than organization investigator. So, the individual investigator must pay attention to information. And we thought tweet is very good for get new information. In many cases, there are a lot of media report bitcoin events. And many people react that.
Solution:
We use the Ritetag API for correct number of tweets. After that, input the data to the AI to check our situation.
3.	Datasets
We use tweets data for datasets. The size of the data was 2 columns 2092 row. The format of the data is csv. The data starts form 2014/4/09. And until 2019/12/29
Firstly, I script data from https://bitinfocharts.com/comparison/bitcoin-tweets.html#alltime.
Then I gat data and number of tweets.
Secondly, I collect bitcoin related incident (Mt. Gox goes bankrupt).
Connect, Two data, tweet number and incident data.
Thirdly, I remove null data, date, And whitespace from dataset.
Fourthly, Add data label for Machine learning.
Fifthly, divide 24 to fit the program.





4.	Results:
![image](https://github.com/Teruaki0903/CYBR101FinalProject/assets/166669315/7bd7f234-b3a7-4827-bd04-bd32968b76c1)

Graph:
This is the full dataset graph. 
The axis means. There was incident or not. (no incident = 0, there was incident = 100) 
The horizontal means. The number of tweets.

Finding:
Bitcoin value was decided by market investors so, if market investors are many, Bitcoin value will be higher, Furthermore, the number of tweets will increase.
It means that it is very hard to compete number of tweet 2014 and 2019. Because 2019 bitcoin investor is much higher than 2014 bitcoin investor.
If we have a lot of time, we will divide bitcoin value. If the tweet was divided, It is showing that The value of the how far from normal.
5.	Functionally overview:
The program is three. The all programs read 1 csv file. The one program read one saved model.
The scraping program: This program script data from web site.
1. Set the URL. And get web page content.
2. get script and get data.
3. make data flame by panda.
4. Output csv file.

The machine learning program: This program Machine lean from csv file.
1. Read data (csv file).
2. Make data label 
3. Prepossessing data. 
4. Make train data and test data.
5. Build model
6. Compile model 
7. Train data
8. Test data (show loss)
9. Test ai model by input number
10. Save model

The bitcoin alarm program: Use ai model, use Ritetag API, send warning mail, Make time schedule. 
1. Input how many times check the tweets.
2. Check next time.
3. Use (time.sleep ) method.
4. Call hashtag function:
4-1. Call Ritetag API: client.hashtag_stats(['bitcoin']) 
4-2. get Number of tweets about bitcoin per one hour.
4-3. Call Ai function:
4-3-1. Read data label from csv file.
4-3-2. Preprocessing.
4-3-3. Load saved model.
4-3-4. Input Number of tweets per one hour.
4-3-4. Check current situation is safe or not.
4-4 (if situation is safe). Just print number of tweets.
4-4 (if situation is not safe). Call mail function.
4-4-1. Dispatch outlook mail
4-4-2. Create mail item.
4-4-3. Set mail setting (make title, body massage (input number of tweets) , send email address)
4-4-4. Send massage.
5. Go back to 3.









Picture of the mail warning (I used debug function to show the picture).
![image](https://github.com/Teruaki0903/CYBR101FinalProject/assets/166669315/7ca69da3-ef54-4d75-bab6-66fb83f3a827)



6.	Conclusions:
There is tendency to tweet if bitcoin price is moved dramatically. But the number of Bitcoin investors are increasing the number of tweets is also increase.
7.	References:
https://ai-inter1.com/beautifulsoup_1/ 図解！Python BeautifulSoupの使い方を徹底解説！(select、find、find_all、インストール、スクレイピングなど)
https://www.tensorflow.org/api_docs/python/tf TensorFlow official reference
https://pypi.org/project/ritetag/ Ritetag document 
https://ritekit.com/api-demo/hashtag-stats Ritetag demo 


