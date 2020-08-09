// Init SpeechSynth API
const synth = window.speechSynthesis;

// DOM Elements
const textForm = document.querySelector("form");
const textInput = document.querySelector("#text-input");
const voiceSelect = document.querySelector("#voice-select");
const rate = document.querySelector("#rate");
const rateValue = document.querySelector("#rate-value");
const pitch = document.querySelector("#pitch");
const pitchValue = document.querySelector("#pitch-value");
const body = document.querySelector("body");

//Browser identifier
// Firefox 1.0+
var isFirefox = typeof InstallTrigger !== "undefined";

// Chrome 1+
var isChrome = !!window.chrome && !!window.chrome.webstore;

// Init voices array
let voices = [];

const getVoices = () => {
  voices = synth.getVoices();

  // Loop through voices and create an option for each one
  voices.forEach((voice) => {
    // Create option element
    const option = document.createElement("option");
    // Fill option with voice and language
    option.textContent = voice.name + "(" + voice.lang + ")";

    // Set needed option attributes
    option.setAttribute("data-lang", voice.lang);
    option.setAttribute("data-name", voice.name);
    voiceSelect.appendChild(option);
  });
};

//Line 35, 36 causes voice list duplication
getVoices();
if (synth.onvoiceschanged !== undefined) {
  synth.onvoiceschanged = getVoices;
}

//Fix for duplication, run code depending on the browser
if (isFirefox) {
  getVoices();
}
if (isChrome) {
  if (synth.onvoiceschanged !== undefined) {
    synth.onvoiceschanged = getVoices;
  }
}
const tr = {
  queue: null,
  pause: null,
  play: null,
  cancel: null,
  defaultRate: 1.1,
  defaultPitch: 1,
  // voice selection to do;
};
function createTextReader(tr) {
  // Check if speaking
  if (synth.speaking) {
    console.error("Already speaking...");
    return;
  }
  if (textInput.value !== "") {
    // Add background animation
    body.style.background = "#141414 url(img/wave.gif)";
    body.style.backgroundRepeat = "repeat-x";
    body.style.backgroundSize = "100% 100%";

    /*
             initializinng window.speechSynthesis 
             */

    let synth = window.speechSynthesis; // abbreviation
    tr.queue = () => {
      /*
                    Creating object of window.speechSynthesis
                    No passinng value to it
  
                    */

      let speakText = new SpeechSynthesisUtterance();
      speakText.text = textInput.value;
      speakText.rate = rate.value;
      speakText.pitch = pitch.value;
      // voice selection to do
      // if( voiceParam) ....

      // Speak end
      speakText.onend = (e) => {
        console.log("Done speaking...");
        body.style.background = "#fff";
      };

      // Speak error
      speakText.onerror = (e) => {
        console.error("Something went wrong");
      };

      // Selected voice
      const selectedVoice = voiceSelect.selectedOptions[0].getAttribute(
        "data-name"
      );

      // Loop through voices
      voices.forEach((voice) => {
        if (voice.name === selectedVoice) {
          speakText.voice = voice;
        }
      });

      synth.speak(speakText);
    };
    tr.pause = () => synth.pause();
    tr.play = () => synth.resume();
    tr.cancel = () => synth.cancel();
  }
}

// EVENT LISTENERS
// Text form submits
window.addEventListener(
  "DOMContentLoaded",
  function (e) {
    createTextReader(tr);
  },
  false
);
window.addEventListener("unload", (e) => tr.cancel(), false);
textForm.addEventListener("submit", (e) => {
  e.preventDefault();
  speak();
  textInput.blur();
});

// Rate value change
rate.addEventListener("change", (e) => (rateValue.textContent = rate.value));

// Pitch value change
pitch.addEventListener("change", (e) => (pitchValue.textContent = pitch.value));

// Voice select change
