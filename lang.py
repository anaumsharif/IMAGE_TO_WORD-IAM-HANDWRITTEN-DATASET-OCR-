from googletrans import Translator

translator = Translator()

out = translator.translate("I Love You ",dest ="mr")
pritesh = translator.translate("I am Pritesh and i have no brains ",dest ="mr")
pritesh1 = translator.translate("I am Pritesh and i have no brains ",dest ="hi")
print(out)
print(pritesh)
print(pritesh1)
print(translator.detect('हम ये नहीं कहना चाहते कि वो ध्यान नहीं दे पाते'))
hindi=translator.translate('हम ये नहीं कहना चाहते कि वो ध्यान नहीं दे पाते')
print(hindi)