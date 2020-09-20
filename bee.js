const BeeTimer = {
    seconds: 120,
    startTimer: function() {
        this.timer = setInterval(function() {
            BeeTimer.updateTimer();
            document.getElementById("time").innerHTML = "&#x23f0; " + BeeTimer.getSeconds();
        }, 1000);
    },
    updateTimer: function() {
        this.seconds -= 1;
        if (this.seconds == 0) {
            showAnswer()
            document.getElementById("textInput").style.borderColor = "red"
        }
    },
    stopTimer: function() {
        clearInterval(this.timer);
    },
    resetTimer: function() {
        this.seconds = 120;
        document.getElementById("time").innerHTML = ""
    },
    getSeconds: function() {
        return this.seconds;
    }
};

var currentWord
newWord()
var difficulty = 1
var mode = 1

function setDifficulty(diff) {
    difficulty = diff
    newWord()
}

function setMode(m) {
    mode = m
    newWord()
}

function newWord() {
    BeeTimer.resetTimer()
    document.getElementById("textInput").style.borderColor = "black"
    if (mode == 2) {
        BeeTimer.startTimer()
    }

    clearTextBox()
    document.getElementById("textInput").disabled = false;
    document.getElementById("hint").innerHTML = ""
    var api_diff
    switch(difficulty) {
        case 2:
            api_diff = "medium"
            break
        case 3:
            api_diff = "hard"
            break
        default:
            api_diff = "easy"
    }
    $.ajax({
        url: "api/dict/"+api_diff,
        dataType: "json",
        success: function(result) {
            var randomWord = result[0]["word"]
            var pronunciation = result[0]["phonetics"][0]["audio"]
            var definition = result[0]["meanings"][0]["definitions"][0]["definition"]
            var partOfSpeech = result[0]["meanings"][0]["partOfSpeech"]
            var sentence = result[0]["meanings"][0]["definitions"][0]["example"]
            currentWord = new Word(randomWord, pronunciation, definition, partOfSpeech, sentence)
            currentWord.getPronunciation()
        }
    });
}

function showAnswer() {
    document.getElementById("textInput").value = currentWord.getWord()
    document.getElementById("textInput").disabled = true;
    BeeTimer.stopTimer()
}

function checkAnswer(ans) {
    answer = ans.value
    word = currentWord.getWord()
    if (mode == 2 && answer.charAt(answer.length-1) != word.charAt(answer.length-1)) {
        document.getElementById("textInput").disabled = true;
        BeeTimer.stopTimer()
        document.getElementById("textInput").style.borderColor = "red"
    } if (answer === currentWord.getWord()) {
        document.getElementById("textInput").disabled = true;
        BeeTimer.stopTimer()
        document.getElementById("textInput").style.borderColor = "green"
    }
}

function clearTextBox() {
    document.getElementById("textInput").value = ""
}

class Word {

    constructor(word, pronunciation, definition, partOfSpeech, sentence) {
        this.word = word
        this.pronunciation = pronunciation
        this.definition = definition
        this.partOfSpeech = partOfSpeech
        this.sentence = sentence
    }
    
    getWord() {
        return this.word
    }
    
    getPronunciation() {
        var audio = new Audio(this.pronunciation);
        audio.play();
        return this.pronunciation
    }
    
    getDefinition() {
        document.getElementById("hint").innerHTML = this.definition
        return this.definition
    }
    
    getPartOfSpeech() {
        document.getElementById("hint").innerHTML = this.partOfSpeech
        return this.partOfSpeech
    }
    
    getSentence() {
        document.getElementById("hint").innerHTML = this.sentence.replace(this.word,"____")
        return this.sentence
    }
}
