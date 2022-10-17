"use strict"
class Translator {
    constructor() {
        this._lang = 'cn';
        this._elements = document.querySelectorAll("[data-i18n]");
    }


    translate(translation) {
        this._elements.forEach(function(element) {
            var keys = element.dataset.i18n.split(".");
            var text = keys.reduce(function(obj, i) { return obj[i] }, translation);
            if (text) {
                element.innerHTML = text;
            }
        });
    }

    Translation() {
        fetch(this._lang + '.json')
            .then(function(response) {
                this.translate(response);
            })

        .then(function(translation) {
                console.log('Request successful', text);
            })
            .catch(function(error) {
                log('Can not load lang file', error)
            });
    }

}
export default Translator;