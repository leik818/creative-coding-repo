from flask import Flask, render_template, request # pip install flask
import torch # pip install torch
from transformers import pipeline

app = Flask(__name__)

hf_name = 'pszemraj/led-large-book-summary'
summarizer = pipeline(
    "summarization",
    hf_name,
    device=0 if torch.cuda.is_available() else -1,
)

@app.route('/', methods=['GET', 'POST'])
def index():
    summary_text = None

    if request.method == 'POST':
        user_input = request.form['user_text'].strip()

        if user_input:
            try:
                summary = summarizer(
                    user_input,
                    min_length=16,
                    max_length=256,
                    no_repeat_ngram_size=3,
                    encoder_no_repeat_ngram_size=3,
                    repetition_penalty=3.5,
                    num_beams=4,
                    early_stopping=True,
                )
                summary_text = summary[0]['summary_text']
            except Exception as e:
                summary_text = f"Error during summarization: {str(e)}"

    return render_template('index.html', summary=summary_text)

if __name__ == '__main__':
    app.run(port=5000, debug=True)

# import torch # pip install torch
# from transformers import pipeline

# hf_name = 'pszemraj/led-large-book-summary'

# summarizer = pipeline(
#     "summarization",
#     hf_name,
#     device=0 if torch.cuda.is_available() else -1,
# )

# # ask for user input
# user_text = input("Enter a passage to summarize:\n")

# # loading indicator
# print("\nSummarizing your text, please wait...")

# # run the summarizer
# result = summarizer(
#     user_text,
#     min_length=16,
#     max_length=256,
#     no_repeat_ngram_size=3,
#     encoder_no_repeat_ngram_size=3,
#     repetition_penalty=3.5,
#     num_beams=4,
#     early_stopping=True,
# )

# # print the result
# print("\nSummary:")
# print(result[0]['summary_text'])


# from transformers import pipeline

# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# ARTICLE = """ New York (CNN)When Liana Barrientos was 23 years old, she got married in Westchester County, New York.
# A year later, she got married again in Westchester County, but to a different man and without divorcing her first husband.
# Only 18 days after that marriage, she got hitched yet again. Then, Barrientos declared "I do" five more times, sometimes only within two weeks of each other.
# In 2010, she married once more, this time in the Bronx. In an application for a marriage license, she stated it was her "first and only" marriage.
# Barrientos, now 39, is facing two criminal counts of "offering a false instrument for filing in the first degree," referring to her false statements on the
# 2010 marriage license application, according to court documents.
# Prosecutors said the marriages were part of an immigration scam.
# On Friday, she pleaded not guilty at State Supreme Court in the Bronx, according to her attorney, Christopher Wright, who declined to comment further.
# After leaving court, Barrientos was arrested and charged with theft of service and criminal trespass for allegedly sneaking into the New York subway through an emergency exit, said Detective
# Annette Markowski, a police spokeswoman. In total, Barrientos has been married 10 times, with nine of her marriages occurring between 1999 and 2002.
# All occurred either in Westchester County, Long Island, New Jersey or the Bronx. She is believed to still be married to four men, and at one time, she was married to eight men at once, prosecutors say.
# Prosecutors said the immigration scam involved some of her husbands, who filed for permanent residence status shortly after the marriages.
# Any divorces happened only after such filings were approved. It was unclear whether any of the men will be prosecuted.
# The case was referred to the Bronx District Attorney\'s Office by Immigration and Customs Enforcement and the Department of Homeland Security\'s
# Investigation Division. Seven of the men are from so-called "red-flagged" countries, including Egypt, Turkey, Georgia, Pakistan and Mali.
# Her eighth husband, Rashid Rajput, was deported in 2006 to his native Pakistan after an investigation by the Joint Terrorism Task Force.
# If convicted, Barrientos faces up to four years in prison.  Her next court appearance is scheduled for May 18.
# """
# print(summarizer(ARTICLE, max_length=130, min_length=30, do_sample=False))
# [{'summary_text': 'Liana Barrientos, 39, is charged with two counts of "offering a false instrument for filing in the first degree" In total, she has been married 10 times, with nine of her marriages occurring between 1999 and 2002. She is believed to still be married to four men.'}]



# #https://huggingface.co/pszemraj/led-large-book-summary
# import torch
# from transformers import pipeline

# hf_name = 'pszemraj/led-large-book-summary'

# summarizer = pipeline(
#     "summarization",
#     hf_name,
#     device=0 if torch.cuda.is_available() else -1,
# )

# wall_of_text = """ New York (CNN)When Liana Barrientos was 23 years old, she got married in Westchester County, New York.
# A year later, she got married again in Westchester County, but to a different man and without divorcing her first husband.
# Only 18 days after that marriage, she got hitched yet again. Then, Barrientos declared "I do" five more times, sometimes only within two weeks of each other.
# In 2010, she married once more, this time in the Bronx. In an application for a marriage license, she stated it was her "first and only" marriage.
# Barrientos, now 39, is facing two criminal counts of "offering a false instrument for filing in the first degree," referring to her false statements on the
# 2010 marriage license application, according to court documents.
# """
# print("\nSummarizing your text, please wait...") 

# result = summarizer(
#     wall_of_text,
#     min_length=16,
#     max_length=256,
#     no_repeat_ngram_size=3,
#     encoder_no_repeat_ngram_size=3,
#     repetition_penalty=3.5,
#     num_beams=4,
#     early_stopping=True,
# )

# print(result)