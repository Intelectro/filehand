//importScripts('C:/__files/DJANGO/DJANGO_TRAIN_01/src/static_in_pro/our_static/js/speakGenerator.js');
//importScripts("{% static 'js/speakGenerator.js' %}");

importScripts('/static/js/speakGenerator.js');
//window.alert('3 HERE HERE ');
onmessage = function(event) {
  postMessage(generateSpeech(event.data.text, event.data.args));
};

