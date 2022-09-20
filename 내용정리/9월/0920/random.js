var lottoColors = ["orange", "blue", "red", "black", "green"];
var lottoBalls = [];
for (var i = 1; i <= 45; i++) lottoBalls.push(i);
var lottoLineCount = 0;

function addLotto() {  
  shuffle(lottoBalls);
  var balls = lottoBalls.slice(0, 6);
  balls.sort((a, b) => a - b);
  
  var boxElem = document.getElementById("lottoBox");
  var lineElem = document.createElement("div");  
  lineElem.className = "lotto-line" + 
    ((++lottoLineCount % 5 == 0) ? " lotto-line-5th" : "");
  for (var n of balls) {
    var ballElem = document.createElement("div");
    ballElem.className = "lotto-ball";
    ballElem.style.backgroundColor = lottoColors[Math.floor((n - 1) / 10)];
    var numElem = document.createElement("div");
    numElem.className = "lotto-number";
    numElem.innerHTML = n;
    ballElem.appendChild(numElem);
    lineElem.appendChild(ballElem);    
  }
  boxElem.appendChild(lineElem);
}

function clearLotto() {
  document.getElementById("lottoBox").innerHTML = "";
  lottoLineCount = 0;
}

function randInt(a, b) {
  return Math.floor(Math.random() * (b - a + 1)) + a;
}

function shuffle(ar) {
  for (var i = ar.length - 1; i > 0; i--) {
    var r = randInt(0, i);
    var temp = ar[i];
    ar[i] = ar[r];
    ar[r] = temp;
  }
}