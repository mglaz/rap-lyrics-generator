# Rap Lyrics Generator 

This was made as our final project to a class taught by Leon Ciechanowski(github.com/leontikos). It is a small project, which aim was to have some fun by scraping song lyrics from Genius and then use them to train Recurrent Networks to generate some new ones with Tensorflow.

Credit to **@ANOVAProjectUSYD** for some parts of the code!
### Quick outline

Within these files you will find a dataset with artist's names and about 1200 song lyrics that we scraped with the crawler that can be found in this repository. If you feel like some significant names are missing from our list, feel free to add them in artists_names.json file.
If you decide to use crawler yourself instead of the lyrics provided, you might want to put the crawler into lyrics folder as when you run it, files are saved in the same place where crawler is. Furthermore, here you can find a final model that we have trained and a 
Jupyter Notebook in which you will find code that was used to create it and use it.

### Install dependencies

``` pip install -r requirements.txt```

If you want to use your gpu to train your own model aste these commands into your command prompt:
 - SET PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1\bin;%PATH%
 - SET PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1\extras\CUPTI\libx64;%PATH%
 - SET PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1\include;%PATH%
 - SET PATH=C:\tools\cuda\bin;%PATH%

### How to run the project?

+ Clone this repository  ```git clone https://github.com/mglaz/rap_lyrics_final```
+ Open Jupyter Notebook  ```jupyter notebook``` (in cmd/terminal)
+ Open 'lyrics_model_working_gpu.ipynb' 
+ Change the directory variable to the path with lyric files on your computer
+ If you want to have some fun with the project run all of the cells and change some parameters

If you want to just test the model, use this command (it is provided in the notebook):
```tf.keras.models.load_model('good_model_100_epochs.h5', compile=False)```

+ Use Generate_text function to generate lyrics with the model. Set the temperature, however you want however keep in mind that with temperature=
<0.6 the lyrics will leak into the model and it can steal existing lyrics. On the other hand majority of the text generated above 1.65 is mostly random gibberish :D
Also, don't forget to change the first word according to which the model will start generating text. It sometimes can affect the results tremendously. Have some fun with it!

### Exemplary Output (Temperature = 0.65 , starting_string = "I", characters=1500)
```
I think I never knew
I don't know if I'm high, forget that month I don't wanna be
You gotta do me a flow, you can see in high school
Over like the Carter Ither thinking some more clouds
But that court like girls and start accept it, all the same last night
Hold up, tell 'em, they squeeze me
And I ain't even rock with my feelings
Get more bottles, they be ready for the feel
So crazy got my hands get it


I know I gotta keep my shawty on go, go, go
Drop the top when it's commas leading to Earth Gramm with the last time
Like I still do fraud Fraud
Flyin' private jets, sip
Shoppin' on the tube, the bottom bitch
She got a bad bitch like chronic smile


They be too against my own swall, got rotable in your mouth
I feel niggas I'm just looking gorgeous
But if I can happen at the night show Ooh-ooh-ooh
Wonder if you ask you a fucking problem-cole
I'm the shit, I get change, boy, that's what they touchin' them
And I feel like I'm hugging on that Chevy
Trapph to vacation I don't even know her mama
Ooh, oh my God, it's over
Watch out, lil bitch
You were better off without y'all
I been thinkin' I've got the drip on sink
Now the war isn't man-with your friends
So now the pressure on your wint, word to the line and
Same time you had down and I work at the grave back?
I'll let you pissed on my mind, I'ma be in my feelings
Not the time of your life, time of your life
But you a methor
You say you tell anyone inside them killers when I was supposed to be
And I'm the type that lived my thing
```
### How to use the crawler to scrape lyrics from Genius?

+ Get your Token for the API here : [link](https://docs.genius.com/)
+ Create a json database of arists either manually or scrap the from sites like e.g. Wikipedia
+ Parse the JSON database at the end of crawl file
+ Files can be either numbered or the title can be used as a name of the file

Thank you for reading and we hope you like it! :) 

**Authors:**

Maciej Glazek & Piotr Drapinski
