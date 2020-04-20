# Rap Lyrics Generator 

This is a small project, which aim was to have some fun by scraping song lyrics from Genius and then use them to train Recurrent Networks to generate some new ones with Tensorflow.

**Credit to @ANOVAProjectUSYD for some parts of the code!**
### Quick outline

Within these files you will find a dataset with artist's names and about 1200 song lyrics that we scraped with the crawler that can be find in this repository.
The search file with is used by inputing a database of artist's names. Furthermore, you will find here a final model that we have trained and a 
Jupyter Notebook in which you will find code that was used to create it and use it.

### Install dependencies

``` pip install -r requirements.txt```

### How to run the project?

+ Clone this repository  ```git clone https://github.com/mglaz/rap_lyrics_final```
+ Open Jupyter Notebook  ```jupyter notebook``` 
+ Open 'lyrics_model_working.ipynb' 
+ Change the directory variable to the path with lyric files on your computer
+ If you want to have some fun with the project run all of the cells and change some parameters

If you want to just test the model, use this command:
```tf.keras.models.load_model('good_model_100_epochs.h5', compile=False)```

+ Use Generate_text function to generate lyrics with the model. Set the temperature, however you want however keep in mind that with temperature=
<0.6 the lyrics will leak into the model and it can steal existing lyrics. On the other hand majority of the text generated above 1.65 is mostly random gibberish :D
Also, don't forget to change the first word according to which the model will start generating text. It sometimes can affect the results tremendously. Have some fun with it!

### How to use the crawler to scrape lyrics from Genius?

+ Get your Token for the API here : [link](https://docs.genius.com/)
+ Create a json database of arists either manually or scrap the from sites like e.g. Wikipedia
+ Parse the JSON database at the end of crawl file
+ Files can be either numbered or the title can be used as a name of the file

Thank you for reading and we hope you like it! :) 

**Authors:**

Maciej Glazek & Piotr Drapinski
