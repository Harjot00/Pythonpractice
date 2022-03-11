from flask import Flask, render_template, request
import translator
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        trans_lang = request.form['lang_selected']
        lang_to_translate = request.form['translate_to']
        text = request.form['text_to_translate']
        translator_obj = translator.Translator()
        translated_text = translator_obj.get_translation(trans_lang,lang_to_translate,text)

        return render_template('translation.html', translation_lang=trans_lang, translate_to=lang_to_translate, translated_text=translated_text, text=text)

    return render_template('homepage.html')








# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
